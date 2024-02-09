'''Calculator Program'''
from calculator import add, subtract, multiply, divide, check_number, check_operation

def print_intro():
    '''Introduction'''
    print("Welcome User!")
    print("This is a Basic Calculator Program")
    print("for Addition, Substraction, Multiplication, and Division.")
    print("Created by Wilber Hua")
    print()

def main():
    '''Main Program'''
    print_intro()

    # Input first number
    number1 = input("Enter a Number: ")

    # If Input returns error, try again
    while check_number(number1) == "error":
        number1 = input("Enter a Number: ")
    number1 = float(number1)

    # Input math operation
    operation = input("Enter a Operation: ")

    # If Input returns error, try again
    while check_operation(operation) == "error":
        operation = input("Enter a Operation: ")
    operation = check_operation(operation)

    # Input second number
    number2 = input("Enter a Number: ")

    # If Input returns error, try again
    while check_number(number2) == "error":
        number2 = input("Enter a Number: ")
    number2 = float(number2)

    # Calculate
    result = ""

    if operation == "+":
        result = add(number1,number2)

    if operation == "-":
        result = subtract(number1,number2)

    if operation == "*":
        result = multiply(number1,number2)

    if operation == "/":
        result = divide(number1,number2)

    # Print Result
    print(number1, operation, number2, "=", result)

main()

input("\nPress <Enter> to quit.")
