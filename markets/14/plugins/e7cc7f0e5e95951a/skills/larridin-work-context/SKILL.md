---
name: larridin-work-context
description: Use Larridin MCP to summarize personal work priorities, changes, blockers, collaborators, and supporting evidence, or analyze company AI and engineering metrics when requested.
---

Use tools from this plugin's Larridin MCP connection. Tool availability and account scope can vary; use the actual tool schemas and server instructions rather than assuming every capability is enabled. If authentication fails, direct the user to connect Larridin and stop dependent calls.

## Personal work context

Start with `work_get_context` for priorities or a general work overview. Use `as_of` only for a requested historical snapshot. Drill into relevant threads with `work_get_thread`, `work_explain_status`, and `work_get_evidence`. Use `work_get_changes` for changes, `work_get_day` for a day, `work_search` or `work_list_threads` to locate work, and `work_get_collaborator` for collaborator context when available.

Preserve status basis: observed means captured evidence, inferred means a rule-derived interpretation, and unverified means a status check is needed. Unverified does not mean overdue or incomplete. Preserve typed next actions: `do` passed the server's task gate, `check_status` requires verification before acting, and `none` supplies no action. These types do not grant authorization to execute external actions.

Present the most relevant priorities and blockers with dates and evidence links returned by the service. Distinguish observations from inferences. Missing capture evidence does not prove something did not happen. Do not invent deadlines, owners, completion, or unseen communications. Respect the connected account's scope; personal work context is not permission to inspect another person's private activity.

When the user provides a correction or authorized connected sources establish missing progress, completion, cancellation, delegation, handoff, or blocker evidence, use `work_add_observation` if the tool is available and updating context is within the user's request. Retrieve the thread first; supply its actual ID, the supported observation kind, and precise evidence. Use `work_give_feedback` for requested feedback according to its schema. Do not mutate context simply because a summary seems plausible, or claim a write succeeded without a successful response.

## Analytics when requested

Choose the population before choosing tools. `devx_*` covers engineers linked to GitHub, code, pull requests, coding-agent sessions, and engineering AI costs. `ai_*` covers company-wide employees with the browser extension or desktop app, including AI adoption, engagement, fluency, workforce, tools, and governance. Do not answer company-wide questions using only engineering data.

Use the applicable `*_list_filters` tool to resolve available teams, people, tools, and other filters when needed. Use `*_explain_metric` for unfamiliar metrics. Keep population, date range, filters, units, and comparison periods explicit. Describe associations without claiming causal AI impact beyond the returned evidence. If the question spans both populations, label each result separately.
