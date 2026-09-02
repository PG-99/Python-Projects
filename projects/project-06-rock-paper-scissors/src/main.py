"""Command-line entry point for Rock-Paper-Scissors (Project 6)."""

from __future__ import annotations

import argparse

from src.game import play_match
from src.rules import RPS, RPSLS, moves

MODES = {"classic": RPS, "lizard-spock": RPSLS}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Play a Rock-Paper-Scissors match.")
    parser.add_argument("--mode", choices=list(MODES), default="classic")
    parser.add_argument("--best-of", type=int, default=3, help="Odd number of rounds")
    args = parser.parse_args(argv)

    beats = MODES[args.mode]
    print(f"Mode: {args.mode}. Moves: {', '.join(moves(beats))}.")
    try:
        result = play_match(match_length=args.best_of, beats=beats)
    except ValueError as error:
        parser.error(str(error))
        return

    print(f"You {'won' if result.winner == 'player' else 'lost'} the match.")


if __name__ == "__main__":
    main()
