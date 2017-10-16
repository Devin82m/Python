import csv

# Testing finding something specifical in a CSV, with and else
testpath = 'C:\Users\Devin\Downloads\users.csv'
developer = "devin"

with open (testpath, 'r') as testf:
    testr = csv.reader(testf)
    for row in testr:
        for field in row:
            if developer in row:
                print row
        else:
            print developer +  " does not exist!"



