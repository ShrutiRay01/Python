# Write a program that reads data from a CSV file and prints it to the console.
import csv

# Function to read and print data from a CSV file
def read_csv_file(filename):
    try:
        # Open the CSV file for reading
        with open(filename, 'r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Iterate over each row in the CSV
            for row in csv_reader:
                print(', '.join(row))  # Print each row as comma-separated values
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

# File name to read from
filename = 'data.csv'

# Call the function to read and print data from the CSV file
read_csv_file(filename)
