---
name: build-mobile-game
description: Adapt or build a touch-first game for Android or iOS with correct aspect ratios, performance, platform controls, and export guidance.
---

# Build Mobile Game


1. Determine whether user wants a browser-playable mobile game, installable Android APK/AAB, or signed iOS app; these are not interchangeable.
2. Read `../../references/platform-and-input.md` and choose Godot or Unity for native-oriented builds, or Phaser/PlayCanvas for mobile web when justified.
3. Design touch targets, multi-touch gestures, on-screen controls, safe areas, portrait/landscape, pause/resume, interruptions and accessibility.
4. Define performance/memory and battery budgets for target devices. Avoid dense 3D rendering on devices without a suitable GPU budget.
5. Verify graphics, audio, assets and input on device/simulator only when available; list any untested devices honestly.
6. Packaging requires platform-specific export templates/signing credentials and developer accounts. Ask for approval before external store submission or credentials.
7. Return portable source and valid local build/export instructions; never claim App Store/Play Store readiness without real device and policy checks.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
