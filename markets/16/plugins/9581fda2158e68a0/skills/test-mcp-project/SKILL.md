---
name: test-mcp-project
description: Validate an MCP server or MCP App with build checks, protocol-level tests, authorization negatives, UI lifecycle checks and honest evidence reporting.
---

# MCP verification

1. Identify intended contracts, transport, auth and clients. List which parts can be tested in the current environment.
2. Run relevant real commands where tools permit: install/build/typecheck/lint/unit tests, MCP Inspector server initialization, tools/list, resources/list or resources/read, tools/call with valid and invalid parameters.
3. Test empty results, auth failures, forbidden IDs, input limits, rate limiting, provider outages, timeouts, retries and confirmation gates. Include negative tests for every privileged write.
4. For MCP Apps: validate `ui://` resource existence, MIME type, `_meta.ui.resourceUri` linkage, CSP, bridge initialization and callbacks, rendering, focus/keyboard, dark mode if supported and fallback without UI capability.
5. Preserve executable commands, environment, observed output, exceptions and artifacts; independently evaluate claimed agent results.
6. Classify each check as PASS, FAIL, NOT RUN or BLOCKED. Never infer pass from code review, mocked UI or an unrun test script.
7. Fix failures and rerun targeted tests. Limit retries, document unrelated pre-existing failures, don't silently change a baseline or delete tests.
8. Output a concise evidence table and remaining blockers. See `../../templates/evidence-report.md` and `../../references/testing.md`.
