# Geo experiment design rules

## Test types

| Type | What changes in treated geos | Measures | Cost |
|---|---|---|---|
| Go-dark | Channel switched off | Total contribution of the channel at current spend | KPI lost in treated geos while off |
| Holdback | Spend cut by a share (for example 50%) | Marginal return of the last part of spend | Smaller loss, smaller signal |
| Heavy-up | Spend increased by a share | Return of extra spend (scaling question) | Extra spend |
| Multi-cell | Several treatments against one shared control | Two or more questions in one calendar | More geos needed |

Go-dark answers "is this channel incremental at all". Heavy-up answers "should we spend more". Do not answer a scaling question with a go-dark.

## Unit and assignment

- The geo must be targetable on and off in every platform involved, and be the unit in which the KPI is recorded.
- More geos give more power and better inference. Meridian GeoX asks for at least 10 geos for a single-cell design and recommends 50 to 100 or more; GeoLift recommends 20 or more. Under 10, consider smaller units (provinces instead of regions, DMAs instead of states) or a switchback.
- Treated share: 10% to 30% of the KPI is typical for go-dark (limits the loss); heavy-up can use more.
- Assignment by stratified randomization: geos sorted by KPI volume, split into strata, one drawn from each. The script searches many such draws and keeps the one with the lowest MDE on older history, then reports the MDE on recent history it was not chosen on.
- Business constraints are allowed (a geo that must stay on, one that must be treated) and are declared before the draw.
- Very large geos (over a third of the KPI) are poor candidates for treatment and poor single controls.

## Duration

- Minimum 2 full weeks, so each weekday appears at least twice (GeoLift recommends at least 15 days with daily data). 3 to 10 weeks is typical (GeoX). Cover at least one purchase cycle.
- Add a cooldown of at least 1 week after the test for search and retargeting, and 2 to 4 weeks for video and upper funnel, then measure through the end of the cooldown.
- History before the test: at least 3 times the test length (GeoX), 4 to 5 times (GeoLift), ideally a full year when seasonality is strong.
- Use the duration curve from the design: MDE falls roughly with the square root of the length, until seasonality and drift dominate.

## Power and the MDE

- MDE is the smallest true effect (as a share of the treated geos' KPI over the window) the test detects with the stated power (80% by default) at the stated alpha (0.10 two-sided by default).
- Compare the MDE with the effect the decision needs. If the channel would only be cut at an effect below 5% and the MDE is 12%, the test cannot support the decision; change the design (more geos, longer, larger cell) or the method.
- For go-dark, compare the MDE with a plausible range of the channel's contribution. A rough prior: the share of the treated KPI the platform attributes to the channel is usually an upper bound for brand search and retargeting and can understate upper funnel.

## Execution checklist

Before launch:

- Write the test plan (template in `assets/test-plan-template.md`) and share it before launch: hypothesis, KPI and source, geos, dates, decision rule.
- Freeze other changes in the tested channel and avoid launching other tests in the same geos.
- Check the calendar: no promotions or launches that hit treated and control geos differently.

Google Ads:

- Location options: "Presence: people in or regularly in your included locations". The default "Presence or interest" serves ads to people outside the geo and contaminates controls.
- Exclude treated geos with negative location targeting in every campaign of the tested channel, including PMax, Demand Gen and video. For holdback, use separate campaigns or budgets per cell.
- Turn off search partners and the Display expansion for tested Search campaigns when they cannot be geo-controlled.
- Campaigns limited by budget: duplicate them, one copy for treated and one for control geos. Otherwise the budget saved in treated geos is spent in control geos and inflates them (GeoX calls this mandatory).
- Watch automated bidding: a go-dark cuts conversions the bidder learns from; keep targets fixed and avoid learning-period changes.
- Deactivate user-level lift studies (Conversion Lift, Brand Lift) on the campaigns under test.

Meta:

- Exclude treated regions at ad set level, including Advantage+ campaigns. Check that Advantage+ audience settings do not override location exclusions.
- If running a Meta lift study at the same time, keep the geo test on a different channel.

During the test:

- Check spend by geo every few days. Spend in go-dark geos should be near zero. Small leakage (under 5% of normal) is acceptable and is reported.
- Do not stop early because the result looks good or bad. Peeking inflates false positives.

## Several cells or several KPIs

- Each treatment cell is read against the shared control. With several cells or KPIs, the chance of one false positive grows. Name one primary KPI before launch; treat the rest as secondary, or adjust with Benjamini-Hochberg.

## Spillover

- Users who cross between treated and control geos (commuters, nearby cities) dilute the effect. Use larger, self-contained geos, or leave a buffer of neighboring geos out of the control pool (`--exclude-controls`).
- National media (TV, influencer, PR) reaches all geos and is not a problem as long as it is the same in both groups.
