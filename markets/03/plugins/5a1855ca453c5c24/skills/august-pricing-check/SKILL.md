---
name: august-pricing-check
description: >
  Run a Van Westendorp-style pricing sensitivity study across August twins for
  a product, plan, or feature. Ask each twin the four canonical price questions
  (too cheap = quality suspect, bargain = good deal, expensive = would pause,
  prohibitively expensive = wouldn't buy) and aggregate into the acceptable
  price band plus the four inflection points (PMC, PME, OPP, IPP). Better than
  eyeballing one twin's answer. Use whenever the user wants directional price
  sensitivity, willingness-to-pay, or a price-band read from twins instead of
  live shoppers. Triggers on: "price check with twins", "van westendorp",
  "pricing sensitivity", "how much would twins pay", "what should I charge",
  "price band", "/august-pricing-check".
---

# August Pricing Check

Van Westendorp-style pricing sensitivity across N=8–12 August twins. Returns
the acceptable price band and its four inflection points, with representative
quotes for each band. Tools live under the August MCP.

**What Van Westendorp gives you:**
- **PMC** (Point of Marginal Cheapness) — below this, quality is suspect
- **PME** (Point of Marginal Expensiveness) — above this, buyers walk
- **OPP** (Optimal Price Point) — resistance is balanced (too-cheap = too-expensive)
- **IPP** (Indifference Price Point) — where "bargain" = "expensive" (typical
  actual paid price)

**When to use:** setting an anchor price, sanity-checking a plan tier, testing
a promo, comparing two SKUs' willingness-to-pay.

**When NOT to use:** you only have one twin available (use `/august-feedback`
instead), the product has no clear price yet (do concept work first), or you
need statistical significance (use a real survey — twins are directional).

---

## STEP 1 — Get the artifact and anchor

Before touching MCP, confirm:

- **What is being priced?** A specific product (name, SKU, description), a
  subscription plan (features + billing cadence), a bundle, a feature add-on.
- **Anchor price** (optional but helpful) — the user's current price or
  candidate range. If none, twins will float; that's fine but noisier.
- **Currency / market** — default USD unless the user specifies.
- **Audience org** — which brand's shoppers? If ambiguous, ASK.

If the artifact is thin ("what should I charge for a supplement?"), push back
once for a real description — twins price better with concrete material.

---

## STEP 2 — Pick the org

Call `list_organizations`. Match the audience:

- Consumer product / plan / bundle → the relevant **brand org**
- B2B / dashboard / Fermat platform pricing → **Fermat org** (dashboard-user
  twins)

If ambiguous, ASK via a concise question with the top 2–3 orgs as options.

---

## STEP 3 — Pick twins (8–12) OR run as focus group

Call `list_twins` for the org. Aim for **8–12 twins** with variety across:
buying stage, budget tier, category affinity, demographic slice. Homogeneous
panels produce narrow bands; diverse panels surface the real spread.

**Two execution paths — pick one:**

- **Fan-out interviews** (default, more control): for each twin, call
  `start_interview(twin_id)` and then `ask_question(interview_id)` with the
  four VW questions bundled. Faster to parse, cleaner attribution.
- **Focus group** (use when the user wants cross-talk / disagreement signal):
  use `list_focus_groups` to select an existing ready group, then
  `start_focus_group` → optionally `add_focus_group_stimuli` for Figma URLs
  → `run_focus_group_round` with the artifact context and four VW questions
  → `end_focus_group` → `get_focus_group_results`. If no suitable ready group
  exists, ask the user to configure one in August or use fan-out interviews.

If you can't find 8+ suitable twins in the org, note the sample size in the
output and continue — don't fabricate.

---

## STEP 4 — Ask the four Van Westendorp questions

For each twin, ask (adapt phrasing to the artifact):

1. **Too cheap** — "At what price would you think this is so cheap that you'd
   doubt its quality?"
2. **Bargain** — "At what price would you think this is a bargain — a great
   deal for the money?"
3. **Expensive** — "At what price would you think this is starting to get
   expensive, so that it's not out of the question, but you'd have to think
   about it?"
4. **Prohibitively expensive** — "At what price would you think this is so
   expensive that you would not consider buying it?"

Always pass the full artifact context in the question payload. Ask for a
one-line rationale per price so you have quotable material.

---

## STEP 5 — Aggregate

Parse each twin's four dollar values into a table. Then compute:

- **PMC** — intersection of "too cheap" (descending cumulative) and
  "not cheap = bargain-or-higher" (ascending cumulative). Below this,
  more people say "too cheap" than "acceptable."
- **PME** — intersection of "expensive" (ascending cumulative) and "not
  expensive" (descending cumulative). Above this, more people say "too
  expensive" than "acceptable."
- **OPP** — intersection of "too cheap" and "prohibitively expensive"
  cumulative curves. Balance point of extreme resistance.
- **IPP** — intersection of "bargain" and "expensive" cumulative curves.
  Median indifference price.

The **acceptable band** is PMC → PME. OPP and IPP sit inside that band.

If a twin gave nonsense answers (all four the same, non-monotonic), drop
them from the aggregate but note it.

---

## STEP 6 — Return the output

Use this template. Don't dump raw transcripts.

```
## Pricing Check — {artifact name}
Org: {org}  |  Twins: N={count}  |  Anchor: {price or "none"}

### Acceptable band: ${PMC} – ${PME}
- OPP (optimal): ${OPP}
- IPP (typical paid): ${IPP}

### Price bands with rationale
- **Too cheap (< ${PMC})** — "{one representative twin quote}"
- **Bargain (${PMC} – ${IPP})** — "{quote}"
- **Acceptable / thinking about it (${IPP} – ${PME})** — "{quote}"
- **Prohibitive (> ${PME})** — "{quote}"

### Notable spread
{1–2 lines on twin variance — e.g. "budget-tier twins capped ${PME} $10 lower
than premium-tier twins"}

### Caveat
N={count} twins is directional, not statistically significant. Validate the
band with a real survey or A/B before locking a price.

### Source
Org: {org}  |  Twins: {twin_1}, {twin_2}, ... {twin_N}
```

If the bands overlap weirdly (e.g., PMC > PME, or IPP outside the band), say
so plainly — that's a signal the twins disagree wildly and the product may
not have a clear price point yet.
