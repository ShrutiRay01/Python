#Write a python program that checks whether a given number is even or odd.

# Function to check if a number is even or odd
def check_even_odd():
    # Taking input from the user
    num = int(input("Enter a number: "))
    
    # Checking if the number is even or odd
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")

# Calling the function
check_even_odd()
