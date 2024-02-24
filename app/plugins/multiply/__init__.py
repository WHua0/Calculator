# pylint: disable=too-few-public-methods

'''Multiply Command'''
from decimal import Decimal, InvalidOperation
from app.commandmanager import Command
from calculator import Calculator

class MultiplyCommand(Command):
    '''Asks for Two Numbers, then Multiplies'''
    def execute(self):
        # Asks for two numbers
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        try:
            # Tries to convert a and b into decimal objects
            a_decimal, b_decimal = map(Decimal, [a, b])
            # If successful, multiplies a and b, and prints result
            result = Calculator.multiply(a_decimal, b_decimal)
            print(f'The result of {a} multiply {b} is equal to {result}.')

        except InvalidOperation:
            # If cannot, print invalid numbers
            print(f'Invalid number input: {a} or {b} is not a valid number.')
