# Calculator Instructions

## Install

1. clone
2. pip install -r requirements.txt

## Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## Usage
from calculator import Calculator
\nfrom calculator.operations import Operation

1. Calculator.execute(a, b, Operation.add)
2. Calculator.execute(a, b, Operation.subtract)
3. Calculator.execute(a, b, Operation.multiply)
4. Calculator.execute(a, b, Operation.divide)

5. Calculator.show_history()
6. Calculator.clear_history()
7. Calculator.show_previous()
