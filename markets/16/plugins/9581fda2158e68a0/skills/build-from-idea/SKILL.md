---
name: build-from-idea
description: Build a complete MCP server or interactive MCP App from a natural-language idea or API brief, including source, real tests, and a runnable handoff where tools permit.
---
# Full build: idea to MCP App

Use when the user says 'build', 'create', 'make', 'implement', 'ship a prototype', or wants an actual MCP application. Do not stop after architecture when code execution is available.

## Phase A — understand and choose
1. Identify the primary workflow, target MCP hosts, data source, read/write effects and need for an interactive UI. Prefer the smallest complete vertical slice.
2. Check available filesystem/terminal/browser/subagent tools; read `../../references/execution-model.md`. If no code tools exist, provide a complete handoff package or implementable code in the available output medium, without claiming running results.
3. Consult `../plan-mcp-app/SKILL.md`, `../design-mcp-tools/SKILL.md`; define tools with schema, auth, output and explicit failure cases. Avoid a generic `execute` tool.
4. For new TypeScript projects, check the **v2** MCP TypeScript SDK documentation first (`@modelcontextprotocol/server`, v2 is current as of late 2026). For MCP Apps, check the current `@modelcontextprotocol/ext-apps` docs and registration helpers. Use Python or existing project tech if more appropriate.

## Phase B — build
5. Create real source files, dependency manifest, README, sample environment file without secrets, test fixtures and scripts. Implement a real underlying operation; don't create inert demos pretending to be integrated.
6. Include tool-only textual/structured outputs first. Add an MCP Apps `ui://` resource and host bridge **only if it materially improves user interaction**. Reference `../build-mcp-ui/SKILL.md` for binding and accessible states.
7. Consult `../../references/design-references.md` for product-specific visual direction. Use references for patterns; do not paste copyrighted code/assets without rights.
8. Apply auth/authorization and failure handling before finalizing. Read `../secure-mcp-server/SKILL.md` when connecting real user data, external actions or any privileged write.
9. Use `../orchestrate-agents/SKILL.md` only when genuine subagent facilities are present and useful. Otherwise complete the same steps sequentially, without imaginary roles or reports.

## Phase C — verify and deliver
10. Run real typecheck/build, unit/integration tests and MCP protocol calls with an actual client/Inspector where possible; render UI in a real compatible host/harness if possible. Do not mark unavailable tests as PASS.
11. Independently inspect security and design quality, fix bounded findings and rerun tests; see `../test-mcp-project/SKILL.md` and `../review-mcp-design/SKILL.md`.
12. Deliver source/files, how to run, tool contract table, test evidence, known limitations and any approvals needed. Do not auto-push/publish/deploy.

**Completion:** at least one useful tool behaves as specified in a real test, or explicitly disclose why environment prevented this. Never describe a skeleton as a deployed working integration.
