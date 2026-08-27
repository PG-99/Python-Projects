"""Pure conversion functions for the Unit Converter (Project 3).

Each function takes one number and returns the converted number. They contain
no input/output, so they are trivial to test against known reference points
(for example, 0 C = 32 F).
"""

from __future__ import annotations

# Conversion factors kept as named constants so the intent is obvious.
_KM_PER_MILE = 1.609344
_LB_PER_KG = 2.2046226218487757


# --- Temperature ----------------------------------------------------------

def c_to_f(celsius: float) -> float:
    """Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


# --- Length ---------------------------------------------------------------

def km_to_miles(km: float) -> float:
    """Kilometres to miles."""
    return km / _KM_PER_MILE


def miles_to_km(miles: float) -> float:
    """Miles to kilometres."""
    return miles * _KM_PER_MILE


# --- Weight ---------------------------------------------------------------

def kg_to_lb(kg: float) -> float:
    """Kilograms to pounds."""
    return kg * _LB_PER_KG


def lb_to_kg(lb: float) -> float:
    """Pounds to kilograms."""
    return lb / _LB_PER_KG
