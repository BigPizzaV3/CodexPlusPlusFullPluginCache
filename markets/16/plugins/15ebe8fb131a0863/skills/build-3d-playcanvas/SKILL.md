---
name: build-3d-playcanvas
description: Build a small interactive browser 3D game using PlayCanvas Engine with camera, movement, collisions, and gameplay.
---

# Build 3D Playcanvas


1. Read `../../references/playcanvas.md`; distinguish the open-source Engine code-first workflow from the hosted PlayCanvas Editor and its account requirements.
2. Validate target devices and rendering fallback. Prefer basic WebGL compatibility before WebGPU-only techniques; ensure test browser actually supports required features.
3. Create a working 3D scene with camera, one controlled entity, lighting, ground/world, clear objectives, interactions and restart. Use simple procedurally created primitives when no asset tools exist.
4. Separate controls, camera, interactions and world state. Ensure sensible depth perception, camera clipping, movement speed, collision handling and state transitions.
5. Choose a practical camera mode (third-person, top-down, first-person) consistent with the core loop. For mobile targets include touch UI and performance budgets.
6. Run actual build/serve tests and browser WebGL checks where available; capture console and runtime failures. Visually inspect multiple views and performance.
7. Return runnable source, verified commands, generated artifacts when present and known limitations.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
