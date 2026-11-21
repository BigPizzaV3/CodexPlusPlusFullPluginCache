---
name: build-narrative-game
description: Design or implement visual novels, branching dialogue, interactive fiction, and story-driven game mechanics with coherent state.
---

# Build Narrative Game


1. Define player agency, branching structure, variables/flags, pacing, scene transitions and narrative endings; avoid fake choice branches that immediately converge without consequence.
2. Read `../../references/renpy.md` for Ren’Py-focused visual novel implementation. Existing custom engines may be retained.
3. Model dialogue and conditional state separately from presentation when possible. Track dead ends, unreachable branches, missing assets and uninitialized variables.
4. Provide accessible typography, readable pacing, rollback/skip settings if supported, clear choices and consistent UI.
5. Validate branch completeness with a graph walkthrough and actual engine lint/build commands when available; include save/load tests.
6. Use original or appropriately licensed narrative, character assets and music. If user requests an existing commercial IP, prefer an original alternative unless rights are confirmed.
7. Deliver scripts, branch map, input/output state definitions, tested endings, and unresolved narrative assumptions.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
