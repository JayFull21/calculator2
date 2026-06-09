from calculator.operations import OPERATIONS
from calculator.validation import parse_number, parse_operator, InputError


def _prompt(message):
    return input(message)


def run():
    print("Welcome to the calculator! Type 'quit' to exit.")
    print(f"Available operators: {' '.join(OPERATIONS.keys())}")

    while True:
        operator = _prompt("\nEnter operator: ").strip()
        if operator.lower() == "quit":
            print("Goodbye!")
            break

        try:
            operator = parse_operator(operator, OPERATIONS)
            a = parse_number(_prompt("Enter first number: ").strip())
            b = parse_number(_prompt("Enter second number: ").strip())
            result = OPERATIONS[operator](a, b)
            print(f"Result: {result}")
        except InputError as e:
            print(f"Input error: {e}")
        except ValueError as e:
            print(f"Error: {e}")