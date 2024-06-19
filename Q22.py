# Function to find minimum and maximum values in a list of numbers
def find_min_max(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None  # Return None for both min and max if the list is empty
    
    # Using min() and max() functions to find minimum and maximum values
    minimum = min(numbers)
    maximum = max(numbers)
    
    return minimum, maximum

# Example list of numbers
numbers = [5, 8, 2, 10, 3, 7]

# Finding minimum and maximum values by calling the function
min_value, max_value = find_min_max(numbers)

# Printing the results
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
