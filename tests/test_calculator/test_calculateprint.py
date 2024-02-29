# pylint: disable = line-too-long

'''CalculatePrint Test'''
import pytest
from calculator.calculateprint import calculate_and_print

@pytest.mark.parametrize('a_string, b_string, operation_string, expected_string', [
    # Tests for Add, Subtract, Multiple, Divide
    ('5', '3', 'add', 'The result of 5 add 3 is equal to 8.'),
    ('10', '2', 'subtract', 'The result of 10 subtract 2 is equal to 8.'),
    ('4', '5', 'multiply',  'The result of 4 multiply 5 is equal to 20.'),
    ('20', '4', 'divide', 'The result of 20 divide 4 is equal to 5.'),
    # Test for divide by 0 exception
    ('1', '0', 'divide', 'An error occurred: Cannot divide by zero.'),
    # Tests for unknown operation
    ('9', '3', 'unknown', 'Unknown operation: unknown.'),
    # Tests for invalid number input a
    ('a', '3', 'add', 'Invalid number input: a or 3 is not a valid number.'),
    # Tests for invalid number input b
    ('5', 'b', 'subtract', 'Invalid number input: 5 or b is not a valid number.')
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    '''Tests Calculate and Print Function'''
    calculate_and_print(a_string, b_string, operation_string)
    # System Captures the output (standard output and standard error) generated by calculate_and_print
    captured = capsys.readouterr()
    # Asserts standard output == expected_string
    assert captured.out.strip() == expected_string, 'Calculate and Print function failed'
