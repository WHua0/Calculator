# pylint: disable=too-few-public-methods

'''Add Command'''
from decimal import Decimal, InvalidOperation
from app.commandmanager import Command
from calculator import Calculator

class AddCommand(Command):
    '''Asks for Two Numbers, then Add'''
    def execute(self):
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            result = Calculator.add(a_decimal, b_decimal)
            print(f'The result of {a} plus {b} is equal to {result}.')

        except InvalidOperation:
            print(f'Invalid number input: {a} or {b} is not a valid number.')
