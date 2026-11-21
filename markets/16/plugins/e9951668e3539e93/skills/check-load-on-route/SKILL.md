---
name: check-load-on-route
description: Check whether a heavy or oversized load can travel a route surveyed in RouteSurvey, and explain where and why it is blocked. Use when the user asks if a load fits a surveyed route, what the largest load on a route is, or how several load options compare on it.
---

Use this skill when the user wants to know whether a load can use a surveyed route. Explicit instructions from the user take priority over this skill.

## What you need

- **The route.** If the user names it, find it with `routesurvey_list_routes`, passing the name as `query`. If several routes match, or none does, show what was found and ask which route they mean. Never pick one silently.
- **The load:** height, width and weight, plus the ground clearance when rail crossings matter. Pass the values with the units the user gave, such as "15 ft 6 in" or "617,000 lb"; the tool converts them. Without a load, the cargo of the route's planned route is used when there is one; say so when that happens. Ask for a missing dimension instead of inventing it.

## Steps

1. Call `routesurvey_check` with the route id and the load.
2. Give the verdict in the first sentence, then the survey points that decide it, with their kilometre positions and the measures they need.
3. Report points that lack the needed measurement as missing data, never as clear.
4. Say that the result supports, and does not replace, the route engineer's sign-off.

## Follow-ups to offer

- The largest load the route can take: `routesurvey_envelope`.
- Several load options side by side: `routesurvey_compare`.
- Photos of a deciding point with `routesurvey_get_point`, or of the whole route with `routesurvey_photos`. The photos appear in the RouteSurvey card; never put image links in the reply.
- A photo report PDF for a client: `routesurvey_report`. Tell the user that anyone with the link can open it until it expires, after 7 days unless they ask for another period.

Do not record measurements or change the route unless the user explicitly asks for that change.
