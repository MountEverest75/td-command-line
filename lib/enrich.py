import os
import csv
import sys
from datetime import time

def enrich_time():
    outputfile = open("banklist_timestamp_new.csv","a")
    inputfile = open("banklist_import.csv","r")
    reader = csv.reader(inputfile, delimiter=',')
    writer = csv.writer(outputfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(["bank_name","city","st","cert","acquiring_instituition","closing_date","time"])
    next(reader)
    for line in reader:
        if len(line) == 7:
            bank_name = line[0]
            city      = line[1]
            st        = line[2]
            cert      = line[3]
            acquiring_instituition = line[4]
            closing_date = line[5]
            updated_date = line[6]
            date_object = datetime.strptime(updated_date, '%d-%b-%y')
            time_converted = (date_object.toordinal() - date(1970, 1, 1).toordinal()) * 24*60*60
            writer.writerow([bank_name, city, st, cert, acquiring_instituition, time_converted])
        else:
            continue
    inputfile.close()
    outputfile.close()

def main():
    enrich_time()
