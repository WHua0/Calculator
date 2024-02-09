'''Function: Operations'''
@staticmethod
def add(a,b):
    '''Add a and b'''
    return a + b

@staticmethod
def subtract(a,b):
    '''Subtract a and b'''
    return a - b

@staticmethod
def multiply(a,b):
    '''Multiple a and b'''
    return a * b

@staticmethod
def divide(a,b):
    '''Divide a by b'''
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
