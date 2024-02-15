# pylint: disable = unused-argument
# pylint: disable = expression-not-assigned
# pylint: disable = line-too-long

'''Operation Test'''
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operation
from tests import conftest


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

@pytest.mark.parametrize("a, b, operation_name, operation, expected", conftest.generate_test_data(10))
def test_operations(a, b, operation_name, operation, expected):
    '''Tests various operations'''
    calculation = Calculation(a, b, operation)
    assert calculation.compute() == expected, f'{operation.__name__} operation failed'
