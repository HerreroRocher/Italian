# Italian Learning Workspace

A personal workspace for systematically acquiring Italian from a fluent Spanish base. Spanish is the bridge language throughout — every grammar contrast, gloss, and explanation is anchored to Spanish, not English.

## What lives here

- **Flashcard mirror** (`markdown-export/`, `markdown-processed/`) — a working copy of the Mochi flashcards as Markdown, plus tooling to reshape them.
- **`CLAUDE.md`** — operational contract Claude Code reads each session.
- **`reverse_flashcards.py`** — reverses Italian-front / Spanish-back cards into Spanish-front / Italian-back and bundles each deck into one `%`-delimited Markdown file for Mochi import.

The **grammar notebook is physical** (a paper notebook Daniel maintains by hand). It is not in this repo. Claude proposes notebook content in transcribable form; Daniel writes it in himself.

## Tooling

| Tool | Role | Sync |
| --- | --- | --- |
| **Mochi** (free tier) | Flashcard SRS, Markdown-authored | **Manual** — no cloud sync on free tier; this repo is the working source of truth, manually pushed back to Mochi |
| **conjuguemos.com** | Conjugation drilling, holds verb sets | External; used for paradigm practice |
| **Physical notebook** | Grammar notebook in strict dependency order — closed-class structural grammar | Hand-written; not in this repo |
| **This repo** | Flashcard mirror + reshape/audit tooling + `CLAUDE.md` contract | — |

Because Mochi sync is manual, card *content* can still be edited programmatically here and AI-audited (dedupe, gloss correctness, interference-trap flags, formatting) before being copied back.

## Notebook state — dependency order

Mirrored here for Claude's context. The authoritative copy is the physical notebook. All sections below are **covered**.

1. Definite & indefinite articles
2. Articulated prepositions (incl. partitive double-duty of the *di*-row)
3. *di* vs *da* contrast
4. Present tense — regular (incl. the *-isc-* subgroup of *-ire* verbs)
5. Top-3 irregulars in present: **essere, avere, andare/fare** (full paradigms)
6. Passato prossimo (auxiliary selection, essere vs avere split, reflexive rule, irregular participles)
7. Imperfetto
8. Clitic / object pronouns — covered in depth (reflexive, indirect, direct; *lo/la/li/le* vs *gli/le*; *ne*, *ci*; placement; elisions like *l'ho*; participle agreement with preceding direct-object clitic)
9. **Futuro semplice** — most recently taught and drilled:
   - *-are* stem **`a → e`** (parlare → parler-)
   - *-care/-gare* **h-insertion** (cercare → cercher-, pagare → pagher-)
   - *-iare* **stem-i merge** (cominciare → comincer-, NOT *comincier-*)
   - Shared endings across all three conjugations: **-ò / -ai / -à / -emo / -ete / -anno**
   - **Boundary:** Italian *andare a + inf* is **literal motion**, NOT a future like Spanish *ir a*. Near/planned future uses plain present or futuro semplice. Spanish *voy a + inf* → Italian plain present.

## Active weak spots

- Essere-aux **participle agreement** in passato prossimo (masc. plural drift `-o → -i`).
- **Reflexives** in passato prossimo with plural/feminine subjects.
- **No *a* before direct-object people** — Spanish *a personal* interference. Queued for focused drill.
- 3rd-sg **essere `è`** slipping to *sono* under load.
- Futuro **-care/-gare h-insertion** and **-iare merge** still slightly leaky.

## Next up

- Promote direct/indirect object pronouns from "seen" to a dedicated, drilled notebook section. This is the prerequisite for sealing the participle-agreement weak spot.
- Run the queued *a*-before-people drill as a warm-up.

## Day-to-day usage

- **"quiz me"** — Claude generates 5–8 English→Italian translation sentences with vocab glosses only (no telegraphing), covertly targeting an active weak spot, then marks and scoreboards.
- **"translate" / "traduci"** — translate the last thing said into Spanish.
- **Free-form Italian** — anything written in Italian gets gently corrected via Spanish.
- **Notebook additions** — Claude drafts new sections in transcribable form (tables/grids over prose); Daniel writes them into the physical notebook. Dependency order is preserved; nothing depending on uncovered material is introduced without flagging.
- **Flashcard audits** — run AI passes over `markdown-export/` for dedupe, gloss errors, missing interference flags; sync back to Mochi manually.

## Flashcard reshape pipeline

`reverse_flashcards.py` reads `markdown-export/` (Italian-front, Spanish-back), produces `markdown-processed/` with Spanish-front / Italian-back cards renamed accordingly, and writes one deck file per subdirectory at the root of `markdown-processed/` with cards separated by `%` lines — ready for Mochi import in the reversed direction.
