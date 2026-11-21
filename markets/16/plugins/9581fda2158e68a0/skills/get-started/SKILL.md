---
name: get-started
description: Use MCP App Builder for a new MCP tool, interactive MCP App, API integration, or existing MCP project. Route the user's intent into an actual implementation workflow.
---
# MCP App Builder — entry point

Use this skill when the user has an MCP App idea, asks how to build one, supplies an API or repo, or asks what this plugin can do. Do not treat generic web/mobile app requests as MCP projects; explain the distinction and defer to an appropriate tool or plugin.

1. Establish the goal, main user action, available source (idea, API docs, repository, screenshots), target host and write effects. Do not ask a long questionnaire. If one fact blocks work, ask only that question; otherwise use transparent defaults.
2. Choose the actual output: (a) tool-only MCP server, (b) MCP App with UI, or (c) modernizing an existing project. Never force a UI where it adds no value.
3. Inspect the host's real coding, filesystem, browser, build, terminal and subagent tools. Only promise operations supported by present tools. When files can be written, write source and run tests rather than stopping at a plan.
4. Route to `build-from-idea` for full implementation, `plan-mcp-app` for architecture-only, `modernize-mcp-project` or `debug-mcp-project` for existing code, `build-mcp-ui` for UI work, and `test-mcp-project` for verification. Load focused skills as required.
5. Read `../../references/execution-model.md` and `../../references/orchestration.md` before delegating. Specialist roles are not independent agents unless the environment executes them.
6. Always deliver a user-visible summary with artifacts, exactly what was tested, failures and remaining steps. Never claim deployment, execution, security certification or host integration without evidence.

For complete builds, read `../build-from-idea/SKILL.md` next and begin implementation. Ask permission for deployments, paid services, destructive operations or sensitive access when required.
