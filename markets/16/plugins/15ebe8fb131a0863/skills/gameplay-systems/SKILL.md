---
name: gameplay-systems
description: Design and implement modular gameplay mechanics such as movement, combat, inventory, crafting, enemies, saving, and progression.
---

# Gameplay Systems


1. Translate feature requests into player actions, game-state transitions, preconditions, feedback and outcomes. Define invariants for health, score, ownership, inventory or quest state.
2. Keep systems separated where useful: input, rules, physics, rendering, audio, persistence and UI. Prefer engine-native conventions over custom frameworks.
3. For movement, verify delta-time handling, jump/coyote time if appropriate, camera behavior, collisions and boundaries. For combat, model damage, invulnerability and death/retry.
4. For inventory/crafting, validate capacity, duplicate handling, resource costs and failure states. For saves, version data and check missing/corrupt files.
5. Use `../../references/gameplay-quality.md` for tuning and `../../templates/acceptance-checks.md` for mechanical test cases.
6. Implement one complete mechanic at a time; test edge cases then integrate it into a level that demonstrates it.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
