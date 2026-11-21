---
name: debug-mcp-project
description: Diagnose and fix a broken MCP server, UI bridge, authentication, transport, tools/list, tools/call or resource-rendering issue from errors, logs or code.
---
# Diagnose MCP defects

1. Establish symptoms and environment: protocol version, installed SDK, transport, host, recent changes, failing command. Inspect actual files/logs if available.
2. Reproduce the failure before changing code; use Inspector/known client when possible. For remote transport, check endpoint reachability, auth and session lifecycle.
3. Identify the failing boundary: startup/initialize, schema validation, tool discovery/call, resource registry/read, Apps resource link, iframe bridge or external provider.
4. Fix the smallest cause while preserving stable tool names and input/output contracts. Look for SDK v1/v2 migration mismatch rather than guessing imports. Verify against current official docs.
5. Add a regression test, rerun the failing case and baseline. When reproduction is blocked, give reasoned diagnosis with clear uncertainty, not a fabricated fix.
6. Never print secrets or raw customer information from logs; don't deploy or push without approval.

Read `../../references/troubleshooting.md`, `../../references/protocol-and-ui.md`, and `../../references/testing.md`.
