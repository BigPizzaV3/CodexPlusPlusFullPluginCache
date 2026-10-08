---
name: vana-run
description: Continue a saved protocol. Use when the user asks for the next step, records progress, reviews progress, or changes an active protocol.
---

# Protocol runner

Protocols persist as files in the user's Data:

```
protocols/<slug>/protocol.md          one protocol: seven H1 sections
protocols/<slug>/log/<YYYY-MM-DD>.md  one file per day, time-headed entries
```

The user's Data is behind the Vana MCP server. Read a protocol or log with its `read_file` tool, save with `write_file`, and list or search with `run_command`.

The saved protocol is the source of truth. Read it before you choose the next action, record progress, or review progress. Use the protocol's own steps, names, units, adaptations, and review rules.

When the user names a protocol loosely, list `protocols/` and match the slug. If more than one protocol matches, ask which one they mean.

A run is the work completed while following a protocol. Its log records enough state to determine progress and the next action.

## Continue a protocol

1. Read `protocol.md` and the most recent log entries.
2. Find the next unfinished action from `# Protocol` and the recorded progress.
3. Apply a relevant rule from `# Adaptation` when the user's context calls for one. Name the rule you applied.
4. Give the user the complete next action with every detail the protocol specifies.

This branch is complete when the user can act without opening the saved file.

## Record progress

1. Read [Log format](references/log-format.md).
2. Take the fields and units from `# Tracking & Review`. Ask a question only when a missing value would change the saved entry or the next action.
3. Add the entry to `protocols/<slug>/log/<YYYY-MM-DD>.md` for the date when the work happened. Read an existing file first because `write_file` replaces the whole file.
4. Confirm what you saved in one line.

This branch is complete when the log preserves the user's report in the shape defined by the protocol.

## Review progress

1. Read the log span the review covers.
2. Compare the entries with the goal and review rules in `# Tracking & Review`.
3. State what is complete, what remains, and any pattern supported by the entries.
4. End with the next action. When the protocol defines review choices, use one of those choices and cite the log entries that support it.

This branch is complete when the user knows their current progress and what to do next.

## Change the protocol

Gather the requested change and the relevant progress from the log. Use `/vana-create` to revise the saved protocol. Replace `protocol.md` and preserve its log.
