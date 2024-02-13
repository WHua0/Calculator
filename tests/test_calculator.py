# pylint: disable = unused-import
# pylint: disable = redefined-outer-name
# pylint: disable = unused-argument
# pylint: disable = line-too-long
# pylint: disable = expression-not-assigned

'''Calculator Test'''
import pytest
from calculator import Calculator

def test_addition():
    '''Tests that add function works '''  
    assert Calculator.add(2, 2) == 4, 'Add operation failed'

def test_subtraction():
    '''Tests that subtract function works '''    
    assert Calculator.subtract(2, 2) == 0, 'Subtract operation failed'

def test_multiplication():
    '''Tests that multiple function works '''    
    assert Calculator.multiply(2, 2) == 4, 'Multiply operation failed'

def test_division():
    '''Tests that divide function works '''    
    assert Calculator.divide(2, 2) == 1, 'Divide operation, not by Zero, failed'

def test_division_by_zero():
    '''Tests that divide by zero exception'''
    with pytest.raises(ValueError, match='Cannot divide by zero!'):
        Calculator.divide(2, 0), 'Divide by Zero exception failed'

@pytest.fixture
def setup_history():
    '''Clears history and adds sample calculations for tests'''
    Calculator.clear_history()
    Calculator.add(2, 2)
    Calculator.subtract(2, 2)

def test_history(setup_history):
    '''Test that history class functions work'''
    assert Calculator.show_history() == [(2, 2, 'add'), (2, 2, 'subtract')], 'Failed to retrieve history!'
    assert Calculator.show_previous() == (2, 2, 'subtract'), 'Failed to retrieve previous log'
    # Tests that history class functions work with No History
    Calculator.clear_history()
    assert Calculator.show_previous() == 'No History!', 'Failed to clear history and/or show no previous log!'
    assert Calculator.show_history() == 'No History!', 'Failed to clear and/or show no history!'
