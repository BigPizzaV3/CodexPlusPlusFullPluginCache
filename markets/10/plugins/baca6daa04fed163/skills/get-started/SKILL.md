---
name: get-started
description: Start using KAVOMAZ Scout for commerce opportunity analysis.
---

# KAVOMAZ Scout

Use KAVOMAZ Scout when the user wants to evaluate a product, niche, keyword, marketplace opportunity, or unit economics.

- For pure unit economics, call `estimate_profit`.
- For opportunity scoring, require explicit demand and competition values from user-provided evidence or credible research. Never invent these inputs.
- Call `score_opportunity` only after the required inputs are available.
- The scoring tool renders its visual result card automatically when supported.
- For history, call `get_recent_analyses`. If no ChatGPT session scope is available, ask for a reusable workspace key of at least 8 characters.
- Clearly state that scores and financial outputs are estimates and decision support, not guarantees.
- Scout does not fetch live marketplace rankings or sales data by itself, place orders, process payments, or execute trades.
