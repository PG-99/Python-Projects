"""Tests for the Profile Greeter CLI.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

# Make ``src`` importable when running pytest from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.main import build_profile, clean_text, weekly_message, _read_hours


# --- clean_text -----------------------------------------------------------

def test_clean_text_strips_whitespace():
    assert clean_text("  Ada  ") == "Ada"


def test_clean_text_rejects_empty():
    with pytest.raises(ValueError):
        clean_text("   ")


# --- weekly_message (boundary hours 3 and 8) ------------------------------

@pytest.mark.parametrize(
    "hours, needle",
    [
        (0, "steady"),
        (2, "steady"),
        (3, "rhythm"),   # lower boundary of the 3-7 band
        (7, "rhythm"),   # upper boundary of the 3-7 band
        (8, "commitment"),  # first hour of the 8+ band
        (40, "commitment"),
    ],
)
def test_weekly_message_bands(hours, needle):
    assert needle in weekly_message(hours).lower()


def test_weekly_message_rejects_negative():
    with pytest.raises(ValueError):
        weekly_message(-1)


# --- build_profile --------------------------------------------------------

def test_build_profile_contains_all_fields():
    profile = build_profile("Ada", "London", "Learn Python", 5)
    assert "Ada" in profile
    assert "London" in profile
    assert "Learn Python" in profile
    assert "5 per week" in profile


def test_build_profile_rejects_empty_name():
    with pytest.raises(ValueError):
        build_profile("  ", "London", "Learn Python", 5)


# --- _read_hours (non-numeric input) --------------------------------------

def test_read_hours_valid():
    assert _read_hours("6") == 6


def test_read_hours_non_numeric():
    with pytest.raises(ValueError):
        _read_hours("five")


def test_read_hours_negative():
    with pytest.raises(ValueError):
        _read_hours("-2")
