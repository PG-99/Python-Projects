"""Match loop for Rock-Paper-Scissors (Project 6).

A "best of N" match runs until one side reaches a majority of wins. The
computer's move chooser is injected so tests can make it predictable.
"""

from __future__ import annotations

import random
from typing import Callable, NamedTuple

from src.rules import RPS, moves, normalize, winner


class RoundOutcome(NamedTuple):
    player_move: str
    computer_move: str
    result: str  # 'win' | 'loss' | 'tie'


class MatchResult(NamedTuple):
    winner: str  # 'player' | 'computer'
    player_wins: int
    computer_wins: int
    rounds: int
    history: tuple[RoundOutcome, ...]


def validate_match_length(match_length: int) -> None:
    """Match length must be a positive, odd number (so there is no draw)."""
    if match_length < 1 or match_length % 2 == 0:
        raise ValueError("Match length must be a positive odd number.")


def required_wins(match_length: int) -> int:
    """Wins needed to take the match (a strict majority)."""
    return match_length // 2 + 1


def play_match(
    match_length: int = 3,
    beats: dict[str, set[str]] = RPS,
    input_func: Callable[[], str] | None = None,
    computer_chooser: Callable[[], str] | None = None,
    output_func: Callable[[str], None] = print,
) -> MatchResult:
    """Play a best-of-``match_length`` match and return the result."""
    validate_match_length(match_length)
    need = required_wins(match_length)

    if input_func is None:
        input_func = lambda: input("Your move: ")
    if computer_chooser is None:
        options = moves(beats)
        computer_chooser = lambda: random.choice(options)

    player_wins = 0
    computer_wins = 0
    history: list[RoundOutcome] = []

    while player_wins < need and computer_wins < need:
        try:
            player_move = normalize(input_func(), beats)
        except ValueError as error:
            output_func(f"  {error}")
            continue  # invalid input does not count as a round

        computer_move = computer_chooser()
        result = winner(player_move, computer_move, beats)
        if result == "win":
            player_wins += 1
        elif result == "loss":
            computer_wins += 1

        history.append(RoundOutcome(player_move, computer_move, result))
        output_func(
            f"You: {player_move} | CPU: {computer_move} -> {result} "
            f"(score {player_wins}-{computer_wins})"
        )

    champion = "player" if player_wins > computer_wins else "computer"
    output_func(f"Match over: {champion} wins {player_wins}-{computer_wins}.")
    return MatchResult(
        winner=champion,
        player_wins=player_wins,
        computer_wins=computer_wins,
        rounds=len(history),
        history=tuple(history),
    )
