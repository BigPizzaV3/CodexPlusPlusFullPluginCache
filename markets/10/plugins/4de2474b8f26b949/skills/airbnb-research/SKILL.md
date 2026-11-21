---
name: airbnb-research
description: Find Airbnb stays for a location, dates and guests or read a supplied public listing with HasData. Use for short-term rental research, not hotels, Zillow housing or booking accommodation.
---

# Research Airbnb stays

Read `../hasdata-research/SKILL.md` and the Travel section of `../hasdata-research/references/tool-catalog.md`.

Discovery uses `hasdata_airbnb_listing_getAirbnbListings` with a supplied location and checkIn. Collect dates and party details needed for a meaningful priced stay instead of inventing a visit. A complete user-provided map bounding box can replace location only when the live schema supports all four coordinates; do not guess coordinates.

Preserve supplied adults. Omit optional children, infants and pets when the user supplies zero: the upstream API rejects explicit zero for these fields. Include positive supplied counts according to the live schema; never change the guest mix to repair an error. A rejected request is not permission for an automatic paid retry.

For a supplied listing URL or selected returned listing, use `hasdata_airbnb_property_getAirbnbPropertyDetails` with url. Details have a different schema; do not pass discovery dates or guest filters that the details tool does not accept.

Compare only returned listing name, source URL, amenities, rating, location and price wording. Preserve the currency, dates and nightly/stay-total basis when established. If details do not establish a date-specific price or availability, say so rather than inheriting those facts from another request.

Use actual nextPageToken only for requested bounded continuation. Do not book, contact hosts, enter traveler documents or promise confirmed availability.
