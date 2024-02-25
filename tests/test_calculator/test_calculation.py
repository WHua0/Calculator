# pylint: disable = expression-not-assigned

'''Calculation Test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operation

def test_calculation_operations(a, b, operation, expected):
    '''Tests various operations using data generated by Faker'''
    calc = Calculation(a, b, operation)
    assert calc.compute() == expected, f'{operation.__name__} operation failed'

def test_division_by_zero():
    '''Tests that divide by zero exception'''
    calc = Calculation(Decimal('2'), Decimal('0'), Operation.divide)
    with pytest.raises(ZeroDivisionError, match = 'Cannot divide by zero'):
        calc.compute(), 'Divide by Zero exception failed'

def test_addition():
    '''Tests addition function'''
    calc = Calculation(Decimal('2'), Decimal('2'), Operation.add)
    assert calc.compute() == 4, 'Failed to compute add function!'

def test_subtract():
    '''Tests subtract function'''
    calc = Calculation(Decimal('2'), Decimal('2'), Operation.subtract)
    assert calc.compute() == 0, 'Failed to compute subtract function!'

def test_multiply():
    '''Tests multiply function'''
    calc = Calculation(Decimal('2'), Decimal('2'), Operation.multiply)
    assert calc.compute() == 4, 'Failed to compute multiply function!'

def test_divide():
    '''Tests divide function'''
    calc = Calculation(Decimal('2'), Decimal('2'), Operation.divide)
    assert calc.compute() == 1, 'Failed to compute divide function!'