def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:  # Check if the denominator is not zero
        return x / y
    else:
        return "Error! Division by zero."

# Main program to interact with the user
def calculator():
    print("Welcome to the Python Calculator!")

    # Ask the user to choose an operation
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user's choice
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Ask the user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform the operation based on user's choice
    if choice == '1':
        print(f"The result of {num1} + {num2} is {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a number between 1 and 4.")

# Run the calculator
calculator()