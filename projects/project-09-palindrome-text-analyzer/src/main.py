"""Command-line interface for the Palindrome and Text Analyzer (Project 9).

Analyze a single piece of text, or (the portfolio upgrade) every line of a file
with ``--file``.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from src.analyzer import is_palindrome, report


def _analyze_file(path: Path) -> None:
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        mark = "P" if is_palindrome(raw) else " "
        print(f"[{mark}] line {number}: {raw}")
    print("\n(P = palindrome, ignoring case, spaces, and punctuation)")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Check palindromes and analyze text.")
    parser.add_argument("text", nargs="?", help="Text to analyze")
    parser.add_argument("--file", type=Path, help="Analyze each line of this file")
    args = parser.parse_args(argv)

    if args.file:
        if not args.file.exists():
            raise SystemExit(f"File not found: {args.file}")
        _analyze_file(args.file)
        return

    text = args.text if args.text is not None else input("Enter text: ")
    print(report(text))


if __name__ == "__main__":
    main()
