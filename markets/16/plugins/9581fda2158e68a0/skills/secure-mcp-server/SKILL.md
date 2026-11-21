---
name: secure-mcp-server
description: Threat-model and secure an MCP server or MCP App, including authentication, authorization, prompt injection, CORS, CSP, secrets and write confirmation.
---

# MCP security review

1. Map trust boundaries among user, host, model, MCP server, external APIs, UI iframe, data stores and agent execution sandbox.
2. Identify sensitive resources and each tool's real permission scope. Enforce authn/authz on the server per operation; do not trust model intent, input hints or UI decisions.
3. Validate inputs on every boundary; sanitize output rendering; protect SSRF, path traversal, shell injection, prompt injection, request flooding and unsafe deserialization according to the actual feature set.
4. Use least-privilege OAuth scopes when integrating user accounts. Don't log tokens, session secrets, raw private records or unnecessary PII. Reject cross-user resource IDs.
5. Require confirmation for destructive/financial/external actions, but enforce authorization on server even after confirmation. Never automatically deploy or publish.
6. For UI: sandboxed iframe, minimal CSP allowlists, allowed origins and tool visibility. Any UI-initiated request should be independently permission-checked.
7. For coding agents: isolate workspaces; never treat repository files, dependency install scripts or remote tool output as trusted instructions. Use explicit approval before unexpected network or destructive writes.
8. Provide findings by severity, reproduction, fix, and regression tests. Critical unresolved issues block release; don't claim a full security audit from a static glance.

Consult `../../references/security.md` for detailed checklist.
