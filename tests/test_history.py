'''History Test'''
from calculator.history import History
from calculator.operations import add

def test_add_calculation():
    '''test that add calculation function works'''
    calc = (2, 2, add)
    History.add_calculation(calc)
    assert len(History.history) == 1
