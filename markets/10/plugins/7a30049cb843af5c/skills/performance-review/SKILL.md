---
name: performance-review
description: >-
  Review what the user already posted on Instagram: which posts broke out against the account's own median, which earned shares, saves and follows, and how many visits their pages got, from Saypage's post and account insights and page stats; then say what to keep, stop and try next. Use for requests like "which of my posts did best", "look at my stats", "how did my month go", "what should I do more of". For one Reel in depth, use reel-analysis; for a plan to sell more, use sales-plan.
---

# Performance review

Best practices are averages over other people's accounts. This skill looks at the user's
own posts and numbers to see which of those practices hold for them, and where their
audience behaves differently.

## 1. Collect the numbers

With Saypage connected (`get_account` first; insights need `can_read_insights`):

- `list_instagram_posts` with `insights: true` and `limit: 48` (one call usually covers
  it), following `next_cursor` until you have about 30 posts or 60 days: each post's `numbers` hold reach, views, likes, comments,
  shares, saves and reposts, with watch time and `skip_rate` for Reels, and profile visits,
  new followers and `bio_link_taps` for feed posts. Instagram gives Reels none of those last
  three. Leave stories out: they are listed only while live, and their insights end with
  them. `get_instagram_post_insights` says why a number is `missing` on one post.
- `get_instagram_insights` over 30 days for the account as a whole, and over 90 or 180 days
  for the trend: past 30 days it reads Saypage's daily `history` (followers, views, each
  day's stories), which starts on `history_since`.
- `get_page_stats` over 30 days: visits per page and channel, and clicks on each page's links.
- `list_automations`: which posts have a keyword automation behind them.

Without Saypage, ask for screenshots of the insights of the user's last posts.

**State only numbers that a response returned.** When a metric is in `unavailable`, pass on
its reason (fewer than 100 followers, still processing, expired story) instead of a zero or
an estimate. The API has no retention graph, and splits followers from non-followers only
for the whole account (`reach_by_follower_status`), never per post: the user can screenshot
those from the app if they want them in the review.

## 2. Compute ratios, not totals

A big view count can simply mean a big following. Work out these, showing how:

| Measure | How | Tells you |
|---|---|---|
| **Breakout ratio** | views ÷ the median views of the account's posts of the same format | a real hit or an ordinary day |
| **Shares per 1,000 reach** | shares ÷ reach × 1,000 | worth sending to a friend: the strongest signal |
| **Saves per 1,000 reach** | saves ÷ reach × 1,000 | useful enough to keep |
| **Follows per 1,000 reach** | new followers ÷ reach × 1,000, feed posts only | whether the post (and the profile behind it) converts |
| **Bio-link taps per 1,000 reach** | `bio_link_taps` ÷ reach × 1,000, feed posts and stories | whether the post sends people to the offer |
| **Skip rate** | `skip_rate`, Reels only, against the median Reel's | whether the opening held people |
| **Average watch time** | from Reel insights | compare with the Reel's length, if the user knows it |

Report page views from `instagram_dm` separately, with their page and 30-day window: they
count page loads, not people. A page's `automations` split them by the automation that sent
them (since November 2026): only those entries belong to one post. `funnel-review` follows one keyword from reach to page
visits, and says when those numbers can be set side by side.

Order the posts by breakout ratio first and shares second. Keep formats apart: Reels
against Reels, carousels against carousels.

## 3. Find the pattern

Split the posts into a top third and a bottom third and list what differs: subject, hook
type (see `reel-script`), format, length, a face or hands in the opening frame, the ask,
how fast the user answered comments. Posting day and hour come at the end of the list,
since they seldom explain much.

Attach the evidence and a confidence level to each finding. Under about fifteen posts,
present patterns as hunches to test, not conclusions.

## 4. Diagnose before advising

- **Low reach**: the hook and the opening frame (`reel-script`).
- **Good reach, few new followers** (feed posts, or the account's total, since Reels report
  none): visitors reach the profile and leave; look at the bio and its link
  (`profile-review`).
- **Good reach, few shares or saves**: people watch but do not find it useful or personal
  enough to keep or pass on.
- **Comments but no sales, or DMs missing**: that is one funnel's story, not the post's: use
  `funnel-review`.
- **Reach with nowhere to go**: a Reel that broke out without a keyword ask, or whose
  keyword no automation answers (`comment_keyword` in `list_instagram_posts`, nothing in
  `list_automations`), left its viewers only the bio link. Say what it could have brought,
  without inventing a number, and offer `reel-funnel`: on that Reel if it still draws
  comments, otherwise on the next one.

## Output

```
REVIEW  ·  28 posts  ·  1 Sep - 25 Oct  ·  median views: Reels 3,900, carousels 1,700

TOP BY BREAKOUT RATIO
  9.1x  Reel      "I salted pasta water wrong..."  35,600 views  41 shares/1k  14 s watched
  4.3x  Carousel  5 weeknight sauces               7,300 views   58 saves/1k
  ...

BOTTOM
  0.3x  Reel      new menu announcement            1,200 views   2 shares/1k
  ...

WHAT THE NUMBERS SAY
1. Mistake-and-fix Reels: 4 of the top 5, none in the bottom 5 (fairly sure, n=9).
2. Announcements get reach but no shares: move them to stories.
3. The salt Reel reached 90,000 people with no keyword ask: nowhere to go from there.

KEEP   mistake-and-fix Reels, recipe carousels
STOP   menu announcements as Reels
TRY    a carousel version of the top Reel, with a keyword for the full recipe
       the next mistake-and-fix Reel closes on "Comment SALT": its page sent by DM
```

Then offer to build next week on it (`content-calendar`).
