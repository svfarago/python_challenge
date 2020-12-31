# What: Module in Python paths across operating systems
import os

# What: Module in Python reads CSV files
import csv

# csvpath is a string value--creates joined path as string -- /resources/budget_data.csv
csvpath = os.path.join("Resources", "budget_data.csv")

# What: Method open -- Read using open method open(csvpath) as csvfile
csvfile = open(csvpath)

# VARIABLES - Create placeholder to iterate through specific rows
total_months = []
total_profit = []
monthly_profit_change = []


# What: Opens csv file using reader method
# Notes: Delimiter and variable holds contents--comma in this case
csvreader = csv.reader(csvfile, delimiter=',')


# What: Reads header in csv file
# Notes: To print it to the screen use >> print(f"CSV Header: {csv_header}") | f converts all to string
csv_header = next(csvreader)

# What: Iterate through the rows
for row in csvreader: 

    # Put the total months and total profit values to their corresponding lists
    # Notes: append means to add to [ ] above | int converts profit to whole number
    total_months.append(row[1])
    total_profit.append(int(row[1]))

# What: Iterate through the profits in order to get the monthly change in profits
# Notes: i is a container = | len = returns number of items in container | -1 is to keep total_profit in range, otherwise results in "out of range" error
# Potato: "-1" - Got error if not used. See "out of range" in Notes above.
for i in range(len(total_profit)-1):
        
    # Take the difference between two months and append to monthly profit change
     monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Printout
print("   ")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")



