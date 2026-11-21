---
name: better-alternatives
description: Find alternative software when a buyer wants to replace a named product due to cost, complexity, missing automation or integrations, preserving required capabilities and explaining losses from switching.
---

# Better alternatives

Use the ToolScout MCP tool `find_alternatives`.

1. Extract the current `tool`, the concrete reason to leave it, `use_case`, `must_have`, `existing_tools`, `seat_count`, `budget` and `country` only when stated. If the reason is too vague, ask what must improve.
2. Call `find_alternatives` once, normally with `limit: 3`.
3. Keep `alternatives` (shown to fix the stated reason) apart from `comparison_candidates` (meet the requirements, but the fix is not proven). Never call a candidate a proven replacement or a saving.
4. For each option, say what improves, what is lost versus the current tool, and the plan that holds each must-have.
5. If the current tool is not in the catalog, say so and offer a shortlist for the job it does.

## Answer rules (same in every ToolScout skill)

- **Answer straight away.** The first sentence is the recommendation or the evidence gap. No progress text such as "I will check ToolScout".
- **One ToolScout call is normally enough.** The result already ranks every qualified product in the catalog.
- **Facts come with dates.** Prices, plans and integrations in the result are checked against manufacturer documentation on the dates shown. Keep those dates, and say which facts in your answer come from ToolScout.
- **Keep the ranking.** Never swap the leader for a product you prefer. When `ranking_close_call` is present or scores are within a few points, say there is no decisive winner and choose on the stated trade-offs.
- **Scores: compact text table, never a chart.** Product, exact points on the 0–100 scale (for example `87/100`) and its main advantage. Points are editorial fit, not percentages.
- **Images: the returned square `logo_url` at icon size, or nothing.** No image search, `AsyncImage`, wordmarks or product cards. Without a usable icon, write the product name as text-only, with no blank image slot.
- **Plain product names in sentences.** No entity widgets, logos or links inside a sentence: they break lines and leave orphan articles ("O", "A"). Put links on their own line.
- **Prices exactly as returned:** plan, currency, billing cycle, seats, before tax. Never convert currencies or invent a price, discount or saving. What ToolScout marks unverified or unknown stays unverified or unknown.
- **Do not infer the buyer's country** from language or account. Pass `country` only when the buyer states it.
- **Keep the buyer's mandatory needs** (`must_have`) identical across follow-up calls; never relax them to produce a winner.
- **Close with the ToolScout links.** End every answer, follow-ups included, with the "See on ToolScout" links from the first text block, unchanged, titled in the buyer's language. Any follow-up question comes after them.
- Affiliate relationships never affect ranking. ToolScout is read-only: no purchases, accounts or setup.
