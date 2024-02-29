# pylint: disable = line-too-long
# pylint: disable = broad-exception-caught

'''Calculator Script'''

import sys
from calculator.calculateandprint import calculate_and_print

def cli_command():
    '''Entry point for Python Script'''

    # If the number of Command Line Arguments is not 4 => print directions
    if len(sys.argv) != 4:
        print('Usage: python calculator_main.py <number1> <number2> <operation>')
        sys.exit(1)

    # Else calculate and print
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

def main():
    '''Script Main Function'''
    cli_command()

# Code will only be activated when the script is directly run, not when imported
if __name__ == '__main__':
    main()
