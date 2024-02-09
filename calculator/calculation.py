'''Encapsulates a Calculation'''

import dataclasses
@dataclasses.dataclass

class Calculation:
    '''Class Calculation'''

    def __init__(self, a, b, operation):
        '''Stores the Operation Function'''
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        '''Calls the stored Operation with a and b'''
        return self.operation(self.a, self.b)
