---
name: get-started
description: Welcome a user who just added Gjirafa Travel. Explain in two or three sentences what it does and offer to search their first bus route.
---

# Get started with Gjirafa Travel

The user has just added Gjirafa Travel. Keep the welcome short: two or three sentences, in the user's language. If the user has already asked for something, do that instead and skip the welcome: what the user asks always comes before this skill.

1. Say what Gjirafa Travel does: it finds intercity bus routes across the Balkans (Kosovo, Albania, North Macedonia, Montenegro) and between the Balkans and the rest of Europe, such as Austria, Germany and Switzerland. Results show departure and arrival times, direct routes and routes with a change, operators and prices. It also answers how paying, tickets and Travel Flex work.
2. Say that tickets are bought on travel.gjirafa.com. Every result links there; nothing is booked or paid in ChatGPT.
3. Mention that Gjirafa Travel can also be opened from the ChatGPT sidebar, which has a search form and popular routes, and that connecting a Gjirafa account lets them see and manage their own bookings ("show my upcoming trips", "until when can I cancel?"); a cancellation or a name change is shown first and only happens after they confirm.
4. Ask where they want to travel, and when. Give one example in their language, such as "Prishtina to Tirana tomorrow" or "Prishtinë – Shkup të premten".

Don't call any tool until the user asks for something. For a new route, follow the `plan-bus-trip` skill; for their own bookings, the `my-trips` skill.
