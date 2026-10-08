---
name: void-analysis
description: >
  Workflow for identifying tenant candidates that would fit a vacancy or
  underrepresented category at a retail center, using Advan REI's void
  analysis endpoint enriched with traffic health and expansion signal data.
  Use this skill whenever a user asks what tenants would work at a center,
  what's missing from a property's tenant mix, who should fill a vacancy,
  what categories are underrepresented, or whether a specific retailer type
  would be a good fit. Trigger on phrases like "what tenants would work here",
  "who should fill this space", "what's missing from this center", "void
  analysis", "tenant candidates", "what categories make sense here", or any
  request about filling a vacancy or improving a center's tenant mix.
---

# Void Analysis Workflow

The void analysis endpoint does the core analytical work — it returns tenant
candidates ranked by dynamic distance, cannibalization risk, and demographic
match. This skill's job is to gather the right parameters before calling it,
filter out candidates that don't belong in a retail center context, enrich
the top results with real-world health and expansion data, and present the
output in a way that's actually useful for a leasing decision.

---

## Step 1: Gather Parameters

Before calling the endpoint, confirm two things. If either is missing from
the conversation, ask — these directly affect the quality of the results.

**Vacancy size:** What is the approximate square footage of the space? This
is the most important filter. A 1,200 sq ft inline space and a 45,000 sq ft
anchor box should return completely different candidate sets. If the user
hasn't specified, ask before proceeding.

**Category preferences or exclusions (optional):** Has the user indicated
they're looking for a specific category (food & beverage, fitness, soft
goods) or want to exclude something? If so, note it — you'll apply it when
filtering results. If no preference is stated, proceed with the full results
and apply the standard retail center filter described in Step 3.

Also confirm the property using ALI, location name, and company name as
usual.

---

## Step 2: Call the Void Analysis Endpoint

Call `void-analysis-api` with the resolved property identifiers and vacancy
size parameter. Use the date range from the UI or as specified by the user.

The endpoint returns a ranked list of tenant candidates scored on:
- **Dynamic distance** — how far the candidate's typical locations are from
  this trade area's profile
- **Cannibalization risk** — likelihood of pulling from an existing nearby
  location of the same brand
- **Demographic match** — how well the trade area's visitor profile aligns
  with the candidate's typical customer base

---

## Step 3: Filter for Retail Center Appropriateness

The endpoint returns candidates across a broad range of categories. Before
presenting results, remove any candidates that don't belong in a traditional
retail center context. Categories to omit by default:

- Auto dealers, car washes, and auto service
- Hotels and lodging
- Hospitals, urgent care, and large medical facilities (small-format urgent
  care or dental that fits inline retail is fine)
- Gas stations and fuel retailers
- Industrial, warehouse, or self-storage uses
- Large-format government or civic uses

Use judgment for edge cases. A drive-through-only concept with no inline
presence, for example, may not fit a traditional center even if it scores
well on demographics. If the user has specified a category preference,
apply that filter here too — prioritize their stated criteria over the
default list.

---

## Step 4: Filter by Vacancy Size

From the filtered results, narrow to candidates whose average store footprint
is compatible with the vacancy. A reasonable match range is ±30% of the
vacancy size unless the user specifies otherwise.

Flag if the vacancy size is unusual — a very large anchor box or a very
small kiosk-scale space may return a thin candidate set, and it's worth
noting that upfront rather than presenting a short list without explanation.

---

## Step 5: Present Results

### Lead with a brief framing

One or two sentences on what the analysis surfaced — is the candidate pool
strong, thin, concentrated in a particular category?

> "The void analysis surfaces eight strong candidates for the 4,200 sq ft
> space, with the clearest opportunities in specialty food, health & wellness,
> and value apparel — all categories underrepresented in this trade area
> relative to the visitor demographic profile."

### Candidate table

| Rank | Tenant | Category | Avg Store Size | Demographic Match | Cannibalization Risk |
|------|--------|----------|---------------|-------------------|----------------------|
| 1 | | | X sq ft | High/Med/Low | High/Med/Low |

Present the top 25 from the filtered, size-matched list, or fewer if the
list is shorter. Don't pad the table with weak candidates just to fill rows.

After the table, offer to expand to the full unfiltered list if the user
wants to see everything the endpoint returned before category and size
filtering was applied.

### Brief narrative

Two to three sentences on the standout candidates and any patterns worth
flagging — a category cluster that keeps appearing, a size mismatch that
limits the field, or a category that keeps appearing near the top of the
rankings.

### Cite data vintage

> *Void analysis based on [date range], via Advan's mobile device panel.*

---

## Handling Thin Results

If filtering by category and size leaves fewer than three candidates, say so
and offer options: widen the size range, broaden the category filter, or look
at what the full unfiltered list shows. Don't present a weak list as if it's
comprehensive.

---

## Follow-Ups

After presenting the candidate table, offer to enrich the top candidates with
two additional signals. This is the natural next step for any candidate the
user wants to pursue seriously — don't do it by default, since it requires
multiple additional data pulls and web searches.

> "Want me to dig deeper on the top candidates? I can pull traffic health
> and expansion signals for each one — that'll tell you which are actively
> growing and whether any have announced a leasing pause or contraction."

When the user confirms, enrich up to 5 candidates:

**Traffic health:** Pull `traffic-summary` and `ranking` for each candidate's
existing nearby locations. Note each candidate's trajectory — growing, stable,
or declining — alongside their void score.

**Expansion signals:** Do a targeted web search for each candidate:
"[Retailer name] expansion [year]" or "[Retailer name] new locations" or
"[Retailer name] leasing activity". Flag any candidate that has announced
closures or a leasing pause — a strong analytical score doesn't matter if
they're not actively opening stores.

Present the enriched results by adding Trajectory and Expansion Signal columns
to the original table for the enriched rows, then update the narrative.

If a specific candidate looks strong and the user wants to go deeper beyond
enrichment, the natural next steps are pulling that retailer's full traffic
profile, checking their trade area overlap with the subject property, or
running a co-tenancy check to see how well they'd complement the existing
tenant mix. Let the
conversation lead.
