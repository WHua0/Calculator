# pylint: disable = line-too-long

'''App'''
import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.introduction import introduction
from app.commandmanager import Command, CommandManager
from app.plugins.menu import MenuCommand

class App:
    '''Class App'''

    def __init__(self):
        '''Constructor'''
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = {}
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_manager = CommandManager()
        self.command_manager.register_command("menu", MenuCommand(self.command_manager))

    def configure_logging(self):
        '''Configures Logging'''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers = False)
        else:
            logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
        logging.info('Logging configured.')

    def load_environment_variables(self):
        '''Loads Environment Variables'''
        settings = dict(os.environ.items())
        logging.info('Environment variables loaded.')
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        '''Gets Environment Variables'''
        return self.settings.get(env_var, None)

    def load_plugins(self):
        ''' Dynamically load all plugins in the plugins directory'''

        # Indicates where the plugins are expected to be found
        plugins_package = 'app.plugins'

        # Iterates through the modules in plugins_pacakge directory
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):

            # If module is a package, imports the module
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')

                # Iterates over all items defined in that module
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)

                    try:
                        # Checks if item is a subclass of Command
                        if issubclass(item, (Command)):
                            # If yes, instantiates the class and registers it with command manager
                            self.command_manager.register_command(plugin_name, item())

                    except TypeError:
                        # If not, ignores
                        continue

    def start(self):
        '''Starts the App'''

        # Prints Introduction
        introduction()

        # Registers Commands
        self.load_plugins()

        # REPL: Read, Evaluate, Print, Loop
        # Tries to Read, Evaluate, Execute the Input Command Name, then Loops
        while True:
            self.command_manager.execute_command(input(">>> ").strip())
