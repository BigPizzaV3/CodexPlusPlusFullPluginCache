---
name: trip-budget
description: Build, reconcile, and optimize a transparent travel budget with unit costs, currencies, taxes, fees, contingency, per-person totals, and target tradeoffs. Use for focused pricing requests or when explicitly invoked for reconciliation. For a complete multi-day trip, return figures to vacation-planner.
---

# Trip Budget

Use one canonical traveler count, room count, date window, and base currency. Read [budget-rules.md](references/budget-rules.md).

Capture every material item as category, description, quantity, unit cost, currency, source/assumption, price status, and inclusion status. Convert with a dated rate and retain the original currency. Separate quoted, observed, estimated, optional, and excluded costs.

Run `scripts/calculate_budget.py` on a JSON budget for deterministic totals when practical. Verify category totals equal the grand total exactly and show total-trip, per-person, target variance, contingency, and optional upgrades separately.

If over target, remove inefficient transfers or low-value excursions first, then adjust one hotel tier, one splurge, or travel timing. Shorten the trip only when better tradeoffs fail. Never hide required costs or use contingency to make the core plan appear cheaper.
