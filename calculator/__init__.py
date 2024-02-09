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
    if b == 0:
        return "error"
    return a / b

def check_number(num):
    '''Checks if input is a number'''
    try:
        float(num)
        return float(num)
    except ValueError:
        print(num, "is not valid number!")
        return "error"

def check_operation(op):
    '''Checks if input is a math operation'''
    op = str(op).lower()
    if op in ("addition", "add", "+"):
        return "+"
    if op in ("subtraction", "subtract", "-"):
        return "-"
    if op in ("multiplication", "multiply", "*"):
        return "*"
    if op in ("division", "divide", "/"):
        return "/"
    print(op, "is not a valid math operation!")
    return "error"
