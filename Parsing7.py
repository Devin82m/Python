import csv

# Testing counting of multiple cloumns
testpath = 'C:\Users\Devin\Downloads\users.csv'

with open (testpath, 'r') as testf:
    testr = csv.reader(testf)
    for column in testr:
        print len(column[0])
        print "***** End first colum ****"
        print len(column[2])
