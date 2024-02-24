# pylint: disable = unused-argument

'''SubtractCommand Test'''
import unittest
from unittest.mock import patch
from app.commands.subtractcommand import SubtractCommand

class TestSubtractCommand(unittest.TestCase):
    '''Tests SubtractCommand'''

    # Mock user input
    @patch('builtins.input', side_effect=['2', '2'])
    # Mock print function
    @patch('builtins.print')

    def test_execute(self, mock_print, mock_input):
        '''Tests Execution'''

        #Create an instance of SubtractCommand
        subtract_command = SubtractCommand()

        # Executes the command
        subtract_command.execute()

        # Asserts output
        expected_output = 'The result of 2 minus 2 is equal to 0.'
        mock_print.assert_called_once_with(expected_output)

    # Mock user input with invalid values
    @patch('builtins.input', side_effect=['abc', 'def'])
    # Mock print function
    @patch('builtins.print')

    def test_execute_invalid_input(self, mock_print, mock_input):
        '''Tests Exception Handling'''

        # Creates an instance of SubtractCommand
        subtract_command = SubtractCommand()

        # Executes the command
        subtract_command.execute()

        # Asserts output
        expected_output = 'Invalid number input: abc or def is not a valid number.'
        mock_print.assert_called_once_with(expected_output)

    if __name__ == '__main__':
        unittest.main() # pragma: no cover
