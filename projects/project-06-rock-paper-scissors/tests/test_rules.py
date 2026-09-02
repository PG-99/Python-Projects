"""Tests for the Rock-Paper-Scissors rules.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rules import RPS, RPSLS, moves, normalize, winner


# --- winner: every classic pair -------------------------------------------

@pytest.mark.parametrize(
    "player, computer, expected",
    [
        ("rock", "scissors", "win"),
        ("rock", "paper", "loss"),
        ("rock", "rock", "tie"),
        ("paper", "rock", "win"),
        ("paper", "scissors", "loss"),
        ("paper", "paper", "tie"),
        ("scissors", "paper", "win"),
        ("scissors", "rock", "loss"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_classic_pairs(player, computer, expected):
    assert winner(player, computer) == expected


def test_unknown_move_raises():
    with pytest.raises(ValueError):
        winner("rock", "banana")


# --- ruleset consistency (works for both rulesets) ------------------------

@pytest.mark.parametrize("beats", [RPS, RPSLS])
def test_exactly_one_winner_for_distinct_moves(beats):
    ms = moves(beats)
    for a in ms:
        for b in ms:
            if a == b:
                assert winner(a, b, beats) == "tie"
            else:
                # Exactly one direction is a win.
                wins = [winner(a, b, beats) == "win", winner(b, a, beats) == "win"]
                assert wins.count(True) == 1, (a, b)


def test_lizard_spock_specific():
    assert winner("spock", "scissors", RPSLS) == "win"
    assert winner("lizard", "spock", RPSLS) == "win"
    assert winner("paper", "spock", RPSLS) == "win"


# --- normalize ------------------------------------------------------------

def test_normalize_full_and_prefix():
    assert normalize("  ROCK ") == "rock"
    assert normalize("r") == "rock"          # unambiguous in classic
    assert normalize("sc") == "scissors"


def test_normalize_ambiguous_prefix_in_lizard_spock():
    with pytest.raises(ValueError):
        normalize("s", RPSLS)                 # scissors vs spock


def test_normalize_unknown():
    with pytest.raises(ValueError):
        normalize("xyz")
