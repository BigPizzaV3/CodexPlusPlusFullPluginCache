---
name: index-aum
description: >-
  Use this skill when the user asks how much AUM is benchmarked to an MSCI index, the ETF/non-ETF split, which linked exchange-traded products track the index, who provides them, or passive ownership linked to an MSCI security.
---

# AUM benchmarked to an MSCI index

Use the MSCI Index app to report benchmark-linked AUM, distinct from index market capitalization and distinct from fund flows.

## Output

Lead with total benchmarked AUM, then ETF/non-ETF split and their own as-of dates. If the user asks for linked products, include provider and show how many rows are displayed versus available.

## Workflow

1. Resolve the index with `search_index_indexes` using a concise name such as `EAFE`, `World`, `EM`, or `ACWI`.
2. Discover the AUM aggregate datapoints with `search_index_datapoints`; do not hardcode ids without discovery. Search concepts should include total AUM, ETF AUM/as-of date, and non-ETF AUM/as-of date.
3. Read `constraints.notes` and fetch supported point-in-time data with `fetch_index_data`.
4. For linked products, discover the list-cardinality linked-ETP datapoint. Use `fetch_index_data` with pagination, ordering, and supported filters such as provider/management style/taxonomy only when documented by the tool contract.
5. For security-level benchmark-linked AUM, resolve the security with `search_index_securities` and discover the constituent/security AUM fields before fetching.

## Presentation

- Identify the index as `<name> (<msci_index_code>)`.
- State AUM units exactly; if returned in millions of USD, convert to billions only with an explicit conversion label.
- ETF and non-ETF as-of dates may differ. Put each date beside its figure rather than assigning one common date to the total unless the returned dates actually agree.
- If useful, show ETF and non-ETF as percentages of the summed split, but do not imply those percentages are fund flows.

## Guardrails

- Benchmarked AUM is not index market capitalization.
- AUM level is not period fund flow. If the user wants inclusion/rebalance flow sizing, use the `index-flows` workflow.
- Product coverage reflects the connected MSCI product dataset; absence from the returned list is not proof a product does not exist.
- Respect entitlements and pagination. Do not claim complete coverage when only one page was fetched.
