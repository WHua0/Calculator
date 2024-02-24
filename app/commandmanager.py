# pylint: disable=too-few-public-methods

'''Command Manager'''
from abc import ABC, abstractmethod

class Command(ABC):
    '''Class Command'''

    @abstractmethod
    def execute(self):
        '''Any subclass of Command must implement its own execute method'''
        # Passthrough

class CommandHandler:
    '''Class CommandHandler'''

    def __init__(self):
        '''Constructor for a dictionary'''
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        '''Registers the Command, Str : Abstract Class Command'''
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        '''Tries to execute the Command'''
        try:
            self.commands[command_name].execute()

        # If fails to execute => KeyError: Invalid Command
        except KeyError:
            print(f'Invalid Command: {command_name}')
