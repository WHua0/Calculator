# pylint: disable=too-few-public-methods
'''Manages Calculations History'''

class History:
    '''Class History'''
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        '''Adds a new calculation to the history'''
        cls.history.append(calculation)

    @classmethod
    def show_history(cls):
        '''Retrieves the entire calculation history'''
        if cls.history:
            return cls.history
        return "No History"

    @classmethod
    def clear_history(cls):
        '''Clears the calculation history'''
        return cls.history.clear()

    @classmethod
    def show_previous(cls):
        '''Retrieves the previous calculation, but returns None if there is none'''
        if cls.history:
            return cls.history[-1]
        return "No History"
