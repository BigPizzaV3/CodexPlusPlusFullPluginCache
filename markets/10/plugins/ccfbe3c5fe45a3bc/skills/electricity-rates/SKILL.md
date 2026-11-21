---
name: electricity-rates
description: Look up current home electricity plans, the utility for a ZIP code, and the price to compare in deregulated US states using the FindEnergyRates tools. Use when someone asks about electricity rates, plans, suppliers, or switching providers.
---

# Electricity rates with FindEnergyRates

Three read-only tools, no sign-in:

1. `electricity_find_utility_by_zip` — ZIP code → the utility (or utilities) serving it and the state.
2. `electricity_search_plans` — plans for that utility, ranked by price. Filters: contract term, rate type, renewable share.
3. `electricity_get_price_to_compare` — the utility's default-service rate, in states that publish one, so an offer can be judged against it.

## Typical flow

ZIP → utility → plans → (where available) price to compare. Ask for the ZIP code if it was not given; a city name is not enough because one city can have several utilities.

## Read `status` before answering

- `ok` — use the data.
- `no_matches` — plans exist for the market but the filters removed them all; suggest relaxing one.
- `no_data_for_scope` — FindEnergyRates does not cover that market right now. Never say the market has no plans or is not deregulated.

## Presenting results

- Rates are cents per kWh. Say so, and show the contract term and any monthly fee next to the rate.
- Plans are ranked by price only. Plans with `referral: true` pay FindEnergyRates on enrollment; tell the user this when you show one. It never affects ranking.
- Link to the plan page (`plan_url`), not to a checkout. Do not enroll, submit forms, or quote a bill.
- If the response carries a dated caveat (for example, a Texas plan whose Electricity Facts Label date is older than the listing), pass it along.
- Outside Texas, FindEnergyRates lists published offers; it is a licensed broker only in Texas (PUCT BR250242).
- Mention the result's last-updated time when the user is deciding whether to switch.
