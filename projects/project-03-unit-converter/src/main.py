"""Command-line interface for the Unit Converter (Project 3).

A single lookup table (``CONVERSIONS``) maps a short key to the function to
call plus the unit labels. This replaces a long if/elif chain: the menu, the
CLI flags, and the actual conversion all read from the same table.
"""

from __future__ import annotations

import argparse
from typing import Callable, NamedTuple

from src.converters import (
    c_to_f,
    f_to_c,
    kg_to_lb,
    km_to_miles,
    lb_to_kg,
    miles_to_km,
)


class Conversion(NamedTuple):
    func: Callable[[float], float]
    from_unit: str
    to_unit: str


# Ordered so the interactive menu numbering is stable.
CONVERSIONS: dict[str, Conversion] = {
    "c2f": Conversion(c_to_f, "C", "F"),
    "f2c": Conversion(f_to_c, "F", "C"),
    "km2mi": Conversion(km_to_miles, "km", "mi"),
    "mi2km": Conversion(miles_to_km, "mi", "km"),
    "kg2lb": Conversion(kg_to_lb, "kg", "lb"),
    "lb2kg": Conversion(lb_to_kg, "lb", "kg"),
}


def convert(key: str, value: float) -> float:
    """Run the conversion named by ``key`` on ``value``.

    Raises ``KeyError`` (via ValueError) for an unknown key.

    >>> round(convert("c2f", 100), 2)
    212.0
    """
    if key not in CONVERSIONS:
        raise ValueError(f"Unknown conversion: {key!r}")
    return CONVERSIONS[key].func(value)


def format_value(value: float) -> str:
    """Format a converted number to two decimal places."""
    return f"{value:.2f}"


def _read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("  Please enter a number (for example 12 or 3.5).")


def _run_interactive() -> None:
    keys = list(CONVERSIONS)
    print("Unit Converter")
    for index, key in enumerate(keys, start=1):
        conv = CONVERSIONS[key]
        print(f"  {index}. {conv.from_unit} -> {conv.to_unit}  ({key})")

    choice = input("Choose 1-6: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(keys)):
        print("  Please choose a number from the menu.")
        return

    key = keys[int(choice) - 1]
    value = _read_number("Value: ")
    result = convert(key, value)
    conv = CONVERSIONS[key]
    print(f"{format_value(value)} {conv.from_unit} = {format_value(result)} {conv.to_unit}")


def main(argv: list[str] | None = None) -> None:
    """Use --convert/--value for a one-shot conversion, else run the menu."""
    parser = argparse.ArgumentParser(description="Convert temperature, length, or weight.")
    parser.add_argument("--convert", choices=list(CONVERSIONS), help="Conversion key, e.g. c2f")
    parser.add_argument("--value", type=float, help="Number to convert")
    args = parser.parse_args(argv)

    if args.convert and args.value is not None:
        result = convert(args.convert, args.value)
        conv = CONVERSIONS[args.convert]
        print(f"{format_value(args.value)} {conv.from_unit} = {format_value(result)} {conv.to_unit}")
    else:
        _run_interactive()


if __name__ == "__main__":
    main()
