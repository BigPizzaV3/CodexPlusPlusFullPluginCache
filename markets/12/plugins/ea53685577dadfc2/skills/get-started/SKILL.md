---
name: get-started
description: Help the user find an office or workspace with CoworkingView: private office, managed or serviced office, coworking space, hot or dedicated desk, meeting room or virtual office, starting from city, budget and team size.
---

# Get started with CoworkingView

CoworkingView is a read-only catalogue of office and workspace options: private offices, managed and serviced offices, coworking spaces, hot and dedicated desks, meeting rooms, day passes and virtual offices.

1. Ask for the city (or district), the kind of space (private office, managed/serviced office, coworking desk, meeting room, virtual office) and, if relevant, team size and budget.
2. Call `list_coworking_locations` first to get the exact city slug, then `search_coworking_spaces` with explicit filters (use `workspaceType` for the kind of space).
3. Use `compare_coworking_spaces` for a shortlist, `get_coworking_market_rates` for typical prices in a city, and `get_coworking_space` for the details of one listing.
4. Always show the price period and currency exactly as returned and link to the listing page on coworkingview.com. Never invent prices, availability or amenities.
5. This tool cannot book or contact an operator; send the user to the listing page for that.
