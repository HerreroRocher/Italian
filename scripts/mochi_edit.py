"""Reusable primitives for editing Mochi card decks via mochi_pack.py round-trips.

This module is the ONLY sanctioned way to touch `data/working.json`. Do not
hand-roll JSON manipulation in a throwaway `python3 -c` script or a one-off
file — every operation you need (add, edit, move, remove, merge, split) is
already a function here. If you find yourself reaching for raw dict mutation,
add a primitive to this file instead so the next agent doesn't re-derive it.

Usage pattern:
    from mochi_edit import load, save, add_to, add_deck, edit_card

    d = load('data/working.json')            # output of: scripts/mochi_unpack.py
    add_to(d, 'Verbs', [('hablar', 'parlare'), ...])
    edit_card(d, 'Verbs', 'F80lGcGS', spanish='estar')   # id copy-pasted from data/view/*.md
    add_deck(d, 'New Deck')
    save(d, 'data/working.json')             # then: scripts/mochi_pack.py pack ...
    # then: scripts/mochi_view.py            # refresh data/view/*.md to match

Card-content model (read this before editing anything):
  - `~:name` is the card's headword/front, shown as-is in `data/view/<deck>.md`
    and in Mochi's own card list. `~:content` is the full card body
    (`## {spanish}\n---\n{italian}\n*{example}*`) shown during review.
  - **These two fields are independently stored and NOT derived from each other.**
    Editing `~:content` alone leaves `~:name` — and therefore the view file —
    showing stale text. `edit_card()` below keeps them in sync automatically;
    that is the main reason to use it instead of editing `~:content` by hand.
  - Card IDs appear two ways: bare in `data/view/<deck>.md` (e.g. `F80lGcGS`,
    the leading backtick-quoted token on each line) and prefixed in JSON
    (`~:F80lGcGS`). Every function here accepts either form.

Splitting/merging cards: no dedicated helper — compose `remove()` + `add_to()`.
Treat that as a meaning change and let `add_to()`'s fresh empty `~:reviews`
stand (per the review-reset rule below); don't try to carry old reviews over.

Gotchas (verified 2026-06-26):
  - Mochi caches by import filename. Re-importing the same `.mochi` name after
    a failed import keeps showing the OLD schema error. Always bump the suffix.
  - Deck `~:sort` is an INTEGER (deck-list position), NOT the keyword `~:created-at`.
    Card sort lives elsewhere; do not confuse them.
  - Deck `~:show-sides?` must be `True` to match existing decks; defaulting to False
    works but renders inconsistently.
  - For meaning-changing card edits, reset `~:reviews` to []. Pure formatting/casing
    fixes leave reviews intact. `edit_card(..., reset_reviews=True)` does this for you.
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


def _norm_id(card_id):
    return card_id if card_id.startswith('~:') else '~:' + card_id


def _fmt(spanish, italian, example=None):
    body = f'\n## {spanish}\n---\n{italian}\n'
    if example:
        body += f'*{example}*\n'
    return body


def _parse(content):
    """Inverse of _fmt: best-effort split of existing content back into
    (spanish, italian, example), used by edit_card() to preserve fields
    you don't pass. Falls back gracefully on hand-written/irregular content."""
    head, _, tail = content.partition('---')
    spanish = head.strip().lstrip('#').strip()
    lines = [ln for ln in tail.strip('\n').split('\n') if ln.strip()]
    example = None
    if lines and lines[-1].strip().startswith('*') and lines[-1].strip().endswith('*'):
        example = lines[-1].strip().strip('*')
        lines = lines[:-1]
    italian = '\n'.join(lines).strip()
    return spanish, italian, example


def find_card(d, deck_name, card_id):
    """Return the raw card dict, or None. card_id accepts either ID form."""
    cid = _norm_id(card_id)
    deck = _decks_by_name(d)[deck_name]
    for c in deck['~:cards']['~#list']:
        if c['~:id'] == cid:
            return c
    return None


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


def edit_card(d, deck_name, card_id, *, spanish=None, italian=None, example=None,
              reset_reviews=False):
    """Edit an existing card in place. Pass only the field(s) you want to
    change — spanish/italian/example default to the card's current value
    (parsed from ~:content), so a one-field fix doesn't require retyping
    the whole card. Keeps ~:name and ~:content in sync (see module docstring).

    Set reset_reviews=True whenever the *meaning* changed (wrong gloss fixed,
    headword disambiguated, translation corrected) per the review-reset rule
    in rules.md. Leave it False for pure formatting/typo/example-add edits.

    Returns True if found and edited, False if no matching card_id in deck_name.
    """
    c = find_card(d, deck_name, card_id)
    if c is None:
        return False
    cur_spanish, cur_italian, cur_example = _parse(c['~:content'])
    new_spanish = spanish if spanish is not None else cur_spanish
    new_italian = italian if italian is not None else cur_italian
    new_example = example if example is not None else cur_example
    c['~:name'] = new_spanish
    c['~:content'] = _fmt(new_spanish, new_italian, new_example)
    if reset_reviews:
        c['~:reviews'] = []
    return True


def rename_deck(d, old_name, new_name):
    """Rename a deck in place. Formatting-only, no reviews affected."""
    _decks_by_name(d)[old_name]['~:name'] = new_name


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
