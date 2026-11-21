---
name: audio-animation
description: Add coherent game animation, audio feedback and ambience with asset provenance, responsiveness and accessible settings.
---

# Audio Animation


1. Identify every interaction that needs feedback (input accepted, impact, collectible, success/failure, warning, menu navigation).
2. Use a consistent animation and audio language from `../../references/art-direction.md` and `../../references/audio-and-animation.md`.
3. Prefer original generated/synthesized sound effects or explicitly licensed clips. Do not copy recognizable commercial game audio or copyrighted soundtrack fragments.
4. Separate gameplay state from audio/animation state; handle pause/resume, mute, repeated triggers, loading delays, frame timing and effects prioritization.
5. On browser, account for autoplay restrictions and first user gesture. Include volume controls and reduced-motion alternatives where relevant.
6. Validate files decode in the actual engine and events play at expected times; do not mark auditory QA passed without hearing or instrumented playback.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
