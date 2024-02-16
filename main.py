# pylint: disable = line-too-long
# pylint: disable = broad-exception-caught

'''Main Calculator Program'''

from decimal import Decimal, InvalidOperation
from calculator import Calculator

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
        # Tries to convert a and b into decimal objects
        a_decimal, b_decimal = map(Decimal, [a, b])
        # Retrieves operation function from the operation name in operation mappings
        operation_function = operation_mappings.get(operation_name)

        # If operation function is found => calculates and prints
        if operation_function:
            print(f'The result of {a} {operation_name} {b} is equal to {operation_function(a_decimal, b_decimal)}.')

        # If operation function is not found => unknown operation
        else:
            print(f'Unknown operation: {operation_name}.')

    # If a and b cannot be converted to decimal objects => invalid number
    except InvalidOperation:
        print(f'Invalid number input: {a} or {b} is not a valid number.')

    # If result is ZeroDvisionError from b = 0 => Error: Division by zero.
    except ZeroDivisionError:
        print('Error: Division by zero.')

    # Catch-All for Unexpected Errors
    except Exception as e:
        print(f'An error occured: {e}.')
