---
name: mappu-trip-handoff
description: Hand a trip plan written with the traveler to Mappu as a draft only its link can open, which they keep by signing in, or point them to Mappu's own planner or importer. Never performs purchases or account changes.
---

# Hand a travel plan back to its traveler

Read [authentication and permission boundaries](https://www.mappu.ai/auth.md).
Confirm what the traveler wants: browse an example, keep a plan you wrote
together, plan from scratch in Mappu, or import a plan they already have. Ask for
missing trip details only when they are necessary; never ask for credentials,
contact details or payment information.

For examples, cite the exact canonical itinerary page. A published example has
not been saved to their account.

Before planning, call `mappu_get_trip_planning_guide` on `https://api.mappu.ai/mcp`
and follow it: it is how Mappu's own planner works and writes, in Mappu's warm
local-guide voice. In short, plan around the traveler's own request and interests:

- Give each day a theme and group its stops by area so the route does not double
  back. Morning, afternoon and evening each include a real place.
- Put stops in the order they happen, with real start times that leave time to
  get from one to the next. Check opening days against each day's actual
  weekday, holidays and the season; never schedule a known closure.
- Name a restaurant or bar only when you are confident it exists and fits;
  otherwise name the market, street or district.
- Write like a guide: what each place is, why it suits this traveler, what to
  look for, and one insider tip. Do not invent prices or schedules.
- Mappu's published walks and audio guides are extras: add one as a stop where
  it fits, never as the outline of a day.

To keep a plan you wrote together, call `mappu_save_trip_plan` on
`https://api.mappu.ai/mcp` with the whole plan at the depth you gave in the
conversation: a title and a short summary, the traveler's language, the
destinations, optional dates, and for each day a themed title, its stops in
order (start time, description, tip, and the place as "Place, City" for the
map), the day's food and its practical tips. Mappu finds the places after the
traveler keeps the draft. Use one `idempotencyKey` per plan and reuse it only to
retry the same plan.

Give the returned `claimUrl` to the traveler and to nobody else; the draft is
viewable only with the code in that link. Tell them what happens next: they open
the link, press Keep this plan and sign in or create a free Mappu account; the
plan is added to My Trips and opens in Mappu. Mention that the draft expires after 7 days
unless kept. Saving runs no model, books nothing, buys nothing and spends no
credits.

If the tool is unavailable or refuses the plan, say so. As alternatives, direct
the traveler to `https://www.mappu.ai/` to plan from scratch, or to
`https://www.mappu.ai/tools/import-my-itinerary` to paste a plan they already
have. Do not encode private trip text into URL query parameters.

Let the traveler complete sign-in, security challenges, privacy/legal choices,
generation, editing and any purchase inside Mappu. Do not reuse the app's OAuth
client or browser tokens, and do not call account or credit APIs.

Report only what actually happened. A link is a handoff, not a kept trip,
confirmed booking or purchase.
