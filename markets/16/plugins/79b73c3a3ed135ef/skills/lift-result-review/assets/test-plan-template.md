# [Company] - incrementality test plan, [channel], [start month year]

Status: draft | approved | running | read
Owner: [name] | Approver: [name] | Plan date: [date]

## Question and decision

- Question: [Does X drive incremental Y at current spend?]
- Decision this test informs: [cut / keep / scale / set target]
- Decision rule, set before launch: [If iCPA < N, keep; if the interval includes 0 and the MDE is below M%, reduce spend by P%]

## Design

- Method: [geo go-dark | geo holdback P% | geo heavy-up P% | switchback | platform lift study]
- Channel and campaigns in scope: [list]
- KPI and source: [orders from Shopify, by region, daily]
- Geo unit: [province]
- Treated geos: [list] ([share]% of KPI)
- Control geos: all others except [buffer geos, if any]
- Assignment: stratified random search, seed [seed], [N] candidates evaluated
- Pre-period used for design: [start] to [end]

## Calendar

- Test: [start] to [end] ([N] days)
- Cooldown: [end+1] to [end+N]
- Readout date: [date]
- Known events in window: [none / list]

## Power and cost

- MDE at 80% power, alpha 0.10: [X]% of treated KPI over the window (validation windows)
- Expected treated KPI in window: [N]
- Spend withheld (go-dark/holdback) or added (heavy-up): [amount]
- KPI at risk if the true effect is [Y]%: [N]

## Execution checklist

- [ ] Location targeting set to Presence in all tested campaigns
- [ ] Treated geos excluded in all tested campaigns, including automated campaign types
- [ ] No other changes planned in tested campaigns during the window
- [ ] Spend by geo monitored on [days]
- [ ] Plan shared with [people] before launch

## Analysis plan

- Primary estimator: TBR, interval from in-time placebos, 90%
- Secondary: synthetic control; in-space placebo p-value
- Reported: effect, lift and interval; iCPA or iROAS against platform-reported CPA or ROAS
- No early stopping
