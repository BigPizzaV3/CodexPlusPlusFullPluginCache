---
name: explain-cost-variance
description: Explain how a Grid payable or commitment relates to budget lines, including estimate versus running comparison, active-payable scope, and attachment reconciliation without altering financial records.
---

# Explain payable and commitment costs

Use the current Grid MCP schemas. This is read-only operational reconciliation, not payment execution or record repair.

1. Establish the project, budget, and payable or commitment identity. Use `grid.list_projects`, `grid.list_budgets`, and relevant `grid.get_budget_line_context` results when IDs are already available there. Otherwise request the missing identifier or a supported record link; do not invent an ID or assume an unavailable global payable search exists.
2. For a payable, call `grid.get_payable_budget_variance`. State the selected budget basis: `estimate` is the default; use `running_preferred` when requested and explain any returned fallback. Retain the default tolerance unless the user requests a different one. The comparison includes active payables for the same project company against coded budget lines, so distinguish the selected payable from the wider comparison.
3. For a commitment, call `grid.get_commitment_context`. Request `include_items` only when needed and disclose returned truncation or item limits. Explain attachment subtotals from the tool's explicit actualization relationships; source/cost-code links alone are not evidence that one amount replaces another.
4. Present the tool's amounts, differences, linked records, warnings, and incomplete or unmatched data. Separate observed figures from possible explanations. Do not equate a budget overage with a duplicate invoice or infer settlement from budget coding.

Conclude with the specific records or missing information the user should inspect. Do not claim to approve, pay, recode, delete, or repair anything through these tools.
