---
name: build-unity-unreal
description: Work on an existing or explicitly requested Unity or Unreal game project with correct editor version, scripting patterns, and packaging limits.
---

# Build Unity Unreal


1. Determine Unity versus Unreal and inspect actual project metadata, editor version, plugins, packages and source-control status. These are distinct engines; never silently migrate.
2. Read `../../references/unity-unreal.md` and official versioned docs. For Unity, preserve C# assemblies, scenes and serialization; for Unreal, preserve Blueprints, C++ modules, project settings and cooked assets.
3. Scope a small feature/bug fix before new content generation. Request missing project assets or toolchain details only when blocking.
4. Use editor/build/automation tooling only if installed and authorized. Avoid invoking expensive graphical/cook processes or downloading huge SDKs without approval.
5. Conduct compile/import tests and gameplay testing when possible; distinguish script compilation from actual editor-level or packaged-game verification.
6. Respect commercial license and marketplace content restrictions, including third-party asset terms. Return meaningful source diffs, commands and blockers.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
