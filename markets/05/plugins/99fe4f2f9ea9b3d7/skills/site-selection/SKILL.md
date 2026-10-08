---
name: site-selection
description: >
  Structured workflow for evaluating one or more candidate retail locations
  using Advan REI foot traffic, trade area, competitive, and cross-shopping
  data. Use this skill whenever a user is assessing whether a site is a good
  fit for a retailer or tenant, comparing multiple candidate locations,
  evaluating market demand at a specific address, or analyzing cannibalization
  risk from a nearby existing store. Trigger on phrases like "should we open
  here", "evaluate this site", "compare these locations", "is this market
  viable", "how does this site stack up", "would this cannibalize our
  existing store", "what's the co-tenancy like", or any request that frames
  a location decision. Also trigger when a broker, retailer, or developer
  asks about a site's potential without using explicit site selection language.
---

# Site Selection Workflow

Site selection answers a decision question: is this a good location, and for
whom? The workflow is data-driven but ends with a directional take — not just
a data dump, but a read on what the numbers mean for the decision at hand.

The workflow has two modes depending on what the user is evaluating:

- **Single site:** Full analysis of one candidate location.
- **Multi-site comparison:** Run the same analysis for each site, then
  synthesize a side-by-side at the end.

Both modes follow the same stages. For multi-site, run all stages for each
location before moving to synthesis.

---

## Before You Start: Orient the Request

Before pulling data, make sure you understand three things. You may already
have them from context — if so, proceed. If not, ask one focused question
rather than a list.

1. **What location(s) are being evaluated?** An address, a named property, a
   market area?
2. **Is there a specific retailer or tenant in mind?** This drives the
   co-tenancy and cannibalization steps. If no retailer is specified, those
   steps are still useful but framed more generally.
3. **What's the decision?** Opening a new store, evaluating a lease, advising
   a client, underwriting a development? The answer shapes what you emphasize
   in the synthesis.

---

## Stage 1: Resolve the Location(s)

If the user named a specific existing property, use ALI, location name, and
company name as usual. If they provided an address or a general description
of a candidate site, use `search` to find the closest matching property or
reference location. Confirm before proceeding if there's any ambiguity.

For multi-site comparisons, resolve all locations before moving to Stage 2.

---

## Stage 2: Subject Site Performance

If the candidate site is an existing property with traffic data (an occupied
center, a current tenant location), pull `traffic-summary` for it. This
establishes baseline performance at this specific location and gives the user
a sense of what the site has historically attracted.

If the site is vacant, a raw address, or a new development with no existing
traffic history, skip this step and note it. The trade area and competitive
context in later stages will carry the location assessment.

Use the date range from the UI or as specified by the user.

---

## Stage 3: Trade Area

Call `trade-area` using the same parameters established in any current session
trade area settings, or default to the closest 70% of visitors if no setting
is available and the user hasn't specified otherwise.

This tells you who is realistically accessible from this location. Capture:
- Approximate size (radius or drive time)
- The geographic shape — is it symmetric, or constrained by highways, water,
  or dense competition on one side?

You don't need to run the full demographic deep-dive here unless the user
asked for it — that's covered in a standalone trade-area-analysis. For site
selection, the key output is the catchment footprint and a top-line
demographic read (median HHI, dominant age cohort) to assess fit with the
intended tenant.

---

## Stage 4: Competitive Landscape

Use `ranking` and/or `performers-list` to identify how competing properties
in the area are performing. Then pull `traffic-summary` for the most relevant
competitors — typically the 2–3 strongest nearby alternatives that would be
drawing from the same trade area.

What you're looking for:
- Is there a dominant competitor already capturing the majority of foot
  traffic in this catchment?
- Are there underperforming competitors that might signal market weakness —
  or an opportunity if the right tenant fills the gap?
- How does traffic at nearby properties trend? Growing markets tend to lift
  well-positioned sites; declining markets carry more risk regardless of
  individual site quality.

Flag the competitive intensity plainly. A site surrounded by strong
performers in the same category is a much harder entry than one where
competition is fragmented or underperforming.

---

## Stage 5: Co-Tenancy and Cross-Shopping

Use `shared-customers` or `shared-customers-retailer` to understand what
other retailers the visitors in this trade area frequent.

If a specific retailer or tenant is in mind, this step answers: are the
customers already here aligned with that retailer's typical shopper? Look for
strong affinity with anchor tenants or complementary categories that would
support the intended use.

If no specific retailer is named, use this step to characterize the trade
area's retail DNA — what categories and brands dominate customer behavior —
and flag whether the site has the co-tenancy to support the type of use the
user is evaluating.

**Co-tenant health check:** For the most significant co-tenants at or near
the candidate site, pull `traffic-summary` and `ranking` to assess whether
they are strong performers. A site with declining or underperforming anchors
is a materially different proposition than one with healthy, growing
co-tenants. Look for:
- YoY traffic trend for key co-tenants — growing, flat, or declining?
- Ranking within their submarket or category — are they top performers or
  laggards?
- Any co-tenant weakness that could signal a future anchor departure or
  reduced draw

Flag co-tenant risk directly if the data shows it. A retailer opening next to
a struggling anchor takes on indirect risk that isn't visible in the site's
own trade area data.

---

## Stage 6: Cannibalization Check (Conditional)

Run this step only if both of the following are true:
- A specific retailer or brand is identified as the potential tenant.
- That retailer has one or more existing locations within a plausible draw
  distance from the candidate site (typically within the trade area or
  overlapping trade area).

If both conditions are met:
1. Pull `traffic-summary` for the existing nearby location(s) of the same
   brand.
2. Pull `trade-area` for the existing location(s) and compare the geographic
   overlap with the candidate site's trade area.
3. Estimate the degree of overlap: do the two trade areas share significant
   geography? If the candidate site's trade area is largely contained within
   the existing location's trade area, cannibalization risk is high. If
   there's limited overlap — the sites serve distinct neighborhoods or the
   candidate site extends reach into a new population — risk is lower.

Present the cannibalization finding clearly and without burying it. If the
overlap is significant, the user needs to know before making a decision.

> "The candidate site's trade area overlaps substantially with the existing
> [Brand] at [Location] — roughly [X]% of the potential customer base is
> already being served. That doesn't rule out this site, but it means the
> incremental opportunity is smaller than the raw trade area would suggest."

If the conditions aren't met, skip this step entirely — don't raise
cannibalization as a concern if there's no nearby same-brand location to
evaluate against.

---

## Stage 7: Comparable Benchmarking

Use `ranking` to benchmark the candidate site — or the most comparable
existing property at or near it — against similar properties in the market.
This establishes whether this location is performing at, above, or below what
you'd expect for the submarket.

For a multi-site comparison, this is where you start to see which site sits
in the stronger performing market and which has the better trajectory.

---

## Stage 8: Retailer Footprint Fit (Conditional)

Run this stage only if a specific retailer is named. Skip it if the analysis
is general or the tenant is unspecified.

Invoke the **retailer footprint skill** in site comparison mode, using the
candidate site as the subject property and the named retailer as the
comparison target. That skill handles all data pulls and interpretation —
don't re-implement the logic here.

For a multi-site comparison, run the retailer footprint skill for each
candidate site and carry the fit assessment (strong / moderate / weak) into
the Stage 9 synthesis. This stage frequently produces the clearest
differentiation between sites: which one's behavioral and demographic profile
most closely matches where the retailer already succeeds.

---

## Stage 9: Synthesize and Present

### Search for real-world context

Do a targeted web search before writing the synthesis. Useful angles for
site selection:
- Recent retail openings, closings, or announced deals in the submarket
- Development pipeline — new supply coming that could affect the competitive
  picture
- Local economic conditions, employment base, population growth
- Any news specific to the retailer being evaluated (expansion plans,
  category performance, brand momentum)
- Infrastructure changes — new transit, road projects, or access changes
  that could affect the catchment

Weave in what's relevant. Skip what isn't.

### Lead with the directional take

Don't open with a table. Open with a clear read on what the data says about
this site.

> "Based on the data, [Location] looks like a credible opportunity for
> [Retailer/Use]. The trade area is well-populated and the competitive set is
> fragmented — no dominant player is locking up this catchment. The main
> risk is [X]."

Or if the picture is mixed:

> "[Location] has a strong trade area but faces meaningful competitive
> pressure from [Competitor], which is already capturing a large share of
> foot traffic in the immediate catchment."

Be direct. The user is making or informing a decision — they need a clear
signal, not just a list of considerations.

### Summary table

| Factor | Finding |
|--------|---------|
| Subject site traffic | [X visits / period, +/-Y% YoY — or N/A if vacant] |
| Trade area size | ~X miles / Y-min drive (Z% threshold) |
| Trade area HHI | $X median |
| Competitive intensity | [Low / Moderate / High] — [brief note] |
| Top cross-shopping affinity | [Brand/category] |
| Cannibalization risk | [Low / Moderate / High — or N/A] |
| Submarket rank | #X of Y comparable properties |
| Retailer footprint fit | [Strong / Moderate / Weak — or N/A] |

For multi-site comparisons, run this table with one column per site so the
user can compare directly.

### Supporting narrative

Two to four sentences covering what the numbers mean together. Highlight
convergent signals (multiple data points pointing the same direction) and
flag any divergence (e.g., strong trade area demographics but high
competitive saturation). If external context from the web search adds
something meaningful, work it in here.

### Cite data vintage

> *Analysis based on [date range], via Advan's mobile device panel.*

---

## Handling Gaps

**No traffic data for the candidate site:** Common for vacant or new
locations. Note it, skip Stage 2, and let the trade area and competitive
data carry the assessment.

**No nearby same-brand locations for cannibalization:** Skip Stage 6 without
comment — don't raise it as a concern when there's nothing to evaluate.

**Partial competitive data:** Present what's available, note what's missing,
don't fill gaps with speculation.

---

## Follow-Ups

Let the conversation lead. The most natural next steps from a site selection
analysis are usually a full demographic breakdown of the trade area, a void
analysis to identify which tenant categories would fit the customer base, or
a deeper competitive pull on a specific competitor that came up in the data.
Mention one if it's obviously relevant — otherwise let the user direct.
