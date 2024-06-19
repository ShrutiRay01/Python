# Write a program that asks the user for their birth year and calculates their age.

# Function to calculate age based on birth year
def calculate_age(birth_year):
    # Get the current year
    from datetime import datetime
    current_year = datetime.now().year
    
    # Calculate the age
    age = current_year - birth_year
    
    return age

# Taking input from the user for birth year
birth_year = int(input("Enter your birth year: "))

# Calculating the age by calling the function
age = calculate_age(birth_year)

# Printing the age
print(f"You are {age} years old.")
