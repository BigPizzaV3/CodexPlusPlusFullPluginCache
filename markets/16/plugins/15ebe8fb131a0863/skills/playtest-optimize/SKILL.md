---
name: playtest-optimize
description: Verify gameplay, usability, performance, bugs, and game feel through measured playtests and reproducible evidence.
---

# Playtest Optimize


1. Read `../../references/testing-and-evidence.md` and choose checks for actual platform and engine. Distinguish compile success, scene launch, interactive playtest and full release qualification.
2. Run real build/import tests, then verify player input, menu, progression, collision, score, win/lose, restart, save/load, pause, resize and asset/audio loading as relevant.
3. For 3D, review camera occlusion, clipping, collision/navigability, visual readability and frame performance under representative load.
4. Collect evidence with timestamps in logs or test artifacts as appropriate; no invented screenshots, benchmark frames or 'playtested' claims.
5. Profile performance before optimizing; prioritize frame-time spikes, asset bloat, overdraw, expensive physics and leaks. Report device/browser/hardware conditions for measurements.
6. Evaluate subjective fun and difficulty through actual human players; automated agents can assess controls and pacing proxies, not certify fun.
7. Apply a bounded fix-and-retest loop; fail the gate when essential mechanics are unverified or broken.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
