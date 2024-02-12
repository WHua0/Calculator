# pylint: disable = unused-import
'''Operation Test'''
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that add function works'''
    assert add(2, 2) == 4, 'Add operation failed'

def test_subtraction():
    '''Test that subtract function works'''
    assert subtract(2, 2) == 0, 'Subtract operation failed'

def test_multiplication():
    '''Test that multiply function works'''
    assert multiply(2, 2) == 4, 'Multiply operation failed'

def test_division():
    '''Test that divide function works'''
    assert divide(2, 2) == 1, 'Divide operation, not by Zero, failed'

def test_division_by_zero():
    '''Test that divide by zero exception'''
    assert divide(2, 0) == 'Cannot divide by zero!', 'Divide by Zero exception failed'
