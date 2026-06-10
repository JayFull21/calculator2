class InputError(ValueError):
    pass


def parse_number(value):
    try:
        return float(value)
    except ValueError:
        raise InputError(f"'{value}' is not a valid number")


def parse_operator(value, valid_operators):
    if value not in valid_operators:
        raise InputError(f"'{value}' is not a valid operator. Choose from: {' '.join(valid_operators)}")
    return value