import csv

# Print a specific column 
testpath = 'C:\Users\Devin\Downloads\users.csv'
#testpath = '/Users/dstclair/Downloads/mfa-users.csv'
with open(testpath, 'rb') as testf:
    testr = csv.reader(testf)
    print [i[0] for i in testr]

