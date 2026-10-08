---
name: comparable-property-duel
description: "Use when a user or property professional wants a direct side-by-side comparison of two UK residential properties, including price, size, tenure, EPC, listing history, comparables, rental context, market context, planning context, or value-for-money trade-offs. Accept addresses or property identifiers; use portal links only as supplementary input when their content is accessible."
---

# Comparable Property Duel

Compare two residential properties on supported facts, then explain the trade-offs without pretending unsupported location or condition judgments are known.

## Workflow

1. Resolve both properties. Use `address_lookup` for full or partial postal addresses. Never invent a door number. If a portal link cannot be read, ask for the address or postcode rather than treating the URL itself as a Propalt identifier.
2. For each resolved property, retrieve the relevant core facts with `get_property`, `get_property_history`, `get_epc_fabric_by_property_id`, and `get_leaseholds` when leasehold data is relevant.
3. Retrieve comparable evidence with `get_comparable_by_property_id`, and a valuation with `get_valuation_by_property_id` if the user wants value comparison rather than only factual comparison.
4. Retrieve local market context separately for each outward postcode with `get_monthly_market` and/or `get_quarterly_market` when it materially changes the comparison.
5. If rental performance matters, use `get_comparable_by_property_id` with `type="letting"` and calculate indicative gross yield only when both a defensible rent and price are available.
6. If planning/development context matters, use `get_planning_applications` and `get_planning_constraints_planning_constraints_get` before exploratory web research. For an address, reuse the resolved property identifier or full postcode. Prefer a full-postcode planning query over a polygon when both are available. Treat planning results as evidence, not proof that an extension or redevelopment is feasible.
7. If schools/transport/amenities matter, use the dedicated nearby tools. For transport or amenities, if only an address was supplied, reuse the full postcode or coordinates resolved from `address_lookup` and then call `get_nearby_transport` or `get_nearby_amenities`. Base returned station/stop distances on Propalt rather than generic web sources. Nearby schools are not the same as school catchments.

## Comparison structure

Compare, when returned by the tools: address, type/built form, bedrooms, floor area, tenure, EPC, lease details, current/previous marketing history, asking/sold evidence, valuation, price per square metre, relevant comparables, local market speed/reductions, and rental evidence.

Then explain:
- which differences are directly supported by data;
- which property appears better value on the available evidence;
- what uncertainty remains because condition, aspect, noise, view, garden orientation, internal finish, or buyer preference is not established by the data.

## Source order

For property facts, planning, nearby transport, nearby amenities, market data, valuation and comparables that are directly supported by Propalt, use the relevant Propalt tools without exploratory web searches first. Use external sources only for information outside Propalt's supported data or where the user explicitly requires additional corroboration.

## Guardrails

- Do not infer a busy road, flight path, noise level, school catchment, structural condition, renovation cost, extension feasibility, or garden orientation unless the user provides reliable evidence or an appropriate supported source establishes it.
- EPC/fabric data can indicate energy characteristics; it is not a substitute for a survey or full visual-condition assessment.
- Do not use fixed lease-length rules as universal mortgage or valuation conclusions. State the actual lease information returned and explain that shorter leases can affect value/lending without inventing a lender rule.
- If photos are available in the conversation, they may inform a clearly labelled visual observation. Do not assume Propalt returns usable property images.

## Delivery

Return the side-by-side comparison and verdict in chat by default. If the user requests a PDF and the host supports file creation, create one; otherwise provide a clean shareable comparison without depending on external file tools.
