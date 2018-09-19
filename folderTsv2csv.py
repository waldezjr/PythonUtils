#!/usr/bin/env python

# Converts all tsv files in the current folder to csv files
# It OVERWRITES any pre-existing csv files
import sys
import os
import csv

for f in sorted(os.listdir(os.getcwd())):
    if f.endswith(".tsv"):
        print ("Converting "+ f)
        converted_file = f[:-3]+"csv"
        with open(converted_file, 'w') as fout:
            writer = csv.writer(fout, dialect=csv.excel)

            with open(f, 'r') as fin:
                reader = csv.reader(fin, dialect=csv.excel_tab)

                for row in reader:
                    writer.writerow(row)
