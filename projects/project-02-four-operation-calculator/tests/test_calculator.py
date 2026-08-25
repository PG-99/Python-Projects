"""Tests for the Four-Operation Calculator.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

# Make ``src`` importable when running pytest from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.calculator import calculate
from src.main import format_result


# --- calculate: all operators, negatives, decimals ------------------------

@pytest.mark.parametrize(
    "left, operator, right, expected",
    [
        (2, "+", 3, 5),
        (5, "-", 8, -3),        # negative result
        (4, "*", 2.5, 10.0),    # decimal operand
        (10, "/", 4, 2.5),      # decimal result
        (-6, "/", -3, 2),       # two negatives
        (0, "*", 99, 0),
    ],
)
def test_calculate_operations(left, operator, right, expected):
    assert calculate(left, operator, right) == expected


# --- division by zero -----------------------------------------------------

def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        calculate(1, "/", 0)


# --- unknown operator -----------------------------------------------------

@pytest.mark.parametrize("bad", ["%", "^", "", "add"])
def test_unknown_operator_raises(bad):
    with pytest.raises(ValueError):
        calculate(1, bad, 2)


# --- output formatting ----------------------------------------------------

@pytest.mark.parametrize(
    "value, text",
    [(5.0, "5"), (2.5, "2.5"), (-3.0, "-3"), (0.0, "0")],
)
def test_format_result(value, text):
    assert format_result(value) == text
