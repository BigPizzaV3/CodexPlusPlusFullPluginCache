---
name: spending_by_category
description: Chart spending by category for a date window, largest first.
---

Use this when the user asks where their money went by category. This is category totals, not the spending pace card.

1. Call spending.by_category. Pass since and until only when the user gives those dates, as YYYY-MM-DD.
2. Present spending by category, largest first.
3. For whether this month is ahead of the plan, call spending.pace instead.
4. Use the numbers exactly as returned. Nothing moves money.

Write the answer in plain text. Use no emoji, coloured dots, check marks or other symbols, and no em or en dashes. Say a status in words, such as ahead, on track or behind.
