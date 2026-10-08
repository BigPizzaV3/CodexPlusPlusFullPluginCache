# Research Notes — LLM & Agent Builder Copilot

Research date: 2026-09-23

## Recommended name

Keep **LLM & Agent Builder Copilot**.

It is concise, descriptive, consistent with the existing skill identity, and fits OpenAI's current 30-character public display-name limit.

Package: `llm-agent-builder-copilot`
Skill: `llm-agent-builder`

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The plugin's first-release value is deciding system complexity, designing tools, orchestration, state, MCP interfaces, guardrails, approvals, tracing, and evals. It does not need its own MCP server.

A future MCP-backed version would make sense only if the plugin itself needs controlled live actions such as:
- inspecting agent traces;
- querying eval runs;
- generating or validating tool schemas against a live service;
- reading deployed agent configuration;
- creating/updating agent workflows in an external platform.

## OpenAI plugin rules checked

Current public-directory validation includes:
- public display name: max 30 characters;
- short description: max 30 characters;
- long description: max 4,000 characters;
- capabilities: max 20, each max 120 characters;
- starter prompts: max 3, each max 128 characters;
- combined `plugin-name:skill-name`: max 64 characters;
- skill frontmatter must include `name` and `description`;
- skills-only ZIPs can omit remote-MCP requirements;
- bundled skills must pass safety/security scans;
- verified developer/business identity and policy attestations are required.

Sources:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Current OpenAI agent architecture

The current OpenAI Agents SDK describes a deliberately small set of primitives:
- agents with instructions/tools;
- agents as tools and handoffs;
- guardrails;
- sessions;
- human-in-the-loop controls;
- tracing.

The SDK uses the Responses API by default but is an orchestration layer. Current OpenAI guidance distinguishes:
- direct Responses API when the application should own a small tool/state loop;
- Agents SDK when managed tool execution, handoffs, sessions, guardrails, tracing, or agent loops materially reduce implementation burden.

The skill therefore keeps the existing complexity ladder:
0. deterministic software;
1. single LLM call;
2. LLM + bounded tools;
3. explicit workflow;
4. autonomous agent;
5. multi-agent system.

## Handoffs vs specialists-as-tools

Current Agents SDK guidance distinguishes:
- **agents as tools** when a manager should retain control, synthesize results, and own the final answer;
- **handoffs** when the selected specialist should become the active agent for the rest of the turn.

This maps directly to the existing agent-design framework and is now recorded in the source registry.

## Guardrail behavior

Current SDK documentation notes that agent-level input/output guardrails apply at workflow boundaries, while tool guardrails apply around guarded function-tool calls. Guardrail placement therefore depends on the actual risk boundary.

Blocking guardrails can be preferable when side effects or token/tool consumption must not begin before validation.

## Tracing

Current Agents SDK tracing records model generations, tools, handoffs, guardrails, and custom events. Tracing is enabled by default in normal supported environments, with documented exceptions such as Zero Data Retention configurations.

The skill should recommend tracing based on privacy/compliance constraints rather than assuming it is always available.

## MCP

The current stable TypeScript SDK line implements the 2026-07-28 MCP specification. The current protocol supports tools, resources, prompts, and extension-based functionality.

The Tasks extension supports asynchronous long-running `tools/call` operations with task status, polling, updates, and cancellation. Agent/MCP designs should verify host support rather than inventing bespoke asynchronous protocols.

MCP reference:
- https://modelcontextprotocol.io/
- https://ts.sdk.modelcontextprotocol.io/v2/
- https://tasks.extensions.modelcontextprotocol.io/

## Core design principles retained

1. Do not use an LLM when deterministic software is enough.
2. Do not use an agent when a bounded workflow is enough.
3. Do not use multi-agent architecture unless specialization, isolation, permissions, or parallelism justify it.
4. Treat model-selected tools as requests, not authorization.
5. Put authorization and validation at deterministic tool/resource boundaries.
6. Require appropriate approval before consequential external side effects.
7. Treat user, web, retrieved, and tool content as untrusted input.
8. Keep state ownership explicit rather than calling all persistence 'memory'.
9. Evaluate the full trajectory and external outcome, not only the final response.
10. Observe model calls, tools, handoffs, approvals, guardrails, retries, latency, cost, and final state.
