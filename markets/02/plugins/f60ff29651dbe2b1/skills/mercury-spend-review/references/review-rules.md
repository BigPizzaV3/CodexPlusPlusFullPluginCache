# Spend review rules

## Counterparty normalization

Convert text to lower case. Trim leading and trailing space. Collapse repeated space. Remove punctuation that does not distinguish the entity. Remove a payment-processor prefix only when the prefix is documented and the remaining name is present.

Keep every original value. Do not merge legal entities only because their names are similar. Do not remove legal suffixes when this could merge two entities.

## Recurring and repeated activity

Require at least three charges from one normalized counterparty.

Classify a pattern as recurring when it has either:

- a 25-to-35-day interval and amount variation of 15% or less; or
- a 6-to-8-day interval and amount variation of 15% or less.

Use the median amount as the variation baseline. If the median is zero, do not calculate a variation rate.

Label other repeat patterns `repeated`. Do not label any pattern a subscription unless the source data states this.

## Possible duplicate group

Use the duplicate-group process in the shared data controls. Require the same normalized counterparty, amounts within 0.01 account-currency units, and a maximum three-day span for the full group.

For a group with `k` transactions, possible duplicate exposure is the sum of at most `k - 1` extra payments. Do not sum pair combinations.

## Vendor increase

Compare equal-length complete periods. Require all of these conditions:

- current-period spend is at least 500 account-currency units;
- the increase is at least 25%;
- the absolute increase is above materiality.

Label a vendor with no prior-period spend `new in period`. Do not divide by zero.

## Transaction outlier

Require at least five earlier transactions for the normalized counterparty. Compare the transaction with the historical median available before that transaction.

Flag an amount only when it is at least three times the historical median and above materiality. If the median is zero, report the pattern without a ratio.

## Materiality

Use the larger of 100 account-currency units or 0.5% of review-period external outflow. State the selected value and denominator.

## Opportunity reconciliation

Assign each monetary amount to one exposure class in this order:

1. possible duplicate exposure;
2. recurring annualized cost;
3. spend above the prior-period run rate;
4. user-supplied reduction scenario.

An item can appear under more than one review label, but its amount can enter the total opportunity range only once.
