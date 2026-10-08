---
name: index-flows
description: >-
  Use this skill to quantify MSCI index-inclusion or deletion impact for a security: estimated passive AUM to buy/sell, estimated/current index weight and AUM, and execution scale such as days-to-trade. Trigger for rebalance-flow sizing, inclusion-monitor questions, or "what happens if this stock enters/leaves MSCI World/ACWI/EM/IMI/Small Cap".
---

# Index inclusion flow impact

Use MSCI's inclusion-monitor and AUM datasets to size estimated benchmark-driven demand or supply. Treat monitor outputs as estimates, not official index-change announcements.

## Output

Lead with estimated flow, implied weight, and execution scale for the requested index family. Include calculation/pro-forma dates and the security identity. Reproduce any mandatory Index Inclusion disclaimer supplied in datapoint `constraints.notes` exactly as returned.

## Workflow

1. Resolve the company/ticker/ISIN with `search_index_securities`. Do not infer a country filter from suffixes such as `(US)`, `ADR`, `CDI`, or `ADS`.
2. Search `search_index_datapoints` for the relevant inclusion-monitor fields rather than guessing ids. Typical concepts are estimated AUM, estimated weight, current AUM/weight, and total family index AUM for the requested family only.
3. Read every selected datapoint's `constraints.notes` before fetching. Follow the documented publication-calendar rule, required `info_points`, rebalance targeting, and mandatory disclaimer. Do not default to today's date if the notes specify another calculation date.
4. Fetch supported point-in-time monitor fields with `fetch_index_data` using the resolved `msci_security_code`.
5. For execution/tradability metrics such as days-to-trade or average traded value, discover the exact fields and follow their documented pro-forma date inputs. Pass `info_points` only when `constraints.notes` explicitly defines the required keys.
6. If the relevant data is rebalancing-aware, resolve the required rebalance date using the documented last/next-rebalancing workflow; never invent the review date.

## Presentation

For each requested index family, show the useful subset of:

- estimated AUM impact
- estimated weight
- current AUM/current weight
- total AUM benchmarked to the family
- days-to-trade / volume basis, when available

State units exactly. If AUM is returned in USD millions, label it as such or convert explicitly to billions.

## Guardrails

- Mandatory Index Inclusion disclaimer: reproduce the exact text from `constraints.notes`; do not paraphrase it.
- Monitor estimates are not announcements and do not mean a security will be added/deleted.
- Days-to-trade is an execution-scale indicator based on the dataset's volume assumptions, not a recommended trading schedule.
- Do not turn estimated flows into a buy/sell recommendation.
- No returned monitor data is not the same as zero flow. Report it as unavailable/outside the returned monitor universe unless the tool says otherwise.
