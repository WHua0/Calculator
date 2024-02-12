'''Calculation Test'''
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize('a, b, operation, expected', [
    (2, 2, add, 4),
    (2, 2, subtract, 0),
    (2, 2, multiply, 4),
    (2, 2, divide, 1),
    (2, 0, divide, 'Cannot divide by zero!')
])

def test_calculation_operations(a, b, operation, expected):
    '''Test calculator operations with the above scenarios'''
    calc = Calculation(a, b, operation)
    assert calc.compute() == expected, f'Failed {operation.__name__} operation with {a} and {b}'
