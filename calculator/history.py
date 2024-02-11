'''Manages Calculations History'''
import dataclasses

@dataclasses.dataclass
class History:
    '''Class History'''
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        '''Add a new calculation to the history'''
        cls.history.append(calculation)

    # '''Retrieve the entire calculation history'''

    # Optional - '''Clear the calculation history'''

    # Optional - '''Retrieve the lastest calculation, but returns None if there is no history'''

    # Optional - '''Find and return a list of calculations by operation  name'''
