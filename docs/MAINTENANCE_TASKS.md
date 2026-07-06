# Maintenance Tasks

Workspace, tooling, and flashcard-audit tasks. Italian-learning roadmap lives in `LEARNING_ROADMAP.md`.

## Top priority: phone → Samba → AI flashcard pipeline

End goal: drop `.mochi` exports from iPhone straight into `data/` over the tailnet (always as `data/export.mochi`, overwriting), then have AI-driven audit/edit/add/delete tooling operate on a derived `data/working.json` + `data/view/` and repack to `data/import.mochi` without losing SRS progress. Steps are dependency-ordered — do not start step N before N-1 is verified.

### 1. Samba server up and running — most pressing

**Superseded 2026-07-06:** the Samba deployment (compose stack, `smb.conf` hardening, credentials, network exposure) now lives entirely in the separate [samba](../samba) repo, consolidated with Jellyfin's media share. See that repo's `CLAUDE.md` for current state — the `smb.conf` hardening item below is done there.

### 2. Safety net — drop current iPhone Mochi state into `data/backups/`

Has to happen **immediately after** step 1 is verified. Any later workflow could corrupt content; this is the rollback point. `data/backups/` is the manual snapshot archive — separate from `data/export.mochi`, which gets overwritten by every new phone drop.

- [x] Export current Mochi state from iPhone (`.mochi` with review history). (Done 2026-06-27.)
- [x] Push via SMB into `data/`, then move to `data/backups/` archive. (Done 2026-06-27 — currently at `data/backups/latest.mochi`. Consider renaming with date stamp before next safety snapshot lands.)
- [ ] `git add` and commit so the safety copy is durable independent of disk.

### 3. Retrieval → AI-readable representation

On manual `unpack` (auto-trigger deferred — start manual to verify the view-population step), `data/export.mochi` becomes:

- `data/working.json` — authoritative, mutable; the file all edit scripts target. Never derived from anything but the most recent unpack.
- `data/view/<deck>.md` — derived, one file per deck, each line carrying its card ID for coordinate-back-to-`working.json`. Regenerated wholesale on every unpack; never edited directly.

History strategy: git only for `working.json` + `view/`. No "commit before next export" discipline rule — `data/export.mochi` overwrites freely, and the manual `data/backups/` archive is the user-curated snapshot store.

- [x] `scripts/mochi_unpack.py` produces `data/working.json` + `data/view/<deck>.md` from `data/export.mochi`. (Done 2026-06-27.)
- [x] Verify round-trip: unpack → edit → repack. (Done 2026-06-27. Unpacked 9 decks → added "Set Phrases & Idioms" deck with 7 cards → repacked to `data/import.mochi`. 10 decks present, IDs intact, file size 8408 B vs 8168 B export.)
- [ ] (Deferred) Auto-unpack on file landing via inotify or systemd-path, once the manual flow is debugged.

### 4. AI-driven card lifecycle scripts

Extends "Tooling roadmap" below; this section frames them as one connected workflow rather than isolated CLI verbs.

- [ ] Audit (overlap with `scripts/mochi_pack.py audit` below).
- [ ] Edit in place — beyond the existing `edit-card` (which is single-card targeted); want batch-edit by AI-emitted patch.
- [ ] Add (overlap with `add-card` below).
- [ ] Delete.

### 5. Repack preserving SRS progress

- [x] `scripts/mochi_pack.py pack data/working.json data/import.mochi` produces a valid `.mochi`. (Done 2026-06-27 — see step 3 round-trip note.) Preserves `reviews[]` per CLAUDE.md (`--reset-reviews` only when meaning changed, not for formatting).
- [ ] Verified import on iPhone restores interval/due/history correctly. (Pending — `data/import.mochi` ready to drop.)

## Flashcard audit (pending edit batch)

Findings from the 2026-06-25 backup. Each fix needs the wipe-and-reimport workflow (see CLAUDE.md).

### Errors (content wrong — `--reset-reviews` required)

- [x] `[Verbs] caminar` → was `Caminare`, fixed to `camminare` (in `data/backups/2026-06-25-fix-camminare.mochi`, pending import)

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

- [ ] `scripts/mochi_pack.py add-card --deck <name> --front <text> --back <text>` (next, agreed)
- [ ] Batch-add from a markdown file (composes with "AI proposes N cards from text" workflows)
- [ ] `scripts/mochi_pack.py audit` — read-only scan emitting fix candidates (capitalization, exact-dup detection, suspect glosses)
- [x] `scripts/mochi_view.py` — regenerate `data/view/*.md` from `data/working.json` without re-unpacking. (Done 2026-07-02, after re-running `mochi_unpack.py` post-edit silently wiped a batch of in-flight card additions.)

## Open questions

- What does the `~:pos` field on a card represent? Values seen: `"O"`, `"8"`. Likely position/sort key but unverified.

## Setup leftovers

- LICENSE file — discussed 2026-06-25, deferred. Public repo; current state is implicit "all rights reserved." Decide if `MIT` / `CC-BY` / explicit license is wanted.
