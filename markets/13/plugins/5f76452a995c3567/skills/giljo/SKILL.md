---
name: giljo
description: "Giljo HQ dashboard -- create, read, and update projects and tasks (and chains). Loads the server-side routing guide, then acts."
bundle_version: 1.1.21
---

# $giljo -- Giljo HQ commands

This command is a thin entry point to Giljo HQ. Do this every time:

1. Call the `get_giljo_guide` tool (no arguments; your MCP client may expose it
   under a prefix, e.g. `mcp__<server>__get_giljo_guide` -- use the name your
   harness lists).
2. Follow what it returns -- it is the single source of truth for:
   - project-vs-task routing (create_project vs create_task),
   - the chain convention (one shared series_number + a/b/c suffixes for ordered,
     dependent steps),
   - the mandatory `Edition Scope: CE | SaaS | Both` line on every project,
   - read-vs-write routing (reads: list_projects / list_tasks / get_context;
     writes: create_* / update_*; never pass tenant_key; an active product is required),
   - the staging -> human-gate -> implement lifecycle.
3. Then carry out the user's request with the Giljo HQ tools.

Giljo HQ agent templates are never installed as files: every spawned agent receives its full profile from the server when its job starts.

## Skills bundle freshness (check once per session)

This skill was generated from Giljo HQ skills bundle `bundle_version: 1.1.21`.
Any Giljo HQ tool response includes `_meta.skills_version` (the version the server currently ships). The FIRST time in a chat session that you call a Giljo HQ tool, compare that `_meta.skills_version` to this file's `bundle_version`. If the server's version is newer, tell the user once: "Your Giljo HQ skills are out of date — run /giljo_setup to update." Do not repeat this notice again in the same session, and never block the user's actual request on it.
