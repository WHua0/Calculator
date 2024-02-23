# pylint: disable=too-few-public-methods

'''Exit Command'''
import sys
from app.commands import Command

class ExitCommand(Command):
    '''Exits System'''
    def execute(self):
        sys.exit('Exiting Calculator App ...')
