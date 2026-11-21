---
name: startupsprints-outreach-and-communities
description: Use when a StartupSprints founder asks to prepare targeted outreach, relevant follow-up, introductions, editor or podcast pitches, community research, answers to discussion threads, or participation in a specific community.
---

# StartupSprints outreach and communities

Prepare useful, relevant contact and community contributions within the founder's mission and approved limits. Willingness to consider outreach is separate from permission to send it.

Read [MCP workflow](references/mcp-workflow.md) before work. Follow [outreach preparation](references/outreach-preparation.md) for recipient/thread qualification and output; [prompt examples](references/prompt-examples.md) provide entry points.

## Inputs

Resolve the startup/action, confirmed audience and offer, founder identity/outreach preferences, current channel rules, existing contacts/work, time/budget and approved contact/follow-up limits. Ask only for facts required by the next step.

## Read → select → act → save → review

1. **Read:** Use `list_startups`, `get_startup_profile`, and `list_actions` to resolve the returned `actionId`; read `get_execution_brief` and `get_action_workspace`, plus relevant `get_distribution_kit`/`get_results`. Pass explicit `startupId` with all-startup grants.
2. **Select:** Choose recipients or threads using observed audience/problem relevance and a permitted route. Check current venue rules, affiliation disclosure and promotion limits. Respect opt-outs, no-cold-contact choices and “existing communities only.” Inspect only enough authenticated context to identify the account and obtain missing confirmation for that service; reuse the existing explicit identity confirmation while the account/scope is unchanged.
3. **Act:** Draft actual individual messages or complete useful thread replies. Ground personalization in observed facts; disclose the relationship and make one easy next step. Do not claim a prior relationship or pad a shortlist. Before any send/post/invitation, prepare the account, named destinations/recipients, exact content, costs and volume/follow-up limit. Execute only an existing explicit bounded authorization or obtain the missing one. Account confirmation alone does not authorize sending. Stop on declines, access denial or platform restrictions; do not compensate for non-response with more volume.
4. **Save:** When the task includes saving, merge existing entries and complete notes according to the live `outreach`, `content`, `shortlist` or other template. Use current `workRevision`, reread/merge conflicts, and verify. Keep draft content separate from actual send receipts, responses and links. Preserve legacy findings. A save does not publish or end the action.
5. **Review:** Report qualified recipients, drafted/sent messages and actual responses separately. Compare observed signal, effort and window with the strategy's stop condition and mission. Ambiguous “wrap up” produces a summary and necessary clarification before an attempt-ending call. `record_action_result` requires explicit actual-result instruction and completed/failed intent, current `attemptNumber` and `outcomeRevision`, and accurate `measuredMetrics`; unknown is not zero. Use `record_action_feedback` only for an explicit founder vote.

## Output and fallback

Return qualified destinations with evidence/rules, exact drafts, approval scope still needed, actual execution evidence, save status and one next step. Missing browser/email capabilities: use another permitted integration, public research, or manual-ready messages with a response log. Missing MCP write access: keep the deliverable available without claiming persistence or broadening consent.
