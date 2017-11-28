# Example of use: python CSVcleaner.py ~/Downloads/source_file ~/Downloads/destination_file 1 14

import csv
import sys
from itertools import islice

sourcef = sys.argv[1]  # Source file path/name e.g. ~/Documents/something.csv
destf = sys.argv[2]  # Destination file path/name e.g. ~/Documents/something.csvCLEAN
linestart = int(sys.argv[3])  # Starting row to delete, remember 0 is the first row and typically is the header
lineend = int(sys.argv[4])  # Ending row to delete

with open (sourcef, 'rb') as file1, open (destf, 'wb') as file2:
    reader = csv.reader(file1)
    writer = csv.writer(file2)
    for i,row in enumerate(reader):
        if linestart <= i < lineend:
            continue  # skip this range
        writer.writerow(row)