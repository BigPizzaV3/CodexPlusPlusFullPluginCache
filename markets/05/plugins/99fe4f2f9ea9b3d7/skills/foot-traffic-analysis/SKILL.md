---
name: foot-traffic-analysis
description: >
  Step-by-step workflow for analyzing foot traffic at a single retail property
  using Advan REI MCP data. Use this skill whenever Reina is asked about a
  property's traffic performance, visit trends, dwell time, visit frequency,
  or general location performance. Trigger on phrases like "how is [property]
  performing", "show me traffic for [location]", "what's the foot traffic at
  [address]", "how have visits trended", "is this center busy", "pull the
  traffic data for", or any request that centers on understanding a specific
  property's visitor activity — even if the user doesn't say "foot traffic"
  explicitly. When in doubt, use this skill before answering.
---

# Foot Traffic Analysis Workflow

A single-property traffic analysis has four stages: resolve the property,
pull core metrics, benchmark against the market, and synthesize. The stages
build on each other — don't skip ahead or collapse them into one big query.

---

## Stage 1: Resolve the Property

Properties in the REI platform are identified by three fields: **ALI** (the
primary unique identifier), **location name**, and **company name**. If the
user has referenced any of these — or if they've been established earlier in
the conversation — use them directly and proceed to Stage 2.

If the property is ambiguous — a partial name, an address, or a loose
description like "the Target on Route 9" — use `search` to find it. Present
the top results concisely and ask the user to confirm before pulling data.
Don't guess and proceed; a misidentified property produces confidently wrong
analysis.

Once confirmed, carry the ALI, location name, and company name forward. You'll
reuse them across every tool call in this workflow.

---

## Stage 2: Pull Core Metrics

Call these three tools in order. Each one adds a layer to the story.

**Date range:** Use whatever date range the user has selected in the UI, or
whatever period they've specified in their question. Only ask about the date
range if it's genuinely ambiguous from context.

### 2a. Traffic Summary — the volume story

Call `traffic-summary` with the resolved property identifiers.

Key outputs to capture:
- Total visit count for the period
- Month-over-month and year-over-year trend
- Any notable spikes or drops

### 2b. Dwell Time — the engagement story

Call `dwell-time` for the same property and date range.

Dwell time tells you whether visitors are spending meaningful time or just
passing through. A high-traffic property with low dwell time often signals
convenience-oriented shopping or a pass-through layout; higher dwell suggests
destination behavior or a strong tenant mix.

### 2c. Visit Frequency — the loyalty story

Call `visit-frequency` for the same property and date range.

Visit frequency distinguishes properties that draw the same loyal customers
repeatedly from those that rely on a constant stream of new visitors. A
grocery-anchored center will typically show higher frequency than a fashion
or home goods property — keep that in mind when interpreting the result.

---

## Stage 3: Benchmark Against the Market

A traffic number without context is just a number. Call `ranking` to place
the property within its submarket or category using the same date range.

The ranking result gives you where this property sits relative to peers and
whether it's gaining or losing ground. Weight this step based on what the
user actually asked — if they want to know if the property is strong, lead
with rank; if they're just asking how busy it is, one sentence is enough.

---

## Stage 4: Synthesize and Present

### Search for real-world context

Before writing the narrative, do a targeted web search for anything that
could explain or color what the data is showing. You're looking for things
like: recent anchor tenant changes or closures, new competition that opened
nearby, local economic conditions, a major employer moving in or out, weather
events or regional disruptions, renovation or construction activity, or any
news that a real estate professional would find relevant when reading these
numbers.

You don't need to find something every time — if a search turns up nothing
useful, move on. But when you do find something that connects, weave it into
the narrative naturally rather than citing it as a footnote. The goal is to
help the user understand *why* the traffic looks the way it does, not just
*what* it looks like.

Search examples that tend to be productive:
- "[Property name] [city] anchor tenant"
- "[Retail chain] closures [year]" if a relevant tenant is in the news
- "[City/submarket] retail market [year]" for broader context
- "[Shopping center name] renovation OR redevelopment"

### Lead with the headline

Open with one sentence that answers the user's actual question. Don't make
them read a table to find the takeaway.

> "Riverside Commons drew roughly 1.2M visits over the period, up 8%
> year-over-year, putting it in the top quartile of grocery-anchored centers
> in the submarket — a trend that tracks with the Whole Foods renovation that
> completed last spring."

### Core metrics table

Always include a table. It's the reference point the user will return to.

| Metric | Value | vs. Prior Year |
|--------|-------|----------------|
| Total visits | X | +/- Y% |
| Avg. monthly visits | X | +/- Y% |
| Median dwell time | X min | +/- Y% |
| Visit frequency (avg. visits/visitor) | X | +/- Y% |
| Submarket rank | #X of Y | ↑/↓ Z positions |

Populate only the rows where you have data. If a metric wasn't returned,
omit the row rather than leaving it blank.

### Trend narrative

Two to three sentences on what's driving the numbers. Look for:
- Whether growth is consistent or concentrated in specific months
- Any divergence between metrics (visits up but dwell down — could signal a
  tenant change or anchoring issue)
- Seasonal or external factors, especially anything surfaced from the web
  search

Be specific when the data supports it. If the data and context together tell
a clear story, tell it directly.

### Cite data vintage

End with the data vintage. Example:

> *Data covers [date range], via Advan's mobile device panel.*

---

## Handling Gaps and Anomalies

**No data returned:** Say so plainly and offer a path forward. Don't speculate
about why.

> "I'm not finding traffic data for that property — it may not be in our
> coverage area. Want me to check a nearby comparable, or should I flag this
> for the support team?"

**Partial data:** Lead with what's available, be explicit about what's
missing. Don't bury the gap.

**Anomalous results:** If a number looks implausible — a 400% traffic spike,
a dwell time under 2 minutes for a grocery store — flag it before presenting
it. The web search may turn up an explanation; if it does, note it. If it
doesn't, say so and recommend verifying.

> "These numbers look unusually high relative to the submarket. I didn't find
> an obvious external explanation — I'd verify before relying on them. Want
> me to pull a peer comparison?"

---

## Follow-Ups

If there's a natural next step given what you found, mention it. This should
feel like something a colleague would say at the end of a conversation, not a
menu of options. Sometimes there's nothing to add — that's fine too.
