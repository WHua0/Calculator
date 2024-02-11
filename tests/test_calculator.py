'''Calculator Test'''
from calculator import Calculator


def test_addition():
    '''Test that add function works '''  
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that subtract function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiplication():
    '''Test that multiple function works '''    
    assert Calculator.multiply(2,2) == 4

def test_division():
    '''Test that divide function works '''    
    assert Calculator.divide(2,2) == 1

def test_division_by_zero():
    '''Test that divide by zero exception'''
    assert Calculator.divide(2,0) == "Cannot divide by zero!"

def test_history():
    '''test that history class functions work'''
    Calculator.clear_history()
    Calculator.add(2,2)
    Calculator.subtract(2,2)
    assert Calculator.show_history() == [(2, 2, 'add'), (2, 2, 'subtract')]
    # test that show_previous function works
    assert Calculator.show_previous() == (2, 2, 'subtract')
    # test that clear history and show history functions work
    Calculator.clear_history()
    assert Calculator.show_history() == "No History!"
