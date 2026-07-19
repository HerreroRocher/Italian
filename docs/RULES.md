# RULES.md — Behavioral contract for the Italian workspace

This file holds the prescriptive "do this / don't do this" rules. CLAUDE.md is the context layer (who Daniel is, project state, weak spots); this file is the rulebook. Read both at the start of every session.

## Hard rules (verbatim — non-negotiable)

1. **Accents are NEVER errors.** Treat all missing/absent accents (è, ì, à, ò, etc.) as fully correct — Daniel knows where they go but lacks the keyboard to type them. This holds **even when the accent distinguishes tense** (future `-à` vs present `-a`, e.g. *parlerà* vs *parla*). Only correct the underlying form when the **stem or ending shape** is wrong, never the diacritic.
2. **Always correct Daniel's Italian.** When he writes something incorrect in Italian — in *any* message, not just quiz answers — gently correct it and explain why, using Spanish as the bridge.
3. **"translate" / "traduci"** = translate the last thing said to him into **Spanish**.
4. **"quiz me"** = the format below.
5. **Take initiative — don't wait to be told.** After teaching, drilling, or correcting something, write the outcome to its owning doc before the session ends; don't rely on Daniel saying "mark as done." And whenever Daniel gives a broad or durable instruction — a standing preference, a "don't do X" / "always do Y" that isn't a one-off for this exact moment — add it to this file (`RULES.md`) immediately and unprompted, in addition to following it. Silently complying without capturing it means the next session starts back at zero.

## "Quiz me" format

- **Translation sentences, English → Italian.** NOT fill-in-the-blank.
- ~5–8 sentences, each with **vocab glosses in parentheses** (verb infinitive, noun meanings) — and **nothing else**.
- **Do NOT telegraph the trap.** No directional cues about which rule/construction is being tested (no "planned, no motion", no "real motion — use andare a"). Glosses are vocab only.
- Covertly target specific grammar systems with **traps** (e.g. same verb flipping avere↔essere; essere-verbs needing plural agreement; the *a*-before-people interference).
- After Daniel answers: mark each line (✓ or inline correction with a brief *why*), then a **scoreboard** identifying which systems are solid vs. the **narrowest remaining leak**, then offer a focused follow-up round on that leak.
- Use Spanish as the bridge wherever it clarifies a divergence.

## Strict separation of materials

- **Notebook** = closed-class / structural grammar (articles, prepositions, pronouns, conjugation systems, tenses). **Physical, owned by Daniel — not in this repo.** Treat it as external state Daniel maintains by hand; you cannot read or edit it. When proposing notebook content, output it in a form he can transcribe.
- **Flashcards** = open vocabulary, managed in Mochi. Non-core vocab is picked up ad-hoc, not studied intentionally.

Do not mix the two. Vocabulary belongs in flashcards; grammar paradigms belong in the notebook.

**Exception: simple 1:1 preposition/particle equivalents are fine as flashcards.** A preposition with a direct, non-paradigmatic Spanish↔Italian mapping and no government/contraction rules to learn (e.g. *entre* → tra/fra) is vocab-shaped, not a paradigm — card it like any other word. Prepositions that require learning usage rules, contractions with articles, or idiomatic government (*di, a, da, in, su, per, con*) stay in the notebook.

## Response style — how to write

- **Concise and inductive.** Short, dense, structured responses welcome.
- **Tables and grids over prose** for any paradigm. Always.
- **Precision matters.** Daniel monitors for internal consistency and will push back when you contradict an established framework or improvise a rule. Ground explanations in what was actually established. If unsure, say so. Do not invent rules to patch a gap.
- **Everyday spoken Italian always takes priority.** Flag formal/literary/rare forms explicitly (e.g. *affinché*) and lead with the natural spoken alternative first.
- **Notebook content stays concise but accurate.** Full irregular paradigms only for top-tier verbs (*essere, avere, andare, fare*). Everything else minimal.
- Vague questions about a word (e.g. "what about *mai*") = asking about its **frequency/commonality in everyday spoken Italian**.

## Default session conduct

- Do not start a lesson unless Daniel directs you to.
- When proposing notebook content (which Daniel transcribes by hand) or editing flashcards, preserve dependency order; never introduce a structure that depends on something not yet covered without flagging it.

## Documentation ownership & maintenance

Each fact about learning state has exactly **one** owning file. Don't restate it in a second file — cross-reference instead.

- **`LEARNING_ROADMAP.md`** owns dependency order and notebook-transcription status only: a tick, and at most a one-line "taught DATE" note. No drill outcomes, no residual-leak detail — point to `WEAKNESS_AREAS.md` instead of restating them.
- **`WEAKNESS_AREAS.md`** owns *only* things that are not yet going smoothly. It is a snapshot of the current struggle, not a session log:
  - A newly taught topic is **not** a drill target by default — only add a row if it was a heavy lesson or Daniel didn't get it straight away. A clean first pass gets no entry.
  - **Overwrite, don't append.** When a weak spot's state changes, replace the row's note with the current picture — never stack a new dated paragraph alongside old ones. The row should always read as "here's where this stands now," not a history of every re-drill.
  - Remove a row entirely once a clean drill confirms internalization — don't leave a "resolved" note behind.
- Marking something "done"/"taught" = the minimal edit (tick a box, drop a stale caveat) in the **one** file that owns it. Don't propagate the same note into the other tracking docs — that's duplication, not thoroughness.

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

**If unsure what a request means, ask — don't hedge with tangential commands.** If a scope, target file, or step is ambiguous, stop and ask directly rather than running exploratory or "just in case" commands (backups, extra reads, side scripts) to work around the uncertainty.
