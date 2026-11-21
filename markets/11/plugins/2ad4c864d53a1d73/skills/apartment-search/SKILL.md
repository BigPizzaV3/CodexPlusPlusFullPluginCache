---
name: apartment-search
description: Search NYC rental apartments with Buzzedin and help a renter set up an alert for their search. Use when someone wants NYC rental listings, lease takeovers, neighborhood rent comparisons, or notifications for new matching apartments.
---

# Find apartments with Buzzedin

Use `search_listings` for current NYC rental inventory. Pass the user's constraints through the tool's structured schema. Ask for clarification when a neighborhood or constraint is ambiguous. Never silently drop a constraint to produce more results.

Use the returned apartment view and include a few relevant listing links in the chat. Keep all claims grounded in returned facts. The overall deal score and selected structured apartment features (such as laundry, outdoor space, pets and light) are public previews when available. Enrichment and scores are estimates, not guarantees. Source photos, source descriptions and detailed premium quality breakdowns are not available through this plugin.

Do not advertise `/search` as a public browsing page or link there to view all matches. Use tool pagination for more results.

If the renter wants notifications, use `create_alert_link` with the same search filters. Explain that they sign in with a free Buzzedin account to finish saving the search as an alert. Returning a link does not create an alert.

A building with rent-stabilized units is not proof that a particular apartment is stabilized. Tenant-posted listings are direct from the tenant, not verified listings. Do not describe neighborhoods as safe, unsafe, good or bad. Do not offer sublets, contact landlords, book viewings or submit applications.

When there are no matches, explain that result and offer to broaden the search or set up an alert. When a call fails or is rate limited, explain the limitation and offer to retry in the chat. Do not invent listings or claim success.
