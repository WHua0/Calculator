# pylint: disable=too-few-public-methods

'''Application'''
from app.introduction import introduction
from app.commandmanager import CommandHandler
from app.exitcommand import ExitCommand
from app.addcommand import AddCommand
from app.subtractcommand import SubtractCommand
from app.multiplycommand import MultiplyCommand
from app.dividecommand import DivideCommand

class App:
    '''Class App'''

    def __init__(self):
        '''Constructor'''
        self.command_handler = CommandHandler()

    def start(self):
        '''Starts the App'''
        # Prints Introduction
        introduction()

        # Valid Commands
        self.command_handler.register_command('exit', ExitCommand())
        self.command_handler.register_command('add', AddCommand())
        self.command_handler.register_command('subtract', SubtractCommand())
        self.command_handler.register_command('multiply', MultiplyCommand())
        self.command_handler.register_command('divide', DivideCommand())

        while True:
            # REPL: Read, Evaluate, Print, Loop
            # Tries to Execute the Input Command Name, then Loops
            self.command_handler.execute_command(input('>>> ').strip())