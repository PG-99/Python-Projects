# Project 8 — Password Strength Checker

Score a password locally, explain how to improve it, and **never store it**.

## Features

- Independent checks: length, lowercase, uppercase, number, symbol, repeated
  runs, and known-common passwords
- A transparent 0–6 score mapped to **weak / medium / strong** with suggestions
- Hidden input via `getpass` (no echo), and no `--password` flag by design
- An explicit disclaimer that a good score is not a guarantee of security

## What I learned

- **Privacy-aware design**: read the password with `getpass`, never print or
  persist it, and avoid a CLI flag that would leak it into shell history
- **Rules produce facts, an aggregator scores them**: each check is a tiny
  function; `evaluate` combines them and *returns* a report instead of printing
- **Unicode-aware checks**: `str.islower/isupper/isdigit` and "non-alphanumeric
  = symbol" handle accented letters and emoji
- **The limits of rule-based scoring**: it can't detect reuse or breaches, so a
  shipped common-password list downgrades obvious choices to weak

## How it works

```
password → independent rules (facts) → evaluate() aggregates → score + rating + suggestions → UI prints
```

`evaluate(password, common)` is pure and fully tested; `main` only handles
hidden input and output.

## Setup

```powershell
cd projects\project-08-password-strength-checker
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main
```

Example:

```
Enter a password to check (input hidden):
Strength: MEDIUM (score 4/6)
Suggestions:
  - Longer is stronger: aim for 12+ characters.
  - Add a symbol (for example ! ? # $).

Note: this is a rule-based estimate, not a guarantee of security. ...
```

## Tests

```powershell
python -m pytest
```

Tests cover each rule, empty / strong / medium / long-single-class passwords,
Unicode, repeated characters, and common-password detection (including the
shipped list).

## Project structure

```text
project-08-password-strength-checker/
├── README.md
├── requirements.txt
├── data/
│   └── common_passwords.txt
├── src/
│   ├── checker.py   # rules + evaluate() (pure, no I/O)
│   └── main.py      # getpass input + output
└── tests/
    └── test_checker.py
```

## Roadmap

- [x] Rule-based scoring with suggestions and a common-password list
- [x] Hidden input and a clear "not a guarantee" disclaimer
- [ ] Estimate entropy and flag keyboard-sequence patterns

## License

MIT — see the [repository license](../../LICENSE).
