#Write a python program that calculates the factorial of a given number.
# Function to calculate the factorial of a number
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Taking input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Checking if the input is a non-negative integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculating the factorial
    result = factorial(num)
    # Printing the result
    print(f"The factorial of {num} is {result}.")
