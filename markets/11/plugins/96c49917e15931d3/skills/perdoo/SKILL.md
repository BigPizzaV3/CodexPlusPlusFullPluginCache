---
name: perdoo
description: Work with actual goals, reviews, meetings, teams, and Explore views in a user's Perdoo workspace through the Perdoo tools.
---

# Perdoo

Use the Perdoo MCP tools for live workspace data and actions. Follow each tool's description and input schema. Treat their results as the source of truth; never invent workspace data, identifiers, permissions, progress, owners, targets, statuses, or dates.

- Distinguish advice or content drafting from a request to change Perdoo. Do not write when the user only asks for ideas, analysis, or proposed wording.
- Resolve names to IDs with the relevant Perdoo read tools. Never guess an ID. If several entities plausibly match, show the smallest useful set of distinguishing details and ask the user to choose.
- Read current state before a partial edit, replacement of collection fields, or any change whose correctness depends on existing values.
- Use the smallest set of calls that fully answers the request. When the user asks for **all** matching records, follow pagination until complete.
- Do not infer missing facts or silently substitute an unsupported operation. Explain the limitation and give the closest supported Perdoo UI fallback.
- After a write, report the returned entity and any partial failure. Never repeat a successful create or submission while retrying failed work.
