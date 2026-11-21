---
name: game-from-idea
description: Build a playable game from a natural-language idea, organizing the core game loop, engine, assets, and actual verification.
---

# Game From Idea


## End-to-end workflow
1. Create a concise playable brief using `../../templates/game-brief.md`; require a player verb, challenge, feedback, success/failure condition, and restart. If missing, derive a minimal plausible version.
2. Route through `select-engine` and record why the engine/platform is appropriate. Avoid automatic Unity/Unreal selection for simple browser games.
3. Use `game-design` and `game-art-direction` to establish mechanics and coherent visual language. Define keyboard/gamepad/touch needs; accessibility; no mandatory network unless the concept requires it.
4. Build the **first vertical slice**: launch/title or immediate start, core interaction, game state, a meaningful goal, failure/success, restart. Include pause and sound toggles where relevant.
5. Add one level/scene, smallest useful content set, simple but consistent artwork, and feedback sounds. Defer large maps, shops, inventory, online accounts, and elaborate progression until the core loop is playable.
6. Run a real executable smoke check if environment allows it. For browser games, capture browser errors and test keyboard/touch; for desktop use editor/headless checks plus interactive verification when available.
7. Independently review against acceptance criteria, repair failures, then package source, setup instructions, build artifacts actually produced and evidence.
8. When execution tools are missing, provide complete source files in a deliverable format where possible and clear unverified run instructions. Never report a functioning preview that wasn't run.
## Deliverable contract
Provide playable scope, engine, project tree, assets and licenses, implemented mechanics, controls, exact test commands and results, remaining defects and next expansion options. Read `../../references/testing-and-evidence.md`.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
