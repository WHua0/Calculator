'''Class Operation'''
from decimal import Decimal

class Operation:
    '''Class Operation'''

    @staticmethod
    def add(a: Decimal, b: Decimal):
        '''Adds a and b'''
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal):
        '''Subtracts a and b'''
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal):
        '''Multiplies a and b'''
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal):
        '''Divides a by b'''
        if b == 0:
            # Handles Divide By Zero Exception
            raise ZeroDivisionError('Cannot divide by zero')

        return a / b
    