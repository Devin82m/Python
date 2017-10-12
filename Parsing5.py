import csv

# Print a specific column 
with open('/Users/dstclair/Downloads/mfa-users.csv', 'rb') as testf:
    testr = csv.reader(testf)
    print [i[1] for i in testr]

