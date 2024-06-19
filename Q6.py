# Write a program that reads the content of a text file and prints it to the console.

# Function to read the content of a text file and print it
def read_from_file():
    # Specifying the name of the text file
    filename = "user_input.txt"
    
    try:
        # Reading the content of the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Printing the content to the console
        print("Content of the file:")
        print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Calling the function
read_from_file()
