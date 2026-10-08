---
name: esg-screen
description: >-
  Use this skill to screen securities/holdings against MSCI ESG ratings, controversies, and business-involvement restrictions such as weapons, tobacco, gambling, alcohol, adult entertainment, thermal coal, arctic drilling, or other mandate exclusions. Trigger when the user gives holdings plus ESG restrictions or asks whether names breach a stated threshold.
---

# ESG and business-involvement screening

Turn mandate language into explicit, auditable tests using MSCI fields. A definitive exclusion requires a defined rule: involvement flag, revenue percentage threshold, rating threshold, controversy threshold, or another stated criterion.

## Output

Group breaches first. For every holding, show identity, measured value/status, threshold or rule applied, pass/fail/unscreened, and evaluation date. State whether current or rebalancing values were used.

## Workflow

1. Parse each restriction into a test. Distinguish involvement flags from revenue-percentage thresholds; they are not interchangeable.
2. If a numeric threshold is essential but omitted, do not invent one. You may still return the measured exposure/status and label the pass/fail conclusion as undetermined until a threshold is specified.
3. Discover exact fields with `search_index_datapoints`. Do not compose ids from memory. When both current and `.rebalancing` variants exist, use current values for "today/current portfolio" questions and rebalancing values only for a review/rebalance construction question.
4. Resolve securities with `search_index_securities`; resolve an index with `search_index_indexes` when the user asks about index-level ESG metrics.
5. Read `constraints.notes`, `strict_gate`, and date availability before fetching.
6. Use `fetch_index_data` for point-in-time screening. If the selected data snaps to another date, state the requested and fetched date.
7. For rebalancing-aware fields, resolve the documented rebalance date rather than guessing one.

## Interpretation

- Missing value = unscreened/unknown, never an automatic pass.
- An involvement flag is categorical; a revenue field is quantitative.
- If the user asks for an ESG rating, include the underlying score when the catalog/tool definition makes that relationship relevant.

## Guardrails

- Never report an exclusion without naming the rule/threshold applied.
- Do not describe the output as a legal/compliance opinion. It is a data screen against the rule supplied by the user.
- Date the assessment; involvement and controversy data can be restated.
- Preserve units and threshold direction exactly.
