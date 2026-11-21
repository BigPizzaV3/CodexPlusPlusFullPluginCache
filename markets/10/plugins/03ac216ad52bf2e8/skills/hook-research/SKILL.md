---
name: hook-research
description: Research real viral Instagram Reels hooks for a product, niche or topic using the Hookest library. Use when the user asks what hooks are working right now, wants real examples for an ad or video, or wants a short hook brief before writing.
---

# Hook research with Hookest

Goal: give the user real, recent hook examples for their topic and a short brief
they can write from. Everything comes from the Hookest MCP tools. Do not invent
examples or metrics.

## Steps

1. **Get valid filters.** Call `list_filters` once. Use only the category slugs
   and country codes it returns. Note the window counts: short windows (7d, 30d)
   can hold very few hooks.

2. **Search.** Call `find_hooks` with:
   - `query`: the product or topic in a few words
   - `category_slugs`: the closest one or two categories, if any fit
   - `added_window`: `7d` or `30d` when the user asks for "this week", "new"
     or "latest" hooks (added to Hookest), paired with `sort: views`
   - `window`: only when the user means the Instagram post date. Pick one with
     enough hooks according to `list_filters` (default `all`)
   - `sort`: `trending` unless the user asks otherwise
   - `limit`: 10

   If the result is thin, drop the query and search by category only, then say
   that you widened the search.

3. **Go deeper on the best 3.** Call `get_hook` for the top results
   (`comment_limit: 3`) to get metrics, the emotion radar and what commenters
   reacted to. Use `find_similar_hooks` on the single strongest one if the user
   wants more of the same kind.

4. **Write the brief.** Keep it short:
   - The 3 to 5 strongest examples: account, views, why it likely works
     (based on the metrics and comments, not guesses), and the Hookest link
   - What they have in common: angle, emotion, length, format
   - 2 or 3 directions the user could take for their own product

## Be honest about the data

- The library is Instagram Reels only. Do not claim TikTok or YouTube coverage.
- A library item's caption is not the spoken hook. Do not present it as a
  transcript.
- Hookest has no data on hook patterns (curiosity gap, pattern interrupt and
  so on). If asked, say so and describe what the examples have in common instead.
- Hookest cannot analyse an arbitrary Instagram URL. If the user pastes one that
  `get_hook` does not find, say it is not in the library and offer `find_hooks`.

## Next step

If the user wants new hooks for their own product, continue with the
`write-hooks` skill.
