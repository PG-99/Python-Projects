# Project 6 — Rock-Paper-Scissors Tournament

Play a best-of-N match against the computer, with round history and a final
score. The rules are pure data, so the lizard-Spock variant is just a bigger
dictionary.

## Features

- Best-of-N matches (odd number of rounds; first to a majority wins)
- Round-by-round history and final score
- Flexible input: full move name or any unambiguous prefix (`r` → rock)
- Two modes via `--mode`: `classic` and `lizard-spock`

## What I learned

- **Encoding rules as data**: a `beats` dictionary maps each move to the set it
  defeats. `winner()` reads the table, so new rules mean new *data*, not new
  `if` branches — the whole point of the lizard-Spock upgrade
- **Input normalization** with unambiguous prefixes (and why `s` is ambiguous
  once "scissors" and "spock" both exist)
- **Dependency injection** of the computer's chooser and the player's input to
  make the match loop deterministic in tests
- **Match state**: two counters, ties that don't end the match, and rejecting
  invalid input without consuming a round

## How it works

```
input → normalize() → winner() (via beats table) → update counters + history → repeat until a majority
```

`play_match` owns the loop and state; `rules.winner` owns who beats whom.

## Setup

```powershell
cd projects\project-06-rock-paper-scissors
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main --mode classic --best-of 3
python -m src.main --mode lizard-spock --best-of 5
```

Example round:

```
You: rock | CPU: scissors -> win (score 1-0)
```

## Tests

```powershell
python -m pytest
```

Tests cover every classic move pair, a consistency property for both rulesets
(exactly one winner between distinct moves), prefix normalization, match-length
validation, full matches, ties that don't end the match, and invalid input that
doesn't consume a round.

## Project structure

```text
project-06-rock-paper-scissors/
├── README.md
├── requirements.txt
├── src/
│   ├── rules.py    # beats table, winner(), normalize()
│   ├── game.py     # match loop (dependency-injected)
│   └── main.py     # modes + CLI
└── tests/
    ├── test_rules.py
    └── test_game.py
```

## Roadmap

- [x] Classic best-of-N with history and validation
- [x] Lizard-Spock by adding data, not conditionals
- [ ] Track match statistics across sessions

## License

MIT — see the [repository license](../../LICENSE).
