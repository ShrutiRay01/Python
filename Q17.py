# Write a program in python that converts a given string to title case (first letter of each word capitalized).

# Function to convert a string to title case
def convert_to_title_case(input_string):
    # Using the title() method to convert to title case
    title_case_string = input_string.title()
    
    return title_case_string

# Taking input from the user
input_string = input("Enter a string: ")

# Converting the string to title case by calling the function
title_case_string = convert_to_title_case(input_string)

# Printing the title case string
print(f"The string in title case is: {title_case_string}")
