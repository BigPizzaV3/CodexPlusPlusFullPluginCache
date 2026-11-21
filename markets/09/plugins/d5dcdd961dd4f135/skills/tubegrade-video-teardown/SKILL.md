---
name: tubegrade-video-teardown
description: Explain why one specific YouTube video worked (or flopped) — how far it beat its channel's normal views, its title format, what its thumbnail actually shows, how the first minute hooks, how it's structured, and how viewers reacted. Use for "why did this video blow up", "break down this video", "what can I learn from this video".
---

# Video teardown

Read `references/tubegrade-tools.md` first.

Goal: a clear, evidence-backed explanation of what made one video perform,
and the lessons the user can transfer.

## 1. Scope
You need the video link or id. Ask nothing else unless the user wants the
lessons applied to their own channel (then get their handle).

## 2. Evidence — ≈ 30 credits (+20 optional)
1. `tubegrade_get_video` (5) — views, age, duration, channel; `growth` if tracked.
2. `tubegrade_get_channel` (5) on its channel — the average views to compare
   against. Compute the outlier ratio yourself: views ÷ channel average.
3. `tubegrade_thumbnails` (1) — look at the thumbnail.
4. `tubegrade_get_transcript` (10) — the hook and structure.
5. `tubegrade_get_comments` (5, top) — what viewers responded to.
6. `tubegrade_viral_formats` (5, `kind` title) — does the title match a
   known format? Skip if the title pattern is obvious.
7. Optional, ask first: `tubegrade_find_similar_thumbnails` (20) — other
   videos packaged like it and how they did.

## 3. Analyse
- **Performance**: ratio vs the channel's normal, views per day of age. Is it
  a true breakout (≥3x), solid (1.5–3x) or normal? A big channel's routine
  upload isn't a breakout.
- **Title**: the promise, the format, the words doing the work.
- **Thumbnail**: what's in the frame and why it stops the scroll; how it
  pairs with the title. Only if you can actually see the image — otherwise
  say so and link it (see the tool notes).
- **Hook (first ~45s)**: quote 2–4 lines with their `[MM:SS]` (translated if
  the video isn't in English); how it sets stakes, previews the payoff,
  opens loops. Required — never just say the transcript was retrieved.
- **Structure**: a section map with timestamps from the transcript; where
  retention devices sit.
- **Audience reaction**: dominant themes from comments.

## 4. Deliver
1. **Verdict** — one paragraph: how well it did and the 2–3 main reasons.
2. **Scorecard** — performance, title, thumbnail, hook, structure: each with
   the evidence (timestamps, quotes, numbers).
3. **Transferable lessons** — 3–5, each phrased as something the user can do.
4. **What not to copy** — anything that depended on this creator's fame,
   timing or budget.

Hand-offs: apply the lessons to a new idea → **tubegrade-packaging-studio** or
**tubegrade-script-writer**.

## Don't
- Don't claim to know watch time, retention or CTR — TubeGrade only sees
  public data. Infer from structure and say it's an inference.
