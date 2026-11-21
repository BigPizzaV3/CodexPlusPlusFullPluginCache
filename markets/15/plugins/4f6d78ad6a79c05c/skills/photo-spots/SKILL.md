---
name: photo-spots
description: Find places to photograph or visit around a travel destination with NoFilter. Use when the user asks for photo spots, photography locations, sightseeing places, or NoFilter recommendations for a city or destination.
---

Use NoFilter's `recommend_photo_spots` tool for recommendations from its public
place catalog. If the connector is not available, guide the user to connect it;
do not present general knowledge as a NoFilter result.

Resolve the requested travel destination to a latitude and longitude using a
reliable available map or geocoding source: a question such as "What are the best
places to photograph in Rome, Italy?" should lead to a search without requiring
the user to know coordinates. Reuse destination coordinates already supplied.
Do not ask the user to enter latitude or longitude. If the place is ambiguous or
cannot be resolved, ask for its city, country or landmark; never invent coordinates.
These are destination coordinates, not a request for the person's current GPS
location. Do not infer their home address or collect device location.

A NoFilter account is optional. The connection page offers one daily search without
an account, three with a connected free account, and fifty for existing paying
accounts. Do not tell guests they must register to try the service. Guest allowance
is tied to the authorization browser; account allowance is shared across assistants.
When the result includes `createFreeAccount`, explain in the user's language how
to search for NoFilter in their app store, create a free account and reconnect via
Profile → Settings → MCP: ChatGPT, Claude and more (Connected assistants in earlier versions). Include the returned guide link and
the app-version availability note. Never imply creating an account requires payment.

Call the tool with numeric `lat` and `lng`. The default radius is 25 km; use
`radiusKm` between 1 and 100 only when the user's requested area requires it.
One successful call consumes one daily search, shared across connected assistants.
Reuse a result for follow-up questions about the same area instead of repeating
the call unnecessarily. Do not silently run a grid of searches.

Present the returned places with their NoFilter links and useful distances.
Describe the selection as catalog recommendations, not a definitive worldwide
ranking. The response has names, coordinates, distances, and highlight status;
it does not verify opening hours, admission prices, photo permissions, weather,
live access, or safety. Clearly distinguish any separately sourced context.

If the tool returns `NO_PLACES`, explain the coverage gap and ask before widening
the area. For `DAILY_LIMIT`, report the UTC reset time and any returned free-account
guidance without repeating the call or recommending a purchase. For an authorization error, reconnect through the
client's normal OAuth flow. Never ask for the app's password or session token.
