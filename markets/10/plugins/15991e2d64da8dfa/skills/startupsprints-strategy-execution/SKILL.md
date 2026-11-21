---
name: startupsprints-strategy-execution
description: Use when a StartupSprints founder asks to advance a mission, continue a strategy or action, choose the next useful task, resolve a blocker, or work on a strategy without a specialist workflow.
---

# StartupSprints strategy execution

Advance the founder's mission by completing the next useful deliverable within the current strategy and constraints. User instructions and prior explicit approvals take precedence over recommendations.

Read [MCP workflow](references/mcp-workflow.md) before startup-specific work. Use [mission coordination](references/mission-coordination.md) for selection and specialist routing; [prompt examples](references/prompt-examples.md) provide reusable entry points.

## Inputs

Resolve the accessible startup, its confirmed mission and audience, selected action, current attempt, blockers, time/budget, founder preferences, existing work, and available capabilities. Ask only for missing facts or permissions that affect the next step; never ask the founder to type internal IDs that tools can resolve.

## Read → select → act → save → review

1. **Read:** Discover actual StartupSprints tools. Use `list_startups`; read `get_startup_profile`. For a requested strategy, find its returned `actionId` through `list_actions`. For “what next,” read `get_next_actions` and relevant `get_results`. Read `get_execution_brief` and `get_action_workspace` for the chosen action; read `get_distribution_kit` when needed. Keep `startupId` explicit on every startup-specific call with an all-startup connection.
2. **Select:** Relate the next deliverable to the mission and the uncertainty or prerequisite it resolves. Respect the founder's selected action and the server's eligibility. The focused plan has at most three actions; respect two actions in progress and three live experiments. Missing browser capability does not alter business eligibility.
3. **Act:** Produce the actual artifact, qualified evidence, repair, or operational measurement definition. Route to a relevant installed specialist when available; use the live brief and the local mission reference when it is absent. Complete independent preparation while a required decision or capability is pending. Confirm each authenticated service identity separately. Reuse a prior explicit confirmation and bounded approval; obtain any missing authorization before sending, publishing, booking, submitting, or spending.
4. **Save:** When requested or included in the task, merge current work and notes using live allowed fields. Send full replacements with current `workRevision`; reread and merge conflicts, then verify persistence. Reusable asset replacements require current `expectedUpdatedAt`. Preserve legacy findings. Saving a draft never starts or completes an experiment.
5. **Review:** Distinguish prepared, executed, and measured states. Compare observed evidence with the mission, success criteria, effort, window, and stop condition. Recommend one concrete next step. “Wrap up,” “done,” or “finish this task” is ambiguous: prepare a summary and clarify the intended completed/failed verdict before `record_action_result`. That call requires an explicit instruction to record actual outcomes, current `attemptNumber` and `outcomeRevision`, and only observed metrics in `measuredMetrics`. Unknown is not measured zero; never infer a usefulness vote.

## Output and fallback

Return the deliverable, why it advances the mission, evidence/uncertainty, actual progress, save status, and the smallest next action. If an integration is unavailable, use another permitted route or prepare work in chat/an authorized file; never claim unavailable access or persistence.
