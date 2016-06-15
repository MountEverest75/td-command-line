# Negative Test Conditions
./query.py >> tdaudit.log
./query.py -d 'sample_datasets' -t  >> tdaudit.log
./query.py -d 'sample_datasets'  >> tdaudit.log
./query.py -d  -t 'www_access' >> tdaudit.log
./query.py -t 'www_access' >> tdaudit.log

# Options given but no values. Result - Should run normally
./query.py -f-e-c-m-M-l  -d 'sample_datasets' -t 'www_access' >> tdaudit.log

# Invalid columns
./query.py -f 'csv' -e 'presto' -c 'user,host,iamnotacolumn' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log

#Testing optionals
./query.py -f  -e  -c  -m  -M  -l  -d 'sample_datasets' -t 'www_access' >> tdaudit.log

# Positive Test Conditions
./query.py -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c 'user,host,time' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log

# My own data set tests
./query.py -d 'financial_datasets' -t 'fdic_failed_banklist' >> tdaudit.log
./query.py -d 'weather_datasets' -t 'annual_summary'
./query.py -f  -e  -c  -m  -M  -l  -d 'weather_datasets' -t 'annual_summary'
./query.py -f-e-c-m-M-l  -d 'weather_datasets' -t 'annual_summary'

# All options
./query.py
./query.py -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -c "time,bank_name,acquiring_institution" -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f  -e  -c  -m  -M  -l  -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f-e-c-m-M-l  -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'csv' -e 'hive' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'csv' -e 'pig' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

./query.py -f 'tabular' -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'tabular' -e 'hive' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'tabular' -e 'pig' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

# No format option
./query.py -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -e 'hive' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -e 'pig' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'


./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c 'user,host,time' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access'
