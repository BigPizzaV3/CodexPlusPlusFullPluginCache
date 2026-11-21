---
name: adspirer-performance-review
description: Review Meta and TikTok ad performance with Adspirer — how are my ads doing, weekly or monthly reports, a cross-channel scorecard, CPA, ROAS, CTR, spend trends, and auditing whether conversion tracking is set up correctly. Read-only; changes nothing.
---

# Performance review

Follow `adspirer-mcp` before any tool call. This skill only reads — it never changes a campaign.

## Where the numbers come from

Each platform has its own performance tool, called directly by name:

| Platform | Tool |
|---|---|
| Meta Ads | `get_meta_campaign_performance` (renders a card) |
| TikTok | `get_tiktok_campaign_performance` |

Meta renders an interactive dashboard; TikTok returns the numbers. Pass `raw_data: true` where the
tool's schema offers it, when the user wants the numbers rather than the rendered summary. For
ad-set / ad-group and creative-level detail, call `get_meta_adset_performance` or
`analyze_meta_ad_performance` (Meta) and `get_tiktok_ad_performance` (TikTok) —
`get_tool_schema` them when the user wants to go a level down.

Only pull the platforms the user has actually connected. Check `get_connections_status` first
instead of firing calls and reporting failures.

## Before you trust a single number

**Verify conversion tracking.** On Meta, call `list_meta_pixels` and `get_meta_pixel_stats`; on
TikTok, `list_tiktok_pixels`. A pixel that has stopped
firing, or never fires the event the campaign optimizes for, is the plumbing every conversion
number depends on.

If tracking is broken, every conversion metric below is fiction, and the honest answer to "how are
my ads doing" is "I can't tell you yet, and here's why." Say that before presenting a CPA. This is
the single most valuable thing this skill does.

Also check the window. Today is always partial, and the most recent day or two can still be settling
on both platforms. A "drop" that is really an unfinished day is the most common false alarm in this job.

## The scorecard

Report per platform, then in total:

- **Spend** — and pace against the monthly budget
- **Conversions** and **cost per conversion**
- **ROAS**, where revenue is tracked
- **CTR** and **CPC** — diagnostic, not goals
- **Change vs the previous equivalent period**

Compare like with like: last 7 days against the 7 before, not against a partial week.

## Say what it means

A table is not a review. Lead with the answer:

> Meta is doing the work — 34 purchases at $41, under your $50 target. TikTok spent $890 for 3.
> The Meta ad set has a frequency of 4.2 and its CTR halved over two weeks; that's creative fatigue,
> not targeting.

Name the biggest problem and the biggest opportunity. Give one recommendation, with the number
attached. Offer to act — don't act. Changes belong to `adspirer-optimize`.

## When something moved sharply

Use the anomaly tools rather than speculating: `explain_meta_anomaly` and `explain_tiktok_anomaly`.
They compare windows and attribute the delta to a cause.

Before blaming the algorithm, check the boring explanations: a campaign paused, a budget changed, a
disapproved ad, a landing page that started 404ing, a conversion tag someone removed on deploy.

## Make it easier to look at

A scorecard across six platforms is a table the user will squint at, and a trend is a shape, not a
column of numbers.


Offer a **Site** when the user will revisit it or send it to a client — a hosted dashboard rather
than a message. Ask first, and default to invitation-only: this page carries their spend and
conversion data. For a one-off look, a chart in the conversation is enough.

## Make it recurring

A review is worth more every week than once. When the user likes what they just read, offer to
schedule it — this host can, and they can create it just by asking.

A recurring task re-runs this review and notifies them by push and email. A **monitoring task** is
better when they'd rather hear only about changes: it re-checks and stays quiet until something
moves.



Each run costs tool calls against their monthly quota, the same as a live conversation. Weekly is the
right default; daily only for accounts spending enough to justify it. Say so before setting it up.

## Don't

- Don't average CPA across platforms with wildly different volumes and call it "blended performance"
  without saying so.
- Don't present a 3-day window as a trend.
- Don't fabricate a number when a tool fails. Say the call failed and which one.
- Don't schedule a daily review for an account that spends $20 a day. The runs cost more attention,
  and more quota, than the findings are worth.
