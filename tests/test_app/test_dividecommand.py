# pylint: disable = unused-argument

'''DivideCommand Test'''
import unittest
from unittest.mock import patch
from app.plugins.divide import DivideCommand

class TestDivideCommand(unittest.TestCase):
    '''Tests DivideCommand'''

    # Mock user input
    @patch('builtins.input', side_effect=['2', '2'])
    # Mock print function
    @patch('builtins.print')

    def test_execute(self, mock_print, mock_input):
        '''Tests Execution'''

        #Create an instance of DivideCommand
        divide_command = DivideCommand()

        # Executes the command
        divide_command.execute()

        # Asserts output
        expected_output = 'The result of 2 divide 2 is equal to 1.'
        mock_print.assert_called_once_with(expected_output)

    # Mock user input
    @patch('builtins.input', side_effect=['2', '0'])
    # Mock print function
    @patch('builtins.print')

    def test_execute_divide_by_0(self, mock_print, mock_input):
        '''Tests Execution'''

        #Create an instance of DivideCommand
        divide_command = DivideCommand()

        # Executes the command
        divide_command.execute()

        # Asserts output
        expected_output = 'An error occurred: Cannot divide by zero.'
        mock_print.assert_called_once_with(expected_output)

    # Mock user input with invalid values
    @patch('builtins.input', side_effect=['abc', 'def'])
     # Mock print function
    @patch('builtins.print')

    def test_execute_invalid_input(self, mock_print, mock_input):
        '''Tests Exception Handling'''

        # Creates an instance of DivideCommand
        divide_command = DivideCommand()

        # Executes the command
        divide_command.execute()

        # Asserts output
        expected_output = 'Invalid number input: abc or def is not a valid number.'
        mock_print.assert_called_once_with(expected_output)

    if __name__ == '__main__':
        unittest.main() # pragma: no cover
