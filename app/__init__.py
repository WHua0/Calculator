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
        # Creates logs directory if it does not exist
        os.makedirs('logs', exist_ok=True)
        # Configures Logging
        self.configure_logging()
        # Loads .env
        load_dotenv()
        # Loads .env variables into settings
        self.settings = self.load_environment_variables()
        # Sets default values Environment, Testing
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_manager = CommandManager()
        self.command_manager.register_command("menu", MenuCommand(self.command_manager))

    def configure_logging(self):
        '''Configures Logging Settings'''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            # If logging.conf exists, configures logging using logging.conf
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers = False)
        else:
            # If not, configures basic logging settings with a default level of info
            logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
        logging.info('Logging configured.')

    def load_environment_variables(self):
        '''Loads Environment Variables into Settings Dictionary'''
        settings = dict(os.environ.items())
        logging.info('Environment variables loaded.')
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        '''Retrieves Environment Variables from Settings, but returns None if it doesn't exist'''
        logging.info('Environment variables retrieved.')
        return self.settings.get(env_var, None)

    def load_plugins(self):
        ''' Dynamically load all plugins in the plugins directory'''

        # Indicates where the plugins are expected to be found
        plugins_package = 'app.plugins'

        # Iterates through the modules in plugins_package directory
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):

            # If module is a package, imports the module
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                logging.info("Command '%s' from plugin '%s' imported.", plugin_name, plugins_package)

                # Iterates over all items defined in that module
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)

                    try:
                        # Checks if item is a subclass of Command
                        if issubclass(item, (Command)):
                            # If yes, instantiates the class and registers it with command manager
                            self.command_manager.register_command(plugin_name, item())
                            logging.info("Command '%s' from plugin '%s' registered.", plugin_name, plugins_package)

                    except TypeError:
                        # If not, ignores
                        continue

            else:
                logging.error("Command '%s' from plugin '%s' failed to import.", plugin_name, plugins_package)

    def start(self):
        '''Starts the App'''

        logging.info('App initiated.')

        # Prints Introduction
        introduction()

        # Registers Commands
        self.load_plugins()

        # REPL: Read, Evaluate, Print/Execute the Input Command Name, then Loop
        while True:
            self.command_manager.execute_command(input(">>> ").strip())
