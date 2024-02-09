'''Calculator'''

# from calculator.operations import add, subtract, multiply, divide

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
        return "Cannot divide by zero!"
    return a / b
