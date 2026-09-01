"""Number Guessing Game (Project 5).

The player guesses a secret number and gets high/low hints within a limited
number of attempts.

Two ideas make this testable without a human at the keyboard:
- ``check_guess`` is a pure comparison.
- ``play`` accepts the secret, the input source, and the output sink as
  arguments (dependency injection). Tests pass a fixed secret and a scripted
  list of guesses, so the game plays out deterministically.
"""

from __future__ import annotations

import random
from typing import Callable, NamedTuple


class GameResult(NamedTuple):
    won: bool
    attempts: int
    secret: int


def check_guess(secret: int, guess: int) -> str:
    """Return 'low', 'high', or 'correct' for a guess against the secret.

    >>> check_guess(50, 30)
    'low'
    >>> check_guess(50, 70)
    'high'
    >>> check_guess(50, 50)
    'correct'
    """
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"


def play(
    secret: int | None = None,
    max_attempts: int = 7,
    low: int = 1,
    high: int = 100,
    input_func: Callable[[], str] | None = None,
    output_func: Callable[[str], None] = print,
) -> GameResult:
    """Run the game loop and return the result.

    A random ``secret`` is chosen only when one is not supplied. Invalid,
    out-of-range, and repeated guesses are rejected *without* consuming an
    attempt.
    """
    if secret is None:
        secret = random.randint(low, high)
    if input_func is None:
        input_func = lambda: input("Your guess: ")

    guesses: set[int] = set()
    attempts = 0
    output_func(
        f"Guess a number between {low} and {high}. You have {max_attempts} attempts."
    )

    while attempts < max_attempts:
        raw = input_func()
        try:
            guess = int(str(raw).strip())
        except (ValueError, TypeError):
            output_func("  Please enter a whole number.")
            continue
        if guess < low or guess > high:
            output_func(f"  Out of range. Enter a number from {low} to {high}.")
            continue
        if guess in guesses:
            output_func("  You already tried that number.")
            continue

        guesses.add(guess)
        attempts += 1
        result = check_guess(secret, guess)
        if result == "correct":
            output_func(f"Correct! You won in {attempts} attempt(s).")
            return GameResult(won=True, attempts=attempts, secret=secret)
        output_func("  Too low!" if result == "low" else "  Too high!")

    output_func(f"Out of attempts. The number was {secret}.")
    return GameResult(won=False, attempts=attempts, secret=secret)
