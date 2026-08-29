# Project 4 — Tip and Bill Splitter

Calculate the tip, grand total, and per-person share of a restaurant bill —
using exact decimal money math.

## Features

- Tip, total, and per-person amounts from a subtotal, tip %, and party size
- **Exact money** with `Decimal` (no floating-point cent errors)
- Validation: rejects negative subtotal/tip and fewer than one person
- `--subtotal`/`--tip`/`--people` flags for one-shot use

## What I learned

- **Why `Decimal` beats `float` for money**: `0.1 + 0.2` is not `0.3` in binary
  floating point, so cents drift. `Decimal("0.1")` is exact, and
  `quantize(Decimal("0.01"))` rounds to whole cents deliberately
- **`ROUND_HALF_UP`** to match how people expect currency to round
- **Returning a `NamedTuple`** (`BillBreakdown`) so callers read
  `result.per_person` instead of guessing tuple positions
- Keeping validation in the core function so both the CLI and tests share it

## How it works

```
text → Decimal(...) → validate → split_bill() (tip, total, per-person) → format :.2f → print
```

`split_bill` does all the arithmetic and rounding; `main` only parses input and
formats the output.

## A note on precision

Each amount is rounded to cents independently, so on uneven splits
`per_person * people` can differ from `total` by a cent (e.g. 99.71 / 3). This
is expected; a future version could assign the leftover cent to one person.

## Setup

```powershell
cd projects\project-04-tip-bill-splitter
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

```powershell
python -m src.main --subtotal 100 --tip 15 --people 4
```

Example output:

```
Subtotal   : 100.00
Tip        : 15.00 (15%)
Total      : 115.00
Per person : 28.75  (split 4 ways)
```

## Tests

```powershell
python -m pytest
```

Tests cover a known split, zero tip, half-up cent rounding, decimal exactness,
and the three validation rules.

## Project structure

```text
project-04-tip-bill-splitter/
├── README.md
├── requirements.txt
├── src/
│   ├── bill.py     # Decimal money math + validation
│   └── main.py     # CLI
└── tests/
    └── test_bill.py
```

## Roadmap

- [x] Tip/total/per-person with Decimal and validation
- [x] CLI flags
- [ ] Distribute the leftover rounding cent fairly

## License

MIT — see the [repository license](../../LICENSE).
