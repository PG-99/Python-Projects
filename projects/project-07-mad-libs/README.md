# Project 7 — Mad Libs Story Generator

Fill named placeholders in story templates and save the finished tale. Templates
are plain text files, so adding a story means adding a file — no code changes.

## Features

- Choose from multiple story templates
- Prompts once per unique placeholder (a repeated `{name}` is asked once)
- Saves each finished story to `output/` with a timestamped filename
- `--template <name>` and `--list` flags

## What I learned

- **`string.Formatter().parse()`** to discover a template's field names without
  guessing at regex — and how it distinguishes real placeholders from escaped
  `{{` / `}}` braces
- **One dictionary fills every occurrence**, so repeated fields stay consistent
- **Templates as data**: the engine never hard-codes a story; new stories are
  just new `.txt` files (the portfolio upgrade is accepting them via pull request)
- **Injecting `now`** into `save_story` so the timestamped filename is testable

## How it works

```
template file → find_fields() → prompt per field → fill_story() (template.format) → print + save_story()
```

The template is data; the parser extracts the required inputs; one dictionary
fills the template consistently; the result is written to a timestamped file.

## Setup

```powershell
cd projects\project-07-mad-libs
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main --list
python -m src.main --template adventure
```

Interactive (menu):

```powershell
python -m src.main
```

Generated stories are written to `projects/project-07-mad-libs/output/`
(git-ignored, since they are personal output).

## Tests

```powershell
python -m pytest
```

Tests cover repeated fields, empty templates, escaped braces, missing values,
extra answers, the timestamped save (via an injected clock), and that every
shipped template parses and fills.

## Project structure

```text
project-07-mad-libs/
├── README.md
├── requirements.txt
├── templates/
│   ├── adventure.txt
│   └── tech_startup.txt
├── src/
│   ├── story.py    # find_fields, fill_story, save_story, loaders
│   └── main.py     # menu + CLI
└── tests/
    └── test_story.py
```

## Roadmap

- [x] Template discovery, filling, and timestamped saving
- [x] Ship multiple templates + template selection
- [ ] Accept community templates through pull requests

## License

MIT — see the [repository license](../../LICENSE).
