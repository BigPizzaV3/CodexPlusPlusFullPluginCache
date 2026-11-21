---
name: get-started
description: Choose the right Design Game Studio workflow when a user wants to make a game, explore capabilities, or work on an existing game project.
---

# Get Started


## First interaction
1. Identify whether the user wants (a) a new playable game, (b) a game design only, (c) an edit/debug of an existing game, or (d) release assistance. Do not reduce a build request to a design document.
2. Extract platform, presentation (2D / 2.5D / 3D), genre, intended player actions, art style, input method, scale, and supplied files. If the idea is broad, make transparent defaults and proceed; ask only for a blocking choice such as target platform when it cannot be reasonably inferred.
3. Check actual host tools: filesystem, terminal, browser, image/asset generation, installed editors, simulator, source control, and genuine subagent APIs. No claims of independent cloud game creation without a working runtime.
4. Route new-game requests to `game-from-idea`; existing-game edits to `improve-existing-game`; failures to `debug-game`; one engine or component request to its specific skill; test/ship requests to corresponding skills.
5. Select a minimum playable loop before expanding visuals or scope. Use `../../references/engine-matrix.md` and `../../references/platform-and-input.md`.
6. For substantial multi-part tasks use `orchestrate-game-agents` only if actual agent delegation tools exist; otherwise follow the same sequence in one session.
## Output
State game concept, chosen first playable scope, engine rationale, available tool capabilities, and the concrete next build step. Then carry out authorized work immediately where tools exist.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
