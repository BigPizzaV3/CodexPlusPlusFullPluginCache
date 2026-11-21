---
name: status-snapshot
description: One-shot workspace status — open task counts, recent playbook runs, failing integrations. Use when the user asks for a status update, snapshot, or "how are things" across the workspace.
---
Give a status snapshot for the user's project (`whoami` first; use "$ARGUMENTS" as the project name if given).

Chain the reads in ONE `execute_batch` call rather than round-tripping:
1. `query_tasks` view="counts" grouped by status.
2. `get_workflow` view="runs" for the most recently used playbooks (from `list_workflows`).
3. `list_integrations` — flag any that are failing or disconnected.

Report as three short sections. Read-only.
