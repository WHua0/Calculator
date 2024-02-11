'''Calculator'''
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.history import History

class Calculator:
    '''Class Calculator'''

    # Performs compute, adds to history, returns result

    @staticmethod
    def add(a,b):
        '''Encapulates, peforms Add Operation, stores Log'''
        calculation = Calculation(a, b, add)
        log = (a, b, add)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def subtract(a,b):
        '''Encapulates, then peforms Subtract Operation'''
        calculation = Calculation(a, b, subtract)
        log = (a, b, add)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def multiply (a,b):
        '''Encapulates, then peforms Multiply Operation'''
        calculation = Calculation(a, b, multiply)
        log = (a, b, add)
        History.add_calculation(log)
        return calculation.compute()

    @staticmethod
    def divide(a,b):
        '''Encapulates, then peforms Divide Operation'''
        calculation = Calculation(a, b, divide)
        log = (a, b, add)
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
