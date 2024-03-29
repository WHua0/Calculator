# pylint: disable = comparison-with-callable
# pylint: disable = line-too-long

'''conftest.py'''
# Configures Pytest
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
                # Expect ZeroDivionError if divide by 0
                expected = 'ZeroDivisionError'
            else:
                # Expect normal results if divide not by 0
                expected = operation_function(a, b)
        except ZeroDivisionError:
            expected = 'ZeroDivisionError'

        # Generates a tuple yielded (manages memory better than return) to the caller
        yield a, b, operation_name, operation_function, expected

def pytest_addoption(parser):
    '''Creates custom CLI option --num_records '''
    # pytest --num_records #
    parser.addoption('--num_records', action = 'store', default = 5, type = int, help = 'Number of Test Records to Generate.')

def pytest_generate_tests(metafunc):
    '''Checks if the test is expecting any of the dynamically generated fixtures'''
    if {'a', 'b', 'expected'}.intersection(set(metafunc.fixturenames)):
        # Retrieves number of records for generating test data
        num_records = metafunc.config.getoption('num_records')
        # Generates parameters from Faker
        parameters = list(generate_test_data(num_records))
        # Modifies parameters to fit test functions
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        # Parametrizes the test functions with the modified parameters
        metafunc.parametrize('a, b, operation, expected', modified_parameters)
