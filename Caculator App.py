# Calculator App

def calculator():
    print("Welcome to Calculator App")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operation."

    print(f"Result: {result}")

# Calling the calculator function
calculator()
