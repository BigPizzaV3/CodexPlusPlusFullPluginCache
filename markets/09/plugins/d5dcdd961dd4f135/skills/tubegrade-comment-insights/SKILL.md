---
name: tubegrade-comment-insights
description: Mine YouTube comments for what viewers actually ask, want, complain about and praise — in their own words — and turn it into video ideas, title language and script fixes. Use for "what do viewers want", "analyze the comments on this video", "find content gaps from comments".
---

# Comment insights

Read `references/tubegrade-tools.md` first.

Goal: viewer demand and language, counted honestly from a bounded sample.

## 1. Scope
Pick the sample:
- **Specific videos** the user names, or
- **A topic**: find 3–5 relevant, well-performing videos with
  `tubegrade_find_outliers` or `tubegrade_search_videos` (5–10 credits), or
- **A channel**: `tubegrade_get_channel_outliers` or `tubegrade_channel_videos`
  and take its 3–5 most relevant recent videos.

## 2. Collect — ≈ 15–30 credits
`tubegrade_get_comments` per video (5 each), `limit` 50–100, `sort` top. Add a
`newest` pull on one video only if recent reactions matter (e.g. a fresh
upload). Keep the sample to 5 videos unless the user asks for more.

If the user wants to know what a video *said* that triggered reactions,
`tubegrade_get_transcript` (10) on that one video.

## 3. Analyse
Read every comment you pulled. Sort them into:
- **Questions** — things viewers asked that the video didn't answer
- **Requests** — "do a video on…", "part 2", follow-ups
- **Pain points / objections** — confusion, disagreement, problems
- **Praise** — what specifically landed (a moment, an explanation, a format)
- **Language** — the exact phrases viewers use for the problem and outcome

Count how many comments fall into each theme across the sample (approximate
is fine; say "about"). Weigh likes: a highly liked comment speaks for many.
Ignore spam, self-promotion and pure emoji.

## 4. Deliver
1. **Sample** — the videos (linked) and how many comments you read.
2. **Top themes** — ranked, each with an approximate count and 1–2 short,
   representative quotes (trimmed; no usernames).
3. **Video ideas** — 3–5 directly from unanswered questions and requests.
4. **Words to use** — viewer phrases for titles, hooks and thumbnails.
5. **Fixes** — if these are the user's own videos, what to clarify or add.

## Don't
- Quote comments without the commenter's name unless the user asks who said
  it; `isChannelOwner` marks the creator's own replies.
- Don't generalise beyond the sample — say how many comments and videos it covers.
