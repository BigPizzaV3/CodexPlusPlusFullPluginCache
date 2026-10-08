---
name: team30-company-os
description: "Use TEAM 30 to select the right specialist role, scope a project, create a verified plan, or check whether a proposed action needs explicit user approval. Trigger for strategy, project planning, role routing, approval gates, and coordinated execution. Do not trigger for simple factual questions."
---

# TEAM 30 — AI Company OS

Use TEAM 30 as a read-only planning and routing layer.

## Workflow

1. For a concrete task, call `team30_route_task` with the user's exact goal, project, and constraints.
2. If the request is a multi-step project, call `team30_build_project_plan` after routing.
3. Before any proposed external communication, payment, deletion, permission change, public deployment, submission, or publication, call `team30_check_action_gate`.
4. State the selected role, scope lock, evidence needed, and next safe action in plain language.

## Boundaries

- Tool results are plans, not proof that an action happened.
- Never claim an external action, test, deployment, or publication without current evidence.
- TEAM 30 tools in this public version do not send messages, spend money, delete data, publish, or change external systems.
- Ask for explicit user approval at the moment a high-risk action is ready.
- Do not request passwords, API keys, payment information, or private access tokens.
