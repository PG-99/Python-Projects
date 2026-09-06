"""Mad Libs story engine (Project 7).

A template is just text with named placeholders like ``{animal}``. The engine
discovers which fields a template needs, fills them from one dictionary (so a
repeated field is always filled with the same word), and can save the result
with a timestamped filename.

Keeping templates as data means new stories are new files, not new code.
"""

from __future__ import annotations

import string
from datetime import datetime
from pathlib import Path


def find_fields(template: str) -> list[str]:
    """Return the unique placeholder names, in order of first appearance.

    Uses ``string.Formatter().parse`` so escaped braces (``{{`` / ``}}``) and
    positional ``{}`` fields are ignored.

    >>> find_fields("Hi {name}, the {name} likes {food}.")
    ['name', 'food']
    """
    fields: list[str] = []
    for _literal, field_name, _spec, _conv in string.Formatter().parse(template):
        # field_name is None for literal text / escaped braces, '' for {}.
        if field_name:
            base = field_name.split(".")[0].split("[")[0]
            if base not in fields:
                fields.append(base)
    return fields


def fill_story(template: str, answers: dict[str, str]) -> str:
    """Fill ``template`` with ``answers``.

    Raises ``ValueError`` listing any placeholders that have no answer.
    """
    missing = [name for name in find_fields(template) if name not in answers]
    if missing:
        raise ValueError(f"Missing values for: {', '.join(missing)}")
    return template.format(**answers)


def save_story(text: str, output_dir: str | Path, now: datetime | None = None) -> Path:
    """Write ``text`` to a timestamped file and return its path.

    ``now`` can be supplied to make the filename deterministic in tests.
    """
    now = now or datetime.now()
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"story-{now:%Y%m%d-%H%M%S}.txt"
    path.write_text(text, encoding="utf-8")
    return path


def load_template(path: str | Path) -> str:
    """Read a template file as text."""
    return Path(path).read_text(encoding="utf-8")


def list_templates(templates_dir: str | Path) -> list[Path]:
    """Return the ``.txt`` templates in a directory, sorted by name."""
    return sorted(Path(templates_dir).glob("*.txt"))
