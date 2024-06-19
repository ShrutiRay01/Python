# Write a python program that calculates the sum of the digits of a given number.

# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Initialize sum to 0
    sum_digits = 0
    
    # Iterate through each digit of the number
    while number > 0:
        # Add the last digit to sum_digits
        sum_digits += number % 10
        # Remove the last digit from the number
        number //= 10
    
    return sum_digits

# Taking input from the user
num = int(input("Enter a number: "))

# Calculating the sum of digits
result = sum_of_digits(num)

# Printing the result
print(f"The sum of digits of {num} is: {result}")
