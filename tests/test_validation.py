import pytest
from calculator.validation import parse_number, parse_operator, InputError


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1", 1.0),
        ("2.5", 2.5),
        ("-3", -3.0),
        ("0", 0.0),
    ],
)
def test_parse_number_valid(value, expected):
    assert parse_number(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "abc",
        "",
        "1.2.3",
        "one",
    ],
)
def test_parse_number_invalid(value):
    with pytest.raises(InputError, match=f"'{value}' is not a valid number"):
        parse_number(value)


@pytest.mark.parametrize("value", ["+", "-", "*", "/"])
def test_parse_operator_valid(value):
    assert parse_operator(value, ["+", "-", "*", "/"]) == value


@pytest.mark.parametrize("value", ["x", "!", "add", ""])
def test_parse_operator_invalid(value):
    with pytest.raises(InputError):
        parse_operator(value, ["+", "-", "*", "/"])
