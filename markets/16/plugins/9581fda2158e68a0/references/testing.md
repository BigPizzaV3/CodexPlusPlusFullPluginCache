# Evidence-based MCP tests

| Layer | Evidence expected |
|---|---|
| Build | dependency install, typecheck, build, unit test command output |
| MCP | initialize, capabilities, tools/list, tools/call and resources/read (where relevant) |
| Contracts | valid/invalid schemas, empty data, pagination, timeout, error envelope |
| Security | forbidden object/tenant, bad auth/scope, unauthorized write, input abuse |
| UI | resource URI + MIME, host bridge, real tool calls, keyboard/focus, responsive/empty/loading/error |
| Compatibility | tool-only fallback for host without UI and known client versions |
| Release | real endpoint reachability only if publishing, rollback notes, no secret logs |

**Status**: PASS = actual observed result; FAIL = actual observed defect; NOT RUN = not attempted; BLOCKED = environmental requirement missing. Code review, static lint, mocked screenshots and hypothetical tests must not be labeled PASS for end-to-end functionality.

Write a report based on `templates/evidence-report.md`. MCP Inspector: https://github.com/modelcontextprotocol/inspector
