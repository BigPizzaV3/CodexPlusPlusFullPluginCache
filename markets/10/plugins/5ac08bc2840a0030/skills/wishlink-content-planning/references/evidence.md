# What the evidence supports, and what it does not

Read this before adding a recommendation to any skill. The list of things that turned out
**not** to work is as load-bearing as the list of things that did — most plausible-sounding
creator advice does not survive a within-creator test, and a skill that repeats it is
confidently wrong at scale.

## How these numbers were produced

A creator-month panel over the full creator population (2026-06-21 to 2026-09-20) and a
post-level content dataset with VideoLens coverage. Estimation is creator + month fixed
effects with creator-clustered standard errors.

Why fixed effects rather than comparing creators: an earlier pass generated claims by
comparing creators to each other and had adversarial verifiers re-argue them one at a time.
Most were refuted. In nearly every case the arithmetic reproduced exactly and the
interpretation failed — the confounds cited were whale creators, creator tier,
survivorship, and volume. Creator fixed effects absorb all of those at once, which is why
they replaced the argument.

## What fixed effects does and does not buy

It removes **time-invariant** creator confounding. It does **not** remove reverse causality
or time-varying confounders. Every finding below is therefore an association measured within
a creator over three months, not a promise about what happens if the creator changes
behaviour. Skills must phrase recommendations accordingly — "creators who did X also saw Y",
never "do X and you will get Y".

One specific known hole: ~77% of the product-count association runs through clicks. Clicks
is downstream of linking products (elasticity +1.214), so controlling for it blocks the
mechanism rather than exposing a confound — but it also means we cannot rule out that
traffic drives product-linking rather than the reverse.

## Supported

- **Distinct products linked** is the composition lever with a robust association,
  elasticity ≈ 1.0. Independently replicated at two grains (creator-month +1.068, post-level
  +0.9991) and robust to dropping the lag-affected month, excluding the top 1%, restricting
  to months with ≥5 orders, and including zero-earning months.
- **Publishing more is mostly how you link more products**, but keeps a real, smaller
  effect of its own. Posts holding products fixed is +0.126 (SE 0.029, CI [0.069,0.183]) —
  clearly non-null, about an eighth the size of the products effect. Measured properly as
  `new_posts` it is +0.185.
- **Returns to posting diminish steeply** and are ~flat above 50 posts/month.
- **Content category matters within a creator** — fashion and home lead, holding products fixed.
- **Regional-language content outperforms English within the same creator.**
- **Channel mix matters**: Instagram > YouTube > Facebook, and this survives whale exclusion.
- **Price band**: moving up the price distribution associates with more commission (+0.105).

## Null — say so rather than inventing a recommendation

- **Posting consistency.** +0.00085 log points per gap day, SE 0.0021, p=0.688. Anything
  above 0.5% per gap-day is ruled out. The raw positive that appears to say *bigger gaps earn
  more* is an artifact: `posting_gap_days` is mechanically 0 whenever a creator published
  ≤1 post, which is 70.3% of rows.
- **Collections.** Headline +0.323 fails five of six stress tests.
- **Sourcing.** +0.205 collapses to −0.061 (p=0.233) once sourcing revenue is netted out of
  the outcome. It was arithmetic.
- **On-screen text overlays.** Unanswerable as posed — every VideoLens post has at least one
  overlay, so there is no comparison group. Overlay *count* is n.s. and turns slightly
  negative once product count is controlled.
- **Production quality.** `studiograde` lighting −0.092, `controlled` −0.040 against plain
  "adequate"; composition and sharpness are noise. Do not tell creators to invest in polish.
- **Brand count.** +0.141 with products in levels, but −0.039 (p=0.30) with products in logs,
  and the log form fits far better. Brand count is largely product count renamed.
- **Bigger creators getting better commission rates.** Grouped by GMV rather than by the
  commission being explained, the effective rate is a flat 3.76–4.16%, and the median
  creator's rate *falls* with size. The apparent "2.24x with size" was selection on the
  numerator.

## Sign-flipped between cross-section and within-creator

- **Reward share.** Pooled +0.873 (p=1.5e-22) becomes **−0.148 (p=0.190)** within creator.
  A skill built on the pooled number would tell creators to chase rewards, which the
  within-creator evidence does not support.

## Unusable columns

- `category_hhi` — computed from the commission distribution, so 100% of one-order months
  are pinned at 1.0. The sign reverses from −0.89 to +0.51 once restricted to months with
  ≥10 orders. Do not use until rebuilt on order counts.
- `active_days` — an attribution outcome, not a behaviour. It counts any day with an
  attribution row including back-catalogue traffic, correlates 0.82 with log clicks, and
  swallows 46% of the measured posting return because it sits downstream.
- `collection_id` — 96.95% NULL.
- `transcript_summary` — ~12% non-null. Qualitative sampling only.
- `lighting` / `composition` / `sharpness` / `post_processing` — free-text LLM sentences leak
  into the category slot; normalise before use.
- VideoLens `*_score`, `*_explanation`, `strengths`, `improvements`, `content_subcategory` —
  all Spark type `void`, 100% NULL.
- `brand` (string) — many more distinct values than `brand_id` has entries. Free text.
  Group by `brand_id`.

## Not measured — do not answer these

- Post-level timing (hour, weekday). The panel has no day grain. Any weekday or
  time-of-day claim has no support here.
- Post age / decay curves. No post-age grain was built.
- Follower counts, reach, impressions, saves, shares. Not present in any source consulted.
- Brand-campaign and paid-collab flags — named as the leading omitted time-varying
  confounder in three of four estimates.
- Commission rate per product, so the price effect cannot be split into "pricier items yield
  more rupees" vs "pricier categories carry higher rates".
