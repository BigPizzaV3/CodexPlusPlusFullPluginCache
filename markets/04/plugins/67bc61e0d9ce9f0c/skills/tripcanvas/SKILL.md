---
name: tripcanvas
description: Create polished, public, shareable travel itinerary websites. Use whenever someone asks to plan a trip, vacation, road trip, honeymoon, family holiday, weekend getaway, travel route, day-by-day itinerary, or a trip plan they can send to friends or family. Especially useful when they want maps, distances, overnight bases, driving times, or a shareable link.
---

# TripCanvas

Turn an ordinary travel request into a finished public website. The person should not need to know how to write a sophisticated prompt or design an itinerary.

## Create a trip website

1. Infer preferences already present in the conversation.
2. Before creation, collect only the two required facts: destination and exact number of days. Ask at most one concise follow-up if either is missing.
3. Treat dates, travelers, transport, pace, interests, mobility needs, budget style, and must-see places as optional. Do not make the person complete a form.
4. Call `create_trip_website` once the required facts are known. Let ChatGPT show the TripCanvas account connection flow if needed.
5. After creation succeeds with `allowed: true`, call `render_trip_card` with the exact non-null summary fields returned by `create_trip_website`.
6. Lead with the finished result and the public link. Mention that anyone with the link can view it without installing the plugin.
7. Briefly summarize the route, nights, and total distance. Do not paste the entire itinerary into chat when the website is available.

If creation returns `allowed: false`, do not call `render_trip_card` and do not create a replacement website. State the returned reset date and show only `info_url`, identifying it as the official TripCanvas account-and-allowance information page. Never mention or show prices, Paddle, checkout, payment, purchase, upgrade, credits, plans, or subscriptions.

## Modify a trip

When the person asks to alter an existing TripCanvas itinerary, call `change_trip_website` with the existing `trip_id` and their exact request. Do not create a second included website as a workaround.

If the tool returns `allowed: false`, explain only that editing is not available with the current access and that the original website remains available and shareable. Show only the returned `info_url`, identifying it as TripCanvas's official account-and-access information page. Never mention or show prices, Paddle, checkout, payment, purchase, upgrade, credits, plans, or subscriptions. Do not create another website to evade the limit.

If the tool returns `allowed: true`, state that the requested change was applied and share the unchanged public URL.

## Reopen or share

Use `get_trip_website` when the person asks for the link again or wants to share an existing trip.

Use `get_tripcanvas_allowance` when the person explicitly asks how many included trip websites remain or when the allowance resets. Reading the status never uses an allowance unit.

## Boundaries

- Treat transport times, opening hours, prices, visa rules, weather, and availability as changeable information. Do not present generated estimates as confirmed facts.
- Never invent a hotel booking. “Night in Córdoba” means an overnight base unless the person supplied a specific reservation.
- Avoid overloading a day. Prefer a believable trip over maximizing the number of attractions.
- Preserve accessibility and pace constraints even when optimizing a route.
- One new website is included per connected account per UTC month. Reopening, sharing, rendering, or revisiting the same website never uses another allowance unit.
- Editing requires a connected account that owns the itinerary and already has editing access. A trip ID or public URL is never proof of ownership.
