# Project 9 — Palindrome and Text Analyzer

Check whether text is a palindrome (ignoring case, spaces, and punctuation) and
report simple text statistics.

## Features

- Palindrome check that ignores case, spaces, and punctuation
- Statistics: characters, letters, digits, words, and unique words
- Unicode-aware (handles accented letters and case-folding)
- Analyze a single string, or every line of a file with `--file`

## What I learned

- **Normalization as a separate step**: `normalize()` builds one comparison
  form with `casefold()` + `str.isalnum()` without touching the original text
- **`casefold` vs `lower`** for correct Unicode case-insensitive comparison
- **Slicing** (`s[::-1]`) to reverse, and **comprehensions** to count
- **Separation of concerns**: analysis functions return data (`TextStats`), and
  only the CLI formats it for humans
- A deliberate design choice: empty / punctuation-only input is **not** a
  palindrome (there is nothing to compare)

## How it works

```
text → normalize() → is_palindrome() / statistics() (pure) → report() formats → print
```

## Setup

```powershell
cd projects\project-09-palindrome-text-analyzer
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main "A man, a plan, a canal: Panama"
```

Output:

```
Palindrome   : yes
Characters   : 30
Letters      : 21
Digits       : 0
Words        : 7
Unique words : 5
```

Analyze a file line by line:

```powershell
python -m src.main --file poems.txt
```

## Tests

```powershell
python -m pytest
```

Tests cover punctuation, mixed case, digits, empty input, punctuation-only,
Unicode, and each statistic (including case-insensitive unique words).

## Project structure

```text
project-09-palindrome-text-analyzer/
├── README.md
├── requirements.txt
├── src/
│   ├── analyzer.py   # normalize, is_palindrome, statistics, report
│   └── main.py       # CLI (single text or --file)
└── tests/
    └── test_analyzer.py
```

## Roadmap

- [x] Palindrome check + statistics with Unicode normalization
- [x] Per-line file analysis via argparse
- [ ] Report the longest palindromic substring

## License

MIT — see the [repository license](../../LICENSE).
