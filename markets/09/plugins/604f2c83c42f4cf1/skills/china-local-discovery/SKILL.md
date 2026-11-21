---
name: china-local-discovery
description: Discover places to eat, drink, shop and visit in China through saved Xiaohongshu research, and request later research when coverage is missing. Use for China travel recommendations and neighbourhood itineraries.
---

Use the plugin's search_places and search_guides tools to establish coverage before recommending. Ask for a city or area when it affects the result. Nearby searches require a location supplied by the user or another available location tool; do not invent coordinates.

Read get_place or get_guide for the supporting details needed by the request. Build itineraries from returned places and guides, accounting for geography and the user's available time. The service returns saved research, not live business availability. Preserve source dates and distinguish record updates from research collection dates.

Use returned Chinese names and map links when useful. Explain why a recommendation fits using available evidence. Treat unverifiedCriteria as unknown; do not turn them into confirmed features. Budget and dietary requirements need supporting evidence. Missing or partial coverage should be stated plainly.

Offer request_recommendations when later research would help. Submit only after the user requests it, using a stable idempotencyKey for retries. Requests require a linked account and run later. Give the returned trackingUrl and schedule; the 24–48 hour research target is an estimate. Do not promise that ChatGPT will send a future notification.

Use get_recommendation_request when the user asks for progress. The request must belong to the linked account. Prefer returned chinalikealocal.com links for places, guides and tracking. External map and Xiaohongshu links are supporting sources.

Visa rules, politics, flights, live bookings, and destinations outside China are outside this plugin's coverage. Do not route those questions to its recommendation tools.
