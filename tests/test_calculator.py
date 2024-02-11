'''Calculator Test'''
from calculator import Calculator


def test_addition():
    '''Test that addition function works '''  
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiplication():
    '''Test that addition function works '''    
    assert Calculator.multiply(2,2) == 4

def test_division():
    '''Test that addition function works '''    
    assert Calculator.divide(2,2) == 1

def test_division_by_zero():
    '''Test that division by zero exception'''
    assert Calculator.divide(2,0) == "Cannot divide by zero!"
