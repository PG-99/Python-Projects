"""Core arithmetic for the Four-Operation Calculator (Project 2).

This module is pure: every function takes numbers and returns a number (or
raises an error). It never calls ``input`` or ``print``, which makes the rules
easy to test in isolation from the command-line interface in ``main.py``.
"""

from __future__ import annotations

# Map each accepted operator symbol to a two-argument function that performs it.
# Using a lookup table keeps ``calculate`` short and avoids a long if/elif chain.
_OPERATIONS = {
    "+": lambda left, right: left + right,
    "-": lambda left, right: left - right,
    "*": lambda left, right: left * right,
    "/": lambda left, right: left / right,
}

# The operators this calculator understands, handy for menus and validation.
SUPPORTED_OPERATORS = tuple(_OPERATIONS)


def calculate(left: float, operator: str, right: float) -> float:
    """Apply ``operator`` to ``left`` and ``right`` and return the result.

    Raises ``ValueError`` for an unknown operator or division by zero.

    >>> calculate(2, "+", 3)
    5
    >>> calculate(10, "/", 4)
    2.5
    """
    if operator not in _OPERATIONS:
        raise ValueError(f"Unknown operator: {operator!r}")
    if operator == "/" and right == 0:
        raise ValueError("Cannot divide by zero.")
    return _OPERATIONS[operator](left, right)
