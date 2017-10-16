import csv

# Testing taking columns from one csv and putting them in another csv

#testpath = 'C:\Users\Devin\Downloads\users.csv'
testPath1 = '/Users/dstclair/Downloads/mfa-users.csv'
testPath2 = '/Users/dstclair/Downloads/mfa-usersNEW.csv'

begin = 0
end = 3

with open(testPath1, "r") as file_in:
    with open(testPath2, "w") as file_out:

        writer = csv.writer(file_out)

        for row in csv.reader(file_in):
            writer.writerow(row[begin:end])