# Write a program that takes a string input from the user and writes it to a text file.

def write_to_file():
    # Taking a string input from the user
    user_input = input("Enter a string to write to a text file: ")
    
    # Specifying the name of the text file
    filename = "input.txt"
    
    # Writing the user input to the file
    with open(filename, 'w') as file:
        file.write(user_input)
    
    # Informing the user that the input has been written to the file
    print(f"Your input has been written to {filename}.")

# Calling the function
write_to_file()
