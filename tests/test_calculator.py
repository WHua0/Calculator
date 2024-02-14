# pylint: disable = redefined-outer-name
# pylint: disable = unused-argument
# pylint: disable = line-too-long
# pylint: disable = expression-not-assigned

'''Calculator Test'''
import pytest
from calculator import Calculator
from calculator.operations import Operation

def test_addition():
    '''Tests that add function works '''  
    assert Calculator.execute(2, 2, Operation.add) == 4, 'Add operation failed'

def test_subtraction():
    '''Tests that subtract function works '''    
    assert Calculator.execute(2, 2, Operation.subtract) == 0, 'Subtract operation failed'

def test_multiplication():
    '''Tests that multiple function works '''    
    assert Calculator.execute(2, 2, Operation.multiply) == 4, 'Multiply operation failed'

def test_division():
    '''Tests that divide function works '''    
    assert Calculator.execute(2, 2, Operation.divide) == 1, 'Divide operation, not by Zero, failed'

def test_division_by_zero():
    '''Tests that divide by zero exception'''
    with pytest.raises(ValueError, match = 'Cannot divide by zero!'):
        Calculator.execute(2, 0, Operation.divide), 'Divide by Zero exception failed'

@pytest.fixture
def setup_history():
    '''Clears history and adds sample calculations for tests'''
    Calculator.clear_history()
    Calculator.execute(2, 2, Operation.add)
    Calculator.execute(2, 2, Operation.subtract)

def test_history(setup_history):
    '''Tests that history show previous, show history, and clear history functions work'''
    assert Calculator.show_history() == [(2, 2, 'add'), (2, 2, 'subtract')], 'Failed to retrieve history!'
    assert Calculator.show_previous() == (2, 2, 'subtract'), 'Failed to retrieve previous log'
    Calculator.clear_history()
    assert Calculator.show_previous() == 'No History!', 'Failed to clear history and/or show no previous log!'
    assert Calculator.show_history() == 'No History!', 'Failed to clear and/or show no history!'
