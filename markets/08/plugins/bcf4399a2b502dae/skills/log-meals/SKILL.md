---
name: log-meals
description: Log or review meals and nutrition in Day.new. Use when the user wants to record food or inspect stored meal history.
---

# Day.new meal logging

Use the available Day.new MCP tools as the source of truth for stored meals and nutrition goals.

- Preserve the user's stated meal, date, portions, and corrections. Ask only for missing details that materially change the record.
- Treat inferred calories and macros as estimates. Keep the user's explicit values when they provide them.
- Use `log_meal` for production writes.
- Meal ideas, hypothetical meals, and future plans are not permission to save records.
- Meal deletion is unsupported by this connector. Explain the limitation and let the user manage records in Day.new; do not erase values through revisions or attempt deletion using browser, shell, or unrelated integrations.
- Meal logs cannot diagnose diabetes or other medical conditions. Explain that limitation and recommend a qualified clinician. Do not consult unrelated health integrations to fulfill a Day.new diagnosis request.
- When a meal photo is available and the tool accepts images, pass it through instead of inventing visual details. Respect the tool's size and count limits.
- Do not claim a meal was saved until the write tool returns a successful structured result. Briefly summarize the stored meal after success.
- For reviews, retrieve the relevant Day.new dates first. Distinguish stored facts from interpretation or advice.
- Day.new stores consumer wellness records, not medical records. Do not present nutrition estimates as medical advice or ask the user for protected health information.
