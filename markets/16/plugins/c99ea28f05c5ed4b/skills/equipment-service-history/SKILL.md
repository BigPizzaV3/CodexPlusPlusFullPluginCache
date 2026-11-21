---
name: equipment-service-history
description: Use when someone asks about a piece of equipment in Binto: when it was last serviced, what was done, what it cost, who did the work, or what service is due.
---

# Equipment service history

Answer from Binto records only. Everything here is read-only.

1. If you do not know which Organization the person means, call `organizations_list`. With one Organization, use it. With several, ask which one, then pass its `id` as `organizationId` on every call.
2. Find the equipment. Call `asset_find` with the person's words (for example "walk-in cooler" or "rooftop HVAC"). If they named a Location, call `location_resolve` first and pass its `locationId`. If several records match, ask which one.
3. Call `asset_history` with the `assetId`. It returns the service records, most recent first, with dates, what was done, cost and who did it. Use `lookFor` when they ask about one thing, such as a compressor or a filter.
4. For the equipment's own details and dates (warranty, next service), call `asset_get`.

When you answer:

- Lead with the most recent service: the date, what was done, and who did it. Then older entries if they asked for the history.
- Give costs only when the record has them. Do not add them up unless asked, and say which entries the total covers.
- Cite each record from `sources`, and include its link from `links`. Links open in Binto and need the person to be signed in.
- If there is no service record, say that none is recorded. Do not infer one from other dates.
