"""Command-line interface for the Password Strength Checker (Project 8).

The password is read with ``getpass`` so it is not echoed to the screen, and it
is never written anywhere. There is deliberately no ``--password`` flag: passing
a password as an argument would leak it into shell history and process lists.
"""

from __future__ import annotations

import getpass
from pathlib import Path

from src.checker import MAX_SCORE, evaluate, load_common_passwords

PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMMON_FILE = PROJECT_ROOT / "data" / "common_passwords.txt"

DISCLAIMER = (
    "\nNote: this is a rule-based estimate, not a guarantee of security. It "
    "cannot\ndetect password reuse, data breaches, or targeted guessing. Use a "
    "password\nmanager and a unique password for every account."
)


def format_report(report) -> str:
    lines = [f"Strength: {report.rating.upper()} (score {report.score}/{MAX_SCORE})"]
    if report.suggestions:
        lines.append("Suggestions:")
        lines.extend(f"  - {s}" for s in report.suggestions)
    return "\n".join(lines)


def main() -> None:
    common = load_common_passwords(COMMON_FILE) if COMMON_FILE.exists() else frozenset()
    password = getpass.getpass("Enter a password to check (input hidden): ")
    report = evaluate(password, common)
    del password  # do not keep it in memory longer than needed

    print(format_report(report))
    print(DISCLAIMER)


if __name__ == "__main__":
    main()
