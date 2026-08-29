"""Money math for the Tip and Bill Splitter (Project 4).

Money is handled with :class:`decimal.Decimal`, not ``float``. Floats cannot
represent values like ``0.10`` exactly, which causes cent-level errors when
they accumulate. ``Decimal`` gives exact base-10 arithmetic, and we round to
cents explicitly with ``quantize``.
"""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from typing import NamedTuple

CENTS = Decimal("0.01")


class BillBreakdown(NamedTuple):
    tip_amount: Decimal
    total: Decimal
    per_person: Decimal


def _money(value) -> Decimal:
    """Coerce a number/string to Decimal, rounded to whole cents."""
    return Decimal(str(value)).quantize(CENTS, rounding=ROUND_HALF_UP)


def split_bill(subtotal, tip_percent, people: int) -> BillBreakdown:
    """Return the tip, grand total, and per-person amount.

    ``subtotal`` and ``tip_percent`` may be numbers or strings; ``people`` must
    be a whole number of at least 1. Raises ``ValueError`` on invalid input.

    >>> split_bill("100", "15", 4)
    BillBreakdown(tip_amount=Decimal('15.00'), total=Decimal('115.00'), per_person=Decimal('28.75'))
    """
    subtotal = Decimal(str(subtotal))
    tip_percent = Decimal(str(tip_percent))

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percent cannot be negative.")
    if people < 1:
        raise ValueError("There must be at least one person.")

    tip_amount = _money(subtotal * tip_percent / Decimal("100"))
    total = _money(subtotal + tip_amount)
    per_person = _money(total / Decimal(people))
    return BillBreakdown(tip_amount=tip_amount, total=total, per_person=per_person)
