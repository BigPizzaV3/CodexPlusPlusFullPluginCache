---
name: build-mcp-server
description: Implement and test a real MCP server exposing tools and resources over a suitable transport, using current official SDKs and secure integration patterns.
---
# Implement MCP server

1. Inspect existing code and versions; preserve the user's stack unless instructed otherwise. For new TypeScript server use official MCP SDK v2 (`@modelcontextprotocol/server`) as current default; confirm APIs in current docs. For Python projects use the current Python SDK.
2. Design contracts using `../design-mcp-tools/SKILL.md`. Each registered tool must perform its named operation, validate inputs and return useful structured/text results; no fake data masquerading as live.
3. Choose stdio for explicitly local spawned integrations and Streamable HTTP over HTTPS for remote hosting; implement the correct request/session lifecycle. Never assume an exposed dev HTTP URL is production hosted.
4. If external accounts are involved, implement OAuth/audience/scope as needed; protect credentials and check authorization per tool action. Use bounded network/file access.
5. Generate package/install instructions, environment template without secrets and code to reproduce data and outputs. Do not silently execute risky setup or external calls.
6. Run available typecheck/build, tests and real tools/list and tools/call checks. Use `../test-mcp-project/SKILL.md`. If unavailable, distinguish code written from code tested.
7. Add UI with `../build-mcp-ui/SKILL.md` only when useful, including tool-only fallback.

Consult current https://ts.sdk.modelcontextprotocol.io/v2/ and `../../references/protocol-and-ui.md` before choosing concrete imports.
