'''Function: Operations'''
from decimal import Decimal

def add(a: Decimal, b: Decimal):
    '''Adds a and b'''
    return a + b

def subtract(a: Decimal, b: Decimal):
    '''Subtracts a and b'''
    return a - b

def multiply(a: Decimal, b: Decimal):
    '''Multiplies a and b'''
    return a * b

def divide(a: Decimal, b: Decimal):
    '''Divides a by b'''
    if b == 0:
        # Handles Divide By Zero Exception
        return 'Cannot divide by zero!'

    return a / b
