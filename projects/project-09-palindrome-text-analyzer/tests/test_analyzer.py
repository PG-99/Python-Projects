"""Tests for the Palindrome and Text Analyzer.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.analyzer import is_palindrome, normalize, statistics


# --- normalize ------------------------------------------------------------

def test_normalize_strips_punctuation_and_case():
    assert normalize("A man, a plan!") == "amanaplan"


def test_normalize_keeps_digits_and_unicode_letters():
    assert normalize("Café 123!") == "café123"


# --- is_palindrome --------------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("A man, a plan, a canal: Panama", True),  # punctuation + spaces + case
        ("RaceCar", True),                          # mixed case
        ("12321", True),                            # digits
        ("hello", False),
        ("", False),                                # empty input
        ("!!! ???", False),                         # punctuation only -> empty
        ("Été", True),                              # unicode palindrome
        ("Was it a car or a cat I saw?", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


# --- statistics -----------------------------------------------------------

def test_statistics_basic_counts():
    stats = statistics("Hi there, hi!")
    assert stats.characters == len("Hi there, hi!")
    assert stats.letters == 9          # H i t h e r e h i
    assert stats.digits == 0
    assert stats.words == 3            # "Hi" "there," "hi!"
    assert stats.unique_words == 2     # hi, there (case-insensitive, punct-stripped)


def test_statistics_counts_digits_and_empty():
    stats = statistics("room 101")
    assert stats.digits == 3
    assert stats.words == 2

    empty = statistics("")
    assert empty == statistics("")  # deterministic
    assert (empty.characters, empty.words, empty.unique_words) == (0, 0, 0)


def test_statistics_unique_words_case_insensitive():
    stats = statistics("Go go GO stop")
    assert stats.words == 4
    assert stats.unique_words == 2  # "go", "stop"
