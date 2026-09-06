"""Tests for the Mad Libs story engine.

Run from the project folder with:  python -m pytest
"""

import sys
from datetime import datetime
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.story import fill_story, find_fields, list_templates, save_story


# --- find_fields ----------------------------------------------------------

def test_repeated_field_listed_once_in_order():
    template = "Hi {name}, the {name} likes {food} and {drink}."
    assert find_fields(template) == ["name", "food", "drink"]


def test_empty_template_has_no_fields():
    assert find_fields("") == []
    assert find_fields("Just plain text.") == []


def test_escaped_braces_are_not_fields():
    # {{ and }} are literal braces, not placeholders.
    assert find_fields("Use {{curly}} braces around {word}.") == ["word"]


# --- fill_story -----------------------------------------------------------

def test_fill_uses_same_value_for_repeated_field():
    template = "{name} and {name} again."
    assert fill_story(template, {"name": "Ada"}) == "Ada and Ada again."


def test_fill_empty_template_returns_empty():
    assert fill_story("", {}) == ""


def test_fill_missing_value_raises_with_names():
    with pytest.raises(ValueError) as info:
        fill_story("{animal} likes {food}", {"animal": "cat"})
    assert "food" in str(info.value)


def test_fill_renders_escaped_braces_literally():
    assert fill_story("{{literal}} {word}", {"word": "hi"}) == "{literal} hi"


def test_extra_answers_are_ignored():
    assert fill_story("Hello {name}", {"name": "Ada", "extra": "x"}) == "Hello Ada"


# --- save_story -----------------------------------------------------------

def test_save_story_writes_timestamped_file(tmp_path):
    now = datetime(2026, 1, 2, 3, 4, 5)
    path = save_story("A story.", tmp_path, now=now)
    assert path.name == "story-20260102-030405.txt"
    assert path.read_text(encoding="utf-8") == "A story."


# --- shipped templates are valid ------------------------------------------

def test_shipped_templates_parse_and_fill():
    templates_dir = Path(__file__).resolve().parents[1] / "templates"
    files = list_templates(templates_dir)
    assert files, "expected at least one template"
    for path in files:
        text = path.read_text(encoding="utf-8")
        answers = {field: "X" for field in find_fields(text)}
        # Should fill without raising.
        assert fill_story(text, answers)
