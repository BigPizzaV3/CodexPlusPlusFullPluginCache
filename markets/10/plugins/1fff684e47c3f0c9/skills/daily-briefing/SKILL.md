---
name: daily-briefing
description: A short sales briefing for a connected ServeStack restaurant — yesterday (or another period) versus a matching earlier period, top items, busy hours, and one or two suggestions.
---

1. Call `get_owner_context`; if the owner has several locations, ask which one (or brief each separately — never add different locations together).
2. Call `get_sales_summary` (default: yesterday vs the same weekday last week).
3. Report: orders, net sales and average order with the change versus the comparison, the top items and the busiest hours. Always state the period, time zone and that these are online orders through ServeStack only — never "total restaurant sales", never "profit".
4. Pass on every warning the tool returns (marketplace orders not included, today still in progress, test orders left out).
5. Offer at most two concrete, low-risk suggestions tied to the numbers (e.g. promote a top item at the slow hour). Present changes in the numbers as what happened, not why — correlation isn't cause.
6. If `get_connection_status` shows something needs attention, mention it with its fix link.
