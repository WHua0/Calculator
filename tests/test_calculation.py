# pylint: disable = expression-not-assigned

'''Calculation Test'''
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize('a, b, operation, expected', [
    (2, 2, add, 4),
    (2, 2, subtract, 0),
    (2, 2, multiply, 4),
    (2, 2, divide, 1)])

def test_calculation_operations(a, b, operation, expected):
    '''Test calculator operations with the above scenarios'''
    calc = Calculation(a, b, operation)
    assert calc.compute() == expected, f'Failed {operation.__name__} operation with {a} and {b}'

def test_division_by_zero():
    '''Tests that divide by zero exception'''
    calc = Calculation(2, 0, divide)
    with pytest.raises(ValueError, match = 'Cannot divide by zero!'):
        calc.compute(), 'Divide by Zero exception failed'
