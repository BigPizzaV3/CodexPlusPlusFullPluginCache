---
name: google-event-research
description: Find events shown by Google for a place or query, or expand a selected event's details with HasData. Use for event listings, dates and venues, not booking tickets or Google Maps business posts.
---

# Find Google events

Read `../hasdata-research/SKILL.md` and `../hasdata-research/references/tool-contract.md`.

Call `hasdata_google_serp_serp_getSearchResults` with the user's event query and relevant supplied geography. Inspect eventsResults; Light is not the event-discovery tool. Start with one full results page.

List the actual returned event titles, date wording, venues and original links. A missing eventsResults collection in a successful response means events were not returned for this fetched scope, not that the city has no events.

When selected event details are requested, immediately call `hasdata_google_serp_events_getEventInformation` with that entry's exact pageToken. It expires within a few minutes and the details tool does not accept a city or keyword. A search plus one expansion needs up to two requests. Do not guess a token, expand every event automatically or refresh an expired token without authorization.

Preserve timezone/date uncertainty and source links. A listing is not confirmation of ticket availability or a booking.
