'''Calculator'''
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.history import History

class Calculator:
    '''Class Calculator'''

    # Performs compute, creates log, adds log to history, returns result
    @staticmethod
    def execute(a: Decimal, b: Decimal, operation):
        '''Encapulates, creates and stores log, performs operation'''
        calculation = Calculation(a, b, operation)
        log = History.create_log(a, b, operation)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def show_history():
        '''Shows History Logs'''
        return History.show_history()

    @staticmethod
    def clear_history():
        '''Clears History Logs'''
        return History.clear_history()

    @staticmethod
    def show_previous():
        '''Shows Previous Log'''
        return History.show_previous()
