# Project 3 — Unit Converter

Convert **temperature**, **length**, and **weight** in both directions, from an
interactive menu or a single command-line flag.

## Features

- Six conversions: C↔F, km↔mi, kg↔lb
- A dictionary-driven menu (no long `if/elif` chain)
- Results formatted to two decimal places
- `--convert`/`--value` flags for one-shot, scriptable conversions

## What I learned

- **A dispatch table**: `CONVERSIONS` maps a key → `(function, from_unit, to_unit)`
  using a `NamedTuple`, so the menu, the CLI, and the math all share one source
- **Function composition** in tests via round-trips (convert there and back)
- **Floating-point precision**: results are rounded only at display time with
  `f"{value:.2f}"`; the stored values stay full precision. `-40 C = -40 F`
  (where the scales meet) is used as an exact reference point

## How it works

```
choice/flag → CONVERSIONS lookup → selected pure function → format_value() → print
```

The chosen key selects one function from the table; that function transforms a
single validated number, and the interface formats it to two decimals.

## Setup

```powershell
cd projects\project-03-unit-converter
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

Interactive menu:

```powershell
python -m src.main
```

One-shot with flags:

```powershell
python -m src.main --convert c2f --value 100
# 100.00 C = 212.00 F
```

Valid keys: `c2f`, `f2c`, `km2mi`, `mi2km`, `kg2lb`, `lb2kg`.

## Tests

```powershell
python -m pytest
```

Tests cover known reference points (0 °C = 32 °F, boiling point, −40 crossover),
negatives and zero, round-trips for length and weight, unknown-key handling,
and two-decimal formatting.

## Project structure

```text
project-03-unit-converter/
├── README.md
├── requirements.txt
├── src/
│   ├── converters.py   # six pure conversion functions
│   └── main.py         # menu + CLI + dispatch table
└── tests/
    └── test_converters.py
```

## Roadmap

- [x] Temperature, length, and weight both ways
- [x] Dispatch table + CLI flags + rounded output
- [ ] Add more units (feet/metres, ounces/grams)

## License

MIT — see the [repository license](../../LICENSE).
