'''Calculator Test'''
from calculator import add, subtract, multiply, divide, input_number, input_operation

def test_addition():
    '''Test that addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2,2) == 4

def test_division():
    '''Test that division function works'''
    assert divide(2,2) == 1

def test_input_number():
    '''Test that input number function works'''
    assert input_number

def test_input_operation():
    '''Test that input operation function works'''
    assert input_operation
    