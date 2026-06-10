import pytest
from calculator.operations import add, subtract, multiply, divide, OPERATIONS


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 5, 5),
    (1.5, 2.5, 4.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -2, 1),
    (0, 5, -5),
    (1.5, 0.5, 1.0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (1.5, 2, 3.0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, 3, -2),
    (1.5, 0.5, 3.0),
    (0, 5, 0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


def test_operations_registry():
    assert "+" in OPERATIONS
    assert "-" in OPERATIONS
    assert "*" in OPERATIONS
    assert "/" in OPERATIONS