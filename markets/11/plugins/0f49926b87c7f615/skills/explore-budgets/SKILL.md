---
name: explore-budgets
description: Explain a Grid production budget, its Estimate and Running amounts, assumptions, line-level costs, and source/child budget relationships using read-only records.
---

# Explore a Grid budget

1. Resolve the project with `grid.list_projects` and budgets with `grid.list_budgets`. Reuse established selections; ask when there are multiple plausible budgets. Prefer returned UUIDs to project codes, which are company-scoped.
2. Start with `grid.get_budget_overview` for top-sheet totals and completeness. Distinguish Estimate, Running, commitments, and actuals as returned rather than treating them as interchangeable. Surface missing or incomplete data before drawing a conclusion.
3. For a specific cost, use `grid.search_budget_lines` and `grid.get_budget_line_context`. Use `grid.get_budget_overview` with `sections: ["rows"]` when a broader row view is needed; read `sections.rows` and request expense or time-card detail only when relevant.
4. Use `grid.get_budget_overview` with `sections: ["assumptions"]` to explain globals, fees, fringes, formulas, and dependency warnings. Request `sections: ["lineage"]` with an explicit `bid_id` for one-hop source/child relationships; label that limited scope and do not infer a complete version history.
   Combine relevant sections in one call when needed; explicit selections return their payloads under `sections`. Budget-selection responses can precede section data.
5. Explain amounts using the returned calculations and their scope. Do not add a linked detail or shared record again just because it appears in multiple views. Preserve the returned currency and units, distinguish missing values from zero, and label any supplementary calculation with its inputs.

Present the requested summary, key drivers, selected budget/phase, and unresolved data gaps. This workflow does not change the budget. If the user requests a supported edit, obtain a tool-generated preview and confirmation through the appropriate write workflow.

## Running review

Follow [update-budget-details — Running review](../update-budget-details/SKILL.md#review-a-saved-actual-against-running)
for the canonical per-bid automatic-question policy and separately confirmed
Running reconciliation. Collapsed Running skips the automatic question; it does
not supply a financial decision or remove cost-capture confirmation.
