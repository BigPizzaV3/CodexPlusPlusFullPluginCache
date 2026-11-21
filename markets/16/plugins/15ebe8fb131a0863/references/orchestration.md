# Real multi-agent coordination

Role assignment is not independent computation. Only claim separate agents if the host exposes actual subagent tools or a configured authorized remote backend.

Game Director owns scope, integration, decisions and user approvals. Optional specialists: Gameplay Designer, Engine Architect, Art Director, Mechanics Implementer, Level Designer, Audio Designer, QA/Playtester and Release Engineer.

For a small game, 1-3 roles are enough; for larger work delegate genuinely independent research or code ownership. Freeze shared contracts (scenes, asset names, interfaces) before parallel editing. Avoid same-file conflicts with branches/worktrees or nonoverlapping ownership. QA and security review must inspect actual artifacts read-only, not just worker summaries.

Each handoff: scope, tool access, worktree/file ownership, artifacts, decisions, exact commands executed, observed output, blockers and next action. Apply bounded loops and resource/cost budgets.

When subagents unavailable, use sequential checkpoints and report no independent agents ran.
