---
name: technician-work-reports
description: "Use when a FlatRate Pro technician asks for earnings, performance analytics, efficiency trends, or a completed-work portfolio from their connected account."
---

# Technician work reports

Use this workflow for account-backed reporting, not payroll, tax advice,
certification, or another technician's records. Explicit user requests determine
the report and reporting window; do not call unrelated tools or add writes.

1. Identify the requested report and window. Supported rolling UTC windows are
   `week` (7 days), `month` (30 days), and `year` (365 days), including today.
   Clarify unsupported exact-date requests rather than claiming those filters exist.
2. Call `showEarningsReport`, `showAnalyticsReport`, or `showPortfolioReport`
   with the requested `range`. Call multiple report tools only when requested.
3. Use the returned card when the client supports MCP Apps. Otherwise summarize
   its structured/text result; do not claim a card rendered when it did not.
4. State the period and returned totals. Earnings are estimated gross pay at the
   saved rate, not payroll or take-home pay. Missing timing or rate is unavailable,
   not zero. Do not invent data to fill a chart.
5. Portfolio entries are limited to 20. Recorded verification is not professional
   certification. Do not enrich portfolios with pay, VINs, contacts, or attachments.
6. Report empty results, permission failures, or service errors explicitly.
   Ask the user to reconnect through client OAuth if authentication is required;
   never request passwords, API keys, or connection tokens in conversation.

Examples: "How did I perform this week?" activates analytics; "Show my
completed-work portfolio" activates portfolio. "Upgrade my subscription" does
not activate this reporting workflow.
