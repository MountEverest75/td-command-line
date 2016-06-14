import os
import pandas as pd
import pandas_td as td
import tdclient

#This function connects and executes query on Treasure Data
def run_dynamic_query(parameters):
    #0. Initialize our connection to Treasure Data
    apikey=os.environ['MASTER_TD_API_KEY']
    endpoint='https://api.treasuredata.com'
    con = td.connect(apikey, endpoint)
    #1. Connect to the query engine
    con_engine=con.query_engine(database=parameters['db_name'], type=parameters['query_engine'])
    if parameters['limit'] > 0:
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
        
    
#This code goes in main function that captures command line arguments
#All inputs given below
#Refactor as one function set_parameters(argv) inside main function
parameters = {}
parameters['db_name'] = 'sample_datasets'
parameters['table_name'] = 'nasdaq'
parameters['query_engine'] = 'presto'
# parameters['col_list'] = ['symbol', 'high', 'low', 'time']
parameters['col_list'] = "*"
parameters['format'] = 'csv'
parameters['limit'] = 0
parameters['min_time'] = '2009-01-01'
parameters['max_time'] = '2010-01-01'
run_dynamic_query(parameters)