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

    # Input Numbers and Math Operations
    number1 = input("Enter a Number: ")
    number1 = check_number(number1)

    operation = (input("Enter a Operation: ")).lower()
    operation = check_operation(operation)

    number2 = input("Enter a 2nd Number: ")
    number2 = check_number(number2)

    # Calculate
    if operation == "addition":
        add(number1,number2)

    elif operation == "subtraction":
        subtract(number1,number2)

    elif operation == "multiplication":
        multiply(number1,number2)

    elif operation == "division":
        if number2 == 0:
            print("Cannot Divide By 0!")
        else:
            divide(number1,number2)

    else:
        pass

main()

input("\nPress <Enter> to quit.")
