"""Rules for Rock-Paper-Scissors (Project 6).

The rules live entirely in data: a ``beats`` dictionary maps each move to the
set of moves it defeats. ``winner`` just consults that table, so switching to
the Rock-Paper-Scissors-Lizard-Spock variant means swapping the dictionary,
not adding new ``if`` branches.
"""

from __future__ import annotations

# Classic game: move -> set of moves it beats.
RPS: dict[str, set[str]] = {
    "rock": {"scissors"},
    "paper": {"rock"},
    "scissors": {"paper"},
}

# Sam Kass / Karen Bryla extension. Same shape, more data.
RPSLS: dict[str, set[str]] = {
    "rock": {"scissors", "lizard"},
    "paper": {"rock", "spock"},
    "scissors": {"paper", "lizard"},
    "lizard": {"spock", "paper"},
    "spock": {"scissors", "rock"},
}


def moves(beats: dict[str, set[str]] = RPS) -> tuple[str, ...]:
    """All valid moves for a ruleset."""
    return tuple(beats)


def winner(player: str, computer: str, beats: dict[str, set[str]] = RPS) -> str:
    """Return 'win', 'loss', or 'tie' from the player's point of view.

    >>> winner("rock", "scissors")
    'win'
    >>> winner("rock", "paper")
    'loss'
    >>> winner("rock", "rock")
    'tie'
    """
    if player not in beats:
        raise ValueError(f"Unknown player move: {player!r}")
    if computer not in beats:
        raise ValueError(f"Unknown computer move: {computer!r}")
    if player == computer:
        return "tie"
    return "win" if computer in beats[player] else "loss"


def normalize(text: str, beats: dict[str, set[str]] = RPS) -> str:
    """Turn user text into a valid move.

    Accepts the full name or any unambiguous prefix (so ``r`` -> ``rock`` in the
    classic game, while ``s`` is ambiguous in lizard-Spock and needs ``sc`` or
    ``sp``). Raises ``ValueError`` if nothing matches uniquely.
    """
    token = text.strip().lower()
    if token in beats:
        return token
    matches = [move for move in beats if token and move.startswith(token)]
    if len(matches) == 1:
        return matches[0]
    raise ValueError(f"Unknown move: {text!r}")
