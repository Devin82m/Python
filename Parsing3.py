import csv

testf = open('/Users/dstclair/Downloads/mfa-users.csv')
testr = csv.reader(testf)
testl = list(testr)

for row in testl:
    print row