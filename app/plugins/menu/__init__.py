# pylint: disable=too-few-public-methods

'''Menu Command'''
import logging
from app.commandmanager import Command

class MenuCommand(Command):
    '''Class MenuCommand'''

    def __init__(self, command_manager):
        '''Constructor'''
        self.command_manager = command_manager

    def execute(self):
        '''Executes method to show all plugin/command names'''
        print('Commands:')
        for plugin_name in self.command_manager.commands.keys():
            print(plugin_name)
        logging.info('Command Menu printed.')
