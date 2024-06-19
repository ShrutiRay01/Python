# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase (assuming case insensitive comparison)
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries to store character frequencies
    frequency1 = {}
    frequency2 = {}
    
    # Count frequencies of characters in str1
    for char in str1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1
    
    # Count frequencies of characters in str2
    for char in str2:
        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1
    
    # Compare the two frequency dictionaries
    return frequency1 == frequency2

# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams by calling the function
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
