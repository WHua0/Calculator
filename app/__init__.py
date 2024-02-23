# pylint: disable=too-few-public-methods

'''Application'''
from app.introduction import introduction
from app.commands import CommandHandler
from app.exit import ExitCommand

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

        while True:
            # REPL: Read, Evaluate, Print, Loop
            # Tries to Execute the Command, then Loops
            self.command_handler.execute_command(input(">>> ").strip())
