---
name: asset-pipeline
description: Acquire, create, import, optimize, and track rights for sprites, textures, 3D models, animation, sounds, and game UI assets.
---

# Asset Pipeline


1. List every asset required for the vertical slice and its role, source type, desired style and required format.
2. Prefer user-supplied assets with usage rights; original generated assets where tools permit; verified CC0/MIT/commercially usable sources as appropriate. Verify each specific asset license and attribution; never assume a whole website uses one license.
3. Maintain `../../templates/asset-register.csv` including origin, asset URL, license, credit, file path, modifications and verification state. Record AI generation where applicable.
4. For sprites, check frame indexing and tile seams; for 3D, check scale, orientation, topology/rig/animation, collision and LODs; for audio, check format, clipping, loudness and loop points.
5. Use Blender or other supported editors only when available. Do not imply automatic rigging, sound synthesis or 3D model generation in a skills-only plugin.
6. Convert/compress to engine-supported assets without altering licenses or losing source. Place generated originals under appropriate asset subpaths.
7. Run import/build smoke checks and visually inspect representative assets before accepting them.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
