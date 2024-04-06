import os
import csv
# set the path to the csv file
file_path = os.path.join("..","resources","election_data.csv")
# assiging variables
name_count = {}
total_votes = 0

def count_assign_names(file_path):
    
    # read the csv file
 with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        name = row[2]
        total_votes += 1
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
  
# Assigning name to variables
charles_Casper_Stockham = name_count.get("Charles Casper Stockham", 0)
diana_DeGette = name_count.get("Diana DeGette", 0)
raymon_Anthony_Doane = name_count.get("Raymon Anthony Doane", 0)

return charles_Casper_Stockham, diana_DeGette, raymon_Anthony_Doane


print("Election Results")
print("--------------------------------")
print(f"Total Vots: {total_votes}")
primt(f'Charles Casper Stockham:', charles_Casper_Stockham)
print(f'Diana DeGette:', diana_DeGette )
print(f'Raymon Anthony Doane:', raymon_Anthony_Doane)
print(f'Winner:', diana_DeGette)


#printing to text file
with open(file_path, "w") as text_file:
    output = (
"Election Results\n"
"---------------------------\n"
f"Total Vots: {total_votes}"
f'Charles Casper Stockham:', charles_Casper_Stockham\
f'Diana DeGette:', diana_DeGette 
f'Raymon Anthony Doane:', raymon_Anthony_Doane
f'winner:',diana_DeGette)












































































