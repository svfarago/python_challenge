# What: Module in Python paths across operating systems
import os

# What: Module in Python reads CSV files
import csv

# What: Method open -- Read using open method open(csvpath) as csvfile
# csvpath is a string value--creates joined path as string -- /resources/election_data.csv
csvpath = os.path.join("Resources", "election_data.csv")


# VARIABLES - Create placeholder for future content | [ ] signifies an empty list.
# Notes: Use [] container for calculations/lists.

all_votes = []
candidates = []
percent_votes = []
candidate_votes = []
percent_votes = []
#total_votes = 0

# What: Opens csv file using reader method
with open(csvpath) as election:

     # Notes: Delimiter and variable holds contents--comma in this case
    csvreader = csv.reader(election,delimiter=",") 

    # What: Identifies and skips header in csv file
    # Notes: To confirm file is being read print it to the screen using >> print(f"CSV Header: {csv_header}") | f converts all to string
    header = next(csvreader)

    # What: Iterate through the rows
    for row in csvreader: 

    # Puts the total votes values to their corresponding lists using [0] for first column
    # Notes: append means to go through all rows and act as a container
        all_votes.append(row[0])


        #What: Create unique candidate list using "candidate []" container above to hold, along with a vote in his/her name.
        # Notes: [2]=column 3, so this scans through the entire list and if the candidate name hasn't already been found
            # and put into the candidates container [], then it appends (adds) the candidate name to the list. 
            # Else = if candidate's name is already in the list, don't re-add but DO count their vote (candidate_votes)
            # Append adds new candidate to the end of the existing candidates list & adds number of votes to the votes list.
            # POTATO - review this for understanding > Append and index are python list methods. White index must be defined otherwise error
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1

    
    #What:Calculates % of candidate votes
    # Notes: Iterate through the rows
    #for votes in candidate_votes: 

    # Puts the percent of votes values to their corresponding lists using [0] for first column
    # POTATO - Notes: must make candidate_votes and all_votes integer otherwise can't divide lists, must divide numbers

        #percent = (candidate_votes/all_votes) * 100
        #percent = round(percent)
        #percent = "%.3f%%" % percent # POTATO: try "%3f" (example 7 at python reference)
        #percent_votes.append(percent)


    # What: Flags winning candidate.
    # Notes: winner looks at max number of candidate votes | POTATO - clarify index references.
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    winner_candidate = candidates[index]

# What: Prints
# Notes: len counts # items in a container | Use "round" and "2" to round to second decimal otherwise really long decimal number
# Using {} to convert info to string format
# The "for i in range" creates a mini-loop to print out the 4 candidates on each line.
# Otherwise it just lists one candidate and their vote > print(f"name: {candidates} (${(str(candidate_votes))})")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(all_votes)}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: ({str(candidate_votes[i])})")  
print("----------------------------")
print(f"Winner: {winner_candidate}")
print("----------------------------")


# What: Outputs to text file
# Notes: "w" for write | \n = hard return | the {} just placeholders with /n as hard returns for lines.
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "----------------------------"
line3 = str(f"Total Votes: {len(all_votes)}")
line4 = "----------------------------"
output.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: ({str(candidate_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "----------------------------"
line6 = str(f"Winner: {winner_candidate}")
line7 = "----------------------------"
output.write('{}\n{}\n{}\n'.format(line5,line6,line7))

