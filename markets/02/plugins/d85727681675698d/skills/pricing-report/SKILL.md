---
name: pricing-report
description: "Use when an estate or letting agent asks for a detailed UK residential pricing report, vendor pricing recommendation, valuation presentation, pricing scenarios, or a marketability assessment for one property. Use Propalt valuation, sold comparables, active competition, property details, HPI, and local market data; clearly label any derived score or pricing scenario as a workflow heuristic rather than a Propalt API metric."
---

# Pricing Report

Create an evidence-led pricing report for one UK residential property.

## Workflow

1. Resolve the full address with `address_lookup`. Use `get_property` for property facts and user-supplied corrections only when needed.
2. Retrieve the selling valuation with `get_valuation_by_property_id`.
3. Retrieve sold comparables with `get_comparable_by_property_id` using `type="selling"` and `current_status=3`. Retrieve active comparable listings with the same tool using `current_status=1` when useful.
4. Retrieve local market conditions with `get_monthly_market` and/or `get_quarterly_market`, plus `get_hpi` for longer-term HPI context.
5. Use `get_income` only as aggregate local context when a supported geography is available. Do not infer an individual buyer's affordability from area income data.
6. Use `get_leaseholds`, `get_epc_fabric_by_property_id`, planning tools, or nearby/location tools only when materially relevant to pricing. When planning or nearby transport materially affects the report, use Propalt's dedicated planning/transport tools first; for an address, reuse the resolved property identifier, full postcode, or coordinates rather than switching to exploratory web search.
7. Build the recommendation by triangulating the AVM, achieved comparable evidence, live competition, subject history, and market conditions. If these disagree, show the disagreement instead of hiding it.

## Source order

For supported property facts, valuation evidence, comparables, market statistics, planning, EPC, tenure, and nearby location evidence, use the relevant Propalt tools before general web research. External sources are appropriate only for information Propalt does not provide or when additional current corroboration is explicitly needed.

## Derived marketability score

A marketability score may be included when useful, but it must be labelled **Derived workflow score, not a Propalt API metric**.

Use only factors actually returned by the current calls. Normalize available factors such as market speed, reduction prevalence, supply/competition, HPI direction, comparable evidence strength, and AVM uncertainty if an uncertainty measure is returned. If a factor is missing, do not invent it; either reweight the available factors transparently or omit the score.

Do not use a fixed price-to-income or mortgage-capacity rule to decide who can afford the property. If income context is shown, label it as area-level context only.

## Pricing scenarios

Prefer evidence-based scenarios rather than fixed universal multipliers. A useful report can show:
- quicker-sale positioning;
- evidence-supported market positioning;
- higher/experimental positioning with the additional time/uncertainty clearly stated.

Derive ranges from the actual AVM/comparable distribution and current competition. Do not hard-code universal percentages such as `BASE × 0.93` or auction reserve discounts as if they were validated Propalt models.

## Report structure

1. Subject property and data quality.
2. Propalt valuation and any returned uncertainty/confidence information.
3. Best 3–5 sold comparables with clear selection rationale based on fields actually returned.
4. Active competition and listing history when available.
5. Local market conditions and HPI context.
6. Derived marketability assessment, clearly labelled as derived.
7. Recommended pricing scenario/range and why.
8. Risks, missing facts, and what the agent should validate during the appraisal.

## Delivery

Return the internal summary and report content in chat by default. If the user requests a PDF and the host supports file creation, produce a professional PDF. Do not make completion depend on `reportlab`, package installation, fixed filesystem paths,.

Include a concise note that the output is market guidance based on automated/market data and is not a formal RICS valuation.
