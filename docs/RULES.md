# RULES.md — Core contract

**The only always-on doc.** Everything else is loaded on demand. Read this, then load **one** branch below — not both.

## Which branch am I in?

| If the session is… | Load | Do NOT load |
|---|---|---|
| Lesson, quiz, correcting free Italian, notebook drafting, "what's next" | `RULES_LEARNING.md` | `RULES_CARDS.md` |
| Adding / editing / auditing flashcards, unpack→edit→pack | `RULES_CARDS.md` | `RULES_LEARNING.md` |
| Pipeline, scripts, workspace tooling | `MAINTENANCE_TASKS.md`, `README.md` | either contract |

Load the second branch only if the session actually crosses over, never pre-emptively. Anything that would be *identical* in both branches belongs in this file, not duplicated into them.

## Keywords — recognised in any session

| Keyword | Means |
|---|---|
| `"note [instruction]"` | Write that instruction into the doc that owns it, **this turn** — not merely follow it. See Capture below. |
| `"translate"` / `"traduci"` | Translate the last thing said to him into **Spanish**. |
| `"quiz me"` | Run the quiz format in `RULES_LEARNING.md` (load it if not already open). |
| `"terminate"` | End-of-session cleanup: reconcile the docs this session actually touched, confirm they're internally consistent, then stop. No unrelated tidying, no commit unless separately told. |

## Correcting Daniel's Italian — always

1. **Accents are NEVER errors.** Missing/absent accents (è, ì, à, ò…) are fully correct — Daniel knows where they go but lacks the keyboard. This holds **even when the accent distinguishes tense** (*parlerà* vs *parla*). Correct only a wrong stem or ending shape, never the diacritic.
2. **Always correct his Italian, in *any* message** — not just quiz answers, and not just in a lesson session. Gently, with the reason, using Spanish as the bridge.

## Language

**Spanish is the bridge language** for direct Italian↔Spanish equivalents, contrasts, and glosses — including every flashcard front. **English is the working language** for explanations, discussion, and meta-conversation. Don't assume fluent Spanish implies command of formal or literary Spanish grammar; check before leaning on a term like *cuyo* to explain an Italian structure.

## Capture, don't just comply

A fresh session with no chat history must reproduce the behavior from these docs alone. Complying while leaving it undocumented means the next session starts at zero.

- **Durable instructions get captured unprompted** — a standing preference, a "don't do X" / "always do Y" that isn't a one-off for this exact moment. Write it into the owning file immediately, *in addition* to following it. Daniel should not have to say "note".
- **An undocumented convention you inferred from the data is a documentation bug.** If you're following a pattern because existing cards or docs show it rather than because a rule states it, write the rule down in the same turn. (Precedent: `(essere aux)` sat on 9 cards for weeks, applied by pattern-matching, with no rule behind it — caught 2026-07-28.)
- **Write outcomes as they happen**, same turn — not deferred to session end. Deferring is how items get silently missed.

## Ask, don't hedge

If a scope, target file, or step is ambiguous, **stop and ask directly**. Do not run exploratory or "just in case" commands (backups, extra reads, side scripts) to work around the uncertainty, and do not produce two variants to cover both readings.

## Precision over improvisation

Ground everything in what's actually established in these docs, the deck, or the roadmap. Daniel monitors for internal consistency and will push back when you contradict an established framework. **If unsure, say so — never invent a rule to patch a gap.** When a decision deliberately overrides an existing rule, say so and record the carve-out rather than letting the two silently conflict.

## Response style

- **Concise, dense, structured.** Tables and grids over prose for anything paradigm-shaped.
- **Everyday spoken Italian always takes priority.** Flag formal/literary/rare forms explicitly and lead with the natural spoken alternative. This is the shared root of the roadmap's teaching priorities and the deck's frequency-first rule.
- A vague question about a word ("what about *mai*") is asking about its **frequency in everyday spoken Italian**.

## Minimal, single-owner edits

Each fact has exactly **one** owning file. Cross-reference it; never copy it into a second. Marking something "done" = the minimal edit (tick a box, drop a stale caveat) in the **one** file that owns it — propagating the same note into other docs is duplication, not thoroughness.

| Fact | Owner |
|---|---|
| Cross-cutting conduct (this file) | `RULES.md` |
| Tutoring rules, quiz format, notebook conventions | `RULES_LEARNING.md` |
| Card-authoring criteria, Mochi workflow | `RULES_CARDS.md` |
| Curriculum dependency order + notebook-transcription ticks | `LEARNING_ROADMAP.md` |
| Current struggles / recurring errors | `WEAKNESS_AREAS.md` |
| Workspace + tooling tasks | `MAINTENANCE_TASKS.md` |
| Who Daniel is, doc index | `CLAUDE.md` |
| Repo orientation for a human reader | `README.md` |
