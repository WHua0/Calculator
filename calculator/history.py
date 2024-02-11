# pylint: disable=too-few-public-methods
'''Manages Calculations History'''

class History:
    '''Class History'''
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        '''Add a new calculation to the history'''
        cls.history.append(calculation)

    @classmethod
    def show_history(cls):
        '''Retrieve the entire calculation history'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Clear the calculation history'''
        return cls.history.clear()

    # Optional - '''Retrieve the lastest calculation, but returns None if there is no history'''

    # Optional - '''Find and return a list of calculations by operation  name'''
