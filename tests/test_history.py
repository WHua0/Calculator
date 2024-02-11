'''History Test'''
from calculator.history import History
from calculator.operations import add

def test_history():
    '''test that history class functions work'''
    # test that add calculation function works
    calc = (2, 2, add)
    History.add_calculation(calc)
    assert len(History.history) == 1
    # Test that show history function works
    assert History.show_history() == [(2, 2, add)]
    # Test that clear history function works
    History.clear_history()
    assert len(History.history) == 0
