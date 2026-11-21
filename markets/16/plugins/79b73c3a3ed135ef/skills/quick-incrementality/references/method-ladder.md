# Choosing a method

Incrementality asks one thing: how much of the KPI would not have happened without this spend. Every method below answers it with a different level of confidence and cost. Pick the most rigorous one the situation allows, and say which one was used.

## The ladder

| Rung | Method | Rigor | When it fits | What it cannot do |
|---|---|---|---|---|
| 1 | Platform lift study (user-level randomized holdout run by the ad platform) | Causal | The channel is on a platform that offers it, the account meets eligibility, and the KPI can be sent to the platform (pixel, CAPI, offline conversions) | Measure other platforms, compare channels on a common footing, or measure search ads that capture existing demand |
| 2 | Geo experiment (go-dark, holdback or heavy-up in randomly chosen regions) | Causal, design-based | Enough geos (10 or more, 30+ is comfortable), the KPI is available by geo and by day, the channel can be targeted by geo | Measure channels that cannot be geo-targeted, or tiny effects in tiny markets |
| 3 | Switchback (alternating on and off periods in one market) | Quasi-experimental | Only one market, effect switches off within a few days (paid search, retargeting), at least 4 blocks | Measure channels with long carryover (TV, YouTube, upper funnel) |
| 4 | Pre/post with comparators (before vs during, against last weeks, last year and a control series) | Directional | A change already happened, or the team needs a quick read with no setup | Separate the change from anything else that moved at the same time |

Rules:

- Go as high as the situation allows. Recommend the higher rung even when the user asked for a lower one, then do what they asked.
- A lower rung is never presented as causal. Label results "directional" for rungs 3 and 4, and say what would make them stronger.
- Correlation between spend and KPI over time, attribution reports, and "conversions went down when we paused" are not incrementality. Say so when they are offered as evidence.
- Several platforms at once: platform lift studies cannot be added together. A geo experiment on the business KPI is the only way to compare channels on the same footing.

## Decision questions

Ask these in order. Stop asking once the method is clear.

1. What decision will the result change? (cut a channel, scale it, set a target, settle a debate)
2. Which channel, platform and campaign types?
3. What is the KPI, and where is it recorded? (backend, CRM, shop, app analytics). Platform-attributed conversions are a last resort.
4. Can the KPI be split by geo and by day? How many geos, and at what level?
5. Can the channel be targeted by geo?
6. Spend per month on the channel, and KPI volume per day.
7. How long can the business tolerate the test, and how much KPI is it willing to risk?
8. Any fixed events in the next 8 weeks? (sales, launches, price changes, tracking changes)

## Typical mapping

| Situation | Recommended method |
|---|---|
| Meta prospecting, account eligible for Conversion Lift | Platform lift study, with conversions sent through CAPI; geo test if Meta must be compared with other channels |
| Brand search ads, one country with regions | Geo go-dark on brand campaigns, KPI = total conversions from backend (paid + organic) |
| Brand search ads, single city or tiny country | Switchback on brand campaigns, 2 weeks on and 2 weeks off, at least 4 blocks, then pre/post as a sanity check |
| YouTube or Demand Gen | Geo experiment with a cooldown of at least 2 weeks after the test, or the platform's lift study when eligible |
| PMax or Shopping in a market with many regions | Geo holdback or go-dark applied to all PMax and Shopping campaigns together, since they compete for the same queries |
| "We paused X last month and nothing happened" | Pre/post with comparators to size the noise, then propose a proper test |
| Budget scaling question ("what if we add 30%?") | Geo heavy-up, not go-dark |
| Several channels, budget allocation | Geo experiments per channel feeding a marketing mix model as calibration |
