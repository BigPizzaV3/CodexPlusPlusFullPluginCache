---
name: plan-mcp-app
description: Architect an MCP server or interactive MCP App from a user's idea, API concept, existing workflow, or product brief before writing implementation code.
---

# Plan an MCP project

1. Determine target users, meaningful actions, target hosts, auth needs, data sensitivity, read/write effects and desired user experience. Use a reasonable default when unspecified and document it.
2. Decide whether the task needs: (a) tool-only MCP, (b) tool-plus-UI MCP App, (c) both with graceful fallback. Never add UI merely for decoration.
3. Identify resource boundaries, typed tool operations, schemas, error cases, rate limits, pagination, idempotency and confirmation for consequential writes. Prefer fewer well-named tools over one generic `execute` tool.
4. Select TypeScript + official MCP SDK as new-project default; Python or existing stack when requested. Verify current SDK API signatures before coding; do not invent unverified imports.
5. Choose transport based on deployment: Streamable HTTP over HTTPS for remote use; stdio only for local hosts that support it. Identify session, auth, and hosting considerations.
6. If UI: sketch states (loading, data, empty, error, permission, retry), host capability negotiation and tool-only fallback. Read `../../references/protocol-and-ui.md` and `../../references/design-references.md`.
7. For substantial projects consider the specialists in `../../references/orchestration.md`. Use real subagents only when tools support them.
8. Propose smallest vertical slice and verification plan, then implement it when coding tools exist and user intent authorizes it.

Output: one-paragraph brief; architecture and trust boundaries; tool contract table; UI decision; project layout; milestones; tests and approval gates. Do not overplan a tiny server.
