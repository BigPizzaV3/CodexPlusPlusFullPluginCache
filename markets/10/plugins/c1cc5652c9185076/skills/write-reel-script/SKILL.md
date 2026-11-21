---
name: write-reel-script
description: Write a short-form video script or generate content ideas, prioritised by what actually drives reach. Use when asked to write a reel script, a hook, a TikTok script, or for ideas on what to post next.
---

# Write a reel script

## Tools

| tool | cost | returns |
|---|---|---|
| `generate_script(topic, duration_seconds, language)` | paid plan, spends content quota | a full script |
| `generate_ideas(count, language)` | paid plan, spends content quota | idea list |
| `find_topics(niche, count, language)` | paid plan; cached reads free | timely, web-searched topics |

These are **synchronous** and return the result directly, with no job to poll.

They are much stronger when the person has connected Instagram and tracked
competitors in the Reelyze dashboard, because the generation learns from what
already works on their account. They still work from a topic alone. If the
output feels generic, that is usually why, and it is worth saying so rather than
regenerating.

`find_topics` returns a cached result for free; only a `fresh: true` run spends
the metered web search, which is capped per billing cycle. Prefer the cached
read unless the person explicitly wants new topics.

## Write to the reach order, not to a formula

Rank every choice in the script by what actually moves distribution, in this
exact order:

1. **The hook, first 3 seconds.** The biggest single lever by a wide margin.
2. **Watch time, the rest of the video.** A *separate* lever. A script can win
   the first 3 seconds and still lose people at 5 to 8 seconds, and low average
   watch time stops the algorithm expanding reach even though the opening
   worked. So the script needs a reason to keep watching at 5s, at 10s, and at
   15s, not only at 0s.
3. shares
4. likes
5. saves
6. reposts
7. comments

A script optimised for comments at the expense of the hook is optimised for the
weakest signal in the list.

## What a usable script contains

- the hook as **exact words**, not a description of a hook
- on-screen text for the opening, since most viewers are watching muted
- a named reason to stay at roughly 5 seconds and again near the middle
- a close that earns a share, which outranks a like
- a length that matches `duration_seconds`, written to be *said* out loud rather
  than read

Be concrete and specific. "Share a personal story" is not a script. The point of
grounding generation in the creator's own posts is to avoid exactly that kind of
output, so do not hand it back in the reply.

## Do not

- Do not promise a script will go viral. 7.7% of reels in Reelyze's measured
  dataset reach 10x the account's follower count, and nothing in a script moves
  that to a certainty.
- Do not pad to length. A 30-second script that works beats a 60-second one that
  drifts, and drift is a watch-time problem.
- Do not add more than five hashtags. See `fix-reel-hashtags`.
