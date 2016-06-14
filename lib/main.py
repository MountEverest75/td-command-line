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
    if parameters['limit'] != '0':
        limit_str = "LIMIT " + str(parameters['limit']) + ";"
    else:
        limit_str = ";"
    
    if parameters['min_time'] == 'NULL' and parameters['max_time'] == 'NULL':
        compose_query = "SELECT " + parameters['col_list']   + " " + \
                        "FROM "   + parameters['table_name'] + " " + limit_str

    else:
        compose_query = "SELECT " + parameters['col_list']   + " " + \
                        "FROM "   + parameters['table_name'] + " " + \
                        "WHERE "  + "td_time_range(time,"    + parameters['min_time'] + "," + parameters['max_time'] + ") " + \
                        limit_str
            
    print(compose_query)
    #2. Run query as a job and wait for job to finish
    with tdclient.Client(apikey) as client:
        job = client.query(parameters['db_name'],compose_query,type=parameters['query_engine'])
        job.wait()
        df = td.read_td_job(job.job_id, con_engine)

    #3. Write the results to a csv file
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

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"f:e:c:m:M:l:d:t:",["format=","engine=","columns=","min_time=","max_time=","limit=","db_name=","table_name="])
	except getopt.GetoptError:
		print('query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d db_name -t table_name')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('query.py [-f <format(tabular or csv)> -e <engine()> -c <columns separated by commas> -m <min_time> -M <max_time> -l <limit>] -d db_name -t table_name')
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
			table_name = arg
			
	parameters = {}
	parameters['db_name'] = db_name
	parameters['table_name'] = table_name
	if engine == '':
		parameters['query_engine'] = "presto"
	else:
		parameters['query_engine'] = engine
		
	if columns == '':
		parameters['col_list'] = "*"
	else:
		parameters['col_list'] = columns
		
	if format == 'csv':
		parameters['format'] = 'csv'
	else:
		parameters['format'] = 'tabular'
		
	# if limit == '':
	# 	parameters['limit'] = str(limit)
	# else:
	# 	parameters['limit'] = '0'
	# if min_time == '':
	# 	parameters['min_time'] = 'NULL'
	# 
	# if max_time == '':
	# 	parameters['max_time'] = 'NULL'
	parameters['limit'] = str(limit)
	parameters['min_time'] = min_time
	parameters['max_time'] = max_time
	
	print(parameters)
	run_dynamic_query(parameters)

if __name__ == "__main__":
	main(sys.argv[1:])