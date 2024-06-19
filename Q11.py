# Write a python program that generates the first n numbers in the Fibonacci sequence.

# Function to generate the first n numbers in the Fibonacci sequence
def fibonacci_sequence(n):
    # Initialize the first two numbers in the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to the nth number
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Taking input from the user for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate the Fibonacci sequence
fib_numbers = fibonacci_sequence(n)

# Printing the Fibonacci sequence
print(f"The first {n} numbers in the Fibonacci sequence are:")
print(fib_numbers)
