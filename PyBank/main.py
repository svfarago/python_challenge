# What: Module in Python paths across operating systems
import os

# What: Module in Python reads CSV files
import csv

# csvpath is a string value--creates joined path as string -- /resources/budget_data.csv
csvpath = os.path.join("Resources", "budget_data.csv")

# What: Method open -- Read using open method open(csvpath) as csvfile
csvfile = open(csvpath)

# VARIABLES - Create placeholder for future content | [ ] signifies an empty list.
# Notes: Only these three require a container for calculations. Increase and decrease profits data is just a lookup of existing data.
total_months = []
total_profit = []
average_change = []


# What: Opens csv file using reader method
# Notes: Delimiter and variable holds contents--comma in this case
csvreader = csv.reader(csvfile, delimiter=',')


# What: Reads header in csv file
# Notes: To print it to the screen use >> print(f"CSV Header: {csv_header}") | f converts all to string
csv_header = next(csvreader)

# What: Iterate through the rows
for row in csvreader: 

    # Puts the total months and total profit values to their corresponding lists using [0] for first column and [1] for second column
    # Notes: append means to go through all rows and act as a container | int converts profit to number
    # POTATO: 
    total_months.append(row[0])
    total_profit.append(int(row[1]))

# What: Iterate through the profits in order to get the average change in profits
# Notes: i is a container = | len = returns number of items in a container or list | -1 is to keep total_profit in range, otherwise results in "out of range" error
# Potato: "-1" - Got error if not used. See "out of range" in Notes above.
for i in range(len(total_profit)-1):
        
    # Take the difference between two months and append to average change
    # Notes compares each month to next and adds the profit to the "i" and keeps a rolling count [i+1] using square brackets as a temp container (i plus the next one below)
    # Then subtrack the current from previous month to get the deltas (change in price). Then find the average.See calc in spreadsheet for more notes
    #POTATO - I think I'm missing basic math. Why "-total_profit[i]"? I played around with the "-" | its right in Excel but uses average.
     average_change.append(total_profit[i+1]-total_profit[i])

#POTATO - My increase and decrease profits are not right ($25 and $43)
# What: Finds greatest increase and decrease
# Notes: Use max and min to look at monthly profit change and put in "max_increase" or "max_decrease"
# Notes: The +1 is the next month when comparing each of the months with one another to get the largest or smallest number. It's not the next or prior but rather whichever month is currently "higest" or "lowest" that it compares against.

max_increase = max(average_change)
max_increase = average_change.index(max(average_change)) + 1

max_decrease = min(average_change)
max_decrease = average_change.index(min(average_change)) + 1 

# What: Print
# Notes: len counts # items in a container | Use "round" and "2" to round to second decimal otherwise really long decimal number
# Using {} to convert info to string format 
print("   ")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease]} (${(str(max_decrease))})")

