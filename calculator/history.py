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
        if cls.history:
            return cls.history
        return "No History"

    @classmethod
    def clear_history(cls):
        '''Clear the calculation history'''
        return cls.history.clear()

    @classmethod
    def show_previous(cls):
        '''Retrieve the previous calculation, but returns None if there is none'''
        if cls.history:
            return cls.history[-1]
        return "No History"

    # Optional - '''Find and return a list of calculations by operation  name'''
