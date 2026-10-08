---
name: setup
description: One-time bootstrap for a new Castform project — install the Castform CLI and scaffold the Codex guide, skills, and starter environment. Run this before any other Castform skill.
---

# Set up Castform

The other Castform skills (`design-environment`, `generate-data`,
`verify-environment`, `launch-run`, `view-progress`, and `train-sft`) assume
the CLI is installed and the current project has been scaffolded.

1. Install or upgrade the CLI:

   ```bash
   uv tool install -U castform
   ```

2. Scaffold the current project for Codex:

   ```bash
   castform setup --agent codex
   ```

   This signs in through the browser when necessary, then writes `AGENTS.md`,
   `GETTING_STARTED.md`, the per-stage skills, and a runnable starter
   environment. It is safe to rerun because existing files are skipped unless
   `--force` is passed.

3. Confirm `castform --version` succeeds and the project contains `AGENTS.md`
   plus `.agents/skills/`.

Continue with the `design-environment` skill.
