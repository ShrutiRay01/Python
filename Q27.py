# Write a program in python that converts a string into a list of its characters.

def string_to_list(input_string):
    # Using list comprehension to convert string to list of characters
    char_list = [char for char in input_string]
    
    return char_list

# Example usage:
input_string = "Hello, World!"

# Converting string to list of characters
char_list = string_to_list(input_string)

# Output the result
print(f"The string '{input_string}' converted to a list of characters is:")
print(char_list)
