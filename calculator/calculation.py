'''Encapsulates a Calculation'''
import dataclasses

@dataclasses.dataclass
class Calculation:
    '''Class Calculation'''

    def __init__(self, a, b, operation):
        '''Encapsulates a single calculation'''
        # Initiates operand a, operand b
        self.a = a
        self.b = b
        # Stores the operation
        self.operation = operation

    def compute(self):
        '''Executes the operation and returns the result'''
        return self.operation(self.a, self.b)

    # Optional - ''' Returns operand a, operand b, operation '''