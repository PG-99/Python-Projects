"""Tests for the Number Guessing Game.

The game is driven by injecting a fixed secret and a scripted list of guesses,
so no randomness or real input is involved.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.game import GameResult, check_guess, play


def scripted(guesses):
    """Return an input_func that yields each guess in turn (as strings)."""
    it = iter(guesses)
    return lambda: str(next(it))


# --- check_guess ----------------------------------------------------------

@pytest.mark.parametrize(
    "guess, expected",
    [(30, "low"), (70, "high"), (50, "correct")],
)
def test_check_guess(guess, expected):
    assert check_guess(50, guess) == expected


# --- play: winning and losing ---------------------------------------------

def test_win_records_attempts():
    result = play(secret=42, input_func=scripted([10, 90, 42]))
    assert result == GameResult(won=True, attempts=3, secret=42)


def test_win_on_first_try():
    result = play(secret=7, input_func=scripted([7]))
    assert result.won and result.attempts == 1


def test_loss_on_attempt_exhaustion():
    # Never guesses 42; three wrong guesses with max_attempts=3 -> loss.
    result = play(secret=42, max_attempts=3, input_func=scripted([1, 2, 3]))
    assert result.won is False
    assert result.attempts == 3
    assert result.secret == 42


# --- guesses that must NOT consume an attempt -----------------------------

def test_duplicate_guess_does_not_consume_attempt():
    # 10 twice, then 42. If the duplicate counted, we would run out first.
    result = play(secret=42, max_attempts=2, input_func=scripted([10, 10, 42]))
    assert result.won and result.attempts == 2


def test_out_of_range_guess_does_not_consume_attempt():
    result = play(secret=42, max_attempts=2, low=1, high=100,
                  input_func=scripted([500, 42]))
    assert result.won and result.attempts == 1


def test_non_numeric_guess_does_not_consume_attempt():
    result = play(secret=42, max_attempts=2, input_func=scripted(["oops", 42]))
    assert result.won and result.attempts == 1


# --- hints are emitted ----------------------------------------------------

def test_hints_reported_via_output():
    lines = []
    play(secret=50, max_attempts=3, input_func=scripted([10, 90, 50]),
         output_func=lines.append)
    joined = "\n".join(lines).lower()
    assert "too low" in joined
    assert "too high" in joined
    assert "won" in joined
