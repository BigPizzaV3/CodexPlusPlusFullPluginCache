---
name: roof-records
description: >-
  Look up roof age by address, roofing permit history, roof material, roof shape,
  and recorded condition scores with GetRoofReport. Use for "How old is my roof?"
  or "Check the roof replacement permits before I buy this house." Explain the
  available records, roof-age confidence, and basis for supported properties.
  Address records currently cover Florida; this is a records review, not an
  on-site roof inspection.
---

# Roof age and permits

Call `get_roof_attributes` with the supplied address, known permalink, or
county and parcel ID. For an ambiguous address, use `search_addresses` and
have the user identify the property before retrieving its records.

Explain the returned roof age together with its confidence and basis. Keep
permit dates, inferred age, and condition scores distinct. Link to `reportUrl`.
Current records cover Florida; explain unsupported lookups without inventing
an age, permit history, or condition assessment.

A records lookup is not a physical inspection or an image diagnosis. It does
not establish present damage or whether replacement is necessary. For a
homebuyer, combine risk or insurance records only when relevant to the request.
