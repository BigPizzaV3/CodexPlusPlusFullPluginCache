---
name: startupsprints-customer-discovery
description: Use when a StartupSprints founder asks to find people who recently had a problem, recruit interview participants, prepare problem or pricing interviews, observe onboarding, investigate switching or lost signups, or analyze actual customer research notes.
---

# StartupSprints customer discovery

Create supported recruitment work and learn from real behavior toward the founder's mission. A shortlist, invitation, scheduled call, and completed interview are separate states.

Read [MCP workflow](references/mcp-workflow.md) before work and [problem interviews](references/problem-interviews.md) for strategy 11, `problem-interviews`. That reference also explains adjacent discovery adaptations. Use [prompt examples](references/prompt-examples.md) as starting points.

## Inputs

Use the confirmed audience/problem, action, hands-on decision, effort/budget, outreach limits, current work and available tools. Ask for a missing fact only when it changes qualification or the next dependent action.

## Read → select → act → save → review

1. **Read:** Discover tools; resolve the startup through `list_startups`, then the returned action through `list_actions`. Read `get_startup_profile`, `get_execution_brief`, and `get_action_workspace`; inspect prior attempts and legacy findings. Use explicit `startupId` for all-startup grants. Live brief and field definitions override reference examples.
2. **Select:** Define a recruitment screen for audience context, a recent real problem, current workaround, and disqualifiers. Respect hands-on, cold-outreach, public-identity and community constraints. Choose the venue because the audience uses it. Prefer available ChatGPT Chrome research when useful; respect the founder's chosen browser. Confirm the actual service/account separately before authenticated research, preserving prior explicit confirmation.
3. **Act:** Find up to five qualified candidates within the effort limit. Record sources, observation date, fit evidence, uncertainty, and a permitted route. Return fewer when evidence is insufficient. Discussion authors without a verified route are audience evidence, not recruitable candidates. Draft exact individual invitations and a neutral last-occurrence interview guide. Present account, recipients, content, cost and contact/follow-up limit for any missing send authorization; reuse prior approval only within its bounds. Founder participation remains required where the brief requires it. Analyze only real notes, with participant references, supported patterns and contradictions.
4. **Save:** When authorized by the task, merge the current `research` work and notes; send the complete replacement with current `workRevision`, reread/merge on conflict, and verify. Candidate identity, source/date/fit/uncertainty belong in `participant`; invitation/route in `recommendation`; keep `status: draft` and interview observations empty before an interview. Use only live allowed keys; preserve old findings and entries.
5. **Review:** Report recruitment, scheduled calls and actual interviews separately. Five candidates do not meet a five-interview target. Do not invent three patterns to meet a goal. On ambiguous “wrap up,” prepare a summary and ask only the necessary verdict/outcome clarification. Never call `record_action_result` until the founder explicitly requests recording actual outcomes and supplies or confirms completed/failed intent. Reread current `attemptNumber`/`outcomeRevision`; list only measured metrics in `measuredMetrics`. Absent interviews or analytics do not establish measured zero. Never infer a feedback vote.

## Output and fallback

Return a source-backed partial shortlist, exact invitations, guide, evidence gaps, progress/save status and next action; after actual interviews, add supported patterns. Missing Chrome or sending access still allows permitted public research, a founder-provided contact list and preparation. MCP unavailable: deliver usable work without claiming it was saved.
