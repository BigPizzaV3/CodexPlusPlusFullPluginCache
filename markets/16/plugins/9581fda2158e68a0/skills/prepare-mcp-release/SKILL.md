---
name: prepare-mcp-release
description: Prepare a generated MCP server or MCP App for user-approved deployment and review, including manifests, endpoint verification, security, test evidence and release notes.
---
# Prepare releases, not imaginary publication

1. Distinguish releasing the **user's generated MCP project** from publishing MCP App Builder itself. Confirm the actual deployment target and user authorization.
2. Check current host/marketplace requirements from official docs; do not assume all MCP clients render Apps UI.
3. Require repeatable build/test commands, valid credentials flow, read/write permission review, tool schema/version compatibility and meaningful non-UI fallbacks.
4. If publishing a remote MCP server, require a real HTTPS Streamable HTTP endpoint and working authentication. Never use example.com or another dummy domain as a live endpoint.
5. Validate listing assets, privacy policy/terms when required, positive and negative review scenarios, and any demonstration recordings with actual URLs. Do not invent them.
6. Generate deployment scripts and rollback instructions where permitted. Don't perform production push/deploy/publish without the user's requested approval and host policy.
7. Return a PASS/FAIL/BLOCKED release report with exact remaining actions.

Read `../../references/release.md` and `../../references/testing.md`.
