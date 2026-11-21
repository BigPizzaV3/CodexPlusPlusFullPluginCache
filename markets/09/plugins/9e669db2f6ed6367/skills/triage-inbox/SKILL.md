---
name: triage-inbox
description: Decide what to work on next in SeoPerseo by reading stored Inbox opportunities and their evidence, and optionally updating their status.
---

Use this skill when the user asks what to work on next, what SeoPerseo found, or asks to review, group or close Inbox opportunities.

## Workflow

1. Resolve the project. Call `projects_list`. If the user named a domain, match it. If more than one project matches or none was named, ask which project before continuing.
2. Call `opportunities_list` for that project. Keep the order the tool returns; it already reflects the measured priority.
3. For each opportunity the user wants to understand, call `opportunities_get` to read its evidence, analysis and recorded next action.
4. Present the top items as a short list. For each one give:
   - the opportunity title;
   - the measured evidence behind it, with the metric and the date it was collected;
   - the next action SeoPerseo recorded.
5. When several opportunities are wordings of the same search need, say so and treat them as one piece of work. Do not split them into separate recommendations.
6. Only when the user explicitly asks to mark something active, done or dismissed, call `opportunities_status_update`. Confirm the new status back to the user.

## Boundaries

- Never recalculate, re-rank or invent a priority score. Report the order and the bands the tools return.
- Never present an AI interpretation as measured data. Say plainly which part is the stored measurement and which part is your reading of it.
- If an opportunity has no stored evidence, say so instead of filling the gap.
- Reading the Inbox spends no credits. `opportunities_status_update` spends no credits either. If the user asks for fresh data, follow the audit or research workflow and confirm the cost first.
