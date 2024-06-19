# Write a python program that takes a string as input and returns its length.
# Function to calculate the length of a string
def string_length():
    # Taking a string input from the user
    user_input = input("Enter a string: ")
    
    # Calculating the length of the string
    length = len(user_input)
    
    # Printing the length of the string
    print(f"The length of the entered string is: {length}")

# Calling the function
string_length()
