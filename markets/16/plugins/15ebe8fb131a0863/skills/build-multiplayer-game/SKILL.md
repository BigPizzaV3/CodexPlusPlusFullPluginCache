---
name: build-multiplayer-game
description: Architect and implement a small networked game prototype with authoritative state, synchronization, and abuse considerations.
---

# Build Multiplayer Game


1. Start by checking if multiplayer is genuinely required. A local/turn-based mode may satisfy an MVP faster and more reliably.
2. Read `../../references/multiplayer.md`; choose a suitable transport and hosted service only with user approval and an available environment.
3. Define a network authority model, session lifecycle, player identity, latency expectations, disconnect/reconnect, state sync and deterministic rules.
4. Never trust client-provided scores, health, inventory or paid entitlements. Require server-side validation for consequential game state.
5. Separate networking from core gameplay and build local single-player/loopback tests first; then two-client tests with simulated lag/loss where tools permit.
6. Document infrastructure costs, moderation/reporting for user-generated content when relevant, and security limits.
7. Do not claim cross-internet multiplayer is live without tested servers, clients and connectivity.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
