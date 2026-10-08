---
name: valuation-brief-builder
description: "Use when an estate agent has one or more upcoming UK residential valuation or appraisal appointments and wants concise pre-visit briefing material. Resolve each address and use Propalt property details, history, valuation/comparables, live competition, EPC, leasehold, rental, and market context as relevant; support multiple properties without requiring PDF generation."
---

# Valuation Brief Builder

Prepare a concise briefing the agent can scan before each valuation appointment.

## Workflow

1. Accept one or more addresses in any clear form. Resolve each with `address_lookup`; do not use `search_properties` as a free-text address lookup.
2. For each resolved property, pull core subject facts with `get_property`, history with `get_property_history`, and EPC/fabric with `get_epc_fabric_by_property_id`. Use `get_leaseholds` when leasehold.
3. Pull valuation evidence with `get_valuation_by_property_id` when a pricing indication is required, and sold comparables with `get_comparable_by_property_id`.
4. Pull live competition with `selling_property_market_activity_properties_for_sale_post` or active comparables from `get_comparable_by_property_id` where appropriate.
5. Pull local market context with `get_monthly_market`, `get_quarterly_market`, `get_hpi`, and `get_market_analysis` only as relevant to the meeting.
6. If rental context matters, prefer `get_comparable_by_property_id` with `type="letting"`; calculate indicative gross yield only when both a supported rent and price are available.
7. If planning or nearby transport materially matters to the appointment, use `get_planning_applications` and/or `get_nearby_transport`. Reuse the resolved property identifier, full postcode, or coordinates from the address-resolution step instead of switching to exploratory web research.
8. Synthesize the facts into 2–4 things the agent should know walking in. Do not merely repeat the raw fields.

## Brief structure

For each property include:
- confirmed address and property basics;
- tenure/lease and EPC highlights where available;
- marketing/sale history;
- Propalt valuation if requested/available;
- strongest sold comparable evidence;
- current competition;
- market direction/speed where useful;
- rental context if relevant;
- data gaps and the key questions to validate at the appointment;
- “Things to know walking in” synthesis.

## Source order

When a required factual property or location detail is available from a Propalt tool, use that Propalt capability before exploratory web research. Supplement externally only for information outside Propalt's supported data or when the user explicitly asks for additional current corroboration.

## Guardrails

- Do not silently skip an unresolved address. If multiple address matches remain plausible, ask the user to choose.
- Do not make survey-level condition claims from EPC data.
- Do not promise a sale price or time to sell.
- Do not invent service charges, lease years, comparable distance, or £/sq-ft fields when the API does not return them.

## Delivery

Return the briefs in chat by default. If the user asks for a printable PDF and the host supports file creation, generate one; otherwise provide clean print-ready text. Do not depend on runtime package installation.
