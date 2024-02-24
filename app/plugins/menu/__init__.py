# pylint: disable=too-few-public-methods

'''Menu Command'''
from app.commandmanager import Command

class MenuCommand(Command):
    '''Class MenuCommand'''
    def execute(self):
        # Prints Command List"
        print('Commands: add, subtract, multiply, divide.')
