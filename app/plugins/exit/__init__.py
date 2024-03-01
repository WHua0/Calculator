# pylint: disable=too-few-public-methods

'''Exit Command'''
import sys
import logging
from app.commandmanager import Command

class ExitCommand(Command):
    '''Exits Python Interpreter and terminates program'''
    def execute(self):
        logging.info('App exited.')
        raise sys.exit('Exiting Calculator App ...')
