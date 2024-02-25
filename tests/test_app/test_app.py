'''App Test'''
import unittest
from unittest.mock import patch
from io import StringIO
from app import App
import sys

class TestApp(unittest.TestCase):
    '''Class TestApp'''

    def test_load_plugins(self):
        '''Tests that at least one plugin loads'''

        app = App()
        app.load_plugins()
        self.assertTrue(len(app.command_manager.commands) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_start(self, mock_stdout):
        '''Tests that introduction loads'''

        app = App()

        with patch('builtins.input', side_effect=['fake_command', 'exit']):
            try:
                app.start()
            except SystemExit as e:
                self.assertEqual(e.code, 'Exiting Calculator App ...')  # Assert the exit message
            else:
                self.fail("Expected SystemExit but it didn't occur")

        self.assertIn('Calculator App Initiated.\n\nPlease type a command.\nType "menu" for details.\nType "exit" to exit.\n\nInvalid Command: fake_command\nType "menu" for details.\nType "exit" to exit.\n', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main() # pragma: no cover
