# Maintenance Tasks

Workspace, tooling, and flashcard-audit tasks. Italian-learning roadmap lives in `LEARNING_TASKS.md`.

## Top priority: phone → Samba → AI flashcard pipeline

End goal: drop `.mochi` exports from iPhone straight into `data/` over the tailnet (always as `data/export.mochi`, overwriting), then have AI-driven audit/edit/add/delete tooling operate on a derived `data/working.json` + `data/view/` and repack to `data/import.mochi` without losing SRS progress. Steps are dependency-ordered — do not start step N before N-1 is verified.

### 1. Samba server up and running — most pressing

Acceptable security baseline now; iterate later.

- [ ] `services/samba-mochi/` compose stack live (`docker compose up -d`), share `Data` reachable from iOS Files via `smb://100.67.6.40` (served from `data/` on host).
- [ ] Confirmed write from iPhone → file appears in `data/` on host with correct ownership.
- [ ] Confirmed unreachable from LAN and public — only tailnet sees port 445.
- [ ] Tighten container PID 1: currently runs as root-in-container even though `docker-samba` (UID 997, GID 983) is pre-created on host and used via `UID`/`GID` env vars. Samba's worker privsep means session-handling code already drops to UID 997, so attacker-controlled bytes never run as root — accepted for now. Real fix later: add `user: "997:983"` + `cap_add: [NET_BIND_SERVICE]` to compose, and pre-do the entrypoint's root-only work (user creation, `smbpasswd`, bind-mount chown — last one already done) so the entrypoint can run as non-root without skipping setup.
- [ ] Harden `smb.conf` (currently dockurr's defaults — no custom override mounted). Gaps: `server min protocol = SMB2` (should be `SMB3_00`), `wide links = yes` + `follow symlinks = yes` (symlink read-escape vector inside container), no `smb encrypt = required`, no `server signing = mandatory`, no `restrict anonymous = 2`, no `map to guest = never`, default file masks. Acceptable now because tailnet-only + single-client + IP-bound publish carry the real defense. Highest-leverage single line if we do nothing else: `server min protocol = SMB3_00`. Fix later by reintroducing a bind-mounted `smb.conf` (the version drafted earlier on 2026-06-26 is a good starting point — was removed when switching to dockurr defaults to ship faster).

### 2. Safety net — drop current iPhone Mochi state into `data/backups/`

Has to happen **immediately after** step 1 is verified. Any later workflow could corrupt content; this is the rollback point. `data/backups/` is the manual snapshot archive — separate from `data/export.mochi`, which gets overwritten by every new phone drop.

- [ ] Export current Mochi state from iPhone (`.mochi` with review history).
- [ ] Push via SMB into `data/`, then move to `data/backups/YYYY-MM-DD-pre-pipeline.mochi` (or rename in place if the phone can pick the target filename).
- [ ] `git add` and commit so the safety copy is durable independent of disk.

### 3. Retrieval → AI-readable representation

On manual `unpack` (auto-trigger deferred — start manual to verify the view-population step), `data/export.mochi` becomes:

- `data/working.json` — authoritative, mutable; the file all edit scripts target. Never derived from anything but the most recent unpack.
- `data/view/<deck>.md` — derived, one file per deck, each line carrying its card ID for coordinate-back-to-`working.json`. Regenerated wholesale on every unpack; never edited directly.

History strategy: git only for `working.json` + `view/`. No "commit before next export" discipline rule — `data/export.mochi` overwrites freely, and the manual `data/backups/` archive is the user-curated snapshot store.

- [x] `scripts/mochi_unpack.py` produces `data/working.json` + `data/view/<deck>.md` from `data/export.mochi`. (Done 2026-06-27.)
- [ ] Verify round-trip: unpack the safety-net `.mochi`, do a no-op edit, repack to `data/import.mochi`, compare against the original — equivalence except for expected nondeterminism (timestamps, ordering).
- [ ] (Deferred) Auto-unpack on file landing via inotify or systemd-path, once the manual flow is debugged.

### 4. AI-driven card lifecycle scripts

Extends "Tooling roadmap" below; this section frames them as one connected workflow rather than isolated CLI verbs.

- [ ] Audit (overlap with `scripts/mochi_pack.py audit` below).
- [ ] Edit in place — beyond the existing `edit-card` (which is single-card targeted); want batch-edit by AI-emitted patch.
- [ ] Add (overlap with `add-card` below).
- [ ] Delete.

### 5. Repack preserving SRS progress

- [ ] After any AI edit batch, repack `data/working.json` to `data/import.mochi` while preserving each card's `reviews[]` array per the rules in CLAUDE.md (`--reset-reviews` only when meaning changed, not for formatting).
- [ ] Verified import on iPhone restores interval/due/history correctly.

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

## Open questions

- What does the `~:pos` field on a card represent? Values seen: `"O"`, `"8"`. Likely position/sort key but unverified.

## Setup leftovers

- LICENSE file — discussed 2026-06-25, deferred. Public repo; current state is implicit "all rights reserved." Decide if `MIT` / `CC-BY` / explicit license is wanted.
