# Project 5 — Number Guessing Game

Guess a secret number with high/low hints and a limited number of attempts.

## Features

- Random secret with high/low feedback after each guess
- Limited attempts, with a win/loss summary
- Invalid, out-of-range, and repeated guesses are rejected **without** wasting
  an attempt
- Three difficulty modes via `--difficulty`

## What I learned

- **`random.randint`** to pick a secret, chosen only when one is not injected
- **Dependency injection**: `play` takes `secret`, `input_func`, and
  `output_func`, so tests script the whole game with no randomness or real
  keyboard input — the key trick for testing interactive loops
- **Managing state in a loop**: tracking attempts and a `set` of prior guesses,
  and deciding which inputs count against the player
- Returning a `GameResult` NamedTuple instead of loose variables

## How it works

```
input_func() → parse/validate → check_guess() → hint via output_func → repeat until win or attempts run out
```

Only valid, in-range, non-duplicate guesses advance the attempt counter.
Injecting a fixed `secret` and a scripted `input_func` makes every path
deterministic.

## Setup

```powershell
cd projects\project-05-number-guessing-game
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main --difficulty medium
```

Example:

```
Guess a number between 1 and 100. You have 7 attempts.
Your guess: 50
  Too high!
Your guess: 25
  Too low!
Your guess: 37
Correct! You won in 3 attempt(s).
Nice! Solved in 3 attempt(s).
```

Difficulty modes: `easy` (1–50, 10 tries), `medium` (1–100, 7), `hard` (1–500, 9).

## Tests

```powershell
python -m pytest
```

Tests cover each hint, a win, a first-try win, attempt exhaustion, and that
duplicate / out-of-range / non-numeric guesses never consume an attempt.

## Project structure

```text
project-05-number-guessing-game/
├── README.md
├── requirements.txt
├── src/
│   ├── game.py     # check_guess + play (dependency-injected)
│   └── main.py     # difficulty modes + CLI
└── tests/
    └── test_game.py
```

## Roadmap

- [x] Hints, attempt limit, and input validation
- [x] Difficulty modes
- [ ] Persistent best scores in a JSON file

## License

MIT — see the [repository license](../../LICENSE).
