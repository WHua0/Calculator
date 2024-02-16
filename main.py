# pylint: disable = line-too-long

'''Main Calculator Program'''

import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from calculator import operations

def calculate_and_print(a, b, operation_name):
    '''Calculate and Print Results'''

    # Defines operation mappings, string => function
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)
        if result:
            print(f'The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}')
        else:
            print(f'Unknown operation: {operation_name}')
    except InvalidOperation:
        print(f'Invalid number input: {a} or {b} is not a valid number.')
    except ZeroDivisionError:
        print('Error: Division by zero.')
    except Exception as e:
        print(f'An error occured: {e}')
