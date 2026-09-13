"""Password strength scoring (Project 8).

Design notes:
- Each rule is a small, independent function that reports a *fact* about the
  password. ``evaluate`` aggregates those facts into a transparent score and a
  list of suggestions. Nothing here prints, and the password is never stored.
- Scoring is rule-based and deliberately simple. It cannot know whether a
  password has been reused or leaked, so a high score is not a guarantee of
  security (the CLI says so explicitly).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

MAX_SCORE = 6
_REPEATED_RUN = re.compile(r"(.)\1\1")  # same character three+ times in a row


class PasswordReport(NamedTuple):
    score: int
    rating: str  # 'weak' | 'medium' | 'strong'
    suggestions: tuple[str, ...]


def has_lower(password: str) -> bool:
    return any(c.islower() for c in password)


def has_upper(password: str) -> bool:
    return any(c.isupper() for c in password)


def has_digit(password: str) -> bool:
    return any(c.isdigit() for c in password)


def has_symbol(password: str) -> bool:
    """A symbol is any non-alphanumeric character (Unicode aware)."""
    return any(not c.isalnum() for c in password)


def has_repeated_run(password: str) -> bool:
    return _REPEATED_RUN.search(password) is not None


def _rating(score: int) -> str:
    if score <= 2:
        return "weak"
    if score <= 4:
        return "medium"
    return "strong"


def evaluate(password: str, common: frozenset[str] = frozenset()) -> PasswordReport:
    """Score ``password`` and return a report with improvement suggestions.

    ``common`` is a set of known-common passwords (lower-cased); a match forces
    a weak rating regardless of composition.
    """
    suggestions: list[str] = []
    score = 0
    length = len(password)

    if length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")
    if length >= 12:
        score += 1
    else:
        suggestions.append("Longer is stronger: aim for 12+ characters.")

    if has_lower(password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")
    if has_upper(password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")
    if has_digit(password):
        score += 1
    else:
        suggestions.append("Add a number.")
    if has_symbol(password):
        score += 1
    else:
        suggestions.append("Add a symbol (for example ! ? # $).")

    if has_repeated_run(password):
        suggestions.append("Avoid repeating the same character three+ times.")
        score = max(0, score - 1)

    if password.lower() in common and password != "":
        suggestions.insert(0, "This is a very common password; pick something unique.")
        return PasswordReport(score=0, rating="weak", suggestions=tuple(suggestions))

    return PasswordReport(score=score, rating=_rating(score), suggestions=tuple(suggestions))


def load_common_passwords(path: str | Path) -> frozenset[str]:
    """Load a common-password list (one per line) as a lower-cased frozenset."""
    text = Path(path).read_text(encoding="utf-8")
    return frozenset(
        line.strip().lower() for line in text.splitlines() if line.strip()
    )
