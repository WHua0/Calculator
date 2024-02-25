# pylint: disable = redefined-outer-name

'''Exit Test'''
import sys
import pytest
from app.plugins.exit import ExitCommand

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
        raise SystemExit  # Raise SystemExit to simulate exit without actually exiting

    monkeypatch.setattr(sys, 'exit', mock_exit)

    with pytest.raises(SystemExit) as exc_info:
        exit_command.execute()

    assert exit_msg == 'Exiting Calculator App ...'
