---
name: debug-game
description: Reproduce and fix a game bug such as crashes, physics glitches, broken controls, missing assets, or failing exports.
---

# Debug Game


1. Ask for missing reproducible steps only if essential; otherwise inspect logs, scene files, code and build settings. Reproduce before modifying when possible.
2. Classify: runtime error, import/asset, physics/collision, state/progression, camera/input, device/export, performance, network, or visual defect.
3. Form one or more testable hypotheses, inspect engine/runtime evidence and identify a minimal root cause.
4. Implement a focused fix, add a regression check and rerun the original reproduction plus related systems.
5. When hardware/engine tooling is unavailable, state the diagnosis confidence and exact commands or steps the user should run; never fabricate traces or reproduction.
6. Output before/after behavior, changed files, test evidence and known limitations. Read `../../references/testing-and-evidence.md`.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
