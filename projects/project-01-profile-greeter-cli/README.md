# Project 1 — Profile Greeter CLI

A tiny command-line program that asks for your name, city, learning goal, and
weekly study hours, then prints a formatted developer profile.

## Features

- Prompts for input, or accepts `--name`, `--city`, `--goal`, `--hours` flags
- Validation: rejects empty text and non-numeric / negative hours
- An encouraging note based on how many hours you study per week

## What I learned

- **f-strings and multiline strings** to format the profile output
- **Pure functions vs. I/O**: `build_profile` / `weekly_message` return strings
  and are easy to test, while `main` handles `input`/`print`
- **Handling bad input** with `int()` and a `try/except ValueError`
- **`argparse`** so the tool works both interactively and with flags

## How it works

```
terminal input  →  clean_text() validation  →  build_profile() + weekly_message()  →  print
```

`main` gathers values (from CLI flags or prompts), converts hours to an `int`
(catching `ValueError`), and the pure functions assemble the final string.

## Setup

```powershell
cd projects\project-01-profile-greeter-cli
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

Interactive:

```powershell
python -m src.main
```

With flags:

```powershell
python -m src.main --name "Ada" --city "London" --goal "Learn Python" --hours 6
```

Example output:

```
===== Developer Profile =====
Name        : Ada
City        : London
Goal        : Learn Python
Study hours : 6 per week
Note        : A solid weekly rhythm. Keep it up!
=============================
```

## Tests

```powershell
python -m pytest
```

Tests cover whitespace stripping, empty-name rejection, the boundary hours 3
and 8, and non-numeric / negative hours.

## Project structure

```text
project-01-profile-greeter-cli/
├── README.md
├── requirements.txt
├── src/
│   └── main.py
└── tests/
    └── test_main.py
```

## Roadmap

- [x] Prompts, validation, and formatted profile
- [x] `--name/--city/--goal/--hours` flags via argparse
- [ ] Save profiles to a file and list them

## License

MIT — see the [repository license](../../LICENSE).
