---
key: personal-baselines
type: measurement
measurement_key: personal_baselines
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#personal-baselines; registry (no published anchor, descriptive statistics)"
last_verified: "2026-07-20"
---

# Personal Baselines

## What it measures

Your rolling per-user statistical distribution for up to 11 behavioral metrics across your last 20 sessions: words per minute, fillers per minute, verbal restarts per minute, response latency (median, ms), turn length (median, seconds), backchannels per minute, embedded acks per minute, hedges per 1,000 words, syntactic priming (0-1), LSM macro (0-1), and content adoption ratio (0-1). For each: your p25 / p50 / p75 percentiles, mean, standard deviation, a confidence tier, and a sparkline with the current session marked as a gold dot. This is descriptive statistics of your own history; the registry lists no external research anchor because none is needed for it.

## Where you see it

The Personal Baselines table (Deep Dive tab). Baselines also power baseline-relative displays elsewhere: the speed arrows and pause markers on the Communication Timeline, and personal-z readings in team trajectory views.

## How to read your number

- Confidence tiers: "insufficient" (fewer than 4 samples, population norms used as fallback, not yet personalized); "blended" (4-9 samples, your data weighted with corpus averages); "stable" (10 or more samples, entirely your own). Focus on stable metrics first; deviations from a stable baseline are genuine departures from your norm, not noise.
- A session value well above your p75 for filler rate or response latency is worth reviewing even if the absolute number seems acceptable.
- The sparkline direction over your last 20 sessions is the most actionable signal: a consistently rising filler-rate trend is a coaching target even if today's session was unremarkable.
- Some metrics are split by conversation context (sales versus discovery, for example); compare within the right context.

## What moves it

- Nothing directly: baselines describe you, they do not grade you. They move as your behavior moves.
- Their power is deconfounding: comparing you to your own history removes platform lag, natural speaking rhythm, and personal style from every baseline-relative read. This is also why fair coaching is possible for speakers whose natural timing differs from population norms.

## Drills

- Baseline-driven focus pick: choose the stable metric with the worst 20-session trend and run its drill for two weeks. See [[drills-library]] and [[session-types]].

## FAQ

**Why does my baseline matter more than the average user's numbers?**
Because "unusual for you" is the real signal. A 2-second gap might be your normal thinking pace or a brand-new hesitation; only your own distribution can tell the difference.

**How fast do baselines personalize?**
By 4 samples the blend starts weighting your data; at 10 or more it is purely yours. About 10 analyzed sessions is where per-user reads become fully trustworthy.

## Research depth

Personal baselining is a load-bearing inclusion-by-design principle: coach you-vs-you first. See [[personal-baseline-principle]] and [[research-risks]] (synchrony artifact, cultural timing).

## Related

[[response-latency]] · [[speech-rate-modulation]] · [[backchannel]] · [[embedded-acknowledgments]] · [[white-belt]] · [[determinism-and-gaming]] · [[personal-baseline-principle]]
