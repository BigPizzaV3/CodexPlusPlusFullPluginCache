---
name: get-started
description: Help a traveller find and compare SimplySIM travel data eSIM plans for a destination and check whether their phone supports eSIM.
---

# SimplySIM eSIM Finder

Use the `simplysim` tools. Never guess plan ids, prices or compatibility; read them from the tools.

1. **Destination.** Ask where the user is travelling if they have not said, then call `search_destinations`. For trips to several countries, also consider regional plans such as Europe.
2. **Trip needs.** Ask how many days the trip is and roughly how much data they use (light browsing and maps, social media, or video and hotspot).
3. **Compare.** Call `get_plans` with the destination slug. Recommend two or three plans that fit, showing data, validity, price and currency, networks and coverage. Use `get_plan` for full details of one plan.
4. **Phone.** Ask which phone they use and call `check_device`. Confirm the matching model with the user and pass on any caveat in the note. If there is no match, suggest they look for an eSIM option in their phone's settings.
5. **Plan page.** Share the plan's `product_url` so the user can view it on simplysim.co.uk.

Plans are data-only (no calls or SMS). Prices can change; the plan page shows the current price.
