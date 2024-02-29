# pylint: disable = too-few-public-methods

'''Divide Command'''
from app.commandmanager import Command
from calculator.calculateprint import calculate_and_print

class DivideCommand(Command):
    '''Asks for Two Numbers, Divides, and Prints'''

    def execute(self):

        # Asks for two numbers
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        # Calculates and Prints
        calculate_and_print(a, b, 'divide')
