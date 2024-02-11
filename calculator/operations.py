'''Function: Operations'''

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
        # Handles Divide By Zero Exception
        return "Cannot divide by zero!"

    return a / b
