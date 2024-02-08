'''Calculator Program'''
from calculator import add, subtract, multiply, divide

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
    number1 = float(input("Enter a Number: "))
    operation = str(input("Enter an Operation:")).lower()
    number2 = float(input("Enter a Second Number: "))

    if operation == "addition":
        print(add(number1,number2))

    elif operation == "subtraction" :
        print(subtract(number1,number2))

    elif operation == "multiplication":
        print(multiply(number1,number2))

    elif operation == "division":
        print(divide(number1,number2))

    else:
        pass

main()

input("\nPress <Enter> to quit.")
