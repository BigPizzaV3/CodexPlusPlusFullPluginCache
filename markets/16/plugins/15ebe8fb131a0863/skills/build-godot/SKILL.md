---
name: build-godot
description: Create, extend, or debug a Godot 2D/3D project using GDScript and editor/headless verification where supported.
---

# Build Godot


1. Read `../../references/godot.md` and determine installed Godot version, project format, GDScript versus C#, target exports and available editor/templates.
2. Respect existing project.godot, scenes, resources and autoloads. Set a baseline and inspect signals, node paths and input actions before changing them.
3. Implement a minimal playable scene using appropriate CharacterBody2D/3D, input mapping, collisions, camera and a win/lose/restart mechanism. Avoid outdated APIs copied from Godot 3.
4. Model reusable scenes, resource references and signal connections explicitly. Do not hardcode fragile absolute node paths.
5. Run `godot --headless --path PROJECT --editor --quit` or version-appropriate import/parse commands when installed, then actual gameplay input tests if a display is available.
6. Only claim exports after necessary export templates/presets exist and commands complete successfully; web exports and C# availability must be checked separately.
7. Deliver the editable Godot project, controls, scene map, test output and any missing engine/export prerequisites.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
