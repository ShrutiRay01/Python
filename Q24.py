
# Function to perform calculation based on operator
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Main program
print("Simple Calculator Program")
print("Supported operations: +, -, *, /")

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Performing calculation and printing the result
result = calculator(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")
