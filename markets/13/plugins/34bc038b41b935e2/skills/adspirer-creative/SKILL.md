---
name: adspirer-creative
description: Write and refresh ad creative with Adspirer — headlines, primary text, and ad copy for Meta (Facebook/Instagram) and TikTok, plus diagnosing and fixing creative fatigue when CTR falls and frequency rises. Respects each platform's character limits.
---

# Ad creative

Follow `adspirer-mcp` before any tool call. Load the platform skill for its exact limits.

## Write from evidence, not imagination

Before writing a single headline, look at what already works:

- `analyze_meta_ad_performance` (Meta) and `get_tiktok_ad_performance` (TikTok) — which
  existing ad and hook has the best CTR and conversion rate, and why. Build on what's already landing.
- `competitor_ads_research` — the live angles a competitor is running, so you differentiate instead
  of echoing.
- The landing page. Copy that promises something the page doesn't deliver converts once and never
  again.

Ask what makes this business different if it isn't obvious. Generic ad copy is a choice, not a fate.

## Character limits

| Platform | Field | Limit |
|---|---|---|
| Meta | Headline | 255 (~40 visible) |
| | Primary text | 2200 (~125 visible) |
| | Description | 255 (~30 visible) |
| Meta carousel | Card headline | ~40 |
| TikTok | Ad text | 100 |

Where the hard limit and the visible limit differ, **write to the visible one.** Meta's 2200-character
primary text truncates at about 125; anything after that is read by nobody.

## What good looks like

- **Hook in the first second.** Social is a scroll — the opening frame and the first line of primary
  text decide whether anyone reads the rest. Lead with the offer or the outcome, not the brand name.
- **Write for sound-off and sound-on.** Most feed video is watched muted first; the on-screen text
  has to carry the hook on its own.
- **Specifics beat adjectives.** "Same-day delivery, no fee" beats "Fast, reliable service."
- **Match the audience, not a search query.** Social is interruption, not intent — give the scroller
  a reason to stop that fits who they are, not what they typed.
- **Give the system variety to test.** Several distinct angles (price, speed, proof, risk reversal,
  outcome) beat one idea reworded — that's what lets Meta/TikTok find the winner.

Write more than you need and cut. Then check every claim is one the business can actually make —
"#1 in the UK" is a legal problem, not a headline.

## Refreshing fatigued creative

Rising frequency plus falling CTR is fatigue. The same people keep seeing the same ad. **No bid or
budget change fixes it** — a fatigued ad set with more budget just annoys the same people faster.

Diagnose: `detect_meta_creative_fatigue` and `detect_tiktok_creative_fatigue`. On Meta, a 7-day
frequency above ~3 with declining CTR is the signal.

Fix, in order of leverage:

1. **New creative concept** — a different hook, not the same image recoloured.
2. **New format** — video where there was static, carousel where there was a single image.
3. **Broaden or rotate the audience** — fatigue is partly an audience-size problem.
4. Only then touch budgets.

Change one variable at a time. Swapping the image *and* the copy *and* the audience teaches you
nothing about which one mattered.

## Show the variants together

Copy is judged by comparison. Fifteen headlines in a bulleted list all read the same; the same
fifteen laid out as cards, grouped by angle, with character counts and the truncation point marked,
are a decision the user can actually make.


For a set the user will circulate for approval, offer a **Site** — invitation-only, since it carries
their unreleased campaign copy. For a quick pick, a table in the conversation is faster than a
deployment.

Either way, render each variant against its platform's **visible** limit, not the hard one. A Meta
primary text that looks fine at 2,200 characters is worthless if the offer sits past 125.

## Applying it

Swap creative with `update_meta_ad` or add a new variation with `add_meta_ad` (Meta), or
`add_tiktok_ad` (TikTok). Keep the winning ad running while the new one
gathers data — pausing the control before the challenger has proven itself is how accounts go
backwards.

Ads may need review before serving. Say so, rather than letting the user think it's live.

Creative fatigue is a recurring problem, not a one-time fix. Rather than promising to check back,
offer to schedule a fatigue check on this host — frequency and CTR, every couple of weeks — so the
next refresh is prompted by the data instead of by someone remembering.
