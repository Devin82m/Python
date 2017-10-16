import csv

# Testing printing multiple columns
testpath = 'C:\Users\Devin\Downloads\users.csv'

with open (testpath, 'r') as testf:
    testr = csv.reader(testf)
    for column in testr:
        print column[0] + " -- " + column[1]
