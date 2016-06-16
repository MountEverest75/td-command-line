# Treasure Data Command Line Utility
## Prerequisites
td-command-line supports the following versions of python
* Python 3.3+
Visit console.treasuredata.com to create an API key
Setup a global variable MASTER_TD_API_KEY to store the API key and add it to .profile and .bashrc files

## Installing Ruby 2+ and Rubygems
Follow setup instructions at the following sites:
https://www.ruby-lang.org/en/documentation/installation/
https://rubygems.org/pages
Run the following setup to access td shell after insalling Ruby and Rubygems.
```sh
$ gem install td
```
## Instructions to Access and Run IPython notebooks and Python code
### Complete the basic Setup by running the following shell commands
```sh
$ export MASTER_TD_API_KEY=”<YOUR_TREASUREDATA_MASTER_
API_KEY>”
$ conda create -n analysis python=3
$ source activate analysis
```

### Install dependencies. This setup will allow access to IPython notebook file.
```sh
(analysis)$ conda install pandas
(analysis)$ conda install matplotlib
(analysis)$ conda install -c https://conda.anaconda.
org/anaconda seaborn
(analysis)$ conda install ipython-notebook
(analysis)$ pip install pandas-td
(analysis)$ pip install td-client
#activate notebook.
(analysis)$ ipython notebook
```

## Artifacts
### Libraries folder /lib
The Libraries folder contains the following artifacts
* query.py - The python script used as command line utility to run queries on Treasure data SaaS service
* enrich.py - Contains the sample code to assign a time column and convering the date value to UTC format
* query_test.sh - Contains the sample commands to run command line utility
* td-bulk-import.sh - Contains the sample command to run bulk import
* TreasureDataIPythonNotebook.ipynb - IPython notebook containing samples to run Treasure Data Python API

## Running Bulk Data Import
Using the sample dataset provided the data import could be executed as follows. The option --time-value was provided to generate sample data. This will not be required during a real data import.
```sh
td import:auto --format csv --column-header --time-column updated_date --time-format "%Y-%m-%d %H:%M:%S" --time-value 1394409600,10 --auto-create financial_datasets.fdic_failed_banklist ../datasets/banklist_import.csv
```
## Running queries
(1) Run Help command as follows
```sh
./query.py -h
```
(2) Run query with mandatory options -d for database name and -t for table name as follows:
```sh
./query.py -d 'financial_datasets' -t 'fdic_failed_banklist'
```

(3) Please refer to query_test.sh for all samples and combinations.
