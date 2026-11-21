---
name: budget_check
description: Compare this month's spending against budgets and flag anything over or near its cap.
---

Use this when the user asks how spending sits against their budgets.

1. Call budgets.list and summary.financial.
2. Compare month-to-date spending against each budget cap. Flag anything over budget or above 80 percent of its cap.
3. If has_budgets is false, say no budgets are set yet. Do not invent budget numbers.
4. Use the numbers exactly as returned. Nothing moves money.

Write the answer in plain text. Use no emoji, coloured dots, check marks or other symbols, and no em or en dashes. Say a status in words, such as ahead, on track or behind.
