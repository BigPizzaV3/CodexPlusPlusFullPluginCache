---
name: trade-area-analysis
description: >
  Workflow for defining and analyzing the trade area of a retail property using
  Advan REI mobile visitor origin data. Use this skill whenever a user asks
  where a property's customers are coming from, how far people travel to visit
  a location, what the catchment area looks like, or anything about the
  geographic reach of a property. Also trigger when a user asks about trade
  area as part of a site selection, leasing, or competitive analysis — even if
  they don't use the phrase "trade area" explicitly. Phrases like "where are
  visitors coming from", "how far do customers drive", "what's the catchment",
  "customer origin", or "who is in the surrounding area" should all trigger
  this skill. Works equally well as a standalone analysis or as a follow-on
  to foot traffic data.
---

# Trade Area Analysis Workflow

The trade area analysis answers a different question than foot traffic: not
how many people visit, but *where they come from*. The output is geographic —
a picture of the real catchment area built from actual visitor origin data,
not assumed drive-time rings.

The workflow has four stages: resolve the property, pull the trade area and
characterize its size, layer in a demographic snapshot, and synthesize with
real-world context.

---

## Stage 1: Resolve the Property

Same as foot traffic. If the user has already provided or confirmed an ALI,
location name, and company name — or if these were established earlier in the
conversation — carry them forward and proceed.

If the property is ambiguous, use `search` to find it, present the top
results, and confirm before pulling data.

---

## Stage 2: Pull the Trade Area

Call `trade-area` with the resolved property identifiers.

**Parameters:** Determine the threshold in this order:

1. **User specified it in the conversation** (e.g., "show me the 50% trade
   area", "use the 80% catchment") → use that, regardless of app settings.
2. **User is in the REI app and hasn't specified** → use whatever threshold
   they have configured in their trade area settings.
3. **No app, no specification** → default to the closest 70% of visitors.

**Date range:** Use the period the user has selected in the UI, or whatever
they've specified. Only ask if it's genuinely unclear.

### Characterize the size

The trade area is defined by where visitors actually originate, not by an
artificial ring — but users need a tangible sense of scale. From the returned
data, derive and report the approximate size in one of these terms, whichever
is most natural given the geography:

- **Radius:** "The trade area extends roughly X miles from the property"
- **Drive time:** "Most visitors are within a Y-minute drive"
- **Both:** Use both when the shape is notably asymmetric or the market
  warrants it (e.g., a coastal or highway-adjacent location where drive time
  and radius diverge meaningfully)

If the trade area is unusually compact or unusually large relative to what
you'd expect for the property type, flag it — it may reflect a dense urban
setting, strong competition nearby, or a destination-oriented tenant mix.

---

## Stage 3: Demographic Snapshot

Call `demography` for the trade area using the same property and date range.

By default, surface a concise top-line snapshot — enough to characterize
who's in the catchment without overwhelming the response. Focus on the
signals most relevant to a real estate or retail professional:

- Median household income (and whether it skews upper/lower relative to
  the metro)
- Dominant age cohort(s)
- One or two standout lifestyle or psychographic segments if they're
  meaningfully concentrated

End the snapshot with a natural offer to go deeper:

> "Want me to break this down further by income band, age distribution, or
> lifestyle segment?"

Don't pull `demography-categories` unless the user asks for the full
breakdown — it's there for drill-down, not the default view.

---

## Stage 4: Synthesize and Present

### Search for real-world context

Before writing the narrative, do a targeted web search to find anything that
helps explain or enrich what the data is showing about the catchment. Useful
angles include:

- Economic character of the trade area (affluent suburb, dense urban core,
  working-class exurb, etc.)
- Major employers or demand generators within the catchment
- Population growth or demographic shifts in the area
- Infrastructure or access factors that shape the catchment (highways,
  transit, topographic barriers)
- Competitive landscape — are there strong competitors drawing from the
  same geography?

As with foot traffic: if the search turns up something that connects, weave
it in. If it doesn't, move on. The goal is context that helps the user
interpret the trade area, not filler.

### Lead with the headline

One sentence that captures the essential story — size, character, and
anything notable.

> "Riverside Commons draws the bulk of its visitors from a roughly 4-mile
> radius, a trade area anchored by the upper-middle-income neighborhoods of
> Maplewood and Crestview, with a median household income around $95K."

### Trade area summary

After the headline, a short structured summary:

| | |
|---|---|
| Trade area threshold | 70% of visitors (or whatever was used) |
| Approximate size | X miles / Y-minute drive |
| Median HHI | $X |
| Dominant age cohort | X–Y |
| Key lifestyle segments | [top 1–2] |

Keep this tight. The table is a reference, not the analysis.

### Narrative

Two to three sentences connecting the geographic and demographic picture to
something actionable. What does this trade area mean for the property? Think
about:

- Whether the catchment is concentrated or dispersed (and what that implies
  for co-tenancy or marketing reach)
- Whether the demographic profile aligns with the current tenant mix — or
  suggests an opportunity
- Any geographic constraint or advantage worth flagging (a highway that
  extends reach to the east, a river that cuts it off to the west)
- Anything from the web search that adds color

### Cite data vintage

> *Trade area and demographics based on [date range], via Advan's mobile
> device panel. Trade area defined as the closest [X]% of visitors by origin
> (per [user's REI app settings / default threshold].)*

---

## Handling Gaps and Anomalies

**No trade area data returned:** Say so plainly and offer to escalate or
check a comparable.

**Unusually small or large catchment:** Flag it and offer a hypothesis if
one is obvious from context (dense competition, destination anchor, barrier
geography). Don't just report it as a fact without comment.

**Demographic data sparse or incomplete:** Present what's available, note the
gap, don't fill it with estimates.

---

## Follow-Ups

If there's a natural next direction given what the data showed, mention it.
The most common ones that arise organically from trade area work are
cross-shopping (who else in the catchment are these visitors going to?),
void analysis (what tenant categories are underrepresented given this
demographic profile?), and competitive context (how does this catchment
compare to a neighboring center?). But let the conversation lead — don't
recite options.
