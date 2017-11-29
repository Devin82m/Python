# Use: python27 GenericCleaner.py source_file destination_file 1 3
# 1 and 3 are the start and end line you wish to remove

import sys

sourcef = sys.argv[1]  # Source file path/name e.g. ~/Documents/something.csv
destf = sys.argv[2]  # Destination file path/name e.g. ~/Documents/something.csvCLEAN
linestart = int(sys.argv[3])  # Starting row to delete, remember 0 is the first row and typically is the header
lineend = int(sys.argv[4])  # Ending row to delete

with open (sourcef, 'rb') as file1, open (destf, 'wb') as file2:        
        for i,row in enumerate(file1):
            if linestart <= i < lineend:
                continue  # skip this range
            file2.write(row)