# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
# csv_file = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
file_to_output = os.path.join("Resources", "budget_analysis.csv")  #creating the output to populate within this folder via a csv format

# Define variables to track the financial data
total_months = 0
total_net = 0
# my added variables to track
initial_value = None
final_value = None
total_change = []
dates = []
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
#     lines = financial_data.read()
#     print(lines)
#     print(type(lines))

    # Skip the header row/Extract first row to avoid appending to net_change_list
    header = next(reader)

    # reading each row of data after the header (my added note)/Process each row of data
    for row in reader:
        date = row[0]
        # assuning relevant data is in second row
        current_profit = int(row[1])

     # Track the total and net change
        total_months += 1
        total_net +- current_profit

    # Process each row of data
    # for row in reader:

        # # Track the total
        # total_change += value

        # # Track the net change

        # Calculate the greatest increase in profits (month and amount)

        # Calculate the greatest decrease in losses (month and amount)
   
# Calculate the average net change across the months

# Generate the output summary


# Print the output


# Write the results to a text file

