'''Calculator Test'''
from calculator import add, subtract, multiply, divide, check_number, check_operation

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
    assert divide(2,0) == "error"
    assert divide(2,2) == 1

def test_check_number():
    '''Test that input number function works'''
    assert check_number(1) == 1.0
    assert check_number(1.0) == 1.0
    assert check_number("a") == "error"

def test_check_operation():
    '''Test that input operation function works'''
    assert check_operation("+") == "+"
    assert check_operation("-") == "-"
    assert check_operation("*") == "*"
    assert check_operation("/") == "/"
    assert check_operation("a") == "error"
