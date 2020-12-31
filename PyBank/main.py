# Module in Python os--for path across operating systems
import os

# Module in Python csv--for reading CSV files
import csv

# csvpath is a string value--creates joined path as string -- /resources/budget_data.csv
csvpath = os.path.join("Resources", "budget_data.csv")

# Method open -- Read using open method open(csvpath) as csvfile
csvfile = open(csvpath)

# Opens csv file using reader method; delimiter and variable holds contents--comma in this case
csvreader = csv.reader(csvfile, delimiter=',')

print(csvreader)

# Reads header--f converts all to string
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")

# Reads data as a row
for row in csvreader:
    print(row)


# CALCULATIONS




# EXPORT text file with results

#Specify file output
output_path = os.path.join("Analysis", "budget_results.csv")

#Open file with "write" mode and specify variable to hold the contents--with closes file after
with open (output_path, 'w') as csvfile:

    #initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #write header row
    csvwriter.writerow (['Date','Profit/Losses'])

    # Write second row
    csvwriter.writerow (['Jan-2010','867884'])








