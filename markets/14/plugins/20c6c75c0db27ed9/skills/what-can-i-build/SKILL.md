---
name: what-can-i-build
description: Answer what a homeowner can build on a specific US property (an ADU, backyard cottage, in-law apartment, home addition, pool, new home or multi-family) or under a city's ADU rules, using FutureLot's zoning analysis.
---

Use this skill when someone asks what they can build on a property or whether a project is allowed.

1. If the question names a property, call `find_property` with the address as given. If it returns
   `exact: false`, the address is not on record and this is the nearest lot on that street: ask whether
   they would like the report for that lot, check it on yes, point to the map button on no, never offer
   the typed address as an option, and never look it up again. If the user has not named a property, ask for the street address of the property
   they want to research; never ask for their own location.
2. If `coverage` is `not_covered`, say FutureLot has not covered that city yet, give no limits, and
   offer the property link.
3. For an ADU (backyard cottage, garage conversion, in-law or basement apartment) call
   `get_adu_feasibility`. For a home addition, pool, new or replacement home, or a duplex or more units
   call `get_project_feasibility` with the matching project.
4. Answer with the verdict first, then the numbers that matter (maximum floor area, footprint, units),
   then the conditions that change the answer. Keep apart what zoning allows, what appears to fit on
   the lot, and what still needs a site check.
5. End with the property link from `report_url`, where the user sees setbacks and the buildable area
   and can try the project on their lot.

For a city with no property in mind, call `get_city_rules`. Never mention prices or offer anything for
sale.
