# Write a python program that checks if a substring is present in a given string.

# Function to check if a substring is present in a given string
def check_substring():
    # Taking the main string input from the user
    main_string = input("Enter the main string: ")
    
    # Taking the substring input from the user
    substring = input("Enter the substring to check: ")
    
    # Checking if the substring is present in the main string
    if substring in main_string:
        print(f"The substring '{substring}' is present in the main string.")
    else:
        print(f"The substring '{substring}' is not present in the main string.")

# Calling the function
check_substring()
