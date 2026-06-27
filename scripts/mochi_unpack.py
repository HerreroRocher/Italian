#!/usr/bin/env python3
"""Unpack data/export.mochi into data/working.json and per-deck markdown views.

Reads:
    data/export.mochi    — latest phone export (overwritten on each landing)

Writes:
    data/working.json    — authoritative, mutable; all edit scripts target this
    data/view/<deck>.md  — derived, AI-cheap scan; regenerated wholesale every run

Usage:
    scripts/mochi_unpack.py
"""

import json
import re
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXPORT = REPO / "data" / "export.mochi"
WORKING = REPO / "data" / "working.json"
VIEW_DIR = REPO / "data" / "view"


def load_mochi(path: Path) -> dict:
    with zipfile.ZipFile(path) as z:
        return json.loads(z.read("data.json"))


def safe_filename(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip() or "_unnamed"


def extract_back(content: str) -> str:
    """Pull the half of card content after the `---` separator, single-line."""
    if not content:
        return ""
    parts = content.split("---", 1)
    tail = parts[1] if len(parts) == 2 else parts[0]
    return " / ".join(line.strip() for line in tail.strip().splitlines() if line.strip())


def render_deck(deck: dict) -> str:
    name = deck.get("~:name", "(unnamed deck)")
    cards = deck.get("~:cards", {}).get("~#list", [])
    lines = [f"# {name}", f"_{len(cards)} cards_", ""]
    if not cards:
        lines.append("_(empty)_")
        return "\n".join(lines) + "\n"
    for card in cards:
        cid = card.get("~:id", "?").lstrip("~:")
        front = card.get("~:name", "(unnamed)")
        back = extract_back(card.get("~:content", ""))
        reviews = len(card.get("~:reviews", []))
        lines.append(f"- `{cid}` **{front}** → {back}  ·  ({reviews}r)")
    return "\n".join(lines) + "\n"


def main() -> None:
    if not EXPORT.exists():
        raise SystemExit(f"missing: {EXPORT}")

    data = load_mochi(EXPORT)

    WORKING.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {WORKING.relative_to(REPO)}")

    # Wipe stale view files so renamed/deleted decks don't linger.
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
