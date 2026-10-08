---
name: retailer-footprint
description: >
  Workflow for comparing a subject property to a retailer's or category's
  existing location footprint using Advan REI's retailer footprint endpoint.
  The endpoint aggregates all of a retailer's or category's locations within
  a defined radius of the subject site and compares them across foot traffic
  variables, demographics, shared customers, and demographic match score.
  Use this skill whenever a user wants to know how a property compares to a
  retailer's typical location, whether a site fits a retailer's footprint,
  how similar a candidate site is to where a retailer already succeeds, or
  wants to evaluate a retailer's presence in a market area. Trigger on
  phrases like "how does this site compare to [retailer]'s locations",
  "does this fit [retailer]'s footprint", "retailer footprint", "how does
  this property benchmark against [retailer]", or any request that involves
  comparing a site to a specific retailer's or category's existing locations.
  Also trigger as part of site selection when a specific retailer is named.
---

# Retailer Footprint Workflow

This skill has two modes depending on whether the user has a subject site:

- **Site comparison mode:** A subject site is provided. Compare it against
  the retailer's or category's nearby locations to assess fit.
- **Nationwide profile mode:** No subject site. Summarize the retailer's or
  category's footprint nationally, with the option to compare across
  geographies.

Determine the mode from context before proceeding. If a subject site has been
established earlier in the conversation, default to site comparison mode. If
the user is asking about a retailer's footprint generally — "what does
[Retailer]'s typical location look like?", "how does [Retailer] perform
nationally?", "walk me through [Retailer]'s footprint" — use nationwide
profile mode.

---

## Mode A: Site Comparison

### Step 1: Confirm the Inputs

Two inputs are required before calling the endpoint. If either is missing,
ask — don't proceed with assumptions.

**Subject site:** Resolve using ALI, location name, and company name as usual.

**Retailer or category:** Who are we comparing against? This could be a
specific brand (Trader Joe's, TJ Maxx) or a broader category (grocery,
off-price apparel, fitness). If the user named one, use it. If the request
is ambiguous — "how does this compare to similar retailers" — ask them to
specify before proceeding.

**Date range:** Use the UI selection or whatever the user specified.

**Distance:** Default is 100 miles. Don't change it yet — Step 2 will
determine whether an adjustment is warranted after seeing how many locations
the endpoint returns.

---

## Step 2: Call the Endpoint and Assess the Footprint Size

Call the retailer footprint endpoint with the subject site, retailer/category,
100-mile radius, and date range.

Before interpreting the results, check how many locations were returned.
Footprint size directly affects how reliable the aggregate comparison is.

### Too few locations (fewer than 5)

A comparison built on fewer than 5 locations is statistically fragile — one
unusual store can skew the entire aggregate. Flag this to the user and
recommend widening the radius before drawing conclusions.

> "The 100-mile radius only captured 3 [Retailer] locations, which may not
> give a reliable picture of their typical footprint. I'd suggest widening
> to 150 or 200 miles for a more stable comparison — want me to rerun it?"

Don't present the comparison results as meaningful if the location count is
this low unless the user explicitly wants to proceed anyway.

### Healthy footprint (5–30 locations)

This is the reliable range. Proceed to interpretation.

### Large footprint (more than 30 locations)

A large footprint isn't necessarily a problem — a national retailer with
dense coverage may legitimately have 50+ locations in range. But it's worth
flagging that the aggregate is averaging across a wide geography and possibly
diverse market types, which can mask variation. Note the count, proceed with
the comparison, and proactively offer location-level data so the user can
see the distribution if the aggregate picture feels too averaged.

> "There are 47 [Retailer] locations within 100 miles — the footprint
> comparison reflects a broad average across diverse markets. I can also
> pull individual location data if you want to see which specific stores
> are most similar to this site."

---

## Step 3: Interpret the Comparison Results

The endpoint compares the subject site against the retailer footprint across
several dimensions. Here's how to read each one:

**Overall demographic match score:** The headline fit signal. A high match
means the subject site's visitor profile resembles the retailer's typical
customer base. A low score doesn't automatically disqualify the site — it
may mean the retailer hasn't tapped this customer type yet — but it warrants
explanation.

**Foot traffic variables (visits, dwell time, visit frequency, hour/day
patterns):**
- *Visit volume:* Is the subject site attracting traffic at a level comparable
  to the retailer's typical locations? Significantly lower volume may indicate
  the site underperforms as a draw; significantly higher may signal strong
  opportunity or a different use pattern.
- *Dwell time:* A subject site with lower dwell than the retailer's footprint
  suggests visitors aren't spending the kind of time the retailer's model
  typically requires. This is a meaningful signal for retailers that depend
  on browse time (specialty, home goods, apparel).
- *Visit frequency:* A site with lower frequency than the retailer's footprint
  may not generate the repeat customer pattern the retailer depends on —
  especially relevant for grocery, fitness, and other high-frequency
  categories.
- *Hour and day patterns:* Does the subject site peak at the same times as
  the retailer's typical locations? A mismatch here — a site that peaks
  weekday mornings vs. a retailer that depends on weekend afternoon traffic —
  is a behavioral fit concern even if volume looks fine.

**Shared customers:** What percentage of the subject site's visitors also
visit the retailer's nearby locations? High shared customers means the
retailer is already drawing from this trade area — which could indicate
strong demand, or that an existing nearby location may cannibalize a new one.
Low shared customers may indicate an untapped customer pool or a genuinely
different visitor base.

**Reading convergent vs. divergent signals:**
- Strong match across demographics, traffic behavior, and shared customers →
  high-confidence fit. The site looks like the retailer's wheelhouse.
- Strong demographic match but divergent traffic behavior → the customer is
  there, but the site doesn't drive the behavior the retailer's model relies
  on. Worth flagging as a risk.
- Strong traffic behavior match but low demographic match → the location
  performs similarly, but the customer profile differs. May work depending
  on the retailer's flexibility, but flag the divergence.
- Low shared customers + strong demographic match → the retailer may not have
  meaningful penetration in this trade area. Could be opportunity, could be
  an indication the customer here behaves differently than expected.
- Low across all dimensions → be direct. The site doesn't profile as a strong
  fit based on the available data.

---

## Step 4: Offer Location-Level Data (When Warranted)

Proactively offer individual location data in these situations:

- The footprint is large (30+ locations) and the aggregate may be masking
  useful variation
- The comparison results are mixed or show meaningful divergence on some
  dimensions — knowing which specific locations are closest to the subject
  site helps calibrate the finding
- The user is trying to identify the most analogous existing location (useful
  for site visits, case studies, or leasing conversations)
- Cannibalization risk is a concern — seeing the individual nearby locations
  and their traffic profile is more useful than an aggregate

When pulling individual location data, surface the locations ranked by
similarity to the subject site on the dimensions that matter most for the
user's question.

---

## Step 5: Present Results

### Lead with the headline fit assessment

One clear sentence on overall fit based on the convergent signals.

> "On balance, [Subject Site] profiles as a strong fit for [Retailer] —
> the demographic match is high, dwell time and frequency are consistent
> with their footprint, and the traffic pattern aligns with their peak
> periods."

Or if the picture is mixed:

> "[Subject Site] matches [Retailer]'s demographic profile well but shows
> meaningfully lower visit frequency than their typical locations — worth
> considering for a retailer that depends on repeat traffic."

### Comparison summary table

Always include these four dimensions — they are the core fit signals:

| Dimension | Subject Site | Retailer Footprint Avg | Assessment |
|-----------|-------------|----------------------|------------|
| Demographic match | X | — | High / Med / Low |
| Avg dwell time | X min | X min | At / Above / Below footprint |
| Avg visit frequency | X | X | At / Above / Below footprint |
| Shared customers | X% | — | High / Moderate / Low |

If the data supports it and the user's question warrants it, extend the
table with additional dimensions:

| Dimension | Subject Site | Retailer Footprint Avg | Assessment |
|-----------|-------------|----------------------|------------|
| Peak day of week | [Day] | [Day] | Aligned / Divergent |
| Peak hour | [Hour] | [Hour] | Aligned / Divergent |
| Visits by radius (1/3/5 mi) | X / X / X | X / X / X | At / Above / Below footprint |
| Visits by drive time (5/10/15 min) | X / X / X | X / X / X | At / Above / Below footprint |
| Distance to nearest footprint location | X mi | — | — |

Add the extended rows when visit timing or proximity to existing locations
is relevant to the user's question — site selection, cannibalization
evaluation, or when the core table shows a divergence that the time/day
pattern might explain. Skip them when the core four tell a clear enough
story on their own.

### Narrative

Two to three sentences connecting the dimensions into a coherent read.
Highlight where signals converge and call out any meaningful divergences.
Reference the footprint location count so the user knows how robust the
comparison is.

### Cite data vintage and footprint parameters

> *Comparison based on [date range] using [N] [Retailer] locations within
> [X] miles, via Advan's mobile device panel.*

---

## Mode B: Nationwide Profile (No Subject Site)

Use this mode when the user wants to understand a retailer's or category's
footprint in general — not in comparison to a specific property.

### Step 1: Confirm the Retailer or Category

Confirm who the user wants to profile. If a specific brand or category hasn't
been named, ask before proceeding.

**Date range:** Use the UI selection or whatever the user specified.

### Step 2: Pull and Summarize the Nationwide Footprint

Call the endpoint without a subject site to retrieve the nationwide profile.
Summarize the retailer's or category's typical location characteristics
across the core dimensions:

- **Traffic profile:** Average visits, dwell time, and visit frequency across
  locations. Note the range if there's meaningful variation.
- **Peak patterns:** Typical peak day of week and hour — this characterizes
  the retailer's operational pattern (destination weekend shopper vs. weekday
  convenience stop, etc.).
- **Demographic profile:** The typical customer across the full set of
  dimensions: median household income, dominant age cohort, primary
  ethnicity/race composition, educational attainment, population density
  of the trade area (urban core, suburban, exurban), and standout lifestyle
  segments that define the retailer's core customer base.
- **Visit distribution by radius and drive time:** How far the typical
  customer travels. This characterizes the retailer as a convenience,
  neighborhood, or destination concept.
- **Location count and geographic spread:** How many locations are in the
  dataset and whether coverage is national, regional, or concentrated.

### Step 3: Offer Geographic Comparison

After presenting the national summary, offer to break it down by geography.
This is most useful when the user is evaluating a specific market, comparing
regions, or assessing whether the retailer performs differently across market
types.

> "That's the national picture. Want me to compare how [Retailer] performs
> across specific markets or regions — for example, how their Northeast
> locations compare to their Sun Belt footprint?"

Geographic comparisons to offer based on context:
- **Metro vs. metro:** How does [Retailer] perform in [Market A] vs.
  [Market B]?
- **Regional:** How does the Northeast footprint compare to the Southeast,
  Midwest, or West?
- **Urban vs. suburban vs. exurban:** Does the retailer's profile shift
  meaningfully by market density?
- **Custom geography:** If the user specifies a region, state, or set of
  markets, pull and compare those directly.

### Step 4: Present the National Summary

### Headline

One sentence characterizing the retailer's typical location.

> "[Retailer] operates primarily as a [destination / neighborhood /
> convenience] concept, drawing customers from a [X]-minute drive on average,
> with a customer base skewing [demographic summary] and peak traffic on
> [day/time]."

### National footprint table

| Dimension | Retailer Avg |
|-----------|-------------|
| Avg monthly visits | X |
| Avg dwell time | X min |
| Avg visit frequency | X |
| Peak day | [Day] |
| Peak hour | [Hour] |
| Visits within 1/3/5 mi | X% / X% / X% |
| Visits within 5/10/15 min drive | X% / X% / X% |
| Median household income | $X |
| Dominant age cohort | X–Y |
| Primary ethnicity / race | [Top 1–2] |
| Educational attainment | [e.g., College-educated majority] |
| Population density | [Urban / Suburban / Exurban] |
| Top lifestyle segments | [Top 2–3] |
| Locations in dataset | N |

If geographic comparisons were requested, add a column per geography.

### Cite data vintage

> *Based on [date range] across [N] [Retailer] locations nationally, via
> Advan's mobile device panel.*

---

## Follow-Ups

For site comparison mode, the most natural next steps are pulling individual
location data (if not already done), running a void analysis to see where
this retailer ranks as a candidate for the center, or checking cannibalization
risk if shared customers came back high. For nationwide profile mode, a
geographic breakdown or a comparison against a specific candidate site are
the natural directions. Let the conversation lead.
