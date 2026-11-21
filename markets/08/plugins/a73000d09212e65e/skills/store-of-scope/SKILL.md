---
name: store-of-scope
description: Use Store of Scope to coordinate a revisioned newsletter-reading workflow after separately authorized host capabilities have read Gmail or produced external artifacts and receipts.
---

# Store of Scope

<!-- noodle-app-package source:fb3c2121eb4fd8990d33245e3eb6f1a042642ee3fbeeb7aa0a875d031a447f9c surface:0f151d604ce3e849494581c52d4beafb5611c9079450a9a816f0474d49c9b954 -->

## When to use this product
- The user wants to configure, inspect, run, pause, recover, or retire Store of Scope.
- The user wants to reconcile normalized newsletter metadata or commit validated workflow receipts.
- The user wants a reviewable three-week plan for unread newsletters.

## Workflows

### Configure a Store of Scope workspace

Create or update validated caller-scoped configuration without silently activating delivery.

1. `tool:get_store_of_scope_status` — Read current revisions and preserve existing state before proposing changes. (read-only; idempotent)
2. `tool:save_workspace_config` — Use the exact current configuration revision after the user reviews senders, schedule, delivery, and approval settings. (write; confirmation required)

### Run daily orchestration

Calculate due branches and acquire one idempotent run before external work begins.

1. `tool:get_store_of_scope_status` — Stop if the workspace is unconfigured, paused, retired, or already has a pending run. (read-only; idempotent)
2. `tool:calculate_due_work` — Supply the date and weekday already resolved in the configured workspace timezone; return cleanly on no_action_due. (read-only; idempotent)
3. `tool:begin_workflow_run` — Use a stable run id and idempotency key for each due branch and local date. (write)

### Commit a validated reading edition

Reconcile archive metadata and commit an edition only after external validation and delivery evidence exist.

1. `tool:reconcile_archive_index` — Pass bounded normalized metadata from an authorized external Gmail read; never pass message bodies, MIME content, or credentials. (write)
2. `tool:commit_workflow_run` — Commit only a passed artifact receipt and, when delivery is enabled, the matching provider delivery receipt. (write)

### Commit a Friday archive refresh

Preserve historical archive ids and commit a validated workbook refresh.

1. `tool:reconcile_archive_index` — A smaller later Gmail result never authorizes deletion of historical archive ids. (write)
2. `tool:commit_workflow_run` — Commit only after workbook validation passes; attach delivery evidence only if confirmation was sent. (write)

### Plan unread newsletters

Propose a deterministic plan first and persist only the exact user-approved digest.

1. `tool:propose_content_plan` — Treat the result as read-only; show dates and counts for review. (read-only; idempotent)
2. `tool:approve_content_plan` — Call only after explicit approval of the exact proposal digest. (write; confirmation required)

### Recover or pause automation

Inspect the recorded state before retrying and give the user a safe stop control.

1. `tool:get_store_of_scope_status` — Use pending and recent run receipts to decide whether to retry, reconcile, or stop. (read-only; idempotent)
2. `tool:set_automation_paused` — Require confirmation and the current configuration revision. (write; confirmation required)

### Retire Store of Scope state

Make all Store of Scope state handles permanently read-only after explicit confirmation.

1. `tool:get_store_of_scope_status` — Show the user the exact current state revisions and explain that retirement is terminal. (read-only; idempotent)
2. `tool:retire_workspace` — Call only after explicit confirmation using all four exact revisions. (write; destructive; confirmation required)

## Boundaries
- Store of Scope does not authorize Google accounts. Use external Gmail and optional Calendar capabilities only after their own connection and permission checks.
- Never store Google credentials, raw message bodies, MIME content, attachment bytes, or full recipient addresses in workflow receipts.
- A deployed MCP does not prove that Gmail, Calendar, workbook or PDF rendering, delivery, or scheduled automation is active.
- Do not claim artifact validation or delivery success without the corresponding external receipt.
- Obtain explicit approval for initial ingestion, first delivery, future unattended delivery, content-plan writes, and workspace retirement.
- On a revision conflict, reread status and reconcile; never overwrite newer state silently.

## Examples
- “Set up Store of Scope.” — use `configure_workspace`.
- “Run today's newsletter workflow.” — use `run_daily_orchestration`.
- “Plan three weeks of unread newsletters.” — use `plan_unread_content`.
- “Pause Store of Scope.” — use `recover_or_pause`.

## MCP surface

[Read the MCP surface reference.](references/mcp-surface.md)
