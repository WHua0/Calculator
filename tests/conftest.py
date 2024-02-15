'''conftest.py'''
from decimal import Decimal
from faker import Faker
from calculator.operations import Operation

fake = Faker()

# Defines operation mappings, string => function
operation_mapping = {
    'add': Operation.add,
    'subtract': Operation.subtract,
    'multiply': Operation.multiply,
    'divide': Operation.divide
}
def generate_test_data(number_of_records):
    '''Generates test data in the amount called'''
    for _ in range(number_of_records):
        # Generates a 2-digit number for a and b
        a = Decimal(fake.random_number(digits = 2))
        b = Decimal(fake.random_number(digits = 2))
        # Generates operation name from the operation mappings list
        operation_name = fake.random_element(elements = list(operation_mapping.keys()))
        # Operation Name => Operation Function
        operation_function = operation_mapping[operation_name]

        # Handles divide by 0 exception
        if operation_function == Operation.divide:
            # if b == 0, b = 1, avoiding division by 0
            b = Decimal('1') if b == Decimal('0') else b

        try:
            if operation_function == Operation.divide and b == Decimal('0'):
                # Expect ZeroDivions Error if divide by 0
                expected = 'ZeroDivisionError'
            else:
                # Expect normal results if divide not by 0
                expected = operation_function(a, b)
        except ZeroDivisionError:
            expected = 'ZeroDivisionError'

        # Generates a tuple yielded to the caller
        yield a, b, operation_name, operation_function, expected
