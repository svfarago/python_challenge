# Module os for path across operating systems
import os

# Module csv for reading CSV files
import csv

# csvpath is string value the path that is joined together as a string
csvpath = os.path.join("Resources", "budget_data.csv")

#Read using open method open(csvpath) as csvfile
csvfile = open(csvpath)

#Opens csv file using reader method; delimiter and variable that holds contents
csvreader = csv.reader(csvfile, delimiter=',')

print(csvreader)

# Reads header
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")

# Reads data
for row in csvreader:
    print(row)

#POTATO - Start here all working above.
#Adding a new rem line just to refresh content on Github. 12/29