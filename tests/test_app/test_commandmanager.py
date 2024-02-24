# pylint: disable = too-few-public-methods

'''CommandManager Test'''
import unittest
from unittest.mock import MagicMock
from app.commandmanager import Command, CommandManager

class MockCommand(Command):
    '''Class MockCommand'''
    def execute(self):
        pass

class TestCommandManager(unittest.TestCase):
    '''Class TestCommandManager'''

    def setUp(self):
        self.manager = CommandManager()

    def test_register_command(self):
        '''Tests Register_Command'''

        command_name = "mock_command"
        command = MockCommand()
        self.manager.register_command(command_name, command)
        self.assertIn(command_name, self.manager.commands)
        self.assertEqual(self.manager.commands[command_name], command)

    def test_execute_command(self):
        '''Tests Execute_Command'''

        command_name = "mock_command"
        command = MockCommand()
        command.execute = MagicMock()
        self.manager.register_command(command_name, command)
        self.manager.execute_command(command_name)
        command.execute.assert_called_once()

    # To Add test_invalid_command

if __name__ == "__main__":
    unittest.main()
