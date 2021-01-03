# What: Module in Python paths across operating systems
import os

# What: Module in Python reads CSV files
import csv

# csvpath is a string value--creates joined path as string -- /resources/budget_data.csv
# yes - potato added txtoutput
csvpath = os.path.join("Resources", "budget_data.csv")
txtoutput = os.path.join("Analysis", "output.txt")


# VARIABLES - Create placeholder for future content | [ ] signifies an empty list.
# Notes: Only these three require a container for calculations. Increase and decrease profits data is just a lookup of existing data.
total_months = []
total_profit = []
average_change = []

# What: Opens csv file using reader method
with open(csvpath) as budget:

     # Notes: Delimiter and variable holds contents--comma in this case
    csvreader = csv.reader(budget,delimiter=",") 


    # What: Reads header in csv file
    # Notes: To confirm file is being read print it to the screen >> print(f"CSV Header: {csv_header}") | f converts all to string
    header = next(csvreader)

    # What: Iterate through the rows
    for row in csvreader: 

        # Puts the total months and total profit values to their corresponding lists using [0] for first column and [1] for second column
        # Notes: append means to go through all rows and store data within [] container | int converts profit to number | append = list (dictionary = use something else)
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # What: Iterate through the profits in order to get the average change in profits
    # Notes: i is a container = | len = returns number of items in a container or list | range = column A=0, B=1 (specified in total_profit above)
    # -1 is to keep total_profit in range, otherwise results in "out of range" error
    # YES answered Potato: "-1" - Got error if not used. See "out of range" in Notes above, is this correct so it stops reading at the last data line?
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to average change
        # Notes compares each month to next and adds the profit to the "i" and keeps a rolling count [i+1] using square brackets as a temp container (i plus the next one below)
        # Then subtrack the current from previous month to get the deltas (change in price). Then find the average.See calc in spreadsheet for more notes
        # yes answered - POTATO - Math is not coming out ($25 and $45)
        # I think it's counting the row below the month (so row 25 = 1 below "Feb" and row 44 = 1 below "Sept")
        average_change.append(total_profit[i+1]-total_profit[i])
        #i+1 = B27 minus i = B26


# What: Profit greatest increase and decrease - actual calculation
# Notes: Use max and min to look at monthly profit change and put in "max_increase" or "max_decrease"
# Notes: It's not the next or prior but rather whichever month is currently "higest" or "lowest" that it compares against.

max_increaseprof = max(average_change)
max_decreaseprof = min(average_change)    

# What: Month of greatest profit increase and decrease - just reports the month
# Solved - create two different sets of variables so 57/58 don't get overwritten by 64/65
# Notes: Use + 1 to pull the next month in the list since average change lands on B26
# index = returns numeric location of a given value within a list
max_increase = average_change.index(max(average_change)) + 1
max_decrease = average_change.index(min(average_change)) + 1


# What: Prints
# Notes: len counts # items in a container | Use "round" and "2" to round to second decimal otherwise really long decimal number
# Using {} to convert info to string format 
print("   ")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase]} (${(str(max_increaseprof))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease]} (${(str(max_decreaseprof))})")


# What: Outputs to text file in Analysis subdirectory
# Notes: "w" for write | \n = hard return | output references path variable at beginning of code so it knows where to .txt file and what to name it as output.txt
# Notes: {} are placeholders with /n as hard returns for above lines 1-7.
output = open(txtoutput,"w")
line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = str(f"Total Months: {len(total_months)}")
line4 = str(f"Total: ${sum(total_profit)}")
line5 = str(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
line6 = str(f"Greatest Increase in Profits: {total_months[max_increase]} (${str(max_increaseprof)})")
line7 = str(f"Greatest Decrease in Profits: {total_months[max_decrease]} (${str(max_decreaseprof)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
