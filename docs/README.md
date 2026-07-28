# Italian Learning Workspace

A personal workspace for systematically acquiring Italian from a fluent Spanish base. Spanish is the bridge language throughout — every grammar contrast, gloss, and flashcard front is anchored to Spanish, not English.

Two things live here: a **tutoring contract** (the rules Claude Code operates under) and a **flashcard pipeline** (Mochi export → edit → repack). The grammar notebook is *physical* — a paper notebook Daniel maintains by hand, not in this repo; Claude proposes transcribable content and Daniel writes it in himself.

## Map

| File | Owns |
|---|---|
| `CLAUDE.md` (repo root) | Session context: who Daniel is, index of everything below |
| `docs/RULES.md` | **The only always-on doc.** Shared conduct + routing to exactly one branch below |
| `docs/RULES_LEARNING.md` | Lesson branch: quiz format, notebook conventions, session conduct |
| `docs/RULES_CARDS.md` | Flashcard branch: authoring criteria + the Mochi edit/repack workflow |
| `docs/LEARNING_ROADMAP.md` | Curriculum in dependency order; ticks = notebook-transcription status |
| `docs/WEAKNESS_AREAS.md` | Current recurring errors — a live snapshot, not a session log |
| `docs/MAINTENANCE_TASKS.md` | Workspace/tooling tasks and their status |
| `data/`, `scripts/` | The deck itself and the primitives that operate on it |

Rules are stated once, in the file that owns them. This README signposts and does not restate; `docs/RULES.md` holds the ownership table. The two branch contracts are **mutually exclusive by design** — a flashcard session must never pay the token cost of loading the tutoring rules, or vice versa.

## Tooling

| Tool | Role | Sync |
|---|---|---|
| **Mochi** (free tier) | Flashcard SRS, Markdown-authored | **Manual wipe-and-reimport** — no cloud sync on free tier |
| **Samba share** | Moves `.mochi` files phone ↔ host over Tailscale | Deployed from the separate [samba](../samba) repo, alongside Jellyfin's media share |
| **conjuguemos.com** | Conjugation drilling, holds verb sets | External |
| **Physical notebook** | Closed-class structural grammar, strict dependency order | Hand-written; not in this repo |

## Flashcard pipeline

```
iPhone ──export──▶ data/export.mochi ──mochi_unpack.py──▶ data/working.json  (canonical, mutable)
                                                        └▶ data/view/*.md   (derived, read-only)
                          mochi_edit.py primitives ──edit──▶ working.json
                          mochi_view.py ──────────refresh──▶ view/*.md
                          mochi_pack.py ───────────pack───▶ data/import-vN.mochi ──▶ iPhone
```

Re-import (wipe decks → empty trash → import) restores cards *and* SRS state from the embedded `reviews[]` arrays. Because sync is manual, card content can be programmatically edited and AI-audited here before going back.

**Do not improvise on this pipeline.** Every step has a rule behind it that was learned the hard way — the review-reset rule, the wipe safety rule, the import-filename cache gotcha, `~:name` vs `~:content`, and why `mochi_view.py` is not `mochi_unpack.py`. They're all in `docs/RULES_CARDS.md` → Mochi edit workflow. Read it before touching the deck.

Snapshots live in `data/backups/YYYY-MM-DD.mochi` at Daniel's discretion; `working.json` and `view/` are otherwise tracked through git.
