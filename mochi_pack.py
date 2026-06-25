#!/usr/bin/env python3
"""Unpack/repack Mochi .mochi files for programmatic editing.

A .mochi file is a zip containing a single data.json (Transit-encoded).

Usage:
    python mochi_pack.py unpack <input.mochi> <output.json>
    python mochi_pack.py pack   <input.json>  <output.mochi>
    python mochi_pack.py test-edit <input.mochi> <output.mochi>
        # Appends " ." to the first card's content; for round-trip testing.
"""

import json
import sys
import zipfile
from pathlib import Path


def unpack(mochi_path: Path, json_path: Path) -> None:
    with zipfile.ZipFile(mochi_path) as z:
        names = z.namelist()
        if "data.json" not in names:
            raise SystemExit(f"expected data.json in {mochi_path}, got {names}")
        with z.open("data.json") as f:
            data = json.load(f)
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"unpacked {mochi_path} -> {json_path}")


def pack(json_path: Path, mochi_path: Path) -> None:
    data = json.loads(json_path.read_text())
    payload = json.dumps(data, ensure_ascii=False)
    with zipfile.ZipFile(mochi_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("data.json", payload)
    print(f"packed {json_path} -> {mochi_path}")


def test_edit(in_mochi: Path, out_mochi: Path) -> None:
    """Round-trip test: tweak one card's content, leave reviews untouched."""
    with zipfile.ZipFile(in_mochi) as z:
        data = json.loads(z.read("data.json"))

    decks = data["~:decks"]
    first_card = decks[0]["~:cards"]["~#list"][0]
    original = first_card["~:content"]
    first_card["~:content"] = original.rstrip() + " .\n"

    payload = json.dumps(data, ensure_ascii=False)
    with zipfile.ZipFile(out_mochi, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("data.json", payload)

    deck_name = decks[0]["~:name"]
    card_name = first_card["~:name"]
    n_reviews = len(first_card.get("~:reviews", []))
    print(f"edited card '{card_name}' in deck '{deck_name}' ({n_reviews} reviews preserved)")
    print(f"  before: {original!r}")
    print(f"  after:  {first_card['~:content']!r}")
    print(f"wrote {out_mochi}")


def main() -> None:
    args = sys.argv[1:]
    if len(args) != 3 or args[0] not in {"unpack", "pack", "test-edit"}:
        print(__doc__, file=sys.stderr)
        raise SystemExit(2)
    cmd, src, dst = args
    src_p, dst_p = Path(src), Path(dst)
    if cmd == "unpack":
        unpack(src_p, dst_p)
    elif cmd == "pack":
        pack(src_p, dst_p)
    else:
        test_edit(src_p, dst_p)


if __name__ == "__main__":
    main()
