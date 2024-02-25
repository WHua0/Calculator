# pylint: disable=too-few-public-methods

'''Exit Command'''
import sys
from app.commandmanager import Command

class ExitCommand(Command):
    '''Exits Python Interpreter and terminates program'''
    def execute(self):
        raise sys.exit('Exiting Calculator App ...')
