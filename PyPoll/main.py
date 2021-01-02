# What: Module in Python paths across operating systems
import os

# What: Module in Python reads CSV files
import csv

# What: Method open -- Read using open method open(csvpath) as csvfile
# csvpath is a string value--creates joined path as string -- /resources/election_data.csv
csvpath = os.path.join("Resources", "election_data.csv")


# VARIABLES - Create placeholder for future content | [ ] signifies an empty list.
# Notes: Only these three require a container for calculations. Remaining is just a lookup of existing data.
#total_months > total_votes | total_profit > percent_votes | average_change > candiate_votes
total_votes = []
percent_votes = []
candidate_votes = []

# What: Opens csv file using reader method
with open(csvpath) as election:

     # Notes: Delimiter and variable holds contents--comma in this case
    csvreader = csv.reader(election,delimiter=",") 


    # What: Reads header in csv file
    # Notes: To confirm file is being read print it to the screen using >> print(f"CSV Header: {csv_header}") | f converts all to string
    header = next(csvreader)

    # What: Iterate through the rows
    for row in csvreader: 

        # Puts the total months and total profit values to their corresponding lists using [0] for first column and [1] for second column
        # Notes: append means to go through all rows and act as a container | int converts profit to number
        total_votes.append(row[0])



# What: Prints
# Notes: len counts # items in a container | Use "round" and "2" to round to second decimal otherwise really long decimal number
# Using {} to convert info to string format 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(total_votes)}")
print("----------------------------")
print("Results here...")
print("----------------------------")
print("Winner: here")
print("----------------------------")


# What: Outputs to text file
# Notes: "w" for write | \n = hard return | the {} just placeholders with /n as hard returns for lines.
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "----------------------------"
line3 = str(f"Total Votes: {len(total_votes)}")
line4 = "----------------------------"
line5 = str(f"Name: % (votes)")
line6 = str(f"Name: % (votes)")
line7 = str(f"Name: % (votes)")
line8 = str(f"Name: % (votes)")
line9 = "----------------------------"
line8 = str(f"Winner: % (votes)")
line10 = "----------------------------"
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10))

