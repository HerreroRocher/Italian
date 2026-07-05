"""Reusable primitives for editing Mochi card decks via mochi_pack.py round-trips.

Usage pattern:
    from mochi_edit import load, save, add_to, add_deck

    d = load('data/working.json')            # output of: scripts/mochi_unpack.py
    add_to(d, 'Verbs', [('hablar', 'parlare'), ...])
    add_deck(d, 'New Deck')
    save(d, 'data/working.json')             # then: scripts/mochi_pack.py pack ...

Gotchas (verified 2026-06-26):
  - Mochi caches by import filename. Re-importing the same `.mochi` name after
    a failed import keeps showing the OLD schema error. Always bump the suffix.
  - Deck `~:sort` is an INTEGER (deck-list position), NOT the keyword `~:created-at`.
    Card sort lives elsewhere; do not confuse them.
  - Deck `~:show-sides?` must be `True` to match existing decks; defaulting to False
    works but renders inconsistently.
  - For meaning-changing card edits, reset `~:reviews` to []. Pure formatting/casing
    fixes leave reviews intact.
"""
import json, secrets, string, time


def load(path):
    return json.load(open(path))


def save(d, path):
    json.dump(d, open(path, 'w'), indent=2, ensure_ascii=False)


def _new_id():
    alphabet = string.ascii_letters + string.digits
    return '~:' + ''.join(secrets.choice(alphabet) for _ in range(8))


def _decks_by_name(d):
    return {dk['~:name']: dk for dk in d['~:decks']}


def _fmt(spanish, italian, example=None):
    body = f'\n## {spanish}\n---\n{italian}\n'
    if example:
        body += f'*{example}*\n'
    return body


def make_card(deck_id, name, content):
    return {
        '~:cloze/indexes': {'~#set': []},
        '~:content': content,
        '~:created-at': {'~#dt': int(time.time() * 1000)},
        '~:deck-id': deck_id,
        '~:id': _new_id(),
        '~:name': name,
        '~:pos': secrets.choice(string.ascii_letters),
        '~:references': {'~#set': []},
        '~:reviews': [],
        '~:tags': {'~#set': []},
    }


def add_to(d, deck_name, entries):
    """Append cards to the named deck.

    Each entry is either (spanish, italian) or (spanish, italian, example).
    The example line is rendered as an italicized one-liner per rules.md.
    """
    deck = _decks_by_name(d)[deck_name]
    for e in entries:
        sp, it, ex = (e[0], e[1], e[2] if len(e) > 2 else None)
        deck['~:cards']['~#list'].append(
            make_card(deck['~:id'], sp, _fmt(sp, it, ex))
        )


def add_deck(d, name):
    """Append a new deck. Returns its id."""
    sort_idx = len(d['~:decks'])
    deck = {
        '~:name': name,
        '~:id': _new_id(),
        '~:show-sides?': True,
        '~:cards-view': '~:list',
        '~:sort': sort_idx,
        '~:cards': {'~#list': []},
    }
    d['~:decks'].append(deck)
    return deck['~:id']


def append_to_content(d, deck_name, card_name, suffix):
    """Append text to a card's content. Pure formatting — does not reset reviews.
    Match is by exact card name within the deck."""
    deck = _decks_by_name(d)[deck_name]
    for c in deck['~:cards']['~#list']:
        if c['~:name'] == card_name:
            c['~:content'] = c['~:content'].rstrip() + '\n' + suffix + '\n'
            return True
    return False


def remove(d, deck_name, predicate):
    deck = _decks_by_name(d)[deck_name]
    before = len(deck['~:cards']['~#list'])
    deck['~:cards']['~#list'] = [c for c in deck['~:cards']['~#list'] if not predicate(c)]
    return before - len(deck['~:cards']['~#list'])


def move(d, from_deck, to_deck, predicate):
    by_name = _decks_by_name(d)
    src = by_name[from_deck]['~:cards']['~#list']
    moving = [c for c in src if predicate(c)]
    by_name[from_deck]['~:cards']['~#list'] = [c for c in src if not predicate(c)]
    target_id = by_name[to_deck]['~:id']
    for c in moving:
        c['~:deck-id'] = target_id
        by_name[to_deck]['~:cards']['~#list'].append(c)
    return len(moving)


def inventory(d):
    """Print deck/card summary."""
    total = 0
    for dk in d['~:decks']:
        n = len(dk['~:cards']['~#list'])
        total += n
        print(f"  [{n:3d}] {dk['~:name']}")
    print(f"  TOTAL: {total}")
