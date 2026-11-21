---
name: cheerful-campaign-pulse
description: "Show how the user's Cheerful influencer campaigns are doing: emails sent, replies, reply rate and opt-ins per campaign, which campaign is behind and why, and how many replies are waiting on the user. Read-only. Use when the user asks \"how are my campaigns doing\", \"campaign report\", \"which campaign has the lowest reply rate\", \"which campaign is behind\", \"how many opt-ins do I have\", \"what's my reply rate\", or \"give me a campaign update\"."
---

# Campaign pulse

Sends, replies and opt-ins across the user's campaigns, the one that is behind, and what is
waiting on them. Read-only: it changes nothing and spends no credits.

## Step 0: Check the connection

If a Cheerful tool is unavailable, or a call answers "Tool not found" or asks to reconnect, stop
and tell the user: "Connect Cheerful from the plugin page, then ask me again." Don't retry.

## Read this first: what the data can and can't tell you

- **Rates need a base.** A campaign with 2 sent and 0 replies is "too early to tell", not "the
  worst". Call a campaign behind only when it has sent enough to compare (about 10+), and say how
  many were sent either way.
- **Paused is not broken.** A paused campaign stopped sending; its replies still count.
- **Teammates' campaigns are included.** If a campaign carries `owner_email`, say whose it is.
- **"Not found" can mean "not yours".** If a campaign can't be opened, list the campaigns again
  instead of guessing; it may belong to someone who hasn't shared it.
- **These are outreach numbers, not spend.** For credits use `billing_usage`, and report credits,
  never dollars.

## Workflow

1. **All campaigns.** Call `campaign_read` with `action="index"` and `include_stats=true`. For each
   campaign take sent, replies, opt-ins and status, and work out the reply rate (replies ÷ sent).
2. **Account totals.** Call `campaign_report` with `action="account"` for the account-wide reply
   rate, opt-in rate and recent opt-ins.
3. **The one that matters.** If the user named a campaign, use it. Otherwise pick the campaign
   with the lowest reply rate among those with enough sends (see above). Call `campaign_report`
   with `action="campaign"` and its `campaign_id` for the funnel and the sending timeline. For
   "give me a summary of <campaign>", use `action="summary"` instead: the same report plus the
   replies waiting on the user and the top posts, in one call.
4. **Why.** Explain from the numbers only: few emails sent yet, sending stopped (paused, or the
   timeline goes flat), replies but few opt-ins (the offer), or no replies at all (the opener or
   the creator fit). Don't invent causes the data doesn't show.
5. **Waiting on the user.** Call `inbox_read` with `action="counts"` (and the `campaign_id` if one
   campaign is in focus). `pending` is replies waiting on the user; `outbox` is sent and waiting
   on the creator. If `capped` is true, say "100+". A missing count means "couldn't count right
   now".

## Output layout

In ChatGPT the report appears as a campaign card automatically. After the card, write at most 2
sentences: the campaign that is behind and the likeliest reason, then one next step. Don't repeat
the card's numbers in prose.

Where no card is shown (for example in Codex), use this layout:

```
**2 campaigns · 6 emails sent · 50% reply rate · 2 opted in**

| Campaign | Status | Sent | Replies | Reply rate | Opted in |
|---|---|---|---|---|---|
| Spring Skincare Seeding | paused | 4 | 3 | 75% | 2 |
| Vegan Snacks Launch | paused | 2 | 0 | 0% | 0 |

**Behind:** Vegan Snacks Launch — 2 sent and no replies yet, so it's too early to judge; sending stopped on Sep 25.
**Waiting on you:** 0 replies need an answer.
**Next:** "Who replied to Spring Skincare Seeding?"
```

## Rules

- Plain language: no ids, field names, status codes or "tool" in the reply.
- Pausing, resuming or editing a live campaign happens in Cheerful at https://app.cheerful.ai.
  Point there for those, without promising anything will be sent. A new campaign can be set up
  here when `create_campaign_draft` is listed.
- Don't promote plans or purchases.
- Don't round 0 replies into "low"; say "no replies yet".
