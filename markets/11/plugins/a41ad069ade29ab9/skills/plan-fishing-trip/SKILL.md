---
name: plan-fishing-trip
description: Plan a fishing outing with FishFriender when the user asks where or when to fish, compare fishing conditions, find waters or spots, or choose tackle for a target species.
---
Identify the location, date and target species when needed. Ask for missing essentials. Never guess coordinates from a vague place name; use a returned spot or water location or coordinates the user supplies. Resolve relative dates using the fishing location's timezone and state the chosen date.
Use find_fishing_spots or find_waters when the user needs a location. Follow the exposed schema and distinguish discovery from verified permission to fish.
Call get_weather_forecast and get_solunar for the selected coordinates and date. Use get_tides when relevant to a tidal location. Reuse returned conditions rather than repeating forecast calls for the same place and day.
Use search_species to resolve a species ID and get_species_info when the user needs species details. For tackle advice, use get_my_gear when personalization is requested and get_best_gear_for_species for the selected species. Separate owned tackle from broader catalog recommendations.
Summarize the location and date, practical weather conditions, useful time windows, and relevant tackle. Cite returned source links when present. Preserve units and distinguish forecast values from observations. Solunar activity is a planning indicator, not a guarantee of catches.
Do not claim that a discovered spot permits fishing or that species rules are current based only on the MCP results. Explain unresolved access or regulation questions when they materially affect the plan.
Show supported condition cards. Say when a source is unavailable instead of fabricating results. On missing authentication, missing SCALE access or rate limits, explain the returned issue and avoid repeated calls.
Do not send feedback or any external message unless explicitly requested by the user.
