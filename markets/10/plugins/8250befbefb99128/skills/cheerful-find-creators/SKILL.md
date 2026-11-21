---
name: cheerful-find-creators
description: "Turn a creator brief into a Cheerful search on Instagram, TikTok or YouTube, report the creators actually found, shortlist the best fits and save them to a list when asked. Searches use Cheerful credits. Use when the user says \"find creators\", \"find influencers\", \"search for TikTok/Instagram/YouTube creators\", \"creators like @handle\", \"build a shortlist\", \"who should I reach out to for this brief\", or \"find 20 US skincare creators with 10k-100k followers\". Not for general influencer-marketing advice, captions or scripts where the user has not asked to find creators."
---

# Find creators

Turn a brief into one Cheerful creator search, show what came back, and help the user pick a
shortlist. Every search uses credits from the user's Cheerful plan, so run one search per request
and don't re-run it to "get more" unless the user asks.

## When not to search

A question about influencer marketing in general ("what is a good engagement rate?", "write a
caption") is not a search request. Answer it directly and spend no credits. Search only when the
user wants actual creators.

## Step 0: Check the connection

If a Cheerful tool is unavailable, or a call answers "Tool not found" or asks to reconnect, stop
and tell the user: "Connect Cheerful from the plugin page, then ask me again." Don't retry.

## Read this first: what the data can and can't tell you

- **Count only the rows you received.** `creator_search` returns a `total` that is the provider's
  pool before filtering, often tens of thousands. Never report it. "Found 8" means 8 rows came back.
- **Most creators have no public email.** That is normal, not a failed search, and not a reason to
  search again. Emails are found later, when creators are added to a campaign in Cheerful.
- **Don't drop what the brief didn't exclude.** No invented follower or engagement floors. A
  1k-follower creator who fits the niche is a valid result.
- **Every note is evidence or an honest gap.** A row's note says WHY it fits, from what came back:
  the account's name or category, or, for the shortlist, a bio phrase or recent post topic from
  `creator_profile` ("bio: 'Giants fan since '86'"). Never write "search match" or "related
  account": if nothing shows the fit, write "fit not confirmed" and keep it out of the shortlist.
- **A place in the brief is checked per row.** If the brief names a city or country, say per row
  whether the data confirms it ("NYC in bio", "US", "location not shown"). One sentence that
  says "location isn't confirmed" for the whole table hides which rows are right.
- **Fan pages, brand pages and media accounts are not creators by default.** If the brief asks
  for fan accounts, they are the target; otherwise label a page that only reposts, a team or a
  publisher as "media/fan page" so the user can decide.
- **Low engagement is a flag, not a filter.** Under about 0.5% on 50k+ followers often means a
  bought audience. Say so next to that creator; keep them in the list.
- **Some searches are slow on purpose.** A keyword search takes a few seconds, a smart search
  about a minute, and a YouTube search runs in the background for 10-45 minutes. Tell the user it is working; don't
  start a second search over the top of one that is still running.
- **Out of credits.** If the search reports the user is out of credits, call `billing_usage` and
  say how many credits are left and when they renew. Nothing more.

## Workflow

1. **Read the brief.** Pull out platform (default Instagram — say so), who the creator is (describe
   the person: "vegan meal prep mom", not the product), country, follower range, engagement floor
   if given, and how many creators (default 10). Ask one question only if the brief has no niche
   at all.
2. **Pick the search.** Call `creator_search`:
   - `action="keyword"` when the brief has hard filters (country, follower range, engagement), or
     names a country the smart search can't bind (the tool description lists the ones it can).
     Put countries in `location` as full names: "United States", not "US".
   - `action="smart"` for an open, descriptive brief with no hard filters.
   - `action="similar"` for "creators like @handle", with the handle as `query`.
   - Leave apostrophes out of `query` ("womens health", not "women's health").
   - Set `limit` to the number asked for (up to 50).
3. **YouTube only.** `creator_search` with `platform="youtube"` starts a background search and
   returns a run id, not creators. It vets each channel's videos and usually takes 10-45 minutes.
   Tell the user it is running in the background and that results are saved to a new list
   automatically (give them the list link). Don't poll in a loop: call `creator_search_status`
   with that `run_id` when the user asks how it is going. If it failed to start, report why and
   stop.
4. **Read the result.** Count the creators returned. If fewer than asked, relax one thing
   (follower range first, then engagement, then country), search once more, and label the extra
   creators "relaxed: <what changed>". Still short? Stop and say how many you have and what you
   would relax next.
5. **Shortlist.** Pick the 3 best fits for the brief and call `creator_profile` for each, with the
   same `platform` the search used. Each can take up to a minute the first time; say so. If a
   profile comes back not enriched yet, say "not enriched yet" rather than "no followers".
   Only promise one minute if you actually call it; skip this step when the user asked for a
   quick list.
6. **Save — only when asked.** If the user asks to save or keep creators, call `list_read` to see
   their lists, then `save_creators_to_list` with the creator rows, `platform` set to the platform
   the search used (always pass it; there is no default), and either `list_id` (one of their own
   lists) or `new_list_name`. One call per platform. Report how many were saved, how
   many were already on the list, any that couldn't be saved (by handle), and the link to the
   list. Only the user's own lists can take new creators; if a list is refused, offer a new one.
   Never save without being asked.
7. **Next step.** Offer what fits: save them to a list, vet one in depth, or (when
   `create_campaign_draft` is listed) put them in a campaign. "Add them to the campaign" means
   `campaign_add_creators`, through the launch-campaign workflow.

## Output layout

In ChatGPT the search results appear as a creator card automatically. After the card, write at
most 2 sentences: the count you got, anything relaxed or flagged, and the next step. Don't list the
creators again in prose.

Where no card is shown (for example in Codex), use this layout:

```
**Found 8 US vegan cooking creators on Instagram** (asked for 10; follower range widened to 5k-100k for 2 of them)

| Creator | Followers | Engagement | Country | Note |
|---|---|---|---|---|
| @daguiltyvegan · Chef Derek | 24.3k | 0.6% | not shown | bio: "plant-based chef, NYC" |
| @healthmylifestyle · Rachel | 40.0k | 2.1% | US | weekly vegan meal-prep reels · relaxed: followers |
| @plantpowerpage | 31.0k | 0.3% | not shown | fit not confirmed · low engagement |

**Shortlist:** @healthmylifestyle — weekly recipes, steady engagement; ...
This search used credits from your plan. Want me to save these to a list or add them to a campaign?
```

## Rules

- Plain language: no ids, field names, status codes or "tool" in the reply.
- Never email or message a creator yourself. Outreach is a campaign: with `create_campaign_draft` listed,
  offer to set one up (the user sends it from the launch card); otherwise it is set up in
  Cheerful at https://app.cheerful.ai.
- Credits, never dollars. Don't promote plans or purchases.
- Never show a creator's email address in the shortlist; say "has a public email" if one exists.
