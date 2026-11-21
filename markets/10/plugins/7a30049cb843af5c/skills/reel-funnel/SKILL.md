---
name: reel-funnel
description: >-
  Turn a Reel's views into customers: choose one goal and one Reel (one already posted that still draws comments, or the next one), then build the whole path and test it: the keyword ask, the DMs, a page made for that Reel, the button to the user's checkout or booking link, and the automation that answers every commenter. Use for requests like "turn this Reel into sales", "build the funnel for this Reel", "sell from my next Reel", "set up a new funnel". For a funnel already running, use funnel-review.
---

# Reel funnel

A Reel that gets views earns nothing until a viewer has a next step they can take in a few
seconds. This skill builds that path for one Reel, from the ask to the sale, and checks that
it works from end to end. The other skills hold the detail of each step; this one sets the
order and finishes the job.

## 1. One goal

Ask in a single message, skipping what the user already said:

1. What should a viewer do after this Reel: buy, book, join the email list, or follow?
2. What are they buying or booking, at what price, and where is the link?

Saypage pages take no payment and hold no form, so the sale happens on the user's own
checkout or booking link (a shop, a payment link, a calendar). If there is nothing to sell
yet, run `offer-finder` first: without an offer, this path leads nowhere.

| Goal | The page's main button | Gate in the DMs |
|---|---|---|
| Sell | their checkout, with the price on the button | none |
| Book | their booking link or calendar | none |
| Grow the email list | what comes next: the offer or the newsletter | `email_gate` |
| Win followers | the offer, or the Reel to watch next | `follow_gate` |

One goal per Reel: a page that asks for two things usually gets neither.

## 2. One Reel

With Saypage connected: `get_account`, then `list_instagram_posts` and `list_automations`,
every page of it (follow `next_cursor` until it is null) before saying no automation answers
a Reel.

**A Reel already posted** is the fastest start: nothing to film, and it may still reach
people. Among the Reels of the last 60 days that no automation answers, compare
`get_instagram_post_insights`, and read `list_instagram_comments` for recent comments and
what people ask. Recommend the one still drawing comments, best of all with people asking
for something the user can send (`opportunity-scan` ranks them when there are many). Say what
stays out of reach:

- **Saypage cannot edit a caption.** The user adds the ask in the Instagram app, or you pick
  a word commenters already use ("recipe"), which needs no edit.
- **Comments made before the automation get no DM.** Once it is on, offer to reply to a few
  of them with the keyword (`reply_to_instagram_comment`, varied wording, with the user's
  go-ahead): they have to comment again to get it.

**The next Reel**: write it with `reel-script`, closing on the ask. Build the page now, then
create the automation once the Reel is live, or leave out `provider_media_id` to arm it for
the next post, where the plan allows it (`status: waiting` until that post gets its first
comment).

## 3. The promise and the keyword

Write one line: what a commenter gets. Everything below has to keep that promise, and only
what is true goes in it. Then choose the keyword, by the rules in `instagram-caption`: one
short word, no spaces, no accents, no emoji. It is said in the Reel, shown on screen and
written in the caption.

If another tool already answers this post, the user turns it off there first, or commenters
get two DMs.

## 4. The page

Build a page for this Reel alone: `get_page_guide` first, and follow its section "A page
made for one Reel". What the Reel promised comes first, in full, then the main button from
step 1. Show `preview_page`, and call `publish_page` once the user agrees.

- **One page, one automation.** A page that only this automation sends keeps its numbers
  readable for `funnel-review`.
- **Tag the outgoing link** when the user's shop or booking tool reads tags, for example
  `?utm_source=instagram&utm_campaign=pasta`, with the keyword as the campaign. Saypage counts
  the click but never sees the sale, so this tag is how their own tool can show which Reel
  sold.
- **On the Connector plan** only the home page goes online: build this page and show its
  preview all the same, then say once what it needs. **On the Free plan** nothing is built:
  say once what the page would do and that it needs a plan ("Plans" in the `saypage` skill).

## 5. The DMs

Write them with `dm-writing`, and let the user choose the words.

- **Use the gate the goal calls for, and no other.** Each gate loses some people: none for a
  sale, `email_gate` for the list, `follow_gate` for followers. Use both only if the user
  asks. When a gate is on, say so in the ask ("Comment GUIDE and leave your email"), so the
  request comes as no surprise.
- **Leave out `extra_link_buttons`**: on this path, each one is an exit before the goal.

## 6. Turn it on

Show the whole path in one block (post, keyword, messages, gate, page, link) and **ask**.
Then `create_automation`. If it answers `activated: false`, give its `reason`: on the
Connector plan it stays a draft, ready for later. On the Free plan it is refused: do not
retry, say once that it needs a plan. Never create a second one for the same post and
keyword: `update_automation` changes anything later and keeps the history.

## 7. Walk the path

A path nobody walked is not finished. Ask the user to comment the keyword from another
account (the account's own comments never trigger it) and check on a phone:

1. The first DM arrives, and its button works.
2. Any gate asks the right thing, then the link DM arrives.
3. The page opens, and its first screen matches the Reel.
4. The main button reaches the checkout or booking page.

`get_automation_activity` shows how far that comment got. When nothing arrives after a few
minutes, check the spelling of the keyword, then `plan.dms_this_month` against
`plan.limits.monthly_dm_limit` in `get_account`, then try another account: Instagram does
not share every account's comments with apps.

## Output

```
FUNNEL  ·  Reel "15-minute lemon pasta"  ·  still drawing comments

GOAL      Sell the 40-recipe book, $12
KEYWORD   PASTA, a word commenters already use; add it to the caption in the app
DMS       opening + "Send me the recipe", then the link + "Open the recipe"
GATE      none
PAGE      toto-cooks.saypage.page/lemon-pasta (live)
BUTTON    "Get the 40-recipe book · $12" -> their checkout, tagged pasta
TEST      comment from a second account: DMs, page and checkout all fine

Next: ask "how did PASTA do?" in 48 hours (funnel-review).
```

Saypage sends no reminders, so give the user that sentence to come back with. Then offer the
next Reel, or `content-calendar` to give each post of the week its own path.
