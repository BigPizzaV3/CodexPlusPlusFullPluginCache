---
name: get-started
description: First steps after connecting Ikuzo. Use when the user has just connected their Ikuzo account, asks what they can do with it, or seems unsure where to start.
---

# Getting started with Ikuzo

1. Call `maps_list` and greet the user with a one-line picture of their account: how many maps, and the biggest one by spots. If they have no map yet, say so warmly.
2. Offer three concrete next steps that fit what you saw, for example:
   - "Show me my map" (uses `maps_show`)
   - "Make a map of the places you want to see in a city" (see the plan-a-trip-map skill)
   - "Find what you saved near a station or a hotel" (uses `places_search` then `spots_nearby`)
3. Mention once, briefly: maps are private unless the user shares them, and every change appears in the Ikuzo app and website right away.

Keep the first reply short. Do not list every tool.
