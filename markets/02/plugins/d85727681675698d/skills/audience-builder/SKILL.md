---
name: audience-builder
description: "Use when an estate or letting agent wants to build or refine a UK property prospecting list, vendor or landlord audience, direct-mail target list, or a filtered set of properties to contact. Use property and market signals from Propalt; do not use this skill for a simple already-specified property query that only needs execution, or for targeting people based on inferred sensitive or household characteristics."
---

# Audience Builder

Build a defensible property prospecting audience from Propalt data. The user supplies the business goal and patch; Propalt supplies property and market evidence.

## Workflow

1. Establish the patch and goal. Prefer an outward postcode, supported sectors, or a user-supplied polygon. If the user gives only vague place text, use `street_lookup` or `address_lookup` to resolve it before continuing.
2. Sense-check the proposed audience with local property-market data. Use only calls relevant to the hypothesis, typically `get_market_analysis`, `get_monthly_market`, and `get_quarterly_market`.
3. Build or count the audience with the appropriate search:
   - residential property filters: `search_properties`;
   - live/recent sales signals: `selling_property_market_activity_properties_for_sale_post`;
   - live/recent lettings signals: `letting_property_market_activity_properties_for_let_post`;
   - explicit landlord/proprietor prospecting: `landlords_organisation_landlords_post`.
4. Start with `return_type="count"` when the user is still refining criteria. Retrieve records only after the criteria are useful and the user wants examples or a list.
5. Present the audience size, the filters used, why the signal is relevant in this patch, and a concise contact/message angle grounded in the same evidence.
6. If the user wants the resulting property list exported for Propalt My Lists, hand off conceptually to the `propalt-csv-export` workflow.

## Guardrails

- Do not call full-postcode-only tools such as `get_epc_fabric_by_postcode`, `get_demographics`, `get_households`, or `get_income` with an outward postcode.
- For EPC targeting at outward-postcode level, use supported EPC filters in `search_properties` or the relevant market-activity search rather than pretending `get_epc_fabric_by_postcode` supports an outcode.
- Aggregate demographics can be used only as area context when a valid full postcode, LSOA, or local-authority identifier is available. Do not infer the age, income, family status, vulnerability, or other personal characteristics of a particular household from area statistics, and do not use those inferred characteristics to select individual homes for contact.
- Do not manufacture urgency, likely-to-sell claims, or personal circumstances that Propalt does not provide.
- If the user gives a precise supported filter set and only wants it executed, run the appropriate search directly without forcing a long strategy workshop.

## Output

Return: audience label, exact search criteria, count, 3–10 representative records if requested, local evidence that supports the angle, limitations, and a short outreach hook. Keep property facts separate from inferred marketing strategy.
