# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Start of the loop
while True:
    # Take two numbers and the operation from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the operation
    if operation == "+":
        print(f"The result is: {add(num1, num2)}")
    elif operation == "-":
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == "*":
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == "/":
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid operation! Please enter one of +, -, *, /.")

    # Ask the user if they want to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break  # Exit the loop if the user doesn't want to continue
