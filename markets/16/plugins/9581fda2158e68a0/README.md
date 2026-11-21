# Build MCP Apps & Agents — OpenAI plugin v1.0.4

A complete **skills-driven** plugin for building, reviewing and improving Model Context Protocol servers and interactive MCP Apps. It is a portable root-manifest package intended for ChatGPT Work and Codex hosts that provide coding and optional real subagent tools.

## User workflows
- Give an idea → `skills/build-from-idea/SKILL.md` (full build).
- Plan architecture → `skills/plan-mcp-app/SKILL.md`.
- Design MCP tools → `skills/design-mcp-tools/SKILL.md`.
- Build a server → `skills/build-mcp-server/SKILL.md`.
- Add interactive UI → `skills/build-mcp-ui/SKILL.md`.
- Debug/modernize an existing project → `skills/debug-mcp-project/` or `skills/modernize-mcp-project/`.
- Improve visual quality → `skills/review-mcp-design/`.
- Secure/test/release → corresponding skills.
- Delegate via real agents → `skills/orchestrate-agents/` only when host provides them.

## What the package includes
Portable `plugin.json`, 13 focused skills, curated source and SDK references, reusable templates, plugin metadata/icon, offline package checks and prompt-level acceptance scenarios. **No bundled secrets and no fictitious MCP server URL.**

## How it executes
Host tools, not these markdown files, perform filesystem changes, actual builds, runtime tests and deployment. Native subagents can collaborate when exposed by the host; the plugin otherwise uses serial roles. The plugin does not itself provide a hosted build service or connected GitHub credentials. See `references/execution-model.md`.

## Publishing
The OpenAI Plugin Creator integration can update an owned private plugin. Public directory approval is a separate developer-submission process. See `references/release.md`.

## Validation
Run `python3 scripts/validate_package.py` from the plugin root. Its package checks do **not** establish runtime success of every skill in ChatGPT or Codex. Use `benchmarks/cases.json` for integrated acceptance tests once installed.
