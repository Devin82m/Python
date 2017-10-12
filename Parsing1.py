import csv

testFile = open('/Users/dstclair/Downloads/export-users.csv')
testReader = csv.reader(testFile)
testList = list(testReader)

print testList