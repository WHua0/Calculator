'''History Test'''
from calculator.history import History
from calculator.operations import add, subtract

def test_history():
    '''test that history class functions work'''
    # test that add calculation function works
    History.clear_history()
    calc1 = (2, 2, add)
    calc2 = (2, 2, subtract)
    History.add_calculation(calc1)
    assert len(History.history) == 1
    History.add_calculation(calc2)
    assert len(History.history) == 2
    # Test that show history function works
    assert History.show_history() == [(2, 2, add), (2, 2, subtract)]
    # Test that show previous function works
    assert History.show_previous() == (2, 2, subtract)
    # Test that clear history function works
    History.clear_history()
    assert len(History.history) == 0
    # Test that show history function works if no history
    assert History.show_history() == "No History"
    # Test that show previous function works of no history
    assert History.show_previous() == "No History"
