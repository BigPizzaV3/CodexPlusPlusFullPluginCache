# Plugin Creator Prompt — LLM & Agent Builder Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `llm-agent-builder-copilot`
- Skill: `llm-agent-builder`
- Display name: `LLM & Agent Builder Copilot`
- Version: `0.1.0`
- Category: `Developer Tools`

## Architecture
Keep v0.1 skills-only.

Do **not** add:
- an MCP server;
- external connectors/apps;
- authentication;
- custom UI;
- live tool execution;
- agent deployment;
- automatic external side effects.

The skill may **design** MCP and agent systems, but the plugin itself does not need MCP.

## Required behavior
Preserve the existing workflow:
- decide whether the use case needs deterministic software, one model call, bounded tools, an explicit workflow, an autonomous agent, or multiple agents;
- choose the lowest reliable complexity level;
- define explicit tool input/output schemas, authorization, side effects, retries, idempotency, failures, and approval requirements;
- distinguish agents-as-tools from handoffs based on conversation/control needs;
- define bounded autonomy, stopping conditions, budgets, and recovery;
- distinguish turn context, session history, workflow state, durable preferences, long-term memory, and external source-of-truth state;
- use least privilege and deterministic authorization at tool/resource boundaries;
- require appropriate approval before consequential actions;
- design evals for outputs, tools, trajectories, approvals, external state, latency, and cost;
- use current official documentation for Agents SDK, MCP, model/tool APIs, guardrails, and version-sensitive platform behavior;
- never invent APIs, tools, permissions, model capabilities, SDK behavior, pricing, limits, or eval results.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding
- listing material
- five positive and three negative tests

## Validate
1. ZIP root and `plugin.json`.
2. `skills: "./skills/"`.
3. Skill frontmatter.
4. Combined plugin/skill identity <= 64 characters.
5. `agents/openai.yaml`.
6. Asset paths remain inside package and do not use `..`.
7. Branding assets are valid and square.
8. Public listing limits.
9. Starter prompts.
10. Submission tests.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
