import csv
import sys

sourcef = sys.argv[1]  # Source file path/name
destf = sys.argv[2]  # Destination file path/name
linestart = int(sys.argv[3])  # Starting row to delete
lineend = int(sys.argv[4])  # Ending row to delete, but add one

with open (sourcef, 'rb') as file1, open (destf, 'wb') as file2:
    reader = csv.reader(file1)
    writer = csv.writer(file2)
    row = list(reader)
    for i in row[slice(linestart, lineend)]: 
        print i
        writer.writerow(i)