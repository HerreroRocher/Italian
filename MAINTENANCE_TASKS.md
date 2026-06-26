# Maintenance Tasks

Workspace, tooling, and flashcard-audit tasks. Italian-learning roadmap lives in `LEARNING_TASKS.md`.

## Flashcard audit (pending edit batch)

Findings from the 2026-06-25 backup. Each fix needs the wipe-and-reimport workflow (see CLAUDE.md).

### Errors (content wrong — `--reset-reviews` required)

- [x] `[Verbs] caminar` → was `Caminare`, fixed to `camminare` (in `backups/2026-06-25-fix-camminare.mochi`, pending import)

### Capitalization sweep — Verbs deck

Infinitives should be lowercase. Currently inconsistent:

| Card front | Current back | Should be |
|---|---|---|
| ver (dup) | `Vedere` | `vedere` |
| entender | `Capire` | `capire` |
| mirar | `Guardare` | `guardare` |
| stay/estar | `Stare` | `stare` |
| encontrar | `Trovare` | `trovare` |
| hablar | `Parlare` | `parlare` |
| caminar | (already fixing) | `camminare` |
| ser | `Essere` | `essere` |
| ir | `Andare` | `andare` |
| buscar | `Cercare` | `cercare` |

Formatting-only — leave `reviews` alone.

### Duplicates — Verbs deck

- [ ] `entrar :: entrare` appears **twice** — keep one, delete other.
- [ ] `ver` appears twice (`vedere` and `Vedere`) — merge into one card after capitalization sweep.

### Cross-deck duplicates

`troppo`, `abbastanza`, `poco`, `molto` appear in **both** Connectives and Quantity & Degree.

- [ ] Decide: dedupe, or accept overlap as intentional?
- [ ] Bigger question: Connectives currently holds frequencies (`spesso`, `poco`), time markers (`oggi/ieri/domani`), and quantifiers (`molto`) that arguably belong elsewhere. Consider deck restructure.

## Tooling roadmap

- [ ] `mochi_pack.py add-card --deck <name> --front <text> --back <text>` (next, agreed)
- [ ] Batch-add from a markdown file (composes with "AI proposes N cards from text" workflows)
- [ ] `mochi_pack.py audit` — read-only scan emitting fix candidates (capitalization, exact-dup detection, suspect glosses)

## Open questions

- What does the `~:pos` field on a card represent? Values seen: `"O"`, `"8"`. Likely position/sort key but unverified.
- Should `markdown-export/` be regenerable from `.mochi` via a `dump-markdown` subcommand? It's been deleted from disk; if we want a human-readable diff view of card content for git, this would be the way.

## Setup leftovers

- LICENSE file — discussed 2026-06-25, deferred. Public repo; current state is implicit "all rights reserved." Decide if `MIT` / `CC-BY` / explicit license is wanted.
- README — was written before the `.mochi` workflow was characterized; may need a refresh to point at `mochi_pack.py` and `backups/`.
