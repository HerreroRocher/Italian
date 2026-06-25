#!/usr/bin/env python3
"""Swap the heading and the content below `---` in every flashcard markdown file."""

import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
SRC = BASE / "markdown-export"
DST = BASE / "markdown-processed"


def reverse_card(text: str) -> tuple[str, str]:
    """Return (new_text, new_title) for a flashcard."""
    lines = text.splitlines()
    try:
        sep = lines.index("---")
    except ValueError:
        raise ValueError("no '---' separator found")

    front = lines[:sep]
    back = lines[sep + 1:]

    if not front or not front[0].startswith("## "):
        raise ValueError("first line is not a '## ' heading")

    front_text = front[0][3:]
    front_extra = front[1:]

    back_stripped = [l for l in back if l.strip()]
    if not back_stripped:
        raise ValueError("no content below separator")

    new_title = back_stripped[0]
    new_heading = "## " + new_title
    new_back_extra = back_stripped[1:] + front_extra

    new_lines = [new_heading, "---", front_text, *new_back_extra]
    result = "\n".join(new_lines)
    if text.endswith("\n"):
        result += "\n"
    return result, new_title


def main() -> int:
    if not SRC.is_dir():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 1

    changed = 0
    skipped = 0
    for path in sorted(SRC.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        try:
            new, new_title = reverse_card(original)
        except ValueError as e:
            print(f"skip {path}: {e}", file=sys.stderr)
            skipped += 1
            continue

        # Filenames look like "<id> - <title>.md"; keep the id, swap the title.
        rel = path.relative_to(SRC)
        m = re.match(r"^(.*? - )(.*)\.md$", rel.name)
        safe_title = re.sub(r"[\\/:*?\"<>|]", "_", new_title).strip()
        new_name = f"{m.group(1)}{safe_title}.md" if m else f"{safe_title}.md"
        out_path = DST / rel.parent / new_name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(new, encoding="utf-8")
        changed += 1

    print(f"reversed {changed} files, skipped {skipped}")

    # Build one combined deck file per subdirectory at the root of DST.
    decks = 0
    for deck_dir in sorted(p for p in DST.iterdir() if p.is_dir()):
        # Deck name is everything after "<id> - " in the directory name.
        m = re.match(r"^.*? - (.*)$", deck_dir.name)
        deck_name = m.group(1) if m else deck_dir.name
        safe_deck = re.sub(r"[\\/:*?\"<>|]", "_", deck_name).strip()

        cards = []
        for card_path in sorted(deck_dir.glob("*.md")):
            cards.append(card_path.read_text(encoding="utf-8").rstrip("\n"))

        if not cards:
            continue

        deck_path = DST / f"{safe_deck}.md"
        deck_path.write_text("\n%\n".join(cards) + "\n", encoding="utf-8")
        decks += 1

    print(f"wrote {decks} deck files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
