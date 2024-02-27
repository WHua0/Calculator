'''Menu Test'''
import sys
from io import StringIO
import unittest
from unittest.mock import MagicMock
from app.plugins.menu import MenuCommand

class TestMenuCommand(unittest.TestCase):
    '''Tests MenuCommand'''

    def test_execute(self):
        '''Tests Execution'''

        # Mocks the CommandManager
        command_manager_mock = MagicMock()
        command_manager_mock.commands = {
            "command1": MagicMock(),
            "command2": MagicMock()
        }

        # Creates an instance of MenuCommand
        menu_command = MenuCommand(command_manager_mock)

        # Redirects stdout to a StringIO object to capture the output
        saved_stdout = sys.stdout

        try:
            sys.stdout = StringIO()

            # Calls the execute method
            menu_command.execute()

            # Gets the printed output
            printed_output = sys.stdout.getvalue().strip()

            # Asserts the printed output
            expected_output = "Commands:\ncommand1\ncommand2"
            self.assertEqual(printed_output, expected_output)

        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main() # pragma: no cover
