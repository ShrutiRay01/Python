# Write a python program that removes all punctuation from a given string.

import string

def remove_punctuation(input_string):
    # Using string.punctuation to get all punctuation characters
    punctuations = string.punctuation
    
    # Using list comprehension to filter out punctuation characters
    no_punct_string = ''.join([char for char in input_string if char not in punctuations])
    
    return no_punct_string

# Taking input from the user
input_string = input("Enter a string with punctuation: ")

# Removing punctuation by calling the function
cleaned_string = remove_punctuation(input_string)

# Printing the string without punctuation
print(f"The string without punctuation is: {cleaned_string}")
