---
name: tubegrade-video-ideas
description: Find video ideas a creator can adapt, backed by videos that actually broke out (beat their own channel's normal views) in their niche. Use for "give me video ideas about X", "what's working in my niche", "find breakout videos I could make my own version of".
---

# Video ideas from breakout evidence

Read `references/tubegrade-tools.md` first.

Goal: a short list of ideas the user can make, each backed by real videos that
over-performed — not a brainstorm.

## 1. Scope (ask only what changes the search)
Reuse what the user already said. Ask at most one question, and only if the
niche is unclear. Useful context: niche/topic, their channel (handle), long-form
or Shorts, language/market. If they gave their channel, one
`tubegrade_get_channel` call tells you their size and topic.

## 2. Gather evidence — budget ≈ 30–60 credits
Run 2–3 lanes, each bounded:
- **Breakouts on the topic**: `tubegrade_find_outliers` with 1–2
  mechanism-shaped queries (the promise, not just the noun — "beginner
  mistakes in X", "I tried X for 30 days"), `days` 180–365, `min_ratio` 2–3.
- **Live check** (if find_outliers is thin): one `tubegrade_search_videos`
  (`upload_date` month or year) and keep results with `outlierRatio` ≥ 2.
- **Adjacent channels** (optional): if the user named a competitor,
  `tubegrade_get_channel_outliers` on it.

Stop gathering when you have ~10 strong candidates. Don't call the same tool
with near-identical queries.

## 3. Judge
For each candidate, keep it only if:
- the ratio is meaningful (≥2x, and the channel isn't tiny),
- the **mechanism** transfers — name it: the promise, format, or angle that
  made it work (e.g. "time-boxed challenge", "myth vs reality", "ranking"),
- the user could actually produce it (no celebrity access, no huge budget),
- it isn't the same idea as another candidate.

Group candidates that share a mechanism; one idea per mechanism.

## 4. Deliver 5–8 idea cards
For each:
- **Idea** — a working title in the user's niche (original wording)
- **Why it should work** — the mechanism, in one sentence
- **Evidence** — 1–3 source videos, each as: title — https://www.youtube.com/watch?v=<id> — views, outlier ratio, age
- **Make it yours** — the specific twist for their channel
- **Confidence** — high / medium / low, and why (sample size, ratio strength,
  how far the adaptation stretches)

Then one line on coverage: what you searched, and anything thin or missing.

## Hand-offs
- Titles and thumbnails for a chosen idea → **tubegrade-packaging-studio**
- A full script → **tubegrade-script-writer**
- Picking ONE idea to make next → **tubegrade-next-video-planner**

## Don't
- Don't present a source video's title as the idea — write an original one.
- Don't rank by raw views alone; outlier ratio is the signal.
