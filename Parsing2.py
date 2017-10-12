import csv

with open('/Users/dstclair/Downloads/mfa-users.csv') as csvFile:
    reader = csv.reader(csvFile)
    field_names_list = reader.next()
    print field_names_list