'''Function: Operations'''

def add(a, b):
    '''Adds a and b'''
    return a + b

def subtract(a, b):
    '''Subtracts a and b'''
    return a - b

def multiply(a, b):
    '''Multiplies a and b'''
    return a * b

def divide(a, b):
    '''Divides a by b'''
    if b == 0:
        # Handles Divide By Zero Exception
        return "Cannot divide by zero!"

    return a / b
