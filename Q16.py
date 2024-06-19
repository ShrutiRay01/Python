# Write a program in python that counts the frequency of each character in a string.
# Function to count the frequency of each character in a string
def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count of each character in the dictionary
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

# Taking input from the user
input_string = input("Enter a string: ")

# Calculating character frequencies by calling the function
char_frequency = count_character_frequency(input_string)

# Printing the character frequencies
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"{char}: {freq}")
