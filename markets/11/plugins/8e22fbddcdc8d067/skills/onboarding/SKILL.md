---
name: onboarding
description: Show a useful trip immediately when someone sets up TripNoted or asks how to get started or what it can do. Use a saved trip, the current chat, or a search of available older chats and memories. If no useful trip is available, show a clearly marked sample. Do not save automatically. Also answer questions about connecting an account, keeping trips or importing bookings. Use trip-planning for requests to plan a specific trip.
---

# Get started with TripNoted

The traveler's own instructions come first. For setup, getting started or a general introduction, show a TripNoted card in this response. Do not ask whether to show a trip first.

Call list_trips to find saved trips and account connection status. Choose one useful trip:

- Prefer the trip the traveler is discussing in this chat. If it is already saved, open it with show_trip(trip_id). Otherwise, show the known plan with show_trip(plan).
- Without a useful trip in this chat, open a relevant saved trip with show_trip(trip_id). Prefer a trip in progress, then the next upcoming trip, then an undated plan. Do not select a cancelled trip.
- If neither gives a useful trip, call the host's history or personal-context search before building a draft. Search for travel plans from older chats and memories; use a remembered destination as a search lead when available. Discover the search tool if needed; use personal_context.search when available. Prefer a current or future plan over an old or abandoned idea. If it matches a saved trip, open that trip. Otherwise, show an unsaved draft from the facts found. If search is unavailable, say so briefly and use useful available memory before the sample. Do not claim to have searched all chats or recovered every trip.
- If there is still no useful trip, show a short sample with show_trip(plan). Name it "Sample: Two days in Lisbon". Use Day 1 for Praça do Comércio and Castelo de São Jorge, and Day 2 for Mosteiro dos Jerónimos and Pastéis de Belém. Mark the sample clearly in the card description and reply. Do not present it as the traveler's own plan.

For a draft from past context, use one of these two source labels in both the card description and reply:

- "Draft from an older chat": only when you can include a returned source chat citation or link that supports the trip facts. Include that citation or link. Examples, test chats and assistant-generated itineraries are not evidence of the traveler's own plans.
- "Draft based on memory": when you have useful remembered facts but cannot cite the original chat. Use the remembered destination, duration and traveler preferences to make a new proposed route. Set the card description to "Draft based on memory. This route and these activities are new suggestions, not recovered plans or bookings. Nothing has been saved." Use the same source label in the reply. Do not describe an alleged original conversation, its title or date, or earlier recommendations.

A search call alone does not prove that a source chat was found. Never invent a source citation or link.

For drafts, keep unknown dates and times empty and use day numbers for undated items. Preserve a known trip length; the card must not show a shorter trip. If the source gives only a destination and duration, make a proposed outline for that duration and identify added stops as new suggestions in the card and reply, not recovered facts. Do not invent bookings, addresses, coordinates or photos. Distinguish proposed activities from confirmed bookings.

Do not call save_trip or change a saved trip during onboarding. Showing a draft does not save it. The traveler can choose Save on the card later.

After the card, reply in one or two short sentences. Say whether it is a saved trip, a draft from this chat, a draft from a retrieved older chat, a draft based on memory, or a sample. For a draft or sample, say it has not been saved. Offer one relevant next step, such as changing a day or replacing the sample destination. Do not suggest connecting an account when one is already connected.

For a specific question about account connection, saved trips or email import, answer that question directly; a sample is not needed. Connecting an account is optional for planning here. Gmail import needs a separate connection in TripNoted.

Never ask for passwords, sign-in codes or email contents in the chat. TripNoted does not book travel.
