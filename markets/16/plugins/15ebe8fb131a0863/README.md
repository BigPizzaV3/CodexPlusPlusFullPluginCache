# Design Game Studio — Tekris Labs game-building plugin

**Subtitle:** Create games from ideas.

**Tagline:** Turn ideas into playable games.

Design Game Studio is a **skills-only** plugin for ChatGPT Work and Codex-compatible hosts. It guides and, where real coding tools permit, performs 2D/3D game development, game design, art and asset workflows, playtesting, debugging, and release handoffs. It is **not** an independent cloud game engine, asset generation service, hosting platform, or managed multi-agent backend.

## Start here

- Give a game idea -> `skills/game-from-idea/SKILL.md`.
- Start with unknown platform/engine -> `skills/select-engine/SKILL.md`.
- Phaser 2D web -> `skills/build-2d-phaser/SKILL.md`.
- PlayCanvas 3D web -> `skills/build-3d-playcanvas/SKILL.md`.
- Godot / Unity / Unreal / Ren'Py -> dedicated skills.
- Existing repo -> `skills/improve-existing-game/SKILL.md` or `skills/debug-game/SKILL.md`.
- Tests -> `skills/playtest-optimize/SKILL.md`.

## Scope and limitations

The host must supply repository/filesystem/terminal/browser or engine tools for real builds. The plugin instructions alone do not execute a game engine. When subagents are available the orchestrator can delegate; otherwise it should use a transparent sequential workflow. No paid service, build, deployment, store submission, or destructive change occurs without user authorization. Asset rights, provider terms and platform build prerequisites must be respected.

## Packaging

- Portable root `plugin.json` (canonical).
- `.codex-plugin/plugin.json` is a compatibility fallback.
- `skills/` contains goal-triggered, focused workflows; `references/` provides engine/game-specific practices.
- `templates/` provides briefs, gameplay checks, asset licensing and handoff documents.
- `benchmarks/` describes unexecuted integration tests.
- `scripts/validate_package.py` validates package structure and metadata.

**Publisher:** Tekris Labs. **Support:** https://tekrislabs.com/contact

## Test locally

`python3 scripts/validate_package.py`

This only proves package structure. Run the benchmark suite in a real coding/game-engine environment before claiming gameplay verification.
