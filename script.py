# pylint: disable = line-too-long
# pylint: disable = broad-exception-caught

'''Main Calculator Program'''

import sys
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

    # Catch-All for Unexpected Errors
    except Exception as e:
        print(f'An error occurred: {e}.')

def cli_command():
    '''Entry point for Python script'''

    # If the number of Command Line Arguments is not 4 => print directions
    if len(sys.argv) != 4:
        print('Usage: python calculator_main.py <number1> <number2> <operation>')
        sys.exit(1)

    # Else calculate and print
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

def main():
    '''Main function'''
    cli_command()

# Code will only be activated when the script is directly run, not when imported
if __name__ == '__main__':
    main()
