#!/Users/rchebolu/anaconda3/anaconda/bin/python3
import sys, getopt
import os
import pandas as pd
import pandas_td as td
import tdclient
from tabulate import tabulate

#This function connects and executes query on Treasure Data
def run_dynamic_query(parameters):
    #0. Initialize our connection to Treasure Data
    apikey=os.environ['MASTER_TD_API_KEY']
    endpoint='https://api.treasuredata.com'
    con = td.connect(apikey, endpoint)
    #1. Connect to the query engine
    con_engine=con.query_engine(database=parameters['db_name'], type=parameters['query_engine'])

	#2. Setup query limit string
    if parameters['limit'] != '0':
        limit_str = "LIMIT " + str(parameters['limit']) + ";"
    else:
        limit_str = ";"

	#3. Compose Query String
    if not 'min_time' in parameters.keys():
        parameters['min_time'] = 'NULL'

    if not 'max_time' in parameters.keys():
        parameters['max_time'] = 'NULL'

    if parameters['min_time'] == 'NULL' and parameters['max_time'] == 'NULL':
        compose_query = "SELECT " + parameters['col_list']   + " " + \
                        "FROM "   + parameters['table_name'] + " " + limit_str

    else:
        compose_query = "SELECT " + parameters['col_list']   + " " + \
                        "FROM "   + parameters['table_name'] + " " + \
                        "WHERE "  + "td_time_range(time,"    + parameters['min_time'] + "," + parameters['max_time'] + ") " + \
                        limit_str

    print("Executing..." + compose_query)
    #4. Run query as a job and wait for job to finish
	#Assign result set to a data frame

    with tdclient.Client(apikey) as client:
        job = client.query(parameters['db_name'],compose_query,type=parameters['query_engine'])
        job.wait()
        try:
            #Assign result set to a data frame
            df = td.read_td_job(job.job_id, con_engine)
        except RuntimeError:
            print("Please review the column names and delimited by commas: " + parameters['col_list'])
            return

	#5. Write the results to a csv or tabular format file
    if parameters['format'] == 'csv':
        print("Downloading results to " + job.job_id + ".csv" + " file")
        df.to_csv(job.job_id + ".csv")
    else:
        #Write data into tabular grid format
        print("Downloading results to " + job.job_id + ".txt" + " file")
        filename = job.job_id + ".txt"
        outfile = open(filename,"a")
        outfile.write(tabulate(df, tablefmt="grid"))
        outfile.close()

#Function to check if a value if numeric
def is_number(s):
	try:
		float(s) # for int, long and float
	except ValueError:
		return False
	return True

#Main function receives command line arguments
def main(argv):
	db_name    = None
	table_name = None
	format     = None
	engine     = None
	columns    = None
	min_time   = None
	max_time   = None
	limit      = None
	try:
		opts, args = getopt.getopt(argv,"hf:e:c:m:M:l:d:t:",["format=","engine=","columns=","min_time=","max_time=","limit=","db_name=","table_name="])
	except getopt.GetoptError:
		print("Database Name and Table Name are mandatory")
		print("Suggested usage: ./query.py -d <db_name> -t <table_name>")
		print("Suggested usage with optionals: ./query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d <db_name> -t <table_name>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("Database Name and Table Name are mandatory")
			print("Suggested usage: ./query.py -d <db_name> -t <table_name>")
			print("Suggested usage with optionals: ./query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d <db_name> -t <table_name>")
			sys.exit()
		elif opt in ("-f", "--format"):
			format = arg
		elif opt in ("-e", "--engine"):
			engine = arg
		elif opt in ("-c", "--columns"):
			columns = arg
		elif opt in ("-m", "--min_time"):
			min_time = arg
		elif opt in ("-M", "--max_time"):
			max_time = arg
		elif opt in ("-l", "--limit"):
			limit = arg
		elif opt in ("-d", "--db_name"):
			db_name = arg
		elif opt in ("-t", "--table_name"):
			table_name = str(arg).strip()

	parameters = {}
	if table_name == None or table_name.strip() == '':
		print("Database Name and Table Name are mandatory")
		print("Suggested usage: ./query.py -d <db_name> -t <table_name>")
		print("Suggested usage with optionals: ./query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d <db_name> -t <table_name>")
		return

	if db_name == None or db_name.strip() == '':
		print("Database Name and Table Name are mandatory")
		print("Suggested usage: ./query.py -d <db_name> -t <table_name>")
		print("Suggested usage with optionals: ./query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d <db_name> -t <table_name>")
		return

	parameters['db_name'] = db_name.strip().lower()
	parameters['table_name'] = table_name.strip().lower()
	if engine == None or engine.strip() == '' or not engine.strip().lower() in ["presto", "hive"]:
		parameters['query_engine'] = "presto"
	else:
		parameters['query_engine'] = engine.strip().lower()

	if columns == None or columns.strip() == '' or columns[0] == '-':
		parameters['col_list'] = "*"
	else:
		parameters['col_list'] = columns.strip().lower()

	if  format == None or format.strip() == '':
		parameters['format'] = 'tabular'
	else:
		if format.strip().lower() in ["tabular", "csv"]:
			parameters['format'] = format.strip().lower()
		else:
			print("No Valid format option specified. Valid options are tabular or csv. Defaulting to Tabular...")
			parameters['format'] = 'tabular'

	if limit == None or limit.strip() == '' or limit.strip() == '0':
		parameters['limit'] = str('0')
	else:
		if is_number(limit):
			parameters['limit'] = str(limit).strip()
		else:
			print("Non numeric value specified for query limit")
			print("./query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d <db_name> -t <table_name>")
			return

	if min_time == None or min_time.strip() == '' or min_time.strip() == 'NULL' or min_time.strip() == 'null' or not is_number(min_time):
		parameters['min_time'] = 'NULL'
	else:
		if is_number(min_time):
			parameters['min_time'] = min_time.strip()
		else:
			print("Non numeric value specified for minimum timestamp. Vaid examples are 1412366345 and NULL or leave it blank")

	if max_time == None or max_time.strip() == '' or max_time.strip() == 'NULL' or max_time.strip() == 'null' or not is_number(max_time):
		parameters['max_time'] = 'NULL'
	else:
		if is_number(max_time):
			parameters['max_time'] = max_time.strip()
		else:
			print("Non numeric value specified for maximum timestamp. Vaid examples are 1412366395 and NULL or leave it blank")

	print(parameters)
	run_dynamic_query(parameters)

if __name__ == "__main__":
	main(sys.argv[1:])
