# pylint: disable=too-few-public-methods

'''Application'''
from app.introduction import introduction
from app.commandmanager import CommandManager
from app.commands.exitcommand import ExitCommand
from app.commands.menucommand import MenuCommand
from app.commands.addcommand import AddCommand
from app.commands.subtractcommand import SubtractCommand
from app.commands.multiplycommand import MultiplyCommand
from app.commands.dividecommand import DivideCommand

class App:
    '''Class App'''

    def __init__(self):
        '''Constructor'''
        self.command_manager = CommandManager()

    def register_default_commands(self, commands_dictionary):
        '''Registers default commands'''

        # Registers each Command in the dictionary with the Command Handler
        for command_name, command_instance in commands_dictionary.items():
            self.command_manager.register_command(command_name, command_instance)

    def start(self):
        '''Starts the App'''
        # Prints Introduction
        introduction()

        # Dictionary of Commands
        commands_dictionary = {
            'menu': MenuCommand(),
            'exit': ExitCommand(),
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand()
        }

        # Registers default commands
        self.register_default_commands(commands_dictionary)

        while True:
            # REPL: Read, Evaluate, Print, Loop
            # Tries to Execute the Input Command Name, then Loops
            self.command_manager.execute_command(input('>>> ').strip())
