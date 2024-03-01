# pylint: disable = line-too-long

'''Script Test'''
import sys
import pytest
from script import cli_command

def test_cli_command(capsys):
    '''Tests CLI Command function'''
    # Saves the original sys.argv and replace it with our arguments
    original_sys_argv = sys.argv
    sys.argv = ['calculator_main.py', '2', '3', 'add']

    # Calls the CLI Command function
    cli_command()

    # Captures the printed output
    captured = capsys.readouterr()

    # Checks if usage message is printed
    assert captured.out == 'The result of 2 add 3 is equal to 5.\n', 'CLI Command Function Failed'

    # Restores original sys.argv
    sys.argv = original_sys_argv

def test_cli_command_2(capsys):
    '''Tests CLI Command function if incorrect len(sys.argv)'''
    # Saves the original sys.argv and replace it with our arguments
    original_sys_argv = sys.argv
    sys.argv = ['calculator_main.py', '2', '3', 'add', 'extra']

    # Sets up a context where pytest will watch for SystemExit to be raised
    with pytest.raises(SystemExit) as e:
        # Calls the CLI Command function
        cli_command()
    # Captures the printed output
    captured = capsys.readouterr()
    # Checks if usage message is printed
    assert captured.out == 'Usage: python calculator_main.py <number1> <number2> <operation>\n', 'CLI Command function with Extra Failed'
     # Checks if sys.exit(1) is called
    assert e.value.code == 1

    # Restores original sys.argv
    sys.argv = original_sys_argv
