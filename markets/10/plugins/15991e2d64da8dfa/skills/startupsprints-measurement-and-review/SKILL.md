---
name: startupsprints-measurement-and-review
description: Use when a StartupSprints founder asks to define first value or activation, verify tracking, review actual experiment or cohort evidence, assess costs and retention, compare results with a mission, record outcomes, or wrap up an experiment.
---

# StartupSprints measurement and review

Make results interpretable and decide the next useful step toward the mission. Missing data, a measured zero and a proposed target carry different meanings.

Read [MCP workflow](references/mcp-workflow.md) before work. Follow [measurement review](references/measurement-review.md) for definitions, evidence and result-write checks; [prompt examples](references/prompt-examples.md) provide entry points.

## Inputs

Resolve startup/action and current attempt, mission qualification, success/stop criteria, cohort and source, observation window, event definitions, denominators, real measurements, prior attempts and actual time/cost. Ask only for missing information necessary for the requested decision or write.

## Read → select → act → save → review

1. **Read:** Resolve the startup with `list_startups` and returned `actionId` with `list_actions`; read `get_startup_profile`, `get_execution_brief`, `get_action_workspace`, and relevant `get_results`. Explicitly target `startupId` with all-startup grants. Discover available analytics/data capabilities. Confirm the intended identity separately before authenticated account-dependent analysis; reuse valid prior confirmation.
2. **Select:** Define what counts toward the mission and this strategy: first meaningful use, qualified conversation, retained member of a specific cohort, or a paid outcome. Choose a bounded test/check with real denominators and a window. Popularity, profiles, draft messages and scheduled calls do not become activations, sales or completed interviews.
3. **Act:** Inspect actual authorized sources and compute reproducible values. Separate observed/founder-reported data, assumptions and missing evidence. Verify tracking using a real test journey when authorized, exclude internal traffic and expose attribution gaps. Do not execute external tests, change instrumentation or incur costs beyond existing authorization. Compare attempts without double-counting people or outcomes.
4. **Save:** Preserve requested definitions, calculations and review drafts through full merged work/notes in the live template with current `workRevision`; reread/merge conflicts and verify. These saves leave the attempt open.
5. **Review:** Give a supported repeat/repair/stop recommendation with the mission implication. “Wrap up,” “finish,” “we're done,” or “save the review” does not by itself authorize an attempt-ending result write. First prepare the summary; if recording intent or completed/failed verdict is unclear, ask only that necessary clarification and continue independent review work. Call `record_action_result` only after explicit instruction to record actual outcomes and explicit completed/failed intent, rereading current `attemptNumber` and `outcomeRevision` immediately before it. It replaces this attempt's outcome and ends it. Require `measuredMetrics`; omit unknown metrics from this list. Required unknown numeric fields may need `0` placeholders, but only a zero listed in `measuredMetrics` is a measured zero. Reread and verify the result. Record feedback only from an explicit founder thumbs-up/down.

## Output and fallback

Return definitions, cohort/window, source-backed values and denominators, missing evidence, actual effort/cost, recommendation and save status. Without analytics, audit the measurement plan and supplied evidence; request the smallest relevant export or observation. Never turn unavailable data into zero or claim a completed experiment from preparation.
