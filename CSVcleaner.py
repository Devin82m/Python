# Example of use: python CSVcleaner.py ~/Downloads/source_file ~/Downloads/destination_file 1 14
# 1 and 14 being the range of rows you wish to remove, it will remove rows 1-13 (I'm not sure why it won't grab the last line, but take that in account)
# TEMPORARY - The lines designated acren't actually removed, but that is the next step, it was easier to test by just writing the range to another file


import csv
import sys

sourcef = sys.argv[1]  # Source file path/name
destf = sys.argv[2]  # Destination file path/name
linestart = int(sys.argv[3])  # Starting row to delete, remember 0 is the first row and typically is the header
lineend = int(sys.argv[4])  # Ending row to delete, but add one

with open (sourcef, 'rb') as file1, open (destf, 'wb') as file2:
    reader = csv.reader(file1)
    writer = csv.writer(file2)
    row = list(reader)
    for i in row[slice(linestart, lineend)]: 
        print i
        writer.writerow(i)