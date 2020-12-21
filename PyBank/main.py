# Module os for path across operating systems
import os

# Module csv for reading CSV files
import csv

# csvpath is string value the path that is joined together as a string
csvpath = os.path.join('..', 'resources', 'budget_data.csv')

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#windows = '..//python_challenge//PyBank//Resources//budget_data.csv


#Read using CSV module using open method using input/output method

with open(csvpath) as csvfile:

#csvfile = open(csvpath)

# CSV reader = opens csv file using reader method; specifies delimiter and variable that holds contents
#SVF - csvreader
    csvreader = csv.reader(csvfile, delimiter=',')

#[[header1, header2],
#    [data1, data2]]

print(csvreader)

# Read the header row first (skip this step if there is now header)
#csv_header = next(csvreader)
#print(f"CSV Header: {csv_header}")

# Read each row of data after the header
for row in csvreader:
    print(row)
