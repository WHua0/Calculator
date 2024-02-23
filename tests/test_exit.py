# pylint: disable = redefined-outer-name

'''Exit Test'''
import sys
import pytest
from app.exit import ExitCommand

@pytest.fixture
def exit_command():
    '''Define Fixture'''
    return ExitCommand()

def test_execute(exit_command, monkeypatch):
    '''Tests Exit Command'''
    exit_msg = None

    def mock_exit(msg):
        nonlocal exit_msg
        exit_msg = msg

    monkeypatch.setattr(sys, "exit", mock_exit)

    exit_command.execute()

    assert exit_msg == 'Exiting Calculator App ...', 'Exit Function failed!'
