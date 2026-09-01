"""Command-line entry point for the Number Guessing Game (Project 5).

The portfolio upgrade is difficulty modes: each mode sets the upper bound and
the number of attempts. The heavy lifting stays in ``game.play``.
"""

from __future__ import annotations

import argparse

from src.game import play

# Difficulty mode -> (high bound, max attempts).
DIFFICULTIES = {
    "easy": (50, 10),
    "medium": (100, 7),
    "hard": (500, 9),
}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Guess the secret number.")
    parser.add_argument(
        "--difficulty",
        choices=list(DIFFICULTIES),
        default="medium",
        help="easy (1-50/10 tries), medium (1-100/7), hard (1-500/9)",
    )
    args = parser.parse_args(argv)

    high, attempts = DIFFICULTIES[args.difficulty]
    result = play(max_attempts=attempts, low=1, high=high)

    if result.won:
        print(f"Nice! Solved in {result.attempts} attempt(s).")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
