---
name: performance-brief
description: Create an evidence-backed Google Ads performance brief through Adszy MCP. Use for week-over-week, month-over-month, or year-over-year comparisons, stakeholder updates, client reports, and concise performance recaps.
---

# Performance Brief

Turn Adszy's read-only metrics into a concise stakeholder-ready narrative.

## Workflow

1. Resolve the account with `list_ad_accounts` when it is ambiguous.
2. Call `compare_periods` with the user's requested comparison.
3. Call `get_account_summary` for the current-period campaign breakdown.
4. Use a focused diagnostic tool only when the comparison needs support, such as `get_change_history`, `get_budget_pacing`, or `get_anomalies`.
5. Write:
   - executive summary;
   - key metric changes;
   - campaign drivers;
   - risks or unknowns;
   - recommended next checks.

## Guardrails

- State both date ranges and the account currency.
- Use absolute and percentage changes where available.
- Do not invent explanations for movements. Separate measured drivers from hypotheses.
- Flag low volume, missing conversion data, and attribution limitations.
- Do not imply that Adszy applied any recommendation.
- Keep the brief readable without hiding material negative findings.
