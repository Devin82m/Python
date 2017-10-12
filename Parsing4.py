import csv

# Testing printing a specific row
testf = open('/Users/dstclair/Downloads/mfa-users.csv', 'rb')
testr = csv.reader(testf)
testl = list(testr)
print testl[11]


# Is the with statement worth using? From what I can tell you have to close() statements just using open, bit with atuomatically does so
# I've run the code above without a close() statement without any ill effects

with open ('/Users/dstclair/Downloads/mfa-users.csv', 'rb') as testf:
    testr = csv.reader(testf)
    testl = list(testr)
    print testl[30]