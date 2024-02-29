# pylint: disable=too-few-public-methods

'''Subtract Command'''
from app.commandmanager import Command
from calculator.calculateprint import calculate_and_print

class SubtractCommand(Command):
    '''Asks for Two Numbers, Subtracts, and Prints'''

    def execute(self):

        # Asks for two numbers
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        # Calculates and Prints
        calculate_and_print(a, b, 'subtract')
