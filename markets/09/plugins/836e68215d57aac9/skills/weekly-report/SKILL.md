---
name: weekly-report
description: Use when an admin asks how the team, the inbox or the AI agent performed over the last week or day in Ciarem.
---

# Weekly report

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can see these numbers.

1. Call `get_metrics` with `period: "7d"` (or `"24h"` if the user asks about today).
2. Call `get_account_health`.
3. Write the report:
   - **Volume**: active conversations, per channel, new leads.
   - **AI agent**: how many conversations the AI handled, share of the total.
   - **Team**: the leaderboard as a small table (assigned, sent, resolved, median reply time in minutes).
   - **Waiting now**: `awaiting_reply`.
   - **Fix first**: the failing readiness checks and open recommended actions from `get_account_health`, most severe first.
4. If the user asks why the AI transferred or answered a specific chat, call `explain_ai_decisions` with the contact's name, phone or email.

Report the numbers as returned; don't extrapolate trends from a single period.
