# pylint: disable = unused-import
# pylint: disable = line-too-long

'''Introduction Test'''
import pytest
from app.introduction import introduction

def test_introduction(capsys):
    '''Tests introduction'''
    introduction()
    captured = capsys.readouterr()
    result = 'Calculator App Initiated.\n\nPlease type a command.\nType "menu" for details.\nType "exit" to exit.\n\n'
    assert captured.out == result, 'introduction function failed!'
