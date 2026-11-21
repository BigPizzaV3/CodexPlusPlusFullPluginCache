---
name: plan-freight-route
description: Plan how cargo moves between real places — ports, terminals, inland cities — and show the route on NoMap's map. Use when someone asks how to ship, move, route or send freight between locations, asks how far apart two places are for a shipment, asks which legs or modes a movement needs, or asks to see a freight route on a map.
---

Use this skill for any request about moving cargo between places. It covers a
single question ("how far is Rotterdam to Shanghai?") and a full planning
conversation ("we need these turbines from Hamburg to a site near Chennai").

## Plan the route

Call `plan_route` **once** with the user's request in plain language. Pass the
whole journey in one call, including intermediate stops and a transport mode
when the user named one: `"Rotterdam to Shanghai via Kolkata"`,
`"Munich to Rotterdam by rail"`. Do not split a journey into one call per leg —
the tool calculates the stops itself, and separate calls produce distances that
do not add up.

Report what comes back, in this shape:

1. The places in order, each with the UN/LOCODE the tool returned.
2. One line per leg: the mode, the endpoints, the distance.
3. The total distance when there is more than one leg.
4. The "Open in NoMap" link.
5. The overview caveat.

### Facts you must not invent

- **Never write a UN/LOCODE the tool did not return.** These identify real
  facilities and a plausible-looking guess is a wrong one. If a place has no
  code in the result, name it without a code.
- **Never state a distance, duration or cost the tool did not give you.** No
  estimating from geography, no arithmetic across legs beyond the total.
- **Report the mode the tool calculated, not the mode that was requested.**
  When a `modeFallbacks` entry appears, a corridor for the requested mode was
  not available and the distance shown belongs to the mode actually used. Say
  so plainly: "rail was requested, but the 2,787 km figure is a road routing."
  Presenting a road distance under a rail label is the specific error this
  rule exists to prevent.
- Distances are planning overviews, not navigational advice. Carry that
  caveat into your answer; do not present figures as sailing or driving
  directions.

### When a place cannot be identified

The tool returns an error naming what it could not resolve, often with
candidate places. Do not pick one and continue. Show the candidates, ask the
user which they meant, then call `plan_route` again with a clearer query. If
there are no candidates, ask for the country or the nearest port or city.

## Show the route

When the user wants to see the route — "show me", "map", "picture", "what does
that look like" — call `route_map` with the same query.

**Display exactly what the tool returns.** Never draw, generate, sketch or
recreate a map of your own, and never substitute another image, however
convenient. An invented map misrepresents a calculated corridor, which is the
whole reason this tool exists.

Leave `inlineImage` false. Set it only if you can decode a base64 image block
into a picture — a client that inlines base64 as text turns a map into roughly
180,000 tokens of gibberish and shows the user nothing.

Use `stats: "none"` when the user wants only the corridor; the default `"all"`
draws the full planning card with the distance panels.

## Search and fetch

`search` and `fetch` exist for flows that need a result identifier before the
detail — deep-research style retrieval. `search` resolves a request into
results carrying an id; `fetch` returns the full route for one of those ids.

For an ordinary planning request, call `plan_route` instead. It returns the
same route in one step.

## Stay inside the workflow

These tools calculate routes between places. They do not know about live
vessel positions, freight rates, customs or tariff rules, permits, vessel
availability or delivery dates. When a request needs one of those, answer from
your own knowledge if you can and say plainly that it does not come from
NoMap — do not imply the tools confirmed it.

See `references/tool-results.md` for the fields each tool returns and how to
read them.
