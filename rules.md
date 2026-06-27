# rules.md — Behavioral contract for the Italian workspace

This file holds the prescriptive "do this / don't do this" rules. CLAUDE.md is the context layer (who Daniel is, project state, weak spots); this file is the rulebook. Read both at the start of every session.

## Hard rules (verbatim — non-negotiable)

1. **Accents are NEVER errors.** Treat all missing/absent accents (è, ì, à, ò, etc.) as fully correct — Daniel knows where they go but lacks the keyboard to type them. This holds **even when the accent distinguishes tense** (future `-à` vs present `-a`, e.g. *parlerà* vs *parla*). Only correct the underlying form when the **stem or ending shape** is wrong, never the diacritic.
2. **Always correct Daniel's Italian.** When he writes something incorrect in Italian — in *any* message, not just quiz answers — gently correct it and explain why, using Spanish as the bridge.
3. **"translate" / "traduci"** = translate the last thing said to him into **Spanish**.
4. **"quiz me"** = the format below.

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

## Mochi flashcard authoring

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

1. Export current state as `.mochi` (with review history) from Mochi iOS. Via SMB+Tailscale (`services/samba-mochi/`), it lands as `data/export.mochi` on host. Snapshot to `data/backups/YYYY-MM-DD.mochi` for safety.
2. `scripts/mochi_unpack.py` derives `data/working.json` (authoritative, mutable) + `data/view/<deck>.md` (regenerated each unpack, never edited directly).
3. Apply edits to `data/working.json` via the `scripts/mochi_edit.py` helpers (load/save/add_to/add_deck/remove/move/append_to_content) or the `scripts/mochi_pack.py edit-card` CLI for single-card targeted edits.
4. `scripts/mochi_pack.py pack data/working.json data/import.mochi` to produce the import artifact.
5. In Mochi iOS: delete all decks, empty trash.
6. Import `data/import.mochi`. Card content updates **and** the embedded `reviews[]` array restores SRS state (interval, due date, remembered-history) verbatim.

**Review-reset rule:** when fixing a card's *meaning* (not just formatting), always reset its `~:reviews` to `[]`. Past "remembered? = true" entries were against the wrong content — keeping them would lock in the error. Pure formatting/whitespace/example-add edits leave reviews alone.

**Safety rule:** never delete in-app before confirming `data/import.mochi` exists on disk and the prior snapshot is committed to `data/backups/`. The wipe step is irreversible.

**Filename rule:** Mochi caches by import filename — if an import fails, bump the suffix (`-v2.mochi`, `-v3.mochi`) before retrying, otherwise the old failure resurfaces.
