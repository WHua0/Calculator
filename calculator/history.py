'''Manages Calculations History'''
import dataclasses
from typing import List
from calculator import Calculation

@dataclasses.dataclass
class History:
    '''Class History'''

    history: List[Calculation] = []
