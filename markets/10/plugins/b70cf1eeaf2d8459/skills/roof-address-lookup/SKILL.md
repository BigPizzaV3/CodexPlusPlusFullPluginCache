---
name: roof-address-lookup
description: >-
  Find a property by address in GetRoofReport for a roof age lookup, roofing
  permit search, property roof report, storm-risk review, or insurance-record
  lookup. Use for "Find the roof report for this address" or "Which property
  matches 21208 NW 238th Ave in High Springs?" Resolve partial or ambiguous
  addresses and return a report permalink. Address records currently cover Florida.
---

# Find a property

Call `search_addresses` using the supplied address. Use returned property
summaries to distinguish candidates. If multiple plausible matches remain,
ask the user to identify the property instead of guessing.

Reuse the selected result's permalink with the relevant report tool. Current
records cover Florida; an unsupported address is not evidence that a property
does not exist or that its roof has no recorded permits. Explain a no-match
result without inventing records.

This lookup is for property records. Do not require it before opening the
cost calculator or roof color visualizer, which operate independently of
record coverage. The public connection does not support bulk database exports.
