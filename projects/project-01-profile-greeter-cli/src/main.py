"""Profile Greeter CLI (Project 1).

Ask for a name, city, learning goal, and weekly study hours, then print a
formatted developer profile.

The code is split into small, pure functions (they take inputs and return
values without touching the screen) plus one ``main`` function that does the
input/output. Keeping the logic pure makes it easy to test.
"""

from __future__ import annotations

import argparse


def clean_text(value: str) -> str:
    """Strip surrounding whitespace and reject empty text.

    >>> clean_text("  Ada  ")
    'Ada'
    """
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("Value cannot be empty.")
    return cleaned


def weekly_message(hours: int) -> str:
    """Return an encouraging message based on weekly study hours."""
    if hours < 0:
        raise ValueError("Hours cannot be negative.")
    if hours < 3:
        return "A small, steady start. Consistency beats intensity."
    if hours <= 7:
        return "A solid weekly rhythm. Keep it up!"
    return "That is serious commitment. Remember to rest, too."


def build_profile(name: str, city: str, goal: str, hours: int) -> str:
    """Build the multiline profile string from validated values."""
    name = clean_text(name)
    city = clean_text(city)
    goal = clean_text(goal)
    return (
        "===== Developer Profile =====\n"
        f"Name        : {name}\n"
        f"City        : {city}\n"
        f"Goal        : {goal}\n"
        f"Study hours : {hours} per week\n"
        f"Note        : {weekly_message(hours)}\n"
        "============================="
    )


def _read_hours(raw: str) -> int:
    """Convert raw hours text to a non-negative int, or raise ValueError."""
    hours = int(raw)  # raises ValueError on non-numeric input
    if hours < 0:
        raise ValueError("Hours cannot be negative.")
    return hours


def main(argv: list[str] | None = None) -> None:
    """Collect values (from flags or prompts), then print the profile."""
    parser = argparse.ArgumentParser(description="Print a developer profile.")
    parser.add_argument("--name", help="Your name")
    parser.add_argument("--city", help="Where you live")
    parser.add_argument("--goal", help="What you want to learn")
    parser.add_argument("--hours", help="Weekly study hours")
    args = parser.parse_args(argv)

    try:
        name = args.name or input("Name: ")
        city = args.city or input("City: ")
        goal = args.goal or input("Learning goal: ")
        hours = _read_hours(args.hours or input("Weekly study hours: "))
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(build_profile(name, city, goal, hours))


if __name__ == "__main__":
    main()
