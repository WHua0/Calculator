# pylint: disable = too-few-public-methods

'''Multiply Command'''
import logging
from app.commandmanager import Command
from calculator.calculateandprint import calculate_and_print

class MultiplyCommand(Command):
    '''Asks for Two Numbers,  Multiplies, and Prints'''

    def execute(self):

        # Asks for two numbers
        a = input('Please provide the 1st Number: ')
        b = input('Please provide the 2nd Number: ')

        # Calculates and Prints
        calculate_and_print(a, b, 'multiply')
        logging.info("Values: '%s', '%s' attempted.", a, b)
