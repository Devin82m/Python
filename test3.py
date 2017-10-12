import csv

my_dict={}
with open("output.csv","rb") as f:
   cr = csv.reader(f, delimiter=',', lineterminator='\n')
   for row in cr:
       my_dict.setdefault(row[0].strip('" '),[]).append(row[1].strip('" '))

with open("outputNEW.csv", "wb") as f:
    writer = csv.writer(f,delimiter=',')
    for i,j in my_dict.iteritems():
        writer.writerow([i]+j)