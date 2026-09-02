"""Tests for the Rock-Paper-Scissors match loop.

The computer's chooser and the player's input are both injected, so matches
play out deterministically.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.game import play_match, required_wins, validate_match_length


def scripted(items):
    it = iter(items)
    return lambda: next(it)


# --- match length validation ----------------------------------------------

@pytest.mark.parametrize("bad", [0, -1, 2, 4, 10])
def test_invalid_match_length(bad):
    with pytest.raises(ValueError):
        validate_match_length(bad)


@pytest.mark.parametrize("n, need", [(1, 1), (3, 2), (5, 3), (7, 4)])
def test_required_wins(n, need):
    validate_match_length(n)
    assert required_wins(n) == need


# --- playing matches -------------------------------------------------------

def test_player_sweeps_best_of_three():
    # Player always plays rock; computer always scissors -> player wins 2-0.
    result = play_match(
        match_length=3,
        input_func=scripted(["rock", "rock"]),
        computer_chooser=scripted(["scissors", "scissors"]),
        output_func=lambda _s: None,
    )
    assert result.winner == "player"
    assert (result.player_wins, result.computer_wins) == (2, 0)
    assert result.rounds == 2


def test_computer_wins():
    result = play_match(
        match_length=3,
        input_func=scripted(["rock", "rock"]),
        computer_chooser=scripted(["paper", "paper"]),
        output_func=lambda _s: None,
    )
    assert result.winner == "computer"
    assert (result.player_wins, result.computer_wins) == (0, 2)


def test_ties_do_not_end_match_but_are_recorded():
    # tie, tie, then player wins twice.
    result = play_match(
        match_length=3,
        input_func=scripted(["rock", "rock", "rock", "rock"]),
        computer_chooser=scripted(["rock", "rock", "scissors", "scissors"]),
        output_func=lambda _s: None,
    )
    assert result.winner == "player"
    assert result.rounds == 4
    assert sum(1 for r in result.history if r.result == "tie") == 2


def test_invalid_input_does_not_consume_a_round():
    result = play_match(
        match_length=1,
        input_func=scripted(["banana", "rock"]),
        computer_chooser=scripted(["scissors"]),
        output_func=lambda _s: None,
    )
    assert result.winner == "player"
    assert result.rounds == 1
