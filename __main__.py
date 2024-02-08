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

    # Calculate
    if operation in ("addition", "add", "+"):
        print(add(number1,number2))

    elif operation in ("subtraction", "subtract", "-"):
        print(subtract(number1,number2))

    elif operation in ("multiplication", "multiply", "*"):
        print(multiply(number1,number2))

    elif operation in ("division", "divide", "/"):
        if number2 == 0:
            print("Cannot Divide By 0!")
        else:
            print(divide(number1,number2))

    else:
        pass

main()

input("\nPress <Enter> to quit.")
