# pylint: disable = unused-argument
# pylint: disable = expression-not-assigned
# pylint: disable = line-too-long
# pylint: disable = unused-import

'''Operation Test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operation

def test_operations(a, b, operation, expected):
    '''Tests various operations using data generated by Faker'''
    calculation = Calculation(a, b, operation)
    assert calculation.compute() == expected, f'{operation.__name__} operation failed'

def test_divide_by_zero():
    '''Tests divide by 0 exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), Operation.divide)
        calculation.compute()
