#Serial search 

import os
import csv

def main():
    # Path to the CSV file (ensures the file is in the same directory or provide the correct path)
    csv_path = os.path.join("budget_data.csv")

    # Example target date to search for
    target_date = "Sep-26"
    
    # Tests the serial search with the target date.
    test_serial_search(csv_path, target_date)

# Function to analyze financial data and load it into memory.
def load_financial_data(csv_path):
    financial_data = []

    with open(csv_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skips the header row
        
        for row in csvreader:
            date = row[0]
            profit_losses = int(row[1])
            financial_data.append((date, profit_losses))

    return financial_data

# Serial search (linear search) to find Profit/Losses by date.
def serial_search(financial_data, target_date):
    for record in financial_data:
        date, profit_losses = record
        if date == target_date:
            return profit_losses
    return None  # Returns None if the date is not found.

# Function to test the serial search
def test_serial_search(csv_path, target_date):
    # Loads the financial data.
    financial_data = load_financial_data(csv_path)
    
    # Performs serial search for the target date.
    result = serial_search(financial_data, target_date)
    
    # Prints out the result.
    if result is not None:
        print(f"Profit/Losses for {target_date}: ${result}")
    else:
        print(f"Date {target_date} not found in the dataset.")

# Calls the main function.
main()




    