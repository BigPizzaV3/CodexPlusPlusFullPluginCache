---
name: modernize-mcp-project
description: Review, refactor or upgrade an existing MCP server or MCP App without breaking its API, user workflows or security boundaries.
---

# Existing-project upgrade

1. Inspect repository state, uncommitted changes, transport, tool names/schemas, UI resources, current dependencies, tests and deployment assumptions. Do not overwrite the user's work.
2. Agree internally on scope from the user request; prefer the smallest compatible diff. Identify externally consumed tool names and schemas as contracts.
3. For legacy UI link metadata or transports, confirm current MCP/MCP Apps documentation, then migrate conservatively with backward compatibility where necessary.
4. Reproduce bugs first. Preserve read/write authorization and any approval semantics.
5. Delegate independent review only when real subagents are supported; avoid overlapping file changes.
6. Run baseline and post-change tests; compare failures, runtime behavior, tool discovery and UI rendering.
7. Deliver a readable change summary, compatibility/migration notes, results and limitations. Ask before disruptive operations such as publishing or pushing.

Read `../../references/protocol-and-ui.md`, `../../references/orchestration.md`, and `../../references/testing.md`.
