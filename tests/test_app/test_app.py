# pylint: disable = line-too-long
# pylint: disable = unused-import

'''App Test'''
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from app import App

class TestApp(unittest.TestCase):
    '''Class TestApp'''

    def test_load_plugins(self):
        '''Tests load_plugins'''

        app = App()
        app.load_plugins()
        self.assertTrue(len(app.command_manager.commands) > 0)

    @patch('sys.stdout', new_callable=StringIO)

    def test_start(self, mock_stdout):
        '''Tests start'''

        app = App()

        with patch('builtins.input', side_effect=['fake_command', 'exit']):
            try:
                app.start()
            except SystemExit as e:
                self.assertEqual(e.code, 'Exiting Calculator App ...')
            else:
                self.fail('Expected SystemExit but it did not occur.')

        self.assertIn('Calculator App Initiated.\n\nPlease type a command.\nType "menu" for details.\nType "exit" to exit.\n\nInvalid Command: fake_command\nType "menu" for details.\nType "exit" to exit.\n', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main() # pragma: no cover
