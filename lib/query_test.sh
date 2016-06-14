./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m 'NULL' -M '1412366395' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -f 'csv' -e 'presto' -c '*' -m '1412366345' -M 'NULL' -l '100' -d 'sample_datasets' -t 'www_access' >> tdaudit.log
./query.py -d 'sample_datasets' -t 'www_access' >> tdaudit.log
