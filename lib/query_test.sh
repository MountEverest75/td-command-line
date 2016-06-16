# FDIC Failed Banks List Data set. Source: https://catalog.data.gov/dataset?res_format=CSV
./query.py -d 'financial_datasets' -t 'fdic_failed_banklist' >> tdaudit.log
./query.py -d 'weather_datasets' -t 'annual_summary'
./query.py -f  -e  -c  -m  -M  -l  -d 'weather_datasets' -t 'annual_summary'
./query.py -f-e-c-m-M-l  -d 'weather_datasets' -t 'annual_summary'

# All Test conditions
#1. Should show suggested usage
./query.py
#2. Should show help
./query.py -h
#3. Should select all columns
./query.py -d 'financial_datasets' -t 'fdic_failed_banklist'
#4. Should select specific columns
./query.py -c "time,bank_name,acquiring_instituition" -d 'financial_datasets' -t 'fdic_failed_banklist'
#5. All options are blank except database and table name. Selects all columns. Defaults all options.
./query.py -f  -e  -c  -m  -M  -l  -d 'financial_datasets' -t 'fdic_failed_banklist'
#6. Similar effect as above. Null values sent into program
./query.py -f-e-c-m-M-l  -d 'financial_datasets' -t 'fdic_failed_banklist'
#7. Similar effect as above. Limits number of records selected. All columns selected, but output sent to CSV file.
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
#8. Similar effect as above. Uses Hive engine. Limits number of records selected to 100. All columns selected, but output sent to CSV file.
./query.py -f 'csv' -e 'hive' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
#9. Similar effect. Engine mentioned as Pig. Not supported but defaults to presto.
./query.py -f 'csv' -e 'pig' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
#10. Time stamp range specified. Number of records selected should be 100
./query.py -f 'csv' -e 'presto' -c '*' -m '1394409630' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'tabular' -e 'presto' -c '*' -m '1394409630' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

#11. Time stamp range specified. Number of records selected should less than 545
./query.py -f 'csv' -e 'presto' -c '*' -m '1394409731' -M '1394409830' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'tabular' -e 'presto' -c '*' -m '1394409731' -M '1394409830' -d 'financial_datasets' -t 'fdic_failed_banklist'

#12. First 100 records selected.
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M '1394410175' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

#13. All 545 records selected.
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M '1394410175' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'tabular' -e 'presto' -c '*' -m 'NULL' -M '1394410175' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

./query.py -f 'tabular' -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -f 'tabular' -e 'hive' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

# No format option
./query.py -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'
./query.py -e 'hive' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

# No engine and format Options
./query.py -c '*' -m '1394409731' -M '1394409830' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

# No column option
./query.py -m '1394409731' -M '1394409830' -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'

# No timestamps
./query.py -l '100' -d 'financial_datasets' -t 'fdic_failed_banklist'


./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access'
./query.py -f 'csv' -e 'presto' -c 'user,host,time' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access'

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
