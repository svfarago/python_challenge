# What: Module in Python paths across operating systems
import os

# What: Module in Python reads CSV files
import csv

# What: Method open -- Read using open method open(csvpath) as csvfile
# Notes: csvpath is a string variable--creates joined path as string -- /resources/election_data.csv
# Notes: txtoutput is a string variable --creates output.txt in existing subdirectory "Analysis"
csvpath = os.path.join("Resources", "election_data.csv")
txtoutput = os.path.join("Analysis", "output.txt")

# What: Create variables
# Notes: [ ] signifies an empty list placeholder/container for future content (calculations, lists, etc.) 
# Notes: Votes and other variables are declaired farther down in % candidate votes where code sequence matters.
all_votes = []
candidates = []
percent_votes = []
candidate_votes = []


# What: Opens csv file using reader method
with open(csvpath) as election:

     # Notes: Delimiter and variable holds contents--comma in this case
    csvreader = csv.reader(election,delimiter=",") 

    # What: Identifies, reads, and skips header in csv file when reading data
    # Notes: To confirm file is being read print it to the screen as f string >> print(f"CSV Header: {header}")
    header = next(csvreader)

    # What: Iterate through the rows
    for row in csvreader: 

    # What: Puts the total votes values to their corresponding lists using [0] for first column
    # Notes: append = list and means to go through all rows and store data within [] container | int converts profit to number 
        all_votes.append(row[0])

        # What: Creates a candidate list using "candidate []" container above plus each candidate's votes
        # Notes: If scans [2]=column 3 through the entire list and if the candidate name hasn't already been found, add the candidate name to the list and count their vote (candidate_votes)
        # Notes: Else = if candidate's name is already in the list, don't re-add name but DO count their vote (candidate_votes)
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1

    
    # What: Define variable total_votes as an integer to be used to calculate % all_votes (< all_votes is currently a list and cannot be used in a formula)
    total_votes = (len(all_votes))
   
    # What: Iterate through candidate_votes [list]
    for votes in candidate_votes: 

        # What: Calculates percentage of votes values to their corresponding lists using [0] for first column
        # Notes: Must make candidate_votes and all_votes integer otherwise can't divide lists, must divide numbers
        # Notes: Tip - Use print statement to ensure code and data is correct >> print (percent_votes) | print (candidate_votes) | print (all_votes)
        # Notes: "%.3f%%" -- 3f provides percent decimal to three places (x.000 %) | this is just the syntax to be used as it is coded this way

        percent = (votes/total_votes) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        percent_votes.append(percent)


    # What: Flags winning candidate
    # Notes: Winner looks at max number of candidate votes in candidates index
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    winner_candidate = candidates[index]

# What: Prints
# Notes: len counts # items in a container | Use "round" and "2" to round to second decimal otherwise really long decimal number
# Notes:Using {} to convert info to string format
# Notes:The "for i in range" creates a mini-loop to print out the 4 candidates on each line. | print statement needs [i] for each field so it prints specific data for each candidate
# Notes:Otherwise it just lists one candidate and their vote if using > print(f"name: {candidates} (${(str(candidate_votes))})")

print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(all_votes)}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")
print("----------------------------")
print(f"Winner: {winner_candidate}")
print("----------------------------")


# What: Outputs to text file in Analysis subdirectory
# Notes: "w" for write | \n = hard return | output references "txtoutput" path variable at beginning of code so it knows where to .txt file and what to name it as output.txt
# Notes: {} are placeholders with /n as hard returns for lines 1-7.

output = open(txtoutput,"w")
line1 = "Election Results"
line2 = "----------------------------"
line3 = str(f"Total Votes: {len(all_votes)}")
line4 = "----------------------------"
output.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "----------------------------"
line6 = str(f"Winner: {winner_candidate}")
line7 = "----------------------------"
output.write('{}\n{}\n{}\n'.format(line5,line6,line7))

