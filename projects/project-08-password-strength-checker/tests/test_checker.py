"""Tests for the Password Strength Checker.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.checker import (
    evaluate,
    has_repeated_run,
    has_symbol,
    load_common_passwords,
)

COMMON = frozenset({"password", "123456", "qwerty"})


# --- individual rules -----------------------------------------------------

def test_symbol_detection_includes_unicode():
    assert has_symbol("a!") is True
    assert has_symbol("abc123") is False
    assert has_symbol("café☕") is True  # emoji counts as a symbol


def test_repeated_run():
    assert has_repeated_run("aaab") is True
    assert has_repeated_run("aabb") is False


# --- evaluate: ratings ----------------------------------------------------

def test_empty_password_is_weak():
    report = evaluate("", COMMON)
    assert report.rating == "weak"
    assert report.score == 0
    assert any("8 characters" in s for s in report.suggestions)


def test_strong_password():
    report = evaluate("Str0ng!Passphrase", COMMON)  # 12+, all classes
    assert report.rating == "strong"
    assert report.score == 6


def test_medium_password():
    # 9 chars, lower+upper+digit, no symbol -> length(1)+lower+upper+digit = 4
    report = evaluate("Abcdefgh1", COMMON)
    assert report.rating == "medium"
    assert 3 <= report.score <= 4


def test_long_but_single_class():
    # 16 distinct lowercase letters (no 3-in-a-row run):
    # length(2) + lower(1) = 3 -> medium, and it should suggest more classes.
    report = evaluate("abcdefghijklmnop", COMMON)
    assert report.rating == "medium"
    assert report.score == 3
    assert any("uppercase" in s for s in report.suggestions)


def test_repeated_run_penalizes_long_single_char():
    # A run of identical characters is penalized, so it stays weak.
    report = evaluate("a" * 20, COMMON)
    assert report.rating == "weak"
    assert any("repeating" in s.lower() for s in report.suggestions)


def test_common_password_forced_weak():
    # "password" would otherwise score for length+lowercase, but is common.
    report = evaluate("password", COMMON)
    assert report.rating == "weak"
    assert report.score == 0
    assert any("common" in s.lower() for s in report.suggestions)


def test_repeated_characters_lower_score():
    with_run = evaluate("Aaaa1111!!!!", COMMON)
    assert any("repeating" in s.lower() for s in with_run.suggestions)


def test_unicode_password_scores():
    # Non-ASCII letters still count as letters; long passphrase with a digit/symbol.
    report = evaluate("Ünïcödé-Pässwörd9", COMMON)
    assert report.score >= 5


# --- common list loader ---------------------------------------------------

def test_load_common_passwords_from_shipped_file():
    data = Path(__file__).resolve().parents[1] / "data" / "common_passwords.txt"
    common = load_common_passwords(data)
    assert "password" in common
    assert "123456" in common
    # evaluate should flag a shipped common password as weak.
    assert evaluate("letmein", common).rating == "weak"
