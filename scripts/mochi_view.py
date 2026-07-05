#!/usr/bin/env python3
"""Regenerate data/view/<deck>.md from data/working.json.

Use this AFTER editing working.json — never run mochi_unpack.py after edits,
that re-derives working.json from data/export.mochi and wipes your changes.

Reads:
    data/working.json

Writes:
    data/view/<deck>.md   — regenerated wholesale
"""

import json
from pathlib import Path

from mochi_unpack import render_deck, safe_filename

REPO = Path(__file__).resolve().parent.parent
WORKING = REPO / "data" / "working.json"
VIEW_DIR = REPO / "data" / "view"


def main() -> None:
    if not WORKING.exists():
        raise SystemExit(f"missing: {WORKING}")

    data = json.loads(WORKING.read_text(encoding="utf-8"))

    VIEW_DIR.mkdir(parents=True, exist_ok=True)
    for stale in VIEW_DIR.glob("*.md"):
        stale.unlink()

    decks = data.get("~:decks", [])
    total_cards = 0
    for deck in decks:
        out = VIEW_DIR / f"{safe_filename(deck.get('~:name', ''))}.md"
        out.write_text(render_deck(deck), encoding="utf-8")
        total_cards += len(deck.get("~:cards", {}).get("~#list", []))
    print(f"wrote {len(decks)} decks, {total_cards} cards to {VIEW_DIR.relative_to(REPO)}/")


if __name__ == "__main__":
    main()
