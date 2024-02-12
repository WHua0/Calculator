# pylint: disable = unused-import
# pylint: disable = line-too-long

'''Calculator Test'''
import pytest
from calculator import Calculator


def test_addition():
    '''Test that add function works '''  
    assert Calculator.add(2, 2) == 4, 'Add operation failed'

def test_subtraction():
    '''Test that subtract function works '''    
    assert Calculator.subtract(2, 2) == 0, 'Subtract operation failed'

def test_multiplication():
    '''Test that multiple function works '''    
    assert Calculator.multiply(2, 2) == 4, 'Multiply operation failed'

def test_division():
    '''Test that divide function works '''    
    assert Calculator.divide(2, 2) == 1, 'Divide operation, not by Zero, failed'

def test_division_by_zero():
    '''Test that divide by zero exception'''
    assert Calculator.divide(2, 0) == 'Cannot divide by zero!', 'Divide by Zero exception failed'

def test_history():
    '''Test that history class functions work'''
    Calculator.clear_history()
    Calculator.add(2, 2)
    Calculator.subtract(2, 2)
    assert Calculator.show_history() == [(2, 2, 'add'), (2, 2, 'subtract')], 'Failed to add and/or retrieve history!'
    # test that show_previous function works
    assert Calculator.show_previous() == (2, 2, 'subtract'), 'Failed to retrieve previous log'
    # test that clear history and show history functions work
    Calculator.clear_history()
    assert Calculator.show_previous() == 'No History!', 'Failed to clear and/or show no history for previous log!'
    assert Calculator.show_history() == 'No History!', 'Failed to clear and/or show no history!'
