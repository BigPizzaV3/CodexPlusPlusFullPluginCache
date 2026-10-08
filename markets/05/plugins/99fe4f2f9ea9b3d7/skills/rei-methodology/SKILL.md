---
name: rei-methodology
description: >
  Reference for explaining Advan REI's data methodologies consistently and
  accurately. Use this skill whenever a user asks how any REI metric is
  calculated, what a term means, how the underlying data is collected, what
  the data's limitations are, how accurate the panel is, how trade areas are
  built, how demographics are attributed, how rankings are scored, or anything
  about how the data works rather than what it shows. Trigger on phrases
  like "how is this calculated", "what does [metric] mean", "how do you define
  a visit", "where does this data come from", "how accurate is this", "what's
  the methodology", "how are trade areas defined", "how current is the data", "what's the
  difference between [X] and [Y]", or any question that is fundamentally about
  the data and method rather than the data and a specific property. Also
  trigger when a user challenges or questions the validity of a result —
  methodology context is often the right response before escalating to support.
---

# REI Methodology Reference

This skill exists to ensure Reina explains Advan's methodologies consistently,
accurately, and at the right level of depth for each user. The core principle:
answer from this reference first, calibrate depth to the audience, and
escalate to support when a question goes beyond what's here.

---

## Calibrating to the Audience

Before explaining a methodology, read the user's question for signals about
their technical depth.

**Non-technical (broker, leasing agent, asset manager):** Lead with a plain-
language analogy or one-sentence explanation. Skip the statistical detail
unless they ask. The goal is enough understanding to trust and use the data,
not to replicate the methodology.

**Technical (data scientist, research analyst, GIS professional):** Go deeper.
Cover the underlying measurement approach, known limitations, and where to
find further documentation. These users will ask follow-up questions and want
precise language.

**Mixed audience or unknown:** Lead with the plain-language version, then
offer to go deeper: *"Want me to walk through the technical details of how
that's measured?"*

---

## The Data Foundation: Advan's Mobile Device Panel

All REI metrics derive from the same underlying source: a panel of opted-in
mobile devices whose location signals are collected, processed, and aggregated
to generate insights about physical locations.

**Panel composition:** Advan observes over 100 million U.S. devices. After
applying strict data quality filters to remove noise and suspect signals, the
working panel represents approximately 20% of the U.S. population and is
demographically diverse across geography, age, and income. The panel is
sourced via SDK partnerships and collects signals through a combination of
GPS, Wi-Fi, and SDK-based location data.

**Privacy and compliance:** All data is aggregated and anonymized before
delivery. No individual device is identifiable in any REI output. Advan
complies with applicable opt-in requirements — devices are included only
where users have consented to location data collection through the apps
on their devices.

**Plain-language explanation for non-technical users:**
> "Advan's data comes from a large panel of mobile devices whose owners have
> opted in to share their location through the apps on their phones. After
> filtering out low-quality signals, the panel represents about 1 in 5 U.S.
> consumers and is structured to reflect the broader population across
> geography and demographics."

---

## Data Quality and Accuracy

When users ask how Advan ensures its data is accurate or how it's been
tested, this is a selling point — answer it directly and confidently.

**Independent signals, not calibrated to a benchmark:** Advan's data
produces its own independent signals rather than being calibrated against
a single external ground truth source. This means the data reflects what
the panel actually observes, without being shaped by or dependent on any
one third-party reference.

**Internal quality controls:** Several layers of quality processing are
applied before data reaches REI:

- *Noise and GPS spoofing filtering:* Suspect or anomalous device signals
  are identified and removed before they enter the working panel.
- *Demographic representativeness weighting:* Panel composition is
  adjusted to reflect the broader population across geography, age, and
  income.
- *Geofence quality review:* Property boundaries are validated before a
  location is included — locations where a confident boundary can't be
  established are excluded rather than approximated.
- *Automated anomaly detection:* Unusual spikes or drops are flagged
  for review so they don't surface to users as reliable data without
  scrutiny.

**How the data holds up in the real world:** Two forms of validation
play out continuously through client use:

- *Company-level alignment:* At the ticker level, Advan's foot traffic
  signals closely align with comp reports from publicly traded retailers.
  This is why hedge fund and fundamental investment clients rely heavily
  on REI data to trade inter-quarter — it's a signal they trust ahead
  of earnings.
- *Location-level alignment:* At the property level, traffic patterns
  consistently align with known real-world events — store openings and
  closings, holiday traffic shifts, anchor changes. Clients regularly
  evaluate Advan data against ground truth sources including physical
  traffic counters and internal sales data, and report high correlation.

**Plain-language response for users who ask:**
> "Advan's data goes through several layers of quality filtering —
> removing noise and spoofed signals, validating property boundaries,
> and weighting the panel to be demographically representative. On the
> accuracy side, our foot traffic signals closely track comp reports for
> publicly traded retailers, which is why a lot of institutional
> investors use this data to trade inter-quarter. At the location level,
> our clients routinely test us against physical counters and sales data
> and consistently find strong correlation."

---

## Visit Definition

**What counts as a visit:** A visit is recorded when an opted-in device is
detected within a property's geofence. There is no minimum dwell time
applied by default — every device detection that falls within the property
boundary counts as a visit. Users who want to filter by dwell threshold
can apply a dwell time filter from the header bar in REI.

**Why no default dwell threshold:** Employees, delivery drivers, and quick
convenience stops are all legitimate components of a property's traffic
picture, and some are meaningful trade area indicators. Rather than
prescribing a single threshold, REI puts the filter in the user's hands
so analysts can define the visit they care about for their specific question.

**Property boundary (geofence):** Each property has a defined geofence — a
geographic polygon corresponding to its physical footprint. A device must
be detected within the geofence to count toward that property's visit tally.

**De-duplication within a day:** Each unique device is counted once per
property per day, regardless of how many times it was detected at that
location during the day.

**Workers and frequent visitors:** Employees and vendors are not excluded
from visit counts by default, because frequent visitors — including staff —
are part of the real foot traffic picture and contribute to trade area
intelligence. Users who want to isolate shopper-only traffic can apply
frequency and dwell filters from the Global Filters menu in REI's header to
filter out devices with patterns consistent with employee behavior.

**Plain-language explanation:**
> "A visit is counted whenever someone's device is detected within the
> property's boundary. We count each device once per day, and we don't
> filter out employees by default — they're real traffic and can be
> meaningful data points. If you want to focus on pure shopper behavior,
> you can apply frequency and dwell filters to narrow it down."

---

## Dwell Time

**Definition:** Dwell time measures how long a visiting device was detected
within the property geofence during a visit. It's expressed as a median
across all visits in the selected period rather than an average, which makes
it more robust to outlier sessions.

**What it measures:** Dwell time is a behavioral signal — it distinguishes
destination shopping (longer dwell, more browsing) from convenience or
errand trips (shorter dwell, get in and get out). It's particularly useful
when comparing similar properties or evaluating retailer fit for a specific
concept.

**Applying a dwell filter:** Because there is no default minimum dwell
threshold, users working with dwell time for a specific analysis — such as
filtering to visits of at least 5 minutes to exclude true pass-throughs —
should apply the dwell time filter in the header bar before pulling metrics.
This makes the filter explicit and consistent with the user's analytical
intent.

**Limitations:** Dwell time reflects how long the device signal was present
within the geofence, not time actually spent inside the store. A device
that lingers in the parking lot contributes to dwell time. In practice,
parking lot behavior is a real component of the retail visit experience, so
this is generally an acceptable proxy — but it's worth noting when precision
matters.

**How dwell is displayed:** REI shows dwell time in 15-minute increments
(e.g., 0–15 min, 15–30 min, 30–45 min, and so on). When citing a dwell
figure, reference the bucket rather than a precise minute value.

**Interpreting dwell buckets:**
- 0–15 min: quick stop, errand, or parking lot detection
- 15–30 min: standard convenience or grocery trip
- 30–45 min: typical shopping trip
- 45–60 min: extended shopping or casual dining
- 60+ min: destination experience (entertainment, sit-down dining, big box)

These are general benchmarks — always compare dwell against the property
type and against peer properties in the same category rather than treating
any single bucket as good or bad in isolation.

---

## Visit Frequency

**Definition:** Visit frequency measures how many times the average visitor
returns to a property over a defined period. Specifically, it's calculated
as the total visits divided by the number of unique devices that visited —
giving an average number of trips per unique visitor.

**What it measures:** Frequency is a loyalty signal. A property with high
frequency is drawing repeat customers; a property with low frequency is
more dependent on constantly attracting new visitors. Grocery-anchored
centers typically show high frequency (multiple visits per month); fashion,
home goods, and entertainment typically show lower frequency.

**Interpreting frequency in context:** Always benchmark frequency against
the property type. A grocery store with a frequency of 3.5 visits per month
is performing normally; a lifestyle center with that same frequency would be
exceptional. A mall with a frequency of 1.2 is normal; a convenience store
with 1.2 would signal a problem.

---

## Trade Area Construction

**Definition:** A trade area in REI is defined by actual visitor origin data,
not assumed drive-time rings. It represents the geographic area from which
a defined percentage of a property's visitors originate.

**How it's built:** Advan identifies the home location of each visiting
device using persistent overnight ping clustering over a rolling 3-week
window — the area where the device is consistently detected during overnight
hours. Those home locations are mapped and aggregated to produce a
distribution of visitor origins. The trade area polygon is then drawn to
capture a defined threshold of that distribution — typically the closest
70% of visitors by origin distance.

**Threshold options:** The 70% threshold is the default and most commonly
used. Lower thresholds (50%, 60%) produce a tighter "core" trade area;
higher thresholds (80%, 90%) capture a broader catchment including less
frequent long-distance visitors. The threshold should be chosen based on
the use case — leasing conversations typically use 70–80%; cannibalization
analysis may use 50–60% to identify core overlap.

**Why this is different from drive-time rings:** Drive-time rings assume
uniform behavior — that all customers within X minutes will visit equally.
Actual trade areas are almost never symmetric. Highway access, competing
properties, natural barriers, and neighborhood boundaries all distort the
real catchment in ways that rings can't capture. Trade areas built from
visitor origin data reflect where customers actually come from.

**Home location attribution caveat:** Home attribution is based on
overnight device behavior over a rolling 3-week window. Devices without
reliable nighttime data, devices shared across household members, or
frequent travelers may be attributed less precisely. At the aggregate
trade area level, this uncertainty is minimal — it's most relevant when
evaluating individual device-level data, which REI doesn't expose.

**Plain-language explanation:**
> "Instead of drawing a circle on a map, Advan's trade areas are built
> from where visitors actually live. We figure out each visitor's home
> by looking at where their device consistently shows up overnight over
> a 3-week period, then map that to see the real geographic catchment.
> That's why trade areas here are often irregular shapes — they follow
> real behavior, not an assumed drive radius."

---

## Demographics

**Definition:** Demographic data in REI characterizes the visitor population
of a property — not the residents of the surrounding area. This is a
critical distinction: REI demographics describe who is actually visiting,
not who lives nearby.

**Attribution methodology:** Once a visiting device's home location is
identified via overnight clustering, Advan attributes demographics to that
visitor using block-group level data from Synergos / Popstats. The
demographic attributes of the visitor's home block group are applied to
that visitor, and these are then aggregated across all visitors to produce
a profile of the visiting population.

**What this means in practice:** If a property in a working-class
neighborhood is primarily visited by people from more affluent zip codes,
REI demographics will reflect the more affluent profile — because it's
showing who is actually visiting, not who lives nearby. This is why REI
demographics often differ meaningfully from simple ring-based lookups and
are more directly useful for retail merchandising and leasing decisions.

**Lifestyle and psychographic segments:** REI uses Spatial.AI PersonaLive
segments. Each PersonaLive segment represents a cluster of households with
similar demographic characteristics, purchasing behavior, and lifestyle
priorities, assigned at the block group level. Segments are applied to
visitors based on their home block group and aggregated to characterize
the visiting population's lifestyle profile.

When explaining a specific PersonaLive segment to a user, describe it in
plain terms — purchasing behavior, lifestyle priorities, retail affinities —
rather than referencing the segment name alone. Don't assume the user knows
what a segment label means.

**Demographic data vintage:** Block-group demographic data from Synergos /
Popstats is updated annually.

---

## Rankings and Benchmarking

**How properties are ranked:** The peer set depends on what is being
ranked:

- **Retailers:** A retailer's locations are ranked against their own
  sister locations by default. Users can also compare against the
  retailer's broader industry category.
- **Shopping centers:** Properties are ranked against other centers in
  the same GLA (gross leasable area) size tier.

**The ranking metric:** The default ranking metric is total visit volume
over the selected period. Users can switch to dwell time, visit frequency,
visits per square foot, or unique visitors depending on what they're
evaluating.

**Geography options:** Rankings can be scoped to a geography the user
selects. Available options include MSA, county, zip code, or a custom
radius around an address. These are built from Census and USPS boundary
definitions, or the user can draw a custom area.

**Interpreting rank:** Rank is always expressed as "X of Y" — both the
rank position and the total count are necessary for context. "3 of 8" and
"3 of 340" are very different findings.

---

## Void Analysis Scoring

**The void analysis endpoint scores potential tenant candidates against
three dimensions:**

**Candidate eligibility — location spacing filter:** Before scoring,
Advan filters out retailers that already have a location too close to the
subject site relative to their own network's typical spacing. Specifically,
Advan calculates each retailer's average distance between their existing
locations. Any retailer with an existing location closer to the subject site
than that average inter-location distance is removed from the candidate set.
This filters out brands where a new location would be structurally too close
to an existing one — before cannibalization risk is even considered.

**Cannibalization risk:** For retailers that pass the spacing filter,
cannibalization risk is calculated from the shared customer percentage —
what share of the subject site's visitors already visit a nearby location
of that same brand. Higher shared customers means more of the potential
customer base is already being captured by an existing location, increasing
the risk that a new store would pull from existing volume rather than
growing the brand's total reach.

**Demographic match:** A score reflecting how well the trade area's visitor
demographic profile aligns with the candidate's typical customer profile
across its existing locations. Higher match means the customers at this
property look more like the candidate's core shoppers.

**How candidates are ranked:** Candidates that pass the location spacing
filter are scored on cannibalization risk and demographic match and ranked
relative to each other for the subject site — not against an absolute scale.

---

## Shared Customers and Cross-Shopping

**Definition:** Shared customers measures the percentage of a property's
visitors who also visited another specified property (or set of properties)
within the same time period. It's a measure of cross-shopping behavior —
how much the two locations' customer bases overlap.

**Calculation:** For a given pair of properties A and B, shared customers
= (devices that visited both A and B) / (devices that visited A), expressed
as a percentage. The result is directional — shared customers from A to B
is not necessarily the same as from B to A.

**What it means:** High shared customers between a subject site and a
retailer's existing locations indicates the trade area is already being
served by that retailer — useful for gauging demand, but also a signal
worth watching for cannibalization risk. Low shared customers may indicate
an untapped customer pool or a meaningfully different visitor base.

**Retailer-level shared customers:** When `shared-customers-retailer` is
used, the comparison is against all locations of a brand within a defined
radius, rather than a single property. This gives a more complete picture
of the brand's penetration in the trade area.

---

## Sales Data and Transaction Intelligence

Advan maintains a panel of approximately 100 million debit and credit cards
that enables estimation of basket size and both online and offline sales.
This data can be used to go beyond foot traffic — connecting visit behavior
to spending behavior and revenue estimation.

When a user asks about sales data, revenue estimates, basket size, or
transaction-level intelligence, let them know this capability exists and
route them to the support team for a fuller discussion.

> "Advan has a panel of roughly 100 million debit and credit cards that
> we use to estimate basket size and online and offline sales. It's a
> natural complement to the foot traffic data. Our support team would be
> happy to walk you through what's available — want me to send them a
> note?"

---

## Data Freshness and Update Cadence

**Update schedule:** REI data is refreshed every Wednesday with a 3-day
lag. This means data through the end of the prior week is typically
available by Wednesday of the following week.

**Historical depth:** REI data is available going back to 2017. Data prior
to 2017 exists but is considered less reliable due to smaller panel size
during that period — flag this if a user is comparing across a very long
time horizon that includes pre-2017 data.

**Date range recommendations:**
- For trend analysis: 12–24 months trailing is the standard window.
- For YoY comparison: match periods of equal length and the same calendar
  months to control for seasonality.
- For a current snapshot: the most recent complete month is the standard
  reference; the current partial week may undercount relative to prior
  complete periods.

**Plain-language explanation for users asking about data recency:**
> "REI data updates every Wednesday, typically reflecting activity through
> the end of the prior week. So on any given Wednesday, you're looking at
> data that's about 3 days old. Historical data goes back to 2017."

---

## Data Coverage and Limitations

**Geographic coverage:** Advan's panel covers the U.S. and Canada.
Additional international data is available outside the standard REI
platform — users interested in international coverage should contact
Advan's support team for options.

**Property coverage:** There are a few specific reasons a property may
not have traffic data in REI:

- **Vertical stacking:** REI does not include traffic for POIs that have
  another POI directly above or below them in the same structure. Because
  only 10–15% of the mobile panel provides elevation data, Advan cannot
  reliably distinguish which floor a device is on — so vertically stacked
  locations are excluded from the standard platform to avoid misattribution.
  Data for these locations can often be pulled outside of REI; direct users
  to contact Advan's support team if they need it.
- **Outdated satellite imagery:** Geofences are built from satellite
  imagery. If a location's imagery is outdated or the property boundary
  cannot be defined with confidence, the location will not have a geofence
  and therefore will not have traffic data.

If a user needs a location that isn't currently available, they have two
options: request that Advan add it (support team), or draw their own
polygon using the Add Location tool in REI's header bar.

> "That location isn't showing traffic data in REI — that usually means
> it's either in a multi-story building where elevation data is limited,
> or its boundary hasn't been defined yet. You can draw your own polygon
> using Add Location in the header, or I can send a request to Advan's
> team to get it added."

**No default dwell filter — implication for comparisons:** Because REI
applies no minimum dwell threshold by default, visit counts include all
device detections within a geofence, including very short-duration
detections. When comparing a REI visit count to data from another source
that applies a minimum dwell filter, the counts may not be directly
comparable. Always flag this if a user is cross-referencing REI data
against other datasets.

**Panel representativeness:** Mobile location data is directional and
representative by nature — Advan's panel of approximately 20% of the U.S.
population is structured to reflect the broader population across
demographics and geographies. As a general principle, the larger the
property and the higher the surrounding population density, the closer
visit counts tend to track to ground truth. Smaller or lower-traffic
locations will be directionally accurate but may have more variability
in absolute counts.

---

## Handling Methodology Questions Beyond This Reference

If a user asks a technical methodology question not covered here — about
a specific algorithm, the exact inputs to a score, proprietary weighting
details, or something that requires Advan's internal documentation —
don't speculate.

> "That's a level of methodological detail I don't have on hand. I can
> send this to Advan's support team if you'd like a precise answer —
> they'll have the technical documentation."

Offer to escalate per the standard support escalation workflow. Don't
invent details to fill the gap.
