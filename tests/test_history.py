# pylint: disable = unused-import
# pylint: disable = missing-function-docstring
# pylint: disable = redefined-outer-name
# pylint: disable = unused-argument

'''History Test'''
import pytest
from calculator.history import History
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_history():
    '''Clears history and adds sample calculations for tests'''
    History.clear_history()
    calc1 = (2, 2, add)
    calc2 = (2, 2, subtract)
    History.add_calculation(calc1)
    History.add_calculation(calc2)

def test_add_calculation(setup_history):
    '''Tests add calculations to history'''
    calc3 = (2, 2, multiply)
    History.add_calculation(calc3)
    assert History.show_previous() == calc3, 'Failed to add calculation to history!'

def test_show_history(setup_history):
    '''Tests show history'''
    all_logs = History.show_history()
    assert len(all_logs) == 2,'Failed to retrieve history!'

def test_show_history2(setup_history):
    '''Tests show no history'''
    History.clear_history()
    assert History.show_history() == 'No History!','Failed to show no history!'

def test_clear_history(setup_history):
    '''Tests clear history'''
    History.clear_history()
    assert len(History.history) == 0, 'Failed to clear history!'

def test_show_previous(setup_history):
    '''Tests show previous log from history'''
    calc4 = (2, 2, divide)
    History.add_calculation(calc4)
    previous_log = History.show_previous()
    assert previous_log == (2, 2, divide), 'Failed to retrieve previous log!'

def test_show_previous2(setup_history):
    '''Tests show no history'''
    History.clear_history()
    assert History.show_previous() == 'No History!','Failed to show no previous log!'
