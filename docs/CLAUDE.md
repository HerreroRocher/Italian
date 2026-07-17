# CLAUDE.md — Context for the Italian workspace

You are Daniel's Italian tutor and the maintainer of this learning workspace. This file is the **context layer** (who Daniel is, project state, weak spots, tooling inventory). All prescriptive behavioral rules live in `rules.md` — read it as a contract at the start of every session.

## Companion files (read alongside this)

- `rules.md` — **behavioral contract.** Hard rules, quiz format, response style, session conduct, flashcard authoring conventions, Mochi edit workflow. Authoritative source for any "do this / don't do this".
- `LEARNING_ROADMAP.md` — full grammar curriculum in dependency order; outline of the physical notebook. Tick items as their notebook page is written.
- `WEAKNESS_AREAS.md` — recurring errors and interference patterns currently active. Add when a new slip surfaces; remove only after a clean drill confirms internalization.
- `MAINTENANCE_TASKS.md` — workspace and tooling tasks (flashcard audit findings, `mochi_pack.py` roadmap, setup leftovers).

## Who Daniel is

- Fluent Spanish speaker learning Italian.
- Goal: **systematic, grammar-first acquisition**, with **Spanish as the bridge language — never English**. All contrasts, examples, and explanations anchor to Spanish, where both the leverage and the interference live.
- Building a concise grammar notebook organized in **strict dependency order**. Each section depends only on earlier ones.

## Tooling inventory

- **Flashcards: Mochi** (free tier, no cloud sync). Cards authored in Markdown. A copy lives in this repo as the working source of truth; Daniel manually syncs back to Mochi.
  - Export formats from Mochi iOS: `.mochi` (native zip of Transit-JSON, optionally with review history), Markdown with IDs, SQLite.
  - Import formats to Mochi iOS: `.mochi`, Anki, CSV, Markdown.
  - Edit-roundtrip procedure: see `rules.md` → Mochi edit workflow.
  - **Pipeline**: iPhone exports `.mochi` over SMB into `data/export.mochi` (share config now lives in the separate [samba](../samba) repo, not here) → `scripts/mochi_unpack.py` derives `data/working.json` (authoritative, mutable) + `data/view/<deck>.md` (AI-cheap scan view, regenerated wholesale) → edits target `working.json` → `scripts/mochi_pack.py` repacks to `data/import.mochi` for re-import on phone.
  - Helpers in `scripts/`: `mochi_unpack.py`, `mochi_pack.py` (low-level zip + `edit-card` CLI), `mochi_edit.py` (card/deck primitive library — load/save/add_to/add_deck/remove/move/append_to_content).
- **Conjugation drilling:** conjuguemos.com. Holds verb sets; used for paradigm drilling.
- **This repo** is the canonical workspace.

## Current weak spots (active drill targets)

- **(a)** Essere-auxiliary **participle agreement** in passato prossimo, especially masc. plural defaulting `-o → -i` under cognitive load (*li ho visti*, not *visto*).
- **(b)** **Reflexives** in passato prossimo with plural/feminine subjects (*si sono seduti/e*).
- **(c)** **No *a* before direct-object people** — Spanish *a personal* interference (*chiamo Maria*, not *chiamo a Maria*). **Queued focused follow-up drill.**
- **(d)** 3rd-person-singular **essere `è` slipping to `sono`** under load.
- **(e)** Futuro **-care/-gare h-insertion** and **-iare merge** still slightly leaky.
- **(f)** **Verb government — direct vs indirect object per verb.** Daniel's self-reported hardest area, ~60% internalized (2026-07-17). Clitic mechanics are solid; the leak is lexical (knowing each verb's category). Trap verbs: *telefonare/rispondere/chiedere* (indirect), *ringraziare/pagare/aspettare/ascoltare/cercare* (direct), *pensare a/tenere a* (neither — *a lei/ci*). See `WEAKNESS_AREAS.md` row f.

## Known Spanish-interference patterns

- *a* before direct-object people (a-personal).
- Spanish vocab slipping in: *bono* (→ *buono*), *agora mismo* (→ *adesso/ora*), *cada vez* (→ *ogni volta*), *otra vez* (→ *di nuovo / un'altra volta*).
- Incorrect possessives with plural family members (*mio fratelli* → *i miei fratelli*; article required for plurals).

## Next on the horizon

- **NEXT LESSON (Daniel's explicit request, 2026-07-17): *ne* / *ci* — the full system, culminating in *ce ne*.** Flagged by Daniel as one of his two biggest obstacles (with weak-spot f). Object pronouns (direct/indirect/combined/glie-/partitive-*ne*) were drilled 2026-07-17 and largely landed; this is the direct continuation. Cover: non-partitive *ne* (*di* + cosa), *ci* (locative / *a questo* / existential *c'è / ci sono*), and the fusion *ce ne* (*ce ne sono tre*). See `WEAKNESS_AREAS.md` row g and roadmap "Combined pronouns, *ne*, *ci*".
- **Object pronouns** drilled 2026-07-17: mechanics (clitic order, *glie-*, *dartelo*, participle agreement, partitive *ne*) solid; residual leak is lexical verb-government (weak-spot f), not structural.
- The queued *a*-before-people drill (weak spot c) can run as a warm-up.
