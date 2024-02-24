# pylint: disable = unused-argument

'''Multiply Test'''
import unittest
from unittest.mock import patch
from app.plugins.multiply import MultiplyCommand

class TestMultiplyCommand(unittest.TestCase):
    '''Tests MultiplyCommand'''

    # Mock user input
    @patch('builtins.input', side_effect=['2', '2'])
    # Mock print function
    @patch('builtins.print')

    def test_execute(self, mock_print, mock_input):
        '''Tests Execution'''

        #Create an instance of MultiplyCommand
        multiply_command = MultiplyCommand()

        # Executes the command
        multiply_command.execute()

        # Asserts output
        expected_output = 'The result of 2 multiply 2 is equal to 4.'
        mock_print.assert_called_once_with(expected_output)

    # Mock user input with invalid values
    @patch('builtins.input', side_effect=['abc', 'def'])
    # Mock print function
    @patch('builtins.print')

    def test_execute_invalid_input(self, mock_print, mock_input):
        '''Tests Exception Handling'''

        # Creates an instance of MultiplyCommand
        multiply_command = MultiplyCommand()

        # Executes the command
        multiply_command.execute()

        # Asserts output
        expected_output = 'Invalid number input: abc or def is not a valid number.'
        mock_print.assert_called_once_with(expected_output)

    if __name__ == '__main__':
        unittest.main() # pragma: no cover
