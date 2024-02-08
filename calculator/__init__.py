'''Definitions'''

def add(a,b):
    '''Add a and b'''
    return a + b

def subtract(a,b):
    '''Subtract a and b'''
    return a - b

def multiply(a,b):
    '''Multiple a and b'''
    return a * b

def divide(a,b):
    '''Divide a by b'''
    return a / b

def check_number(num):
    '''Checks if input is a number'''
    while True:
        try:
            int(num)
            return float(num)
        except ValueError:
            try:
                float(num)
                return float (num)
            except ValueError:
                print(num, "is not valid number!")
                num = input("Enter a Number: ")

def check_operation(op):
    '''Checks if input is a math operation'''
    while True:
        if op in ("addition", "add", "+"):
            return "addition"
        if op in ("subtraction", "subtract", "-"):
            return "subtraction"
        if op in ("multiplication", "multiply", "*"):
            return "multiplication"
        if op in ("division", "divide", "/"):
            return "division"
        print(op, "is not valid math operation!")
        op = input("Enter a Operation: ").lower()
