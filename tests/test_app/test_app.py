'''App Test'''
import unittest
from unittest.mock import patch
from io import StringIO
from app import App

class TestApp(unittest.TestCase):
    '''Class TestApp'''

    def test_load_plugins(self):
        '''Tests that at least one plugin loads'''

        app = App()
        app.load_plugins()
        self.assertTrue(len(app.command_manager.commands) > 0)

    @patch('sys.stdout', new_callable=StringIO)

    def test_start(self, mock_stdout):
        '''Tests that intoduction loads'''

        app = App()

        with patch('builtins.input', side_effect=['fake_command', 'exit']):
            app.start()

        self.assertIn('Welcome to the App', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
