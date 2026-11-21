---
name: select-engine
description: Select a suitable game engine and target architecture for a 2D, 3D, mobile, browser, narrative, or existing game idea.
---

# Select Engine


1. Determine primary target: browser link, Windows/macOS/Linux desktop, mobile package, console, VR, or narrative. Check performance target, internet access, rendering style, coding skills and existing technology.
2. Consult `../../references/engine-matrix.md` and `../../references/platform-and-input.md`.
3. Default to Phaser for 2D browser games; PlayCanvas Engine for code-first web 3D; Godot for standalone indie 2D/3D when editor is available; Ren'Py for visual novels; preserve existing Unity/Unreal projects when appropriate.
4. Do not conflate 2.5D or isometric camera with an engine; these can be achieved in multiple engines. For Unity/Unreal request large runtime budgets explicitly.
5. Check relevant official docs and installed engine/API versions before drafting imports or config. Don't hardcode unverified package versions or export names.
6. Explain export and platform limitations (e.g., device-specific tools, signatures, simulators, controller support, browser physics/performance, license obligations) where materially relevant.
7. Output a short decision record with selected engine, alternates, constraints and exact first-scene implementation plan. Continue development if requested.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
