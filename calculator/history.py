'''Manages Calculations History'''
import dataclasses
from typing import List
from calculator import Calculation

@dataclasses.dataclass
class History:
    '''Class History'''

    history: List[Calculation] = []

    # '''Add a new calculation to the history'''

    # '''Retrieve the entire calculation history'''

    # '''Clear the calculation history'''

    # Optional - '''Retrieve the lastest calculation, but returns None if there is no history'''

    # Optional - '''Find and reutnr a list of calculations by operation  name'''
