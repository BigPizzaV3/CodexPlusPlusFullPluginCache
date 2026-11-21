---
name: roof-planning
description: >-
  Plan a roof replacement or review a home's roof with GetRoofReport's roof cost
  estimator, roofing calculator, roof color visualizer, and property roof reports.
  Use for combined requests such as "Help me budget for a new roof and compare
  shingle colors" or "I'm buying a house; review its roof age, permits, and storm
  risk." Calculator and visualizer launches are independent of location; address
  records currently cover Florida.
---

# Roof planning with GetRoofReport

Use the connected RoofReport MCP tools for the homeowner's requested task.
The calculator and visualizer open independently of property-record coverage.
Do not require a Florida address or run an address lookup before opening them.

## Replacement cost

Call `estimate_roof_cost` when the user wants a roof replacement estimate,
roofing calculator, or the cost of a new roof. An empty argument object opens
the estimator. Address details and `squareFeet` are optional context; supply
them only when the user gives them.

Show the full calculator when the host supports its embedded view. The user
enters their property details inside that calculator. The tool does not return
a calculated price and chat arguments do not prefill it. Do not substitute an
invented quick estimate for the calculator or claim that a quote was produced.
If the host does not show the embed, offer the returned `quoteUrl`.

## Roof colors

Call `preview_roof_color` to visualize a roof color on a house photo, compare
shingle colors, or find examples from a named brand or product line. Optional
`brand`, `line`, and `color` arguments search the shingle catalog. They do not
prefill the photo visualizer. The user uploads their house photo inside the
visualizer; this tool cannot accept the photo as an argument.

Use returned catalog examples for product-specific questions. For a photo
preview, show the embedded visualizer where supported, or offer the returned
`visualizerUrl`. Claude's current package uses catalog cards and external links
because nested frames require host security review. Do not describe a catalog
photo as a generated preview of the user's house.

## Property records and homebuyer review

- Use `search_addresses` for a partial or ambiguous street address. Reuse the
  returned permalink for subsequent calls rather than guessing a parcel.
- Use `get_roof_attributes` for roof age, its confidence and basis, material,
  shape, condition score, and roofing permit records.
- Use `get_risk_profile` for historical hurricane/hail exposure and available
  wind, flood, evacuation, and sinkhole risk information.
- Use `get_insurance_profile` for the records-based four-point outlook,
  inferred wind-mitigation features, and insurance context.

For a homebuyer, combine only the records relevant to their question and link
to the returned `reportUrl`. Ask for an address if one is needed. If the tool
returns multiple candidates, let the user identify the property. Current
property records cover Florida; clearly explain an unsupported lookup without
implying that all US addresses have reports. Do not redirect a cost or color
request into a property report just because its address is unsupported.

A records review is not an on-site or image-based roof inspection. Roof age,
historical exposure, and condition scores do not establish current damage,
replacement need, or insurance eligibility. Keep the basis and uncertainty
visible. This public connection exposes six tools; it does not provide bulk
SQL access, certified inspections, or an automated contractor purchase.

If the RoofReport tools are not connected, explain how to connect the plugin's
MCP server at `https://getroofreport.com/public/mcp` with no authentication, or
offer the relevant tool page on `https://getroofreport.com`.
