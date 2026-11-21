# Bidding and budgets

## Find the real target first

- Check whether the campaign uses a portfolio bid strategy. If it does, the campaign's own target fields show 0 or blank, and the target lives in the portfolio. A change to the portfolio moves every campaign in it.
- A portfolio can be owned by the manager account (MCC), not the client account. It is then visible under the manager's shared library, and changes must be made there.
- Read the target against the portfolio's whole set of campaigns: a new ad group competes inside the portfolio, not only inside its campaign.

## The levers under Smart Bidding

- The levers are the target (tCPA, tROAS), the budget, the conversion goal and the data fed to the bidder (conversion values, offline conversions, enhanced conversions).
- Manual bid adjustments for location, schedule, audience and demographics are not used by Smart Bidding. Device at -100% still excludes the device. Under Target CPA, a device adjustment changes the CPA target for that device. Advice like "raise bids 20% in Madrid at night" does not apply to Smart Bidding campaigns.
- Changing the target moves volume and cost together. Lower tCPA or higher tROAS: fewer conversions, lower CPA. The reverse buys volume at a higher marginal CPA.
- Change targets in steps of 10% to 20%, then wait. Large jumps reset learning and make the effect unreadable.

## Choosing a strategy

The ladder, each step needing better data than the last:

1. Maximize conversions, to gather conversion data.
2. Target CPA, once conversions are steady (tens per month per campaign or portfolio).
3. Maximize conversion value, once conversion values are real and vary between conversions.
4. Target ROAS.
5. Profit or lifetime-value bidding: values reflect margin or LTV, imported from the backend.

Before moving to value-based bidding, check:

- Values are set and not a constant (1.0 everywhere is not a value).
- Values vary in a way that matters (order size, plan, lead quality).
- Values are attributed to the click correctly, including late updates.

Set tROAS from unit economics (margin, LTV, payback), not by copying last quarter's realized ROAS. A target copied from a good period chokes volume.

## Budgets

- Budget matters when the campaign loses impression share to budget. If lost IS (budget) is near zero, more budget changes nothing.
- Budget changes above roughly 20% at once disturb pacing; move in smaller steps when the campaign is learning.
- Read pacing over 7 days at least, 14 for search, 28 for PMax and Demand Gen. Do not react to one day.
- Shared budgets hide which campaign takes the money. Use them only for campaigns of equal priority.
- Some countries add a regulatory surcharge on top of media spend. Check the current rate for the countries served when setting daily budgets (see `platform-facts.md`).

## Seasonality adjustments

Use them only for short, sharp conversion-rate changes the bidder cannot anticipate: a sale or launch of a few days. Not for gradual seasonality, which Smart Bidding already learns. Remove them when the event ends.

## Learning periods

After a change of bid strategy, target or conversion goal, calibration typically takes 1 to 2 conversion cycles (Google). Judge the result over a month or at least 50 conversions. Batch other edits (ads, keywords, negatives) instead of spreading them over that period.

## Brand campaigns

- Brand captures existing demand. Its CPA is not comparable to non-brand.
- More brand budget does not create demand. The question for brand is defensive: how much traffic competitors take when you are absent. That needs a test, not a rule.

## Conversion goals

- Accounts with many conversion actions must set conversion goals per campaign. Account-default goals feed every action to the bidder, including micro-conversions, and distort bidding.
- New campaigns copy the goals of the reference campaign explicitly; do not let defaults assign them.
