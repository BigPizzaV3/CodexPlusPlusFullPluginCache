---
name: game-design
description: Turn a game concept into a playable loop, progression model, state transitions, and scoped acceptance criteria.
---

# Game Design


1. Define fantasy, player agency, target session duration, intended feeling, core verbs, reward signals, and failure/retry.
2. Write a two-sentence **core loop**: player action -> world response -> reward/risk -> next decision. Avoid systems that do not reinforce it.
3. Specify game states: launch, gameplay, paused, won, lost, restarted, saved/loaded when in scope. Define deterministic level/score transitions and scoring rules.
4. Separate must-have vertical-slice mechanics from optional production expansion. Set one measurable completion condition for each.
5. Model difficulty with observable parameters: time, speed, enemy cadence, spawn counts, health, level length; avoid promising game is 'fun' without human playtesting.
6. Address onboarding, discoverability, feedback loops and accessible options. Use `../../references/gameplay-quality.md` and `../../templates/game-brief.md`.
7. Produce a compact game-design spec, state chart in prose, feature priority and test criteria. If asked to build, pass to engine-specific workflow rather than stopping at design.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
