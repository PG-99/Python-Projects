# Project 2 — Four-Operation Calculator

A command-line calculator for `+`, `-`, `*`, and `/` that keeps running until
you quit, and prints a history of the session's calculations.

## Features

- The four basic operations on integers and decimals
- Clear errors for **division by zero** and **unknown operators**
- Re-prompts on invalid numbers/operators instead of crashing
- Session **history** printed on exit

## What I learned

- **Separating logic from I/O**: `calculate()` is pure and fully tested; the
  looping and prompting live in `main.py`
- **A dictionary of operators** (`{"+": ...}`) replaces a long `if/elif` chain
- **Raising `ValueError`** for bad operators and divide-by-zero, then handling
  it at the interface layer
- **Parameterized pytest cases** to cover many inputs concisely

## How it works

```
input → read_number()/read_operator() validation → calculate() → format_result() → print + history
```

`calculate(left, operator, right)` looks the operator up in a table, guards
against division by zero, and returns a number. The interface formats it and
stores it in the session history list.

## Setup

```powershell
cd projects\project-02-four-operation-calculator
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main
```

Example session:

```
First number (or 'q' to quit): 10
Operator ('+', '-', '*', '/'): /
Second number: 4
10 / 4 = 2.5
First number (or 'q' to quit): q

History this session:
  10 / 4 = 2.5
Goodbye!
```

## Tests

```powershell
python -m pytest
```

Tests cover all four operators, negative and decimal operands, division by
zero, unknown operators, and result formatting.

## Project structure

```text
project-02-four-operation-calculator/
├── README.md
├── requirements.txt
├── src/
│   ├── calculator.py   # pure arithmetic
│   └── main.py         # command-line interface
└── tests/
    └── test_calculator.py
```

## Roadmap

- [x] Four operations with validation and error handling
- [x] Session history and parameterized tests
- [ ] Support a full expression like `10 / 4` on one line

## License

MIT — see the [repository license](../../LICENSE).
