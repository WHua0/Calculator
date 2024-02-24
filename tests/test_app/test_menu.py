'''Menu Test'''
import unittest
from unittest.mock import patch
from app.plugins.menu import MenuCommand

class TestMenuCommand(unittest.TestCase):
    '''Class TestMenuCommand'''

    @patch('builtins.print')

    def test_execute(self, mock_print):
        '''Tests Register_Command'''
        menu_command = MenuCommand()
        menu_command.execute()
        mock_print.assert_called_once_with('Commands: add, subtract, multiply, divide.')

if __name__ == '__main__':
    unittest.main() # pragma: no cover
