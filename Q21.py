# Write a python program that counts the occurrences of a specific element in a list.

# Function to count occurrences of a specific element in a list
def count_occurrences(input_list, element):
    count = 0
    
    # Iterate through the list and count occurrences of the element
    for item in input_list:
        if item == element:
            count += 1
    
    return count

# Example list
example_list = [1, 2, 3, 4, 2, 2, 3, 1, 2, 5]

# Element to count occurrences of
target_element = 2

# Counting occurrences by calling the function
occurrences = count_occurrences(example_list, target_element)

# Printing the result
print(f"The element {target_element} appears {occurrences} times in the list.")
