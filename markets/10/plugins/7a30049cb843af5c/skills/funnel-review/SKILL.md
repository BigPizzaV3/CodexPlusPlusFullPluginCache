---
name: funnel-review
description: >-
  Review and optimize keyword funnels already running: follow each one from a Reel's views to comments, DM taps, links sent, page visits and the sales the user reports, compare funnels with each other, find the step that loses the most people, fix that one step in the DMs or on the page, and check next time whether it worked. Use for requests like "how did my keyword do", "optimize my funnel", "improve my conversion", "is my automation working", "people comment but nobody buys", "why doesn't anyone tap the DM".
---

# Funnel review

`performance-review` asks which posts worked. This skill asks what happened to the people a
Reel sent down the path, where they stopped, and what to change. Each round changes one thing,
so the next one can tell whether it helped: that loop is what improves a funnel, more than any
single rewrite.

If no automation has run yet, there is nothing to read: use `reel-funnel` instead.

## 1. Collect the numbers

With Saypage connected: `get_account`, then `list_automations`, following `next_cursor`
until it is null, which gives each one's `gates` and destination (`page_id` or
`custom_link`). Rank only once you have every page. For the funnels you review,
`list_automations` with their `automation_id` gives the messages: `opening_message_copy`,
`opening_message_button_label`, `private_message_copy` (the link message) and
`recipe_link_button_label`.

Then, for the funnels that ran, ten at most: the most `links_sent` first, then the newest
Reels (`get_automation_activity` allows about six calls a minute: when it refuses, wait the
seconds it names):

| Step | Where it comes from |
|---|---|
| Views and reach | `get_instagram_post_insights` on the automation's post (an ad has none) |
| Keyword comments | `triggered` and `people` in `get_automation_activity`; a post's `comments` also hold the account's own replies |
| Raised hands it missed | `missed` there (30 days): the keyword while it was off, another spelling, or a plain ask for the link, from people it never DMed |
| First DM sent | `first_dm_sent` |
| Tapped | `tapped` |
| Gates | `asked_to_follow`; `asked_for_email` and `gave_email` |
| Links sent | `links_sent` |
| Stopped | `not_sent` by cause: `never_tapped` (got the first DM, did not tap), `window_expired`, `plan_limit` |
| Page loads from DMs | this automation's `views` in the page's `automations`, in `get_page_stats` (or `page_views` in `list_instagram_posts` with `insights: true`); before November 2026, only `instagram_dm` for the whole page |
| Clicks from DMs | this automation's `clicks` there (`page_clicks`); `destinations` names the links |
| Sales or bookings | only from the user's shop or booking tool: `sales-attribution` joins its orders with the funnel by a tagged link, the email or a code |

Ask how many sales or bookings came in since the funnel started, and whether their tool shows
the link's tag. If they have no number, say the path stops at the click, and that a tagged
link would show the rest next time.

**State only numbers that a response returned or the user gave.** When a metric is in
`unavailable`, pass on its reason.

**Leave out the user's own tests.** `recent` names each commenter: on a small funnel, accounts
that are plainly theirs can be most of the numbers. An automation counts from its
`activated_at`, so `links_sent: 0` on a new one is no result.

## 2. Check that the numbers belong together

These tools count over different windows. Before putting page loads next to `links_sent`,
all three must hold:

1. **The page loads are this automation's own**: its entry in the page's `automations`,
   which Saypage counts since it began tagging DM links per automation (November 2026). For
   loads before then, or a funnel older than that, only the page's `instagram_dm` total
   exists: it belongs to one automation only if this automation alone sends the page, as
   its main link or an extra button (`list_automations`).
2. **`days` covers the whole life of the funnel.** `get_page_stats` goes back 90 days, while
   the activity summary covers 13 months.
3. **The automation stayed on this post.** An automation moved from another Reel carries
   that Reel's history in its summary.

If one fails, report page loads on their own, with their window, and draw no ratio across
them. Even when all three hold, page loads count every load, repeat visits and link-preview
bots included, so call the figure "page loads per link sent", which can pass 100%, and never
a conversion rate or a number of people.

Clicks are taps on a page's links, not people: one person can tap twice, and a few taps are
missed. Saypage counts them since November 2026, so a funnel that ran before then shows fewer
than it got, and it sees nothing after the click.

## 3. Read the path

Wait for at least 48 hours of activity. Below about 30 keyword comments, show the counts and
skip the percentages: a few people more or less would swing them.

- **Keyword comments per 1,000 views**: `triggered` ÷ views × 1,000.
- **Tap rate**: `tapped` ÷ `first_dm_sent`.
- **Gate rate**: `gave_email` ÷ `asked_for_email`.
- **Delivery**: `links_sent` ÷ `triggered`.
- **Click rate**, when step 2 holds: `instagram_dm` in `click_channels` ÷ `instagram_dm` in
  `channels`, labelled as an estimate.
- **Sale rate**, when the user gave a number and step 2 holds: sales ÷ clicks from DMs,
  labelled as an estimate.

People still under way (`waiting_for_tap`, `waiting_for_follow`, `waiting_for_email`,
`in_progress`) are not lost yet: say how many there are.

There is no universal good rate, so quote no benchmark. Compare a funnel with the user's
earlier funnels, and with itself after a change.

## 4. Compare the funnels

With several automations, line them up before fixing anything, one row per funnel, using the
measures of step 3. Then:

- **Start with the funnel where a fix reaches the most people**: new keyword comments keep
  coming on a live Reel, and a quiet one has little left to win, so note its fix for next time.
- **Copy what the best funnel does.** When one taps far better than the others, read both
  sets of messages side by side: its wording, its button, its gate, its keyword. Different
  Reels bring different people, so treat the gap as a lead to test, not as proof.

## 5. Find the weakest step, and fix only that

| What you see | Usual cause | Fix |
|---|---|---|
| Reach, few keyword comments | the ask comes late, is not said aloud, or promises little | the ask, in `reel-script` and `instagram-caption` |
| Many comments, few `triggered` | people write another word | `missed` shows which (`near_keyword`, `asked_for_link`); then widen or change the keyword (`update_automation`) |
| `not_sent` with cause `plan_limit` | the plan's monthly DM limit | compare `plan.dms_this_month` with `plan.limits.monthly_dm_limit`, and tell the user plainly |
| `not_sent` with cause `window_expired` | Instagram's 24-hour window closed before the next DM | fewer steps or a shorter gate; a closed window cannot be reopened |
| `failed` as a `stage` in `recent` | delivery problem | give each `reason`; do not guess |
| Low tap rate | the first DM does not say what they get | rewrite `opening_message` and its button (`dm-writing`) |
| Stopped at a gate | the gate asks too much for what they get | reword it, or weigh dropping it |
| Links sent, few page loads | the link message gives no reason to open it | rewrite `link_message` (`dm-writing`) |
| Page loads, few clicks | the page | below |
| Clicks go to the wrong link | a secondary link competes with the main button | `destinations`: cut it or move it down the page (`get_page_guide`) |
| Clicks, no sales | the offer, or the page they land on after Saypage | ask the user; `offer-finder` |

**When the page does not send people on**, reread the page and go through "A page made for one Reel" in
`get_page_guide`: does the first screen match the Reel, is the main button visible at once,
does it say what they get and the price, does the page answer the doubts from the comments?
If the page holds up, the question is the offer (`offer-finder`), and the user may know more
than the numbers do: ask what people say when they do not buy.

Propose one change, written out in full. Two changes at once cannot be told apart.

## 6. Apply it, with the user's go-ahead

- **DMs and keyword**: `update_automation`. A live automation stays live and keeps its
  history. Each message stays in the user's language, and button labels stay within 20
  characters. The change applies to new comments only.
- **Page**: `update_page`, `preview_page`, then `publish_page` once they agree.

## 7. Check it worked

Followers cannot be split into two groups here, so each test runs one after the other: note
the numbers, change one thing, then compare what came after.

The activity summary keeps adding up, so keep today's numbers and the date in the output. At
the next round, subtract them to get the period since the change, and wait for about 30 new
keyword comments before judging it. A better result on a fresher, bigger Reel may come from
the Reel, so say so. Keep what helped, undo what did not, then move to the next weakest step.

## Output

```
FUNNEL  ·  PASTA  ·  Reel "15-minute lemon pasta"  ·  since 3 Oct

views               52,300
keyword comments       612   12 per 1,000 views
first DM sent          604
tapped                 391   65% of first DMs    <- biggest loss
links sent             388
page loads from DMs    402   about 1 per link sent (loads, not people)
clicks from DMs        118   29% of page loads (taps, not people)
sales                   31   from your shop, your number

STILL UNDER WAY   9 waiting for the tap

WEAKEST STEP   a third of people never tap the first DM
WHY            the message doesn't say what they get
CHANGE         "Here's the 15-minute pasta 🍋 Tap below and the recipe is yours."
               button: "Send me the recipe"
COMPARE WITH   tapped 391 of 604 on 10 Oct: review again in a week
```

Run every rewritten message through `natural-voice` before showing it.
