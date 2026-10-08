---
name: "Plan a ski weekend"
description: "Plan a ski trip - find candidate resorts near the user, compare snow conditions, and show the driving route."
---

When the user wants to plan a ski trip or weekend, follow this flow:

1. Call `search_resorts` with their starting city (`home` - any city name works),
   `isOpen=true`, a reasonable `maxTravelMinutes` (default 180) and `minPistesKm=30`
   to get solid candidate resorts.
2. Call `get_snow_forecast` for the top 2-3 candidates to compare snow conditions
   on the planned dates.
3. Call `get_route` for the user's favorite pick to show the driving route on the map.

Present a clear recommendation: best resort for the dates, expected snow, drive time,
and the route map. Mention season status (isOpen) and link to powly.de for details.
If travel times are estimates (travelEstimated=true), say so.
