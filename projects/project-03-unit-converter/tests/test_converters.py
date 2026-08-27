"""Tests for the Unit Converter.

Run from the project folder with:  python -m pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.converters import (
    c_to_f,
    f_to_c,
    kg_to_lb,
    km_to_miles,
    lb_to_kg,
    miles_to_km,
)
from src.main import CONVERSIONS, convert, format_value


# --- Known reference points -----------------------------------------------

@pytest.mark.parametrize(
    "func, value, expected",
    [
        (c_to_f, 0, 32),        # freezing point
        (c_to_f, 100, 212),     # boiling point
        (c_to_f, -40, -40),     # the point where the scales meet
        (f_to_c, 32, 0),
        (f_to_c, 212, 100),
        (f_to_c, -40, -40),
    ],
)
def test_temperature_reference_points(func, value, expected):
    assert func(value) == pytest.approx(expected)


def test_negative_and_zero_temperatures():
    assert c_to_f(-17.78) == pytest.approx(-0.004, abs=1e-3)
    assert f_to_c(0) == pytest.approx(-17.7778, abs=1e-4)


# --- Round trips (convert there and back) ---------------------------------

@pytest.mark.parametrize(
    "there, back, value",
    [
        (km_to_miles, miles_to_km, 42.195),
        (miles_to_km, km_to_miles, 26.2),
        (kg_to_lb, lb_to_kg, 75),
        (lb_to_kg, kg_to_lb, 165),
    ],
)
def test_round_trip_returns_original(there, back, value):
    assert back(there(value)) == pytest.approx(value)


def test_length_and_weight_known_points():
    assert km_to_miles(1.609344) == pytest.approx(1.0)
    assert kg_to_lb(1) == pytest.approx(2.20462, abs=1e-5)


# --- Dispatch table + formatting ------------------------------------------

def test_convert_uses_lookup_table():
    assert convert("c2f", 100) == pytest.approx(212)


def test_convert_unknown_key_raises():
    with pytest.raises(ValueError):
        convert("miles2lightyears", 1)


def test_all_menu_keys_are_callable():
    for key, conv in CONVERSIONS.items():
        assert conv.func(1) is not None, key


@pytest.mark.parametrize("value, text", [(212.0, "212.00"), (1.005, "1.00"), (0, "0.00")])
def test_format_value_two_decimals(value, text):
    assert format_value(value) == text
