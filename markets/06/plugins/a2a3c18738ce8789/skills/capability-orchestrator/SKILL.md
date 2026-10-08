---
name: capability-orchestrator
description: Use at the start of non-trivial user requests when the task may benefit from installed skills, plugins, connected apps, connectors, MCP tools, or native specialist capabilities. Determine the user's intent, select the smallest effective set of relevant capabilities, and delegate each subtask to the most specialized available capability before attempting the work generically.
---

# Capability Orchestrator

Use this skill as a control plane. Do not replace specialist capabilities
with generic reasoning when a suitable specialist is available.

For trivial social conversation, acknowledgements, or simple questions
that clearly need no specialist capability, do not run the full routing workflow.

## Hard invariants

- Prefer a direct specialist over a generic router.
- Use the smallest effective set of capabilities.
- Never delegate to capability-orchestrator.
- Maximum routing depth: 4.
- Do not load unrelated capability context.
- Do not claim a capability ran unless it was actually invoked.
- Respect user overrides unless they conflict with safety or platform rules.
- Installation, connection, authentication, and permission grants remain
  explicit user actions when the host requires them.

## Understand intent

Identify the requested outcome, inputs, constraints, domain, freshness
needs, account access needs, file operations, and expected artifact.

## Decide whether to decompose

Keep the request direct when one specialist can complete it.
Decompose only when independent or sequential subtasks require different
capabilities.

Use one of these shapes:
- Direct
- Complementary
- Sequential
- Discovery
- Native fallback

## Inspect available capabilities

Inspect capabilities already available in the current environment first.
Consider specialist skills, plugins, connected apps, connectors, MCP tools,
native tools, generic routers, and direct model reasoning.

If no suitable capability is available and capability discovery exists,
follow `references/discovery-policy.md`.

## Select the route

Apply `references/routing-policy.md`.

User overrides:
- "do not use plugins" disables plugin delegation.
- "use only X" restricts delegation to X when X can safely perform the task.
- An explicitly requested valid capability has priority over automatic
  selection unless a higher-priority platform or safety rule prevents it.

## Delegate with minimal context

For every delegated subtask, follow `references/delegation-contract.md`.
Send only the objective, relevant context, constraints, expected output,
and dependencies required by that specialist.

## Synthesize and report

Combine complementary results only as much as needed to satisfy the user.
Do not rewrite specialist output merely to make the orchestrator appear
active.

At the end, report only capabilities actually invoked. If none were
invoked, report that none were used.

For host-specific behavior, follow `references/surface-adaptation.md`.
