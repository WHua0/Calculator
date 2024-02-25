# pylint: disable=too-few-public-methods
# pylint: disable = broad-exception-caught

'''Multiply Command'''
from decimal import Decimal, InvalidOperation
from app.commandmanager import Command
from calculator import Calculator

class DivideCommand(Command):
    '''Asks for Two Numbers, then Divides'''
    def execute(self):
        # Asks for two numbers
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        try:
            # Tries to convert a and b into decimal objects
            a_decimal, b_decimal = map(Decimal, [a, b])
            # If successful, divides a by b, and prints result
            result = Calculator.divide(a_decimal, b_decimal)
            print(f'The result of {a} divide {b} is equal to {result}.')

        except InvalidOperation:
            # If cannot, print invalid numbers
            print(f'Invalid number input: {a} or {b} is not a valid number.')

        except Exception as e:
            # Catch-All for Unexpected Errors
            print(f'An error occurred: {e}.')
