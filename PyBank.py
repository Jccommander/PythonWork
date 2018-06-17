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

# Set variable for total months at zero

    totalmonths = 0
    totalprofits = 0
    greatest_inc = 0
    greatest_dec = 0

# Create an empty list to store changes month over month in order to create an average

    avglist = []

    # Count the total number of months in the dataset

    for row in budgetreader:
        totalmonths = totalmonths + 1

    # Add the total profits and losses together

        totalprofits = totalprofits + int(row[1])

    # Average the profits and losses
        #Start by capturing each change month over month
        

    # Find the greatest increase in profits
        # Create a conditional that checks if the current value is bigger than the previous stored
        # value. If it is, then commit that value to the variable
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])

    # Find the greatest decrease in profits
        # Create a conditional that checks if the current value is smaller than the previous stored
        # value. If it is, then commit that value to the variable
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])

# Print each resulting number to the terminal with descriptions and formatting

# Write a new text file