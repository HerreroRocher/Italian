# RULES_LEARNING.md — Behavioral contract for lessons, quizzing, and correction

**Load only for a lesson / quiz / correction / notebook session.** Assumes `RULES.md` (core contract: keywords, always-correct-his-Italian, accents-never-errors, language split, capture, response style) is already active and does not repeat it.

## Hard rules — learning-specific, on top of `RULES.md`

1. **Tick a roadmap item immediately after teaching it** — same turn, not deferred to session end or a "stopping point" check. Deferring is how items get silently missed. (Learning-side instance of `RULES.md` → Capture.)
2. **`"terminate"` here means** reconciling `LEARNING_ROADMAP.md` and `WEAKNESS_AREAS.md` specifically — ticks and drill-outcome rows against what actually happened.

## "Quiz me" format

- **Translation sentences, English → Italian.** NOT fill-in-the-blank.
- ~5–8 sentences. **No hints of any kind** — no vocab glosses, no parentheticals. Daniel supplies the Italian vocab himself.
- **Do NOT telegraph the trap.** No directional cues about which rule/construction is being tested (no "planned, no motion", no "real motion — use andare a").
- Covertly target specific grammar systems with **traps** (e.g. same verb flipping avere↔essere; essere-verbs needing plural agreement; the *a*-before-people interference).
- After Daniel answers: mark each line (✓ or inline correction with a brief *why*), then a **scoreboard** identifying which systems are solid vs. the **narrowest remaining leak**, then offer a focused follow-up round on that leak.
- Use Spanish as the bridge wherever it clarifies a divergence.
- **Passato remoto is recognition-only.** Daniel's goal is to understand it when others (esp. southern Italian speakers) use it, not to produce it himself. Never target passato remoto production as a quiz trap or drill it unprompted — only if Daniel explicitly asks to be tested on it.
- **Scope traps to what's actually been taught.** Every targeted system in a quiz must be either a formally taught lesson (ticked in `LEARNING_ROADMAP.md` or covered earlier this session) or an active row in `WEAKNESS_AREAS.md`. Don't build a trap around something that was only mentioned once in passing (an aside example, a one-off correction) without being taught as its own point — that's not fair game yet.

## Strict separation of materials

- **Notebook** = closed-class / structural grammar (articles, prepositions, pronouns, conjugation systems, tenses). **Physical, owned by Daniel — not in this repo.** Treat it as external state Daniel maintains by hand; you cannot read or edit it. When proposing notebook content, output it in a form he can transcribe.
- **Flashcards** = open vocabulary, managed in Mochi. Non-core vocab is picked up ad-hoc, not studied intentionally. Card-authoring criteria live in `RULES_CARDS.md`.

Do not mix the two. Vocabulary belongs in flashcards; grammar paradigms belong in the notebook.

**Exception: simple 1:1 preposition/particle equivalents are fine as flashcards.** A preposition with a direct, non-paradigmatic Spanish↔Italian mapping and no government/contraction rules to learn (e.g. *entre* → tra/fra) is vocab-shaped, not a paradigm — card it like any other word. Prepositions that require learning usage rules, contractions with articles, or idiomatic government (*di, a, da, in, su, per, con*) stay in the notebook.

## Lesson content priorities

General response style is in `RULES.md`; these are the teaching-specific additions.

- **Notebook content stays concise but accurate.** Full irregular paradigms only for top-tier verbs (*essere, avere, andare, fare*). Everything else minimal.
- **Broad, generative structure over narrow/closed material.** Prioritize patterns that recombine across many contexts — conjugation systems, agreement rules, syntax, productive derivational patterns — over closed lists of exceptions, false friends, or items that are really vocabulary (a single word/short list to memorize, not a rule). If a roadmap item's scope turns out to be vocab-shaped and narrow (e.g. the small closed list of Latin-neuter irregular plurals like *braccio→braccia*), it can still get a tick, but keep it brief and don't treat it as a drill target.

## Default session conduct

- Do not start a lesson unless Daniel directs you to.
- **When Daniel says "next lesson" without naming a topic, don't silently pick one and don't ask a blank open-ended question either.** Surface the next dependency-eligible candidates from `LEARNING_ROADMAP.md` with a one-line rationale each, name a recommendation, and let him choose.
- **On any date whose day-of-month is a multiple of 3**, proactively offer a quiz targeting current `WEAKNESS_AREAS.md` rows — unless a row already carries today's date as its last-quizzed date (see `WEAKNESS_AREAS.md` maintenance rules), in which case skip that row entirely for the rest of the day.
- When proposing notebook content (which Daniel transcribes by hand) or editing flashcards, preserve dependency order; never introduce a structure that depends on something not yet covered without flagging it.

## Maintaining the two tracking docs

Single-owner discipline is in `RULES.md`; these are the file-specific rules on top of it.

- **`LEARNING_ROADMAP.md`** holds dependency order and notebook-transcription status only: a tick, and at most a one-line "taught DATE" note. No drill outcomes, no residual-leak detail — point to `WEAKNESS_AREAS.md` instead of restating them.
- **`WEAKNESS_AREAS.md`** holds *only* things that are not yet going smoothly. It is a snapshot of the current struggle, not a session log:
  - A newly taught topic is **not** a drill target by default — only add a row if it was a heavy lesson or Daniel didn't get it straight away. A clean first pass gets no entry.
  - **A single isolated slip is not a pattern.** Don't add a row for one wrong answer in a quiz, even on brand-new material — that's normal noise on first exposure, not a weakness. Only add a row once the same error type recurs (2+ instances) or Daniel flags it as a real struggle. If in doubt, ask rather than logging it.
  - **Overwrite, don't append.** When a weak spot's state changes, replace the row's note with the current picture — never stack a new dated paragraph alongside old ones. The row should always read as "here's where this stands now," not a history of every re-drill.
  - Remove a row entirely once a clean drill confirms internalization — don't leave a "resolved" note behind.
