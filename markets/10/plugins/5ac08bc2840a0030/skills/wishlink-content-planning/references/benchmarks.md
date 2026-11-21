# Cohort benchmarks

Every number here is computed from the full creator population on
`workspace.business_intelligence.silver_product_daily_v2` between **2026-06-21 and
2026-09-20**. No sampling. Percentiles are exact (`numpy.quantile`), not approximate.

These are frozen constants. They do not change until someone re-runs the estimation and
updates this file. A skill quoting a number that is not in this file is quoting an
invented number.

Absolute population counts and revenue totals are intentionally not recorded in this file —
they are Wishlink business intelligence, not something a content-planning skill needs to
function. Tier cutoffs are kept below in rupees because the skill classifies a specific
creator's own earnings against them at runtime — that's a functional requirement, not
descriptive business intelligence.

## Tiers

Tiers are cut on **3-month total creator commission, over earners only**. Percentiles
across all creators are degenerate: most creators earn exactly zero, so the all-creator
median is ₹0.00 and every band below roughly the two-thirds mark collapses onto the same
point.

| Tier | Cut (3-month commission, INR) | Share of all commission |
|---|---|---|
| `T0_no_earnings` | 0 | 0.00% |
| `T1_below_median_earner` | > 0 to 136.07 | 0.35% |
| `T2_p50_p75` | > 136.07 to 836.75 | 1.63% |
| `T3_p75_p90` | > 836.75 to 5,444.26 | 5.91% |
| `T4_p90_p95` | > 5,444.26 to 16,646.87 | 8.64% |
| `T5_p95_p99` | > 16,646.87 to 103,020.34 | 28.52% |
| `T6_top1pct_of_earners` | > 103,020.34 | 54.94% |

About a third of all creators earn anything at all.

**The top 1% of earners earn 55% of all creator commission.** Advice tuned to the top tier
is irrelevant to the vast majority of the base, which is why every skill here branches on
tier.

## Effect sizes (within-creator, creator + month fixed effects)

Coefficients are on `log1p(commission)` unless noted. Creator fixed effects absorb every
time-invariant creator trait — follower count, niche, audience, tier, tenure. SEs clustered
by creator.

| Lever | Within-creator | Naive cross-section | Note |
|---|---|---|---|
| Distinct products linked | **+1.006 to +1.068** elasticity | 0.451 | Replicated at post level: +0.9991 |
| Posts published (products controlled) | **+0.126, SE 0.029, CI [0.069,0.183]** | 0.679 | Real, but ~1/8 the size of products |
| `new_posts` (products controlled) | +0.185 | — | Publishing measured correctly |
| Posts alone (uncontrolled) | +0.589 elasticity | 0.973 | Cross-section 1.65x too optimistic |
| Median price | +0.105 elasticity | 0.185 | Quintile steps +11/+17/+27/+37% |
| Channel: 10pp Instagram → YouTube | −10% | similar | Not a whale artefact |
| Channel: 10pp Instagram → Facebook | −13% | similar | |
| Brand concentration (months with ≥2 earning brands) | +0.748 | +3.069 | Raw FE (−1.218) is equally unusable |

### Diminishing returns on posting

| Posts in month | Marginal effect per post |
|---|---|
| 0–5 | +0.167 |
| 5–20 | +0.057 |
| 20–50 | +0.042 |
| 50+ | **+0.004** |

Always model volume in logs: within-R² is 0.034 linear vs 0.119 log.

### Variance decomposition

Of the within-creator month-to-month variance that is explained at all: cadence 76.4%,
composition 11.0%, brand 7.7%, channel 5.0%. But total within-R² is only **0.193** — over
80% of a creator's month-to-month movement is not explained by any behaviour in this panel.
That number is the single best argument against confident coaching.

## Content effects (post level, Instagram only)

Post-level, creator fixed effects, first 7 days of each post's life, holding product count
fixed. Base category is beauty/personal care.

| Content category | log commission_7d |
|---|---|
| fashion | **+0.383*** |
| home | **+0.381*** |
| tech_gadgets | +0.181*** |
| travel | +0.138** |
| lifestyle | +0.132*** |
| fitness_wellness | +0.066 (n.s.) |
| food_beverage | +0.008 (n.s.) |

**Reach and conversion rank differently.** tech_gadgets gets the most clicks (+0.587) but
the worst conversion (−0.006, i.e. −0.6pp). home is strong on both (conversion +0.010).
Category mostly moves reach; all conversion effects are ≤1pp.

### Language (vs English, same creator)

| Language | log commission_7d |
|---|---|
| Malayalam | **+0.545*** |
| Telugu | +0.343*** |
| Kannada | +0.330*** |
| Tamil | +0.266*** |
| Marathi | +0.184*** |
| Hindi | +0.132*** |

Tagged pure-English content is **negative** (−0.109***). The same creator earns more on
regional-language content — this is a within-creator result, not "regional creators are
bigger".

### Audience

male-targeted +0.186*** vs female base; unisex null.

### Topic lift, top-decile vs bottom-half posts

Descriptive lift only — **not** creator-controlled, so it is confounded with category and
creator. Use it to describe what winning posts look like, never as a causal claim.

Over-represented: discount hunting 22.17x · affordable childrens fashion 6.60x ·
value for money 5.91x · affordable kids fashion 5.51x · sale alerts 5.32x ·
online sales 5.26x · textile quality 5.01x · product quality review 4.54x

Under-represented: hair care routine 0.22x · sun protection 0.23x · skin brightening 0.25x ·
scalp health 0.28x · skincare routine 0.31x · beauty products 0.33x

## Data freshness

The most recent ~14 days read roughly **30% low** because attribution is still settling.
Any comparison involving the trailing two weeks is unsafe.

## Coverage limits

- VideoLens covers **50.16%** of posts and is **Instagram-only** (100% of covered posts).
  No content finding extends to YouTube or Facebook.
- 18.5% of performance rows have NULL `post_id` (storefront, app, save-product flows) and
  are structurally absent from all post-level analysis.
- No view / impression / reach column exists in any VideoLens table. Clicks is the earliest
  observable funnel stage, so a content effect on reach cannot be separated from one on
  click-through.
