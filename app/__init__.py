'''App'''
import pkgutil
import importlib
from app.introduction import introduction
from app.commandmanager import Command, CommandManager

class App:
    '''Class App'''

    def __init__(self):
        '''Constructor'''
        self.command_handler = CommandManager()

    def load_plugins(self):
        ''' Dynamically load all plugins in the plugins directory'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        '''Starts the App'''
        # Prints Introduction
        introduction()

        # Register commands
        self.load_plugins()

        # REPL: Read, Evaluate, Print, Loop
        # Tries to Execute the Input Command Name, then Loops
        while True:
            self.command_handler.execute_command(input(">>> ").strip())
