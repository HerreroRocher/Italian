#!/usr/bin/env python3
"""Unpack/repack/edit Mochi .mochi files.

A .mochi file is a zip containing a single data.json (Transit-encoded).

Usage:
    mochi_pack.py unpack <in.mochi> <out.json>
    mochi_pack.py pack   <in.json>  <out.mochi>
    mochi_pack.py edit-card <in.mochi> <out.mochi> --name <card-name>
                             [--content <new-content>] [--reset-reviews]
"""

import argparse
import json
import sys
import zipfile
from pathlib import Path


def _load(mochi_path: Path) -> dict:
    with zipfile.ZipFile(mochi_path) as z:
        return json.loads(z.read("data.json"))


def _save(data: dict, mochi_path: Path) -> None:
    payload = json.dumps(data, ensure_ascii=False)
    with zipfile.ZipFile(mochi_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("data.json", payload)


def _iter_cards(data: dict):
    for deck in data["~:decks"]:
        for card in deck["~:cards"]["~#list"]:
            yield deck, card


def unpack(args: argparse.Namespace) -> None:
    data = _load(args.src)
    args.dst.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"unpacked {args.src} -> {args.dst}")


def pack(args: argparse.Namespace) -> None:
    data = json.loads(args.src.read_text())
    _save(data, args.dst)
    print(f"packed {args.src} -> {args.dst}")


def edit_card(args: argparse.Namespace) -> None:
    if args.content is None and not args.reset_reviews:
        sys.exit("edit-card: nothing to do (pass --content and/or --reset-reviews)")

    data = _load(args.src)
    matches = [(d, c) for d, c in _iter_cards(data) if c["~:name"] == args.name]
    if not matches:
        sys.exit(f"edit-card: no card named {args.name!r}")
    if len(matches) > 1:
        decks = ", ".join(d["~:name"] for d, _ in matches)
        sys.exit(f"edit-card: {len(matches)} cards named {args.name!r} (in {decks}); narrow scope not yet supported")

    deck, card = matches[0]
    changes = []
    if args.content is not None:
        before = card["~:content"]
        card["~:content"] = args.content
        changes.append(f"content: {before!r} -> {args.content!r}")
    if args.reset_reviews:
        n = len(card.get("~:reviews", []))
        card["~:reviews"] = []
        changes.append(f"reviews cleared ({n} dropped)")

    _save(data, args.dst)
    print(f"edited '{args.name}' in deck '{deck['~:name']}':")
    for c in changes:
        print(f"  - {c}")
    print(f"wrote {args.dst}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    u = sub.add_parser("unpack")
    u.add_argument("src", type=Path)
    u.add_argument("dst", type=Path)
    u.set_defaults(func=unpack)

    k = sub.add_parser("pack")
    k.add_argument("src", type=Path)
    k.add_argument("dst", type=Path)
    k.set_defaults(func=pack)

    e = sub.add_parser("edit-card")
    e.add_argument("src", type=Path)
    e.add_argument("dst", type=Path)
    e.add_argument("--name", required=True)
    e.add_argument("--content")
    e.add_argument("--reset-reviews", action="store_true")
    e.set_defaults(func=edit_card)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
