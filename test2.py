import csv

with open('output.csv') as doc:
    csvReader = csv.reader(doc)
    for row in csvReader:
        print(row)