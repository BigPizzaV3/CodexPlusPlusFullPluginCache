---
name: campaign-recap
description: Recap a social media campaign or content pillar using Socialinsider data — volume published, engagement earned, best posts, and how it compares to non-campaign output. Use when the user asks how a campaign, launch, hashtag or content pillar performed, wants a campaign wrap-up or post-mortem, or asks whether a content theme is working.
---

# Campaign recap

Report what a campaign or content pillar actually delivered.

## Rules

1. **Call `socialinsider_get_date_context` first, always.** Campaign questions are the most
   year-sensitive of all — never assume the current year.
2. **Resolve the campaign name, never guess it.** Call `socialinsider_resolve_campaign` with
   whatever the user said. It fuzzy-matches against the project's real tags and returns the best
   match plus alternatives. If the best match is not an obvious hit, show the user the candidates
   and ask which one they meant.
3. **Count server-side.** Use `socialinsider_count_posts` with `campaign_query` for volume. Never
   paginate `socialinsider_get_posts` per profile and add up the pages yourself.
4. **Read-only.**

## Steps

1. `socialinsider_get_date_context`.
2. `socialinsider_list_profiles` (and `socialinsider_list_campaigns` if the user has no name in
   mind and wants to see what exists).
3. `socialinsider_resolve_campaign` — turn the user's phrasing into the exact tag.
4. `socialinsider_count_posts` with the resolved `campaign_query`, the project, and the window.
   This returns the grand total, a per-profile breakdown, and any profiles that errored. Report
   errored profiles rather than quietly under-counting.
5. `socialinsider_get_top_posts` with `campaign_name` set, per profile that carried the campaign,
   `limit: 5`.
6. For the comparison baseline, run `socialinsider_get_posts_summary` twice per profile: once with
   `campaign_name` set and once without. The second is all output for the window, so campaign
   performance versus the profile's own everyday average is the difference between them.

## Output

- **Verdict** — one sentence: did the campaign beat the profile's normal output, and by how much.
- **Volume** — posts published, split by platform and profile. Note any profile that published
  nothing under the tag when it was expected to.
- **Performance versus baseline** — campaign average engagement per post against the window's
  overall average, as a percentage. This is the number that answers "did it work".
- **Top posts** — the best five, with the metric and the reason each landed.
- **What to repeat, what to drop** — concrete, tied to the numbers.

When the campaign window is short or the post count is small (under roughly ten posts), say plainly
that the sample is too small for a confident read and give the numbers without the verdict. Do not
manufacture a trend out of three posts.
