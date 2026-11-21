---
name: adspirer-optimize
description: Find and fix wasted Meta and TikTok ad spend with Adspirer — cut spend that isn't converting, exclude audiences and placements, fix creative fatigue, reallocate budget to what works, and check whether campaigns are pacing over or under budget. Proposes changes and asks before spending or moving money.
---

# Cutting waste and pacing budget

Follow `adspirer-mcp` before any tool call. Load the platform skill for field rules. This skill
proposes changes and applies them **only after the user agrees to that specific change**.

## Find the waste

| Platform | Tool (call directly by name) |
|---|---|
| Meta | `analyze_meta_wasted_spend`, and `detect_meta_creative_fatigue` for sliding CTR |
| TikTok | `analyze_tiktok_wasted_spend` |

Waste on social has a few shapes and they need different fixes:

- **Spend with zero conversions.** The obvious one. But check the volume first — an ad set with
  $40 spend and no conversions may simply not have had a chance yet at a $60 CPA.
- **Spend converting far above target.** Worse than zero, because it looks like it's working.
- **Creative fatigue.** The social-specific leak: an ad set whose frequency climbs while CTR slides
  is burning budget showing tired creative to the same people. `detect_meta_creative_fatigue` names it.
- **Placements and audiences that never convert.** Narrow or exclude the placements and audience
  segments that spend without returning.

## Before you cut anything

**Check the tracking first.** Run `list_meta_pixels` and `get_meta_pixel_stats` (Meta) or
`list_tiktok_pixels` (TikTok). A campaign that looks like it
converts nothing very often converts fine and reports nothing. Pausing it would destroy a working
campaign — this mistake is common and expensive.

**Check the volume.** Ten clicks and no conversions is not evidence. Roughly, you want at least
3× the target CPA in spend, or ~100 clicks, before you call something a loser.

**Check the assist.** The campaign with no last-click conversions may be the one introducing people
to the brand. Look at view-through and assisted conversions before killing an upper-funnel campaign.

## Fix it, in this order

1. **Refresh creative before pausing** when the problem is fatigue — new creative on a proven ad set
   keeps the audience and the learning. Pausing a whole ad set to fix one tired ad is a blunt instrument.
2. **Exclude placements and audiences** that spend without converting (precise and reversible).
3. **Pause** the ad, ad set, or campaign — the narrowest thing that solves the problem.
4. **Reallocate** what you freed up.

**Never delete when pausing will do.** Removing keywords, deleting creatives, archiving campaigns —
these lose history and some cannot be undone. Say what will be lost and get an explicit yes.

## Reallocating budget

`optimize_meta_budget` and `optimize_tiktok_budget` recommend a split across campaigns/ad sets. They
recommend; they don't apply. Apply a move with `update_meta_campaign` / `update_meta_ad_set` (Meta)
or `update_tiktok_campaign` / `update_tiktok_ad_group` (TikTok) — `get_tool_schema` them first for
the exact fields, and expect a preview that needs `confirm: true`.

Move money toward proven CPA, not toward the highest volume. Move in steps — a campaign whose budget
doubles overnight re-enters the learning phase and gets worse before it gets better. 20–30% at a
time, then wait a week.

Show the arithmetic: *"Move $30/day from Campaign A ($140 CPA, target $50) to Campaign B ($38 CPA).
Same total spend. If B holds, that's roughly 12 more leads a month."*

## Pacing

Compare spend so far against elapsed days in the period.

- **Underpacing** usually means the budget is capped, bids are too low for the auction, the target
  CPA is set below what the account can achieve, or the audience is too narrow. Check impression
  share before raising the budget — if the campaign isn't budget-limited, more budget changes
  nothing.
- **Overpacing** means the month runs out early. Cut the daily budget or fix what's expensive; don't
  just let it stop mid-month.

Meta and TikTok can overspend the daily budget on any given day and settle over a longer window.
A single-day overspend is not a bug — say so before someone panics.

## Then verify

After every change, read the object back and confirm it took. Report what actually happened, not
what you asked for. Tell the user what to expect: a learning period, a dip, a delay before the data
means anything.

## Don't promise to keep watching — schedule it

Pacing drifts, CPAs creep, and a campaign that was fine on Monday is over budget by Friday. Saying
"I'll keep an eye on it" is a promise you cannot keep; the conversation ends when the user closes it.

Offer to schedule the check on this host. They can create one just by asking, and it lands with a
notification wherever they already are.

Use a **monitoring task** rather than a plain recurring one: it re-checks pacing and CPA and stays
quiet unless something crosses the line, so the user isn't trained to ignore it.



Each run costs tool calls against their quota. Mid-month and month-end beats daily for pacing; daily
is for accounts where a day of overspend is real money.



If the user reviews budget with someone else, offer a **Site** for the proposed split — invitation-only,
since it exposes spend. Otherwise a table in the conversation is enough.
