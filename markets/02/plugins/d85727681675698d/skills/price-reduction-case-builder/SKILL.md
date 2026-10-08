---
name: price-reduction-case-builder
description: "Use when an estate agent needs to assess or explain a price reduction for a stalled UK residential listing, including long days on market, repeated reductions, weak viewing activity, vendor resistance, or an asking price that may not be supported by current evidence. Use Propalt history, valuation, comparables, competition, and market trends before recommending a reduction."
---

# Price Reduction Case Builder

Build a clear vendor conversation from evidence. If the data does not support a reduction, say so and identify the uncertainty rather than forcing the case.

## Workflow

1. Resolve the property with `address_lookup`.
2. Retrieve `get_property`, `get_property_history`, `get_valuation_by_property_id`, `get_comparable_by_property_id`, and relevant local market data from `get_monthly_market` and/or `get_quarterly_market`.
3. Use `selling_property_market_activity_properties_for_sale_post` for current competing stock when useful. Use `get_hpi`, `get_leaseholds`, and `get_epc_fabric_by_property_id` only when relevant.
4. Ask for missing agent-side signals: viewing volume/trend, repeated feedback themes, offers received, vendor objective/timeline, and any material property condition or presentation information not represented in Propalt.
5. Assess the cause of the stall. Separate evidence for pricing from possible presentation, condition, access, photography, or low-volume market explanations.
6. If a reduction is supported, recommend a defensible range/guide price using achieved comparables, the Propalt valuation, live competition, listing history, and market direction. Show why the recommendation follows from the evidence.
7. If current portal search-bracket behaviour is important, verify it from a current reliable source before using it. Do not hard-code third-party portal thresholds or ranking behaviour into the advice.
8. Produce either a concise call crib sheet or a vendor email when the user chooses the channel.

## Source order

Use Propalt first for supported valuation, comparable, listing-history, live-competition, EPC/leasehold and local-market facts. Do not perform exploratory web searches for those facts before calling the relevant Propalt tools. External sources are appropriate only for unsupported information such as current third-party portal search behaviour or when explicit corroboration is requested.

## Guardrails

- Do not infer viewing feedback, vendor finances, mortgage balance, or personal urgency.
- Do not promise that a specific reduction will generate a sale or a target number of weeks.
- Avoid repeated small-reduction folklore presented as fact; make the recommendation from the subject property's evidence.
- A poor EPC or lease issue can be part of the value discussion but is not proof of the listing's problem.

## Output

Include: current position, strongest evidence, what the market appears to be rejecting, recommended range or reason not to reduce, cost/risks of holding the current price in qualitative terms supported by the data, and the chosen conversation/email format.
