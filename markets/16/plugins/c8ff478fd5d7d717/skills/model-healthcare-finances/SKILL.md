---
name: model-healthcare-finances
description: Calculate healthcare service unit economics, capacity-constrained volume, operating results, delayed collections, and startup funding with explicit assumptions. Use for financial feasibility, break-even, cash-flow, and expansion-versus-startup comparisons.
---

# Model healthcare finances

Read [working rules](../../references/working-rules.md) and the [calculator specification](references/calculator.md). Input facts, proxies, and scenarios must remain distinguishable in the [assumption register](../../assets/assumption-register.csv).

Use `scripts/feasibility_model.py` with a new user-workspace JSON input when Python execution is available. It is standard-library-only and makes no network calls. Follow the schema in the specification and use `assets/synthetic-mobile-care.json` only as a structurally complete synthetic example. Execute with `python <skill-folder>/scripts/feasibility_model.py <input.json> --output-dir <new-output-directory>`. Confirm successful execution and inspect `summary.json`, `monthly.csv`, and `service-economics.csv` before citing results. Do not claim an executed result when only a formula was supplied.

Model collected revenue per completed encounter using an explicit amount basis, then deduct direct variable costs and billing fees. Apply demand and capacity consistently before computing totals. Show first-year expected earned collections separately from cash received, year-end receivables, recurring operating result, prelaunch expenses, capital spending, and cash funding needs. The helper reports a planning estimate, not GAAP statements or a payment prediction.

Compare coherent downside/base/upside and existing-practice/standalone scenarios. Include a no-expansion baseline where relevant. Preserve service mix and resource constraints in break-even analysis; negative contribution has no volume-only remedy. Fixed-cost and capacity steps require distinct scenarios. Check the helper's monthly break-even qualification rather than presenting it as an exact launch-year recovery target.

Keep downstream clinic contribution separate from direct service economics and include only clinically appropriate, sourced assumptions with associated costs and available capacity. Model a service company's expenses/fees independently. Do not count a management fee as both eliminated clinic cost and new outside revenue. Use a separate expanded model for debt, taxes, grants, inventory/vendor timing, multi-year forecasts, or multiple constrained resources; state limitations if these determine the recommendation.

Deliver editable inputs, executed outputs or clearly unexecuted formulas, source/assumption register, key sensitivities, and a concise explanation of what changes the decision. Do not overwrite source inputs, silently fill unknowns with zero, or equate a positive scenario with a recommendation to invest.
