# pylint: disable=too-few-public-methods

'''Add Command'''
from app.commandmanager import Command
from calculator.calculateandprint import calculate_and_print

class AddCommand(Command):
    '''Asks for Two Numbers, Adds, and Prints'''

    def execute(self):

        # Asks for two numbers
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        # Calculates and Prints
        calculate_and_print(a, b, 'add')
