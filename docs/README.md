# Italian Learning Workspace

A personal workspace for systematically acquiring Italian from a fluent Spanish base. Spanish is the bridge language throughout — every grammar contrast, gloss, and explanation is anchored to Spanish, not English.

## What lives here

- **Flashcard pipeline** — Mochi `.mochi` exports flow in from iPhone over Tailscale via the on-host Samba share (`services/samba-mochi/`), get unpacked into a working JSON + per-deck markdown views (`data/`), edited and audited via `scripts/`, repacked for re-import. Detailed below.
- **`CLAUDE.md`** — operational context Claude Code reads each session (who Daniel is, tooling).
- **`RULES.md`** — behavioral contract: hard rules, quiz format, response style, flashcard authoring conventions, Mochi edit workflow.
- **`MAINTENANCE_TASKS.md` / `LEARNING_ROADMAP.md` / `WEAKNESS_AREAS.md`** — running task lists and learning state.

The **grammar notebook is physical** (a paper notebook Daniel maintains by hand). It is not in this repo. Claude proposes notebook content in transcribable form; Daniel writes it in himself.

## Tooling

| Tool | Role | Sync |
| --- | --- | --- |
| **Mochi** (free tier) | Flashcard SRS, Markdown-authored | **Manual wipe-and-reimport** — no cloud sync on free tier; `.mochi` exports flow into `data/` via the on-host Samba share, edits applied here, repacked file goes back to phone |
| **conjuguemos.com** | Conjugation drilling, holds verb sets | External; used for paradigm practice |
| **Physical notebook** | Grammar notebook in strict dependency order — closed-class structural grammar | Hand-written; not in this repo |
| **This repo** | Flashcard pipeline (`data/`, `scripts/`, `services/samba-mochi/`) + tutor contract (`CLAUDE.md`, `RULES.md`) | — |

Because Mochi sync is manual, card *content* can be edited programmatically here and AI-audited (dedupe, gloss correctness, interference-trap flags, formatting) before being copied back.

## Learning state

The notebook curriculum, current weak spots, and what's next are live-tracked state, not repeated here — see `LEARNING_ROADMAP.md` and `WEAKNESS_AREAS.md` for the current picture.

## Day-to-day usage

- **"quiz me"** — Claude generates 5–8 English→Italian translation sentences with vocab glosses only (no telegraphing), covertly targeting an active weak spot, then marks and scoreboards.
- **"translate" / "traduci"** — translate the last thing said into Spanish.
- **Free-form Italian** — anything written in Italian gets gently corrected via Spanish.
- **Notebook additions** — Claude drafts new sections in transcribable form (tables/grids over prose); Daniel writes them into the physical notebook. Dependency order is preserved; nothing depending on uncovered material is introduced without flagging.
- **Flashcard audits** — run AI passes over `data/view/<deck>.md` for dedupe, gloss errors, missing interference flags; apply edits to `data/working.json`; repack and re-import to Mochi manually.

## Flashcard pipeline

1. iPhone exports current Mochi state as `.mochi` (with embedded review history).
2. Drops over the tailnet via the on-host Samba share (`services/samba-mochi/`) — lands at `data/export.mochi`, overwriting each time.
3. `scripts/mochi_unpack.py` derives:
   - `data/working.json` — full-fidelity Transit-JSON, the canonical edit target.
   - `data/view/<deck>.md` — one cheap-to-scan markdown file per deck for AI audit (card IDs surfaced inline). Regenerated wholesale each unpack; never edited directly.
4. Edits apply to `working.json` via the `scripts/mochi_edit.py` primitive library or the `scripts/mochi_pack.py edit-card` CLI.
5. `scripts/mochi_pack.py pack` repacks `working.json` → `data/import.mochi`.
6. Re-import on iPhone (wipe decks → empty trash → import) restores cards plus SRS state from the preserved `reviews[]` arrays.

Snapshots at user discretion live in `data/backups/YYYY-MM-DD-*.mochi`. Working state is otherwise tracked through git history.

Detailed workflow rules (review-reset rule for meaning changes vs formatting; safety rule for the wipe step; filename-cache gotcha) live in `RULES.md`.
