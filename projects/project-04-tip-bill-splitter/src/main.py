"""Command-line interface for the Tip and Bill Splitter (Project 4).

The interface parses text into numbers and formats the result; all the money
rules live in ``bill.split_bill``.
"""

from __future__ import annotations

import argparse
from decimal import Decimal

from src.bill import split_bill


def _read_decimal(prompt: str, allow_int: bool = False) -> str:
    """Prompt until the text parses as a number; return the raw string."""
    while True:
        raw = input(prompt).strip()
        try:
            Decimal(raw)
            if allow_int and Decimal(raw) != int(Decimal(raw)):
                raise ValueError
            return raw
        except Exception:
            print("  Please enter a number.")


def run(subtotal, tip_percent, people: int) -> str:
    """Build the printable summary for one bill."""
    result = split_bill(subtotal, tip_percent, people)
    return (
        f"Subtotal   : {Decimal(str(subtotal)):.2f}\n"
        f"Tip        : {result.tip_amount:.2f} ({tip_percent}%)\n"
        f"Total      : {result.total:.2f}\n"
        f"Per person : {result.per_person:.2f}  (split {people} ways)"
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Split a bill with tip.")
    parser.add_argument("--subtotal", help="Bill subtotal, e.g. 84.50")
    parser.add_argument("--tip", help="Tip percent, e.g. 18")
    parser.add_argument("--people", type=int, help="Number of people")
    args = parser.parse_args(argv)

    subtotal = args.subtotal if args.subtotal is not None else _read_decimal("Subtotal: ")
    tip = args.tip if args.tip is not None else _read_decimal("Tip percent: ")
    people = args.people if args.people is not None else int(_read_decimal("People: ", allow_int=True))

    try:
        print(run(subtotal, tip, people))
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
