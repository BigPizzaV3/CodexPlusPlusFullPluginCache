---
name: improve-existing-game
description: Understand and extend an existing game repository, feature, scene, or mechanic with minimal justified changes and regression checks.
---

# Improve Existing Game


1. Inspect project and engine version, run instructions, build baseline, scenes and source ownership; do not replace the whole project with a fresh scaffold.
2. Identify exact requested behavior and relevant scenes/scripts/assets. Specify expected observable acceptance criteria before editing.
3. Create the smallest change compatible with current architecture. Preserve save files, user data, asset licenses, input mappings and unrelated styling.
4. Run original tests and a focused regression test for the change, plus one smoke test in the relevant level or scene when tools permit.
5. If existing implementation is broken, distinguish pre-existing failures from introduced ones; avoid claiming the entire game passes if only isolated checks ran.
6. Deliver diff summary, changed files, evidence, remaining risks, and reversible instructions.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
