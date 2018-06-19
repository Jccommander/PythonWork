# Goal is to take a list of election votes, and return the total number of votes cast, a complete list of
# candidates who received votes, the percentage of votes each candidate won, the total number of votes
# each candidate won, and the winner of the election based on popular vote

# The dataset is over a million rows, with three fixed columns, one listing a voter ID, one listing a county
# and the last listing which candidate the voter voted for

# Import modules for use

import os
import csv

# Create path to CSV file

electionpath = os.path.join('..', 'CSV Files', 'election_data.csv')

# Create variable for total votes and the winner, both set to 0

total_vote = 0
winner = 0

# Create two dictionaries, one to store the individual candidates and their votes, and the other to hold
# the candidates percentage values; also create a list for candidate names

can_dict = {}
percent_dict = {}
can_list = []

# Create function to count the votes for individual candidates

def voteCounter(candidate):

    # First, the function should check to see if a candidate is present in the dictionary, if not
    # then the candidate should be added to the dictionary with a starting value of 1

    if row[2] not in can_dict:
        can_dict[row[2]] = 1
    
    # If the candidate is already present, then their tally should be increased by 1

    else:
        can_dict[row[2]] = can_dict[row[2]] + 1

# Open and read the CSV file

with open(electionpath, newline='') as electionfile:
    electionreader = csv.reader(electionfile, delimiter=',')

    # Skip the header of the dataset

    next(electionreader)

    # Iterate through the spreadsheet, counting each vote and running the vote counter function on each row
    # Then, it captures the individual candidate names so they can be matched with their count later

    for row in electionreader:
        total_vote = total_vote + 1
        voteCounter(row)
        if row[2] not in can_list:
            can_list.append(row[2])
        
    # Calculate the percentage of votes won by a candidate
        # Iterate through the now completed dictionary, performing a percentage equation for each candidate.
        # These percentage values should be stored in the percent dictionary

    for candidate in can_dict:
        percent_dict[candidate] = (round(can_dict[candidate] / total_vote * 100,2))

    # Also during this iteration, a conditional should be made that compares the total vote tally of each
    # candidate to see who has the most points, storing the highest value in the winner variable, and the
    # candidate string in a new variable called winner_str so that it can be called later
        if can_dict[candidate] > winner:
            winner = can_dict[candidate]
            winner_str = candidate

# Print results with formatting

    # To print the list of candidates, percentages and total votes, use a for loop to iterate for as many
    # candidates that are present

print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_vote}")
print("---------------------------")

for candidate in can_list:
    print(candidate + ": " + str(percent_dict[candidate]) + "% (" + str(can_dict[candidate]) + ")")

print("---------------------------")
print(f"Winner: {winner_str}")
print("---------------------------")

# Export results in a text file

    # Set an output path for the text file

output_path = os.path.join(".", "Election-Results.csv")

    # Create and open the new text file

with open(output_path, 'w', newline='') as csvfile:

    # Set the file to write

    electionwriter = csv.writer(csvfile, delimiter=',')

    # Write the individual lines to be printed to the text file

    electionwriter.writerow(["Election Results"])
    electionwriter.writerow(["---------------------------"])
    electionwriter.writerow([f"Total Votes: {total_vote}"])
    electionwriter.writerow(["---------------------------"])

    for candidate in can_list:
        electionwriter.writerow([candidate + ": " + str(percent_dict[candidate]) + "% (" + str(can_dict[candidate]) + ")"])

    electionwriter.writerow(["---------------------------"])
    electionwriter.writerow([f"Winner: {winner_str}"])
    electionwriter.writerow(["---------------------------"])