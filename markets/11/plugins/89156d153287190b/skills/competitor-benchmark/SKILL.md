---
name: competitor-benchmark
description: Benchmark a brand against its competitors on social media using Socialinsider data — share of engagement, posting cadence, engagement rate and format mix side by side. Use when the user asks how they compare to competitors, wants a competitive or industry benchmark, share-of-voice analysis, or asks who is winning on a platform.
---

# Competitor benchmark

Compare several profiles over the same window and say who is actually winning and why.

## Rules

1. **Call `socialinsider_get_date_context` first, always** — then reuse the exact same `date`
   object for every profile. A benchmark across mismatched windows is worthless.
2. **Same platform, same window.** Never compare an Instagram profile against a LinkedIn one in
   the same table. Group by platform and produce one table per platform.
3. **Never invent ids.** Resolve every profile through `socialinsider_list_profiles`. If the user
   names a competitor that isn't tracked, say so and stop — do not silently drop it and do not add
   it (adding profiles counts against their subscription; see the note at the end).
4. **Read-only** unless the user explicitly asks to start tracking someone.

## Steps

1. `socialinsider_get_date_context`.
2. Resolve the competitive set:
   - `socialinsider_list_profiles` for the project.
   - `socialinsider_list_brands` when the project is brand-grouped — brands are the intended unit
     of benchmarking, so compare brand against brand rather than a single profile against a brand.
3. Confirm the set with the user when it is ambiguous: list who you are about to compare, on which
   platform, over which window. One line, then proceed.
4. For every profile in the set, over the identical window:
   - `socialinsider_get_posts_summary` — post count, total engagement, average per post,
     engagement rate, post-type breakdown.
   - `socialinsider_get_profile_data` — follower count and growth over the window.
5. Optional, when the user wants to know *what* the competition is doing well:
   `socialinsider_get_top_posts` with `limit: 3` for the leaders only.

## Output

One table per platform, sorted by engagement rate (not by raw engagement — raw totals just
rank by follower count):

| Profile | Followers | Follower Δ | Posts | Total eng. | Eng./post | Eng. rate |

Then:

- **Ranking and gap** — where the user's brand sits, and the size of the gap to the leader in
  percentage terms.
- **Cadence versus efficiency** — separate the brands that win by posting more from the brands
  that win per post. These need opposite responses.
- **Format edge** — which post types the leaders use that the user's brand under-uses.
- **Two moves** — the highest-leverage changes, each grounded in a number from the table.

Always normalise by follower count before declaring a winner, and say so. If a competitor's
engagement rate is inflated by a single outlier post, name that post rather than the average.

If the user wants an untracked competitor added, state the exact profile URL, run
`socialinsider_profile_search` to verify it, present what will be created, and wait for explicit
confirmation before calling `socialinsider_add_profile` — it consumes their profile limit.
