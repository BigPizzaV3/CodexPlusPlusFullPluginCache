---
name: daily-briefing
description: Build a morning briefing from IRM365. Use when the user asks what's on today, what they should work on, for a daily or morning summary, or what they missed.
---

# Daily briefing

1. Call `get_workspace_context` for the person and their timezone.
2. Call `list_followups` with `window: "overdue"`, then with `window: "today"`. Page through results while `has_more` is true, up to 100 follow-ups each.
3. Call `search_leads` with `priority: "hot"` and pick out leads whose `last_contacted_at` is more than three days ago, or empty.
4. If opportunities are shared, call `search_opportunities` with `closing_before` set to seven days from today.

Write the briefing in this order, using short lists:

- **Overdue**: follow-up, lead reference and name, how late it is. Oldest first.
- **Today**: follow-ups in time order, with the time in the user's timezone.
- **Hot leads going cold**: each with the days since last contact.
- **Closing this week**: opportunity, stage, expected value in AED, close date.

End with the three actions that matter most today, one line each. Leave out an empty section rather than writing "none". Never invent phone numbers, emails or notes; the connection does not share the phone and email fields.
