# Script straight from https://gist.github.com/nsonnad/7598574
# Usage: python tsv2csv.py < file_input.tsv > file_output.csv

import sys
import csv

tabin = csv.reader(sys.stdin, dialect=csv.excel_tab)
commaout = csv.writer(sys.stdout, dialect=csv.excel)

for row in tabin:
    commaout.writerow(row)