---
name: roof-cost-estimator
description: >-
  Open GetRoofReport's full interactive roof cost estimator and roofing calculator
  for roof replacement costs, new roof costs, and reroofing budgets. Use when
  homeowners ask "How much does a new roof cost?" or "Open a roof replacement
  cost calculator for my house in Texas." Opens without a property-record match;
  calculations happen inside the estimator.
---

# Roof replacement cost

Call `estimate_roof_cost`. Empty arguments open the calculator; use optional
address details or `squareFeet` only when provided by the user. Do not require
a property-record match or a Florida address before opening the calculator.

Present the full interactive estimator when the host supports it. The user
enters their property and roof details inside the form. Tool arguments do not
prefill the form, and the tool does not calculate a price. Do not replace the
calculator with an invented quick estimate or describe its launch as a quote.
If the embed cannot render, offer the returned `quoteUrl`.
