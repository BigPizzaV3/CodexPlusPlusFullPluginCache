---
name: build-2d-phaser
description: Implement or modify a playable browser 2D game in Phaser, including scenes, physics, input, and a browser build.
---

# Build 2D Phaser


1. Read `../../references/phaser.md` and official versioned Phaser docs. Phaser 4 is 2D-focused; check current APIs instead of copying outdated Phaser 3 examples uncritically.
2. Use the project’s existing build system or scaffold an official Phaser/Vite/TypeScript project when tools/network are available; don't invent installs. Set a baseline before editing.
3. Create a minimal scene with render loop, deterministic game state, keyboard input plus touch when mobile is a target, collision, feedback and reset. Ensure canvas fits viewport without distortion or illegible text.
4. Keep assets importable and consistent; use generated geometric textures until authorized assets are ready. Do not depend on unstable CDN assets to make a deliverable runnable.
5. Isolate mechanics from presentation where practical and avoid fragile one-file megascenes for projects with multiple systems.
6. Validate `npm` installation and build with actual commands when available; run browser smoke tests using real key/touch interactions and watch console/errors.
7. Check win, lose, pause, restart, focus loss and resize. Record an evidence log and exact files changed.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
