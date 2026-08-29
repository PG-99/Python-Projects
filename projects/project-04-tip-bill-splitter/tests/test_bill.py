"""Tests for the Tip and Bill Splitter.

Run from the project folder with:  python -m pytest
"""

import sys
from decimal import Decimal
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.bill import split_bill


# --- Known calculations ---------------------------------------------------

def test_simple_split():
    result = split_bill("100", "15", 4)
    assert result.tip_amount == Decimal("15.00")
    assert result.total == Decimal("115.00")
    assert result.per_person == Decimal("28.75")


def test_zero_tip():
    result = split_bill("50", "0", 2)
    assert result.tip_amount == Decimal("0.00")
    assert result.total == Decimal("50.00")
    assert result.per_person == Decimal("25.00")


def test_rounds_to_cents_half_up():
    # 84.50 * 18% = 15.21 exactly; total 99.71
    result = split_bill("84.50", "18", 3)
    assert result.tip_amount == Decimal("15.21")
    assert result.total == Decimal("99.71")
    # 99.71 / 3 = 33.2366... -> 33.24
    assert result.per_person == Decimal("33.24")


def test_uses_decimal_not_float():
    # 0.1 + 0.2 style errors must not appear.
    result = split_bill("0.10", "0", 1)
    assert result.total == Decimal("0.10")


# --- Validation -----------------------------------------------------------

def test_negative_subtotal_rejected():
    with pytest.raises(ValueError):
        split_bill("-1", "10", 2)


def test_negative_tip_rejected():
    with pytest.raises(ValueError):
        split_bill("10", "-5", 2)


def test_fewer_than_one_person_rejected():
    with pytest.raises(ValueError):
        split_bill("10", "10", 0)
