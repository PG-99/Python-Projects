"""Palindrome check and text statistics (Project 9).

Separation of concerns:
- ``normalize`` produces one canonical comparison form (lower-cased,
  alphanumeric only) *without* mutating the original text.
- ``is_palindrome`` and ``statistics`` consume text and return data; they never
  print. Formatting for humans lives in ``report`` / the CLI.
"""

from __future__ import annotations

import string
from typing import NamedTuple


class TextStats(NamedTuple):
    characters: int
    letters: int
    digits: int
    words: int
    unique_words: int


def normalize(text: str) -> str:
    """Return a lower-cased, alphanumeric-only form for comparison.

    Uses ``casefold`` (more aggressive than ``lower`` for Unicode) and keeps
    only characters where ``str.isalnum`` is true.

    >>> normalize("A man, a plan!")
    'amanaplan'
    """
    return "".join(ch for ch in text.casefold() if ch.isalnum())


def is_palindrome(text: str) -> bool:
    """True if ``text`` reads the same forwards and backwards once normalized.

    Requires at least one alphanumeric character, so empty or
    punctuation-only input is not considered a palindrome.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("hello")
    False
    """
    normalized = normalize(text)
    return bool(normalized) and normalized == normalized[::-1]


def _word_key(token: str) -> str:
    """Canonical form of a word: case-folded, outer punctuation stripped."""
    return token.casefold().strip(string.punctuation)


def statistics(text: str) -> TextStats:
    """Count characters, letters, digits, words, and unique words."""
    tokens = text.split()
    unique = {key for key in (_word_key(t) for t in tokens) if key}
    return TextStats(
        characters=len(text),
        letters=sum(1 for ch in text if ch.isalpha()),
        digits=sum(1 for ch in text if ch.isdigit()),
        words=len(tokens),
        unique_words=len(unique),
    )


def report(text: str) -> str:
    """Build a readable report combining the palindrome result and stats."""
    stats = statistics(text)
    verdict = "yes" if is_palindrome(text) else "no"
    return (
        f"Palindrome   : {verdict}\n"
        f"Characters   : {stats.characters}\n"
        f"Letters      : {stats.letters}\n"
        f"Digits       : {stats.digits}\n"
        f"Words        : {stats.words}\n"
        f"Unique words : {stats.unique_words}"
    )
