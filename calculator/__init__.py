'''Calculator'''
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.history import History

class Calculator:
    '''Class Calculator'''

    # Performs compute, creates log, adds log to history, returns result

    @staticmethod
    def add(a: Decimal, b: Decimal):
        '''Encapulates, creates and stores log, performs Add operation'''
        calculation = Calculation(a, b, add)
        log = History.create_log(a, b, add)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def subtract(a: Decimal, b: Decimal):
        ''''Encapulates, creates and stores log, performs Subtract operation'''
        calculation = Calculation(a, b, subtract)
        log = History.create_log(a, b, subtract)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def multiply (a: Decimal, b: Decimal):
        ''''Encapulates, creates and stores logs, performs Multiply operation'''
        calculation = Calculation(a, b, multiply)
        log = History.create_log(a, b, multiply)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def divide(a: Decimal, b: Decimal):
        ''''Encapulates, creates and stores logs, performs Add Divide Operation'''
        calculation = Calculation(a, b, divide)
        log = History.create_log(a, b, divide)
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
