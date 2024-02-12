'''Operation Test'''
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that add function works'''
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtract function works'''
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiply function works'''
    assert multiply(2, 2) == 4

def test_division():
    '''Test that divide function works'''
    assert divide(2, 2) == 1

def test_division_by_zero():
    '''Test that divide by zero exception'''
    assert divide(2, 0) == "Cannot divide by zero!"
