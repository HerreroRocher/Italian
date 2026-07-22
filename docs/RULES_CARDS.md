# RULES_CARDS.md — Behavioral contract for the Mochi flashcard pipeline

Card-authoring criteria and the free-tier edit/repack workflow. Only needed when actually touching the deck — not for a lesson/quiz session; see `RULES_LEARNING.md` for that (and for the general "ask, don't hedge with tangential commands" rule, which applies here too).

## Mochi flashcard authoring

**Card selection criteria — what qualifies as a card (default; do not re-ask):**
- **Frequency first.** Only add words/constructions used a lot in everyday spoken Italian. Skip rare, formal, literary, or bureaucratic register unless Daniel is explicitly drilling that register.
- **Non-triviality over transparency.** A card is only worth adding if the Italian form or construction is *not* reliably derivable from Spanish alone — either via regular cognate correspondence (*importar→importare*, *doler→dolere*, *dar→dare*) or by mechanically applying a pattern Daniel already has from an existing card (*ponerse a + inf→mettersi a + inf* is dead weight once *poner→mettere* is known). Frequency does not overrule this — a frequent word that's a plain cognate isn't worth a card. Prioritize: false friends, non-cognate lexemes for common concepts, and constructions where Spanish and Italian diverge (different governing preposition, dropped/added reflexive, different periphrasis). Test: would Daniel already produce the right Italian form if he had to guess, without ever having seen the card? If yes, skip it.
- **One card per concept: the single most common word wins.** When several Italian synonyms exist for a Spanish concept, add the most-frequently-used one as the card. Only add a second synonym on the same card (`sinonimo1 / sinonimo2`) if it is *independently* high-frequency, not just a passable alternative — don't pad cards with rare synonyms.
- **Broad fit over narrow fit.** Prefer generative vocabulary that recombines across many situations (adverbs, connectives, common verbs, functional expressions) over words that only work in one narrow context.
- **No closed idioms/sayings/proverbs.** Fixed expressions with a single frozen meaning and no productive reuse (*in bocca al lupo*, *chi va piano va sano e va lontano*, etc.) do not belong in the deck — they were deliberately purged. This is a durable rule, not a one-off cleanup.
- **Functional multi-word constructions still qualify** — these are not "sayings" in the excluded sense because they're productive/glue-like and recur constantly (*stare per* + inf, *avere voglia di* + inf, *avere bisogno di* + noun/inf, *non vedere l'ora di* + inf). The `Set Phrases & Idioms` deck is for these, not for proverbs.
- **Verbs**: prefer the single most common Italian verb per Spanish synonym cluster (e.g. Sp *ganar* → IT splits into *vincere*/*guadagnare*; pick both only because Italian genuinely forces the split, not because both are equally common translations of one sense).

**Audit checklist when reviewing existing cards:**
- Duplicates (within and across decks)
- Wrong Spanish glosses
- Missing interference-trap flags
- Formatting consistency

**Mood markers.** On any card whose Italian construction triggers a specific mood, annotate the Italian side:
- `(ind.)` when Italian takes the **indicative** but the Spanish equivalent would take subjunctive (e.g. *anche se* takes indicative; Spanish *aunque* often takes subjunctive).
- `(cong.)` when Italian takes the **subjunctive** but the Spanish equivalent would take indicative, OR where the subjunctive trigger is non-obvious (*magari fosse vero*, *nonostante sia*, *qualunque cosa tu faccia*).
- **No marker** when both languages behave the same way (no leverage from the annotation).

**Example sentences.** Every non-verb card must include a short Italian example sentence demonstrating natural use:
- Format: italicized one-liner (`*...*`) on a new line after the Italian translation.
- Keep ≤8 words where possible; everyday spoken register.
- **Verbs are exempt** unless the Italian syntax diverges from Spanish — in which case include an example that demonstrates the divergence. Triggers to include a verb example: no preposition where Spanish uses one (*aspettare*, *chiamare* — no a-personal); inverted construction (*piacere*); split auxiliary (*finire*); auxiliary doubling as possession (*avere*); false friend (*tenere* ≠ Spanish *tener*); Italian collapsing two Spanish verbs (*portare* = *llevar*/*traer*).

## Mochi edit workflow (free tier)

The free-tier roundtrip is **wipe-and-reimport**, verified 2026-06-25:

1. Export current state as `.mochi` (with review history) from Mochi iOS. Via SMB (share config lives in the separate [samba](../samba) repo), it lands as `data/export.mochi` on host. Snapshot to `data/backups/YYYY-MM-DD.mochi` for safety.
2. `scripts/mochi_unpack.py` derives `data/working.json` (authoritative, mutable) + `data/view/<deck>.md` (regenerated each unpack, never edited directly).
3. Apply edits to `data/working.json` **exclusively** via the `scripts/mochi_edit.py` primitives — never with an ad-hoc inline script that hand-rolls the JSON. Every operation below is already covered; if one is missing, add it to `mochi_edit.py` rather than working around it. Card IDs (the backtick-quoted token at the start of each `data/view/<deck>.md` line, e.g. `F80lGcGS`) can be passed to every function below bare or `~:`-prefixed — both resolve.

   | Task | Call |
   |---|---|
   | Load / save | `load(path)` / `save(d, path)` |
   | Add card(s) to a deck | `add_to(d, deck, [(spanish, italian), (spanish, italian, example), ...])` |
   | Add a new deck | `add_deck(d, name)` |
   | Look up one card | `find_card(d, deck, card_id)` → raw dict or `None` |
   | Edit an existing card | `edit_card(d, deck, card_id, spanish=..., italian=..., example=..., reset_reviews=...)` — pass only the field(s) changing; unset ones keep their current value |
   | Move card(s) between decks | `move(d, from_deck, to_deck, predicate)` |
   | Remove card(s) | `remove(d, deck, predicate)` |
   | Append text to a card (formatting only) | `append_to_content(d, deck, card_name, suffix)` |
   | Split or merge cards | no dedicated helper — compose `remove()` + `add_to()`; treat it as a meaning change (fresh cards get empty `~:reviews` automatically) |

   `add_to` accepts either `(spanish, italian)` or `(spanish, italian, example)` tuples — pass an example for any non-verb card and for verbs whose IT syntax diverges from Sp.

   **`~:name` vs `~:content` — do not edit content directly.** A card's displayed headword (in `data/view/*.md` and in Mochi's own card list) comes from `~:name`, a field that is stored independently of `~:content` and is never re-derived from it. Editing `~:content` by hand (e.g. via `append_to_content` for anything beyond a pure suffix, or raw dict mutation) without also updating `~:name` leaves the view showing stale text even though the underlying answer changed. `edit_card()` updates both together — use it for any rename/regloss instead of touching `~:content` directly. `scripts/mochi_pack.py edit-card` (CLI, operates on a packed `.mochi` directly) is the alternative for a single targeted edit outside this JSON workflow, but for anything touching `working.json` prefer the primitives above.
4. To refresh the human-scannable views after step 3, run `scripts/mochi_view.py` — NOT `mochi_unpack.py`. Unpack re-derives `working.json` from `data/export.mochi` and will wipe your in-flight edits.
5. `scripts/mochi_pack.py pack data/working.json data/import.mochi` to produce the import artifact.
6. In Mochi iOS: delete all decks, empty trash.
7. Import `data/import.mochi`. Card content updates **and** the embedded `reviews[]` array restores SRS state (interval, due date, remembered-history) verbatim.

**Review-reset rule:** when fixing a card's *meaning* (not just formatting), always reset its `~:reviews` to `[]`. Past "remembered? = true" entries were against the wrong content — keeping them would lock in the error. Pure formatting/whitespace/example-add edits leave reviews alone.

**Safety rule:** never delete in-app before confirming `data/import.mochi` exists on disk and the prior snapshot is committed to `data/backups/`. The wipe step is irreversible.

**Filename rule:** Mochi caches by import filename — if an import fails, bump the suffix (`-v2.mochi`, `-v3.mochi`) before retrying, otherwise the old failure resurfaces. Confirmed 2026-07-14: an in-app "can't find end of central directory" error on a `data/import.mochi` that verified as a perfectly valid zip locally (`zipfile.testzip()`, `unzip -t`) was fixed purely by re-importing the identical bytes under a bumped filename. Root cause is either the filename cache above or a torn SMB read (phone had the file open/mid-copy when it got overwritten in place) — either way, **always repack to a fresh incrementally-suffixed filename after any edit-and-repack cycle** rather than overwriting `data/import.mochi` in place, instead of assuming the file itself is bad and re-diagnosing from scratch.

**Do not make ad-hoc backup copies of `data/working.json` before editing it.** Git already tracks it (per `MAINTENANCE_TASKS.md` history strategy) — `git diff` / `git checkout` is the recovery path, not a scratchpad copy. Copying it elsewhere first is wasted motion, not a safety step. When asked to make flashcard edits, edit `working.json` directly via the `mochi_edit.py`/`mochi_pack.py` helpers, then run `mochi_view.py` — don't pause to snapshot state that's already versioned.
