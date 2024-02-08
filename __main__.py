'''Calculator Program'''
from calculator import add, subtract, multiply, divide, input_number, input_operation

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
    number1 = input_number()
    operation = input_operation()
    number2 = input_number()

    # Calculate
    if operation == "addition":
        print(add(number1,number2))

    elif operation == "subtraction":
        print(subtract(number1,number2))

    elif operation == "multiplication":
        print(multiply(number1,number2))

    elif operation == "division":
        if number2 == 0:
            print("Cannot Divide By 0!")
        else:
            print(divide(number1,number2))

    else:
        pass

main()

input("\nPress <Enter> to quit.")
