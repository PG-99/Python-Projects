"""Command-line interface for the Four-Operation Calculator (Project 2).

Responsibilities are split cleanly:
- ``calculator.calculate`` owns the arithmetic (pure, tested).
- The functions here own input/output: reading numbers, looping, formatting.
"""

from __future__ import annotations

from src.calculator import SUPPORTED_OPERATORS, calculate


def format_result(value: float) -> str:
    """Show whole numbers without a trailing ``.0`` but keep real decimals.

    >>> format_result(5.0)
    '5'
    >>> format_result(2.5)
    '2.5'
    """
    if value == int(value):
        return str(int(value))
    return str(value)


def read_number(prompt: str) -> float:
    """Keep asking until the user types something ``float`` can parse."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("  Please enter a number (for example 12 or 3.5).")


def read_operator(prompt: str) -> str:
    """Keep asking until the user types a supported operator."""
    while True:
        symbol = input(prompt).strip()
        if symbol in SUPPORTED_OPERATORS:
            return symbol
        print(f"  Please enter one of: {' '.join(SUPPORTED_OPERATORS)}")


def main() -> None:
    """Run calculations in a loop until the user chooses to quit."""
    print("Four-Operation Calculator. Type 'q' at any number prompt to quit.")
    history: list[str] = []

    while True:
        first = input("First number (or 'q' to quit): ").strip()
        if first.lower() in {"q", "quit"}:
            break
        try:
            left = float(first)
        except ValueError:
            print("  Please enter a number.")
            continue

        operator = read_operator(f"Operator {SUPPORTED_OPERATORS}: ")
        right = read_number("Second number: ")

        try:
            result = calculate(left, operator, right)
        except ValueError as error:
            print(f"  {error}")
            continue

        line = f"{format_result(left)} {operator} {format_result(right)} = {format_result(result)}"
        print(line)
        history.append(line)

    if history:
        print("\nHistory this session:")
        for entry in history:
            print(f"  {entry}")
    print("Goodbye!")


if __name__ == "__main__":
    main()
