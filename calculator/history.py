# pylint: disable=too-few-public-methods
'''Manages Calculations History'''
from decimal import Decimal

class History:
    '''Class History'''
    history = []

    @classmethod
    def create_log(cls, a: Decimal, b: Decimal, operation):
        '''Converts a new calculation to floats and string'''
        cls.a = a
        cls.b = b
        # Converts Opperation Function to a String
        cls.operation = operation.__name__
        return (cls.a, cls.b, cls.operation)

    @classmethod
    def add_calculation(cls, calculation):
        '''Adds a new calculation to the history'''
        cls.history.append(calculation)

    @classmethod
    def show_history(cls):
        '''Retrieves the entire calculation history'''
        if cls.history:
            return cls.history
        # If there no is history, returns history
        return 'No History!'

    @classmethod
    def clear_history(cls):
        '''Clears the calculation history'''
        return cls.history.clear()

    @classmethod
    def show_previous(cls):
        '''Retrieves the previous calculation'''
        if cls.history:
            return cls.history[-1]
        # If there no is history, returns history
        return 'No History!'
