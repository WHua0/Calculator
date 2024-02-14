# pylint: disable = expression-not-assigned

'''Operation Test'''
import pytest
from calculator.operations import Operation
def test_addition():
    '''Tests that add function works'''
    assert Operation.add(2, 2) == 4, 'Add operation failed'

def test_subtraction():
    '''Tests that subtract function works'''
    assert Operation.subtract(2, 2) == 0, 'Subtract operation failed'

def test_multiplication():
    '''Tests that multiply function works'''
    assert Operation.multiply(2, 2) == 4, 'Multiply operation failed'

def test_division():
    '''Tests that divide function works'''
    assert Operation.divide(2, 2) == 1, 'Divide operation, not by Zero, failed'

def test_division_by_zero():
    '''Tests that divide by zero exception'''
    with pytest.raises(ValueError, match = 'Cannot divide by zero!'):
        Operation.divide(2, 0), 'Divide by Zero exception failed'
