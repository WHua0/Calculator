'''Calculator'''
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Class Calculator'''

    @staticmethod
    def add(a,b):
        '''Encapulates, then peforms Add Operation'''
        calculation = Calculation(a, b, add)
        return calculation.compute()

    @staticmethod
    def subtract(a,b):
        '''Encapulates, then peforms Subtract Operation'''
        calculation = Calculation(a, b, subtract)
        return calculation.compute()

    @staticmethod
    def multiply (a,b):
        '''Encapulates, then peforms Multiply Operation'''
        calculation = Calculation(a, b, multiply)
        return calculation.compute()

    @staticmethod
    def divide(a,b):
        '''Encapulates, then peforms Divide Operation'''
        calculation = Calculation(a, b, divide)
        return calculation.compute()
