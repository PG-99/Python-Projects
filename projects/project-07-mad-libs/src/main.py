"""Command-line interface for the Mad Libs generator (Project 7).

Pick a template, answer one prompt per placeholder, then see and save the
finished story.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from src.story import (
    fill_story,
    find_fields,
    list_templates,
    load_template,
    save_story,
)

# Folders relative to the project root (this file lives in src/).
PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = PROJECT_ROOT / "templates"
OUTPUT_DIR = PROJECT_ROOT / "output"


def _choose_template(argv_name: str | None) -> Path:
    templates = list_templates(TEMPLATES_DIR)
    if not templates:
        raise SystemExit(f"No templates found in {TEMPLATES_DIR}")

    if argv_name:
        match = next((t for t in templates if t.stem == argv_name), None)
        if match is None:
            raise SystemExit(f"Unknown template: {argv_name}")
        return match

    print("Available stories:")
    for index, template in enumerate(templates, start=1):
        print(f"  {index}. {template.stem}")
    choice = input("Choose a number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(templates)):
        raise SystemExit("That was not a valid choice.")
    return templates[int(choice) - 1]


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate a Mad Libs story.")
    parser.add_argument("--template", help="Template name (without .txt)")
    parser.add_argument("--list", action="store_true", help="List templates and exit")
    args = parser.parse_args(argv)

    if args.list:
        for template in list_templates(TEMPLATES_DIR):
            print(template.stem)
        return

    template_path = _choose_template(args.template)
    template = load_template(template_path)

    answers: dict[str, str] = {}
    for field in find_fields(template):
        answers[field] = input(f"Enter a {field.replace('_', ' ')}: ").strip()

    story = fill_story(template, answers)
    print("\n" + story + "\n")

    saved = save_story(story, OUTPUT_DIR)
    print(f"Saved to {saved}")


if __name__ == "__main__":
    main()
