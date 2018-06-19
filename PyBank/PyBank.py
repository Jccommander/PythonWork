# Goals: Create script that takes CSV file and counts total number of months in the dataset, total net
# amount of profit/losses, the average change in profit/losses between months, the greatest increase in
# profits (date and amount) over the entire period, and the greatest decrease in losses (date and amount)

# The CSV data set is a series of rows organized by two columns, one containing dates, and the other
# containing sets of numbers representing profits / losses, assumption is that the dataset will always
# be organized by date in chronological order

# Import os and csv modules for use

import os
import csv

# Path to the CSV file

budgetpath = os.path.join('..','CSV Files','budget_data.csv')

# Open the CSV file, and set it to read

with open(budgetpath, newline='') as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=',')

    # Skip the header in the dataset

    next(budgetreader)

# Set variable for total months, total profits, greatest increase, greatest decrease and previous value to
# zero

    totalmonths = 0
    totalprofits = 0
    greatest_inc = 0
    greatest_dec = 0
    prev_val = 0

# Create an empty list to store changes month over month in order to create an average

    avglist = []

    # Count the total number of months in the dataset

    for row in budgetreader:
        totalmonths = totalmonths + 1

    # Add the total profits and losses together

        totalprofits = totalprofits + int(row[1])

    # Average the profits and losses
        # First, capture the current row value
        curr_val = int(row[1])
        # Append the average list with the current value minus the previous value
        avglist.append(curr_val - prev_val)
        # Set the previous value to the current row, so it's ready for the next loop
        prev_val = int(row[1])

    # Find the greatest increase in profits
        # Create a conditional that checks if the current value is bigger than the previous stored
        # value. If it is, then commit that value to the variable
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            great_inc_string = row[0]

    # Find the greatest decrease in profits
        # Create a conditional that checks if the current value is smaller than the previous stored
        # value. If it is, then commit that value to the variable
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            great_dec_string = row[0]

# Finish the average change over months by taking the average list, summing it, then dividing it by the
# total number of items in the list

final_avg = round(sum(avglist) / len(avglist),2)

# Print each resulting number to the terminal with descriptions and formatting

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofits}")
print(f"Average Change: ${final_avg}")
print(f"Greatest Increase in Profits: {great_inc_string} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {great_dec_string} (${greatest_dec})")

# Write a new text file
    
    # Set an output path for the text file

output_path = os.path.join(".", "Financial-Analysis.csv")

    # Create and open the new text file

with open(output_path, 'w', newline='') as csvfile:

    # Set the file to write

    financewriter = csv.writer(csvfile, delimiter=',')

    # Write the individual lines to be printed to the text file

    financewriter.writerow(["Financial Analysis"])
    financewriter.writerow(["------------------------------"])
    financewriter.writerow([f"Total Months: {totalmonths}"])
    financewriter.writerow([f"Total: ${totalprofits}"])
    financewriter.writerow([f"Average Change: ${final_avg}"])
    financewriter.writerow([f"Greatest Increase in Profits: {great_inc_string} (${greatest_inc})"])
    financewriter.writerow([f"Greatest Decrease in Profits: {great_dec_string} (${greatest_dec})"])