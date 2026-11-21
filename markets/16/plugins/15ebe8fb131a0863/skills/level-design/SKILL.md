---
name: level-design
description: Design levels and game environments with readable objectives, pacing, difficulty, progression, and meaningful player decisions.
---

# Level Design


1. Derive the level's teaching objective, player path, points of challenge, optional discovery, and exit state from game mechanics.
2. Create blockouts before final art. Establish start/safe area, checkpoints, signposting, enemy/hazard placement and completion condition.
3. For 2D, validate tile collision, jump distances and camera bounds; for 3D, validate traversal, collision geometry, line of sight, scale and navigation.
4. Introduce new mechanics safely, then vary challenge and create a final competence test. Avoid long empty corridors and decorative rooms with no gameplay contribution.
5. Read `../../references/level-design.md` and record a playable flow from spawn to win/lose/restart.
6. Test with scripted walkthroughs or human playtest, include stuck-state detection and ensure the level is completable without undocumented controls.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
