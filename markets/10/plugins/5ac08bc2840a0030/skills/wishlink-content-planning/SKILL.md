---
name: wishlink-content-planning
description: Plan content for a Wishlink creator by reading their own analytics and content patterns — what to post next, how often, which products and brands to push, and why their earnings moved. Use this whenever a creator asks what to post, what to make next, what's working, how often to post, whether to post daily, which brands or products to push, what pays best, why their earnings or clicks dropped, why nobody is buying, why they've earned nothing yet, or asks for content ideas or a plan for the week or month. Use it for vague asks too ("I'm out of ideas", "help me plan", "is something broken?", "what am I doing wrong") — content planning is the most common thing creators ask for, and this skill carries both their live data and the measured evidence about what actually earns.
---

# Content planning

Plan a creator's next move by reading what they're actually doing, comparing it to what the
measurements say tends to work, and handing back two or three things worth changing.

Most content advice online is folklore. What makes this different is that the evidence behind
it compares each creator to *themselves* in a different month — so it can't be explained away
by "that creator was just bigger". Several things creators firmly believe turn out not to
hold, and saying so is often the most valuable part of the reply.

## Keep the numbers internal

The measurements are Wishlink's internal analytics. They decide what you recommend; the
creator never reads them. No platform-wide rates, no cohort sizes or medians, no tier names
or percentile positions, no coefficients or p-values, nothing about how other creators are
doing in aggregate.

Their own numbers are always fine — that's their data.

Read `references/disclosure.md` before writing; it has direct translations from finding to
phrasing. `references/benchmarks.md` holds the magnitudes and `references/evidence.md` covers
what held up and what didn't. All three are internal.

Quick test before sending: if this reply were screenshotted publicly, would it reveal how
Wishlink's creator base performs in aggregate? If yes, rewrite.

## Step 1 — Read their analytics

Use a 90-day window ending **at least two weeks back**. The trailing fortnight reads
materially low because attribution is still settling, and diagnosing it invents causes for
things that haven't finished happening.

| Tool | What you learn |
|---|---|
| `get_earnings_summary` | commission, gmv, clicks, orders, conversion rate — the shape of their funnel |
| `get_daily_metrics` | the month-to-month trajectory; where a change began |
| `get_content_ranking` (`product`) | distinct products, and which ones actually earn |
| `get_content_ranking` (`post`) | their best and worst posts, with clicks and conversion |
| `get_brand_breakdown` | brand spread, per-brand conversion and AOV |
| `get_channel_breakdown` | where the commission comes from |
| `get_active_rewards`, `get_rewards_history` | reward income, which can look like performance and isn't |
| `get_social_login_status` | whether their socials are actually connected |

Work out their tier internally from the earnings total — it changes which advice is
appropriate — but never tell them their rank or band.

## Step 2 — Read their content patterns

This is the part most planning advice skips. Their own content is the best available evidence
about their audience.

From `get_content_ranking`:

- **Spread of products.** How many distinct products across how many posts? A creator
  recycling four products across twenty-six posts has a different problem from one spreading
  sixty across forty.
- **Top vs bottom posts.** Compare their best-earning posts against their weakest on clicks
  *and* conversion. A post with clicks but no orders is a product or price problem. A post
  with neither is a reach problem. Say which one they have.
- **What their winners have in common.** Category, brand, price level, format as far as the
  names reveal it. If their top earners are consistently one kind of product and their recent
  posts have drifted elsewhere, that's the finding.
- **Concentration.** If one brand or one product carries most of their commission, they're
  exposed to it going quiet — worth naming, gently.

From `get_brand_breakdown`: which brands convert for *them*, not which are biggest. A brand
with heavy clicks and weak conversion is costing them attention.

## Step 3 — Locate them, then pick the lever

**If setup is broken** — orders arriving but no commission, invalid links, socials
disconnected — fix that and stop. No content plan survives a broken account.

**If nothing is reaching anyone** (few clicks): this is reach and distribution. Products
linked, category, language, channel.

**If clicks come but orders don't**: product, price and category. More volume won't fix it.

**If they were earning and dropped**: go to the drop section below before planning anything.

**If they're already earning steadily**: the question is which lever has room left.

## The levers, strongest first

**Distinct products linked.** This is the strongest thing in the evidence by a distance, and
it's close to proportional — meaningfully more products in a month goes with meaningfully
more commission. It replicates across two independent ways of measuring.

**Posting more is mostly how you link more products, not mainly a separate lever.** Holding
product count fixed, post count still has a real effect, just a much smaller one — roughly
an eighth the size of the products effect. When someone asks "should I post more?", the more
useful question is "how many different products are you putting in front of people?" And
returns to raw volume fall away sharply — past roughly fifty posts a month the next post adds
almost nothing, so a creator already at that volume needs a different change entirely.

**Language.** Creators shooting in their audience's own language tend to do better than the
same creator posting in English — this is one of the largest effects measured, and it's
within-creator, so it isn't just "regional creators are different people". **No tool tells
you their audience's language or location**, so you have to ask, in the reply, in plain words:
where's most of your audience, and what language do you shoot in? Never infer it from their
name, bio, or brand mix. If they're posting English to a regional audience, this is usually
the single most valuable thing you can offer — and you can't offer it until you've asked.

**Category.** Fashion and home lead; beauty and personal care sit at the bottom, which matters
because beauty is where a lot of creators start by default. Tech pulls clicks but converts
worst of anything measured — good for reach, weak for earnings. Home is strong on both.
(Instagram evidence only; it doesn't extend to YouTube or Facebook.)

**Price band.** Moving up the price distribution goes with more commission, in steps. Talk in
bands, never precise price points — the underlying measure is approximate.

**Channel.** Instagram outperforms YouTube, and YouTube outperforms Facebook, for the same
creator shifting effort between them.

**What winning posts look like.** The posts that earn most lean heavily on value and deal
framing — discounts, sale alerts, "is it worth it" quality reviews, affordability. Routine and
tutorial content underperforms commercially. This one is descriptive rather than
within-creator, so frame it as "the posts that earn most tend to look like this".

## Things creators believe that didn't hold up

Worth telling them, because each one saves money or effort:

- **Posting consistency.** Checked, and there's no sign that spacing posts evenly changes
  earnings. If someone is exhausted and asking permission to cut back, the evidence supports
  them.
- **Production quality.** Checked, and better lighting and polish do not move sales. Nobody
  needs to buy a ring light for this.
- **More brands.** Once you account for how many products they're linking, brand count isn't
  its own lever.
- **Rewards as a strategy.** Reward income is income, but chasing it doesn't predict more
  commission for the same creator.
- **Collections, and sourcing as a growth lever.** Neither survives scrutiny.
- **Better commission rates once you're bigger.** Rates don't really improve with size —
  they're set by brand and category. A creator pushing for this is spending energy on
  something that isn't there.

## If they're asking about a drop

Start from the right prior: **most drops aren't the creator's fault.** Measured behaviour
explains only a small share of the average decline, and plenty of drops happen with posts,
brands and everything else flat.

0. **State their commission trend on its own, before touching rewards or anything else.**
   Commission and reward are different things — commission is what their content earned,
   reward is incentive money on top of it. Work out whether *commission itself* rose, fell,
   or collapsed, month over month, using commission alone. Do this before step 2, and hold
   the result in mind through it — a drop diagnosis that starts by explaining the total
   without separating these two first will keep pattern-matching to whichever one moved,
   not to which one actually mattered.
1. **Check the calendar first — but only as far as it actually reaches.** Is the drop inside
   the unsettled trailing fortnight, or is a partial month being compared against a full one?
   Both look like collapses that aren't, and can explain away part of a drop. They cannot
   explain away all of it if the funnel itself has already collapsed: if clicks and orders
   are down by the same order of magnitude as commission, that is not attribution catching
   up — traffic and orders are not delayed the way commission postings can be. A calendar
   caveat softens a number; it does not license waving off a drop that the rest of the
   funnel already confirms is real.
2. **Check rewards — but check the right direction.** A reward ending can look exactly like
   a performance drop. The trap runs the other way too: if reward is now a *large share* of
   a *small* total, that is usually not "reward fell" — it's commission collapsing underneath
   a reward that barely moved, and reward's share only looks big because the total it's a
   share of is now tiny. Compare reward's rupee value across months, separately from its
   share of the total, before deciding which one is doing the explaining.
3. **Check products linked**, then posts, then brand mix, then channel mix.
4. **Say how much their behaviour actually explains, using their own commission trend from
   step 0.** If nothing changed on their side, say so plainly — that's the most common answer
   and the most useful one. If commission itself collapsed, say that plainly too, even if a
   reward payment is cushioning the total — a creator whose content stopped earning needs to
   know that, whatever the total on screen says.

Two failure modes pull opposite ways here. Don't alarm someone over ordinary variance; swings
are large and most movement isn't explained by anything measurable. But never wave off a real
collapse as "normal" either — someone who kept a quarter of last month's income has a genuine
problem regardless of what's statistically ordinary. Investigate anyway.

## If they've earned nothing yet

This is common and needs its own handling. Advice written for earning creators assumes a
working funnel they don't have.

Check setup first, then find where the funnel stops, then work the levers above — usually
products linked and language.

On expectations: be realistic without handing over platform statistics. First earnings
usually start small and build slowly, and much of what moves the numbers isn't in anyone's
control. Talk in terms of time and trajectory rather than odds. Don't imply effort reliably
converts to income — it doesn't, and that framing leaves them blaming themselves. Don't be
bleak either. Point at what's in their control and be someone they'd want to ask again.

## Questions the data can't answer

Best time of day, best day of week, ideal video length, hook duration, audio or trending-sound
strategy, how long an old post keeps earning. None of it was measured — there's no
time-of-day or post-age grain in the data at all.

Say so directly. Creators respect "we haven't measured that" more than a confident guess, and
a made-up posting time is exactly the kind of thing they'll act on.

Note the difference when you answer: production quality was *checked and found not to matter*,
while posting time was *never measured*. Those are different statements and worth keeping
distinct.

## Writing the reply

Answer the person before the question. Many of these messages come from someone anxious about
income or worn out from posting. One genuine sentence acknowledging that, before any analysis,
costs nothing and changes how the rest lands.

Then: what you see in their numbers, two or three concrete changes, and the audience-language
question if it's still open. Keep caveats to a short closing rather than front-loading them —
a reply that opens with disclaimers reads as a compliance notice, not help.

Give them something they can act on this week.

## Staying honest

- These are associations, not guarantees. "Creators who did this also saw that" is the claim.
  Fixed effects removes who-the-creator-is; it doesn't prove direction.
- Most of what moves a creator's month isn't explained by anything measured here. Don't imply
  a content plan controls their income.
- Use their tier to choose advice, never to label them.
- Compare them to their own recent months, not to a cohort.
- Never state platform-wide performance, cohort sizes, or raw statistics.
- Content findings are Instagram-only.
- Don't diagnose the trailing fortnight.
