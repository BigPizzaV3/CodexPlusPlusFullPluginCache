---
name: property-research
description: Compare public Zillow or Redfin homes for sale, monthly rentals, sold listings or property details with HasData. Use for housing-listing research with a location/budget or URL, not short-term holiday stays or appraisals.
---

# Compare property listings

Read `../hasdata-research/SKILL.md` for shared scope and safety, then the Property section of `../hasdata-research/references/tool-catalog.md`. Zillow and Redfin have different filter names and enums. Use the selected tool's live schema.

Resolve whether the user means sale, rental or sold listings and retain their location and budget. Map that intent to the actual type enum. A single property URL calls for details, not a new area-wide search. Use price, bedrooms and other filters only when explicitly relevant, and do not infer preferences from protected personal characteristics.

Preserve returned prices, price periods, units, addresses and source URLs. Distinguish asking price, estimated value, historical sale price and monthly rent. Do not sum fees whose inclusion is unclear. Keep listings with unknown requested fields visibly separate instead of inventing values or saying they meet every criterion.

Deduplicate returned property URLs or IDs, not addresses alone. Read individual details only for a selected candidate when needed within the budget. Do not enable agent email extraction as a side effect of property comparison.

Describe the bounded results and supplied filters. A listing is not confirmation that the property remains available, and a returned estimate is not a professional appraisal. Explain research tradeoffs from observed fields without advising on financing, protected-class neighborhood selection, or guaranteed investment returns. Do not contact agents, book tours or submit applications.
