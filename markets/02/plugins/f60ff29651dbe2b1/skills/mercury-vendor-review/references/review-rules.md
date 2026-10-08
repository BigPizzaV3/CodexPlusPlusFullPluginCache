# Vendor review rules

## Counterparty normalization

Convert text to lower case. Trim leading and trailing space. Collapse repeated space. Remove punctuation that does not distinguish the entity. Remove a payment-processor prefix only when it is documented and the remaining name is present.

Keep every original value. Do not merge legal entities only because their names are similar.

## Possible duplicate group

Use the duplicate-group process in the shared data controls. Require distinct IDs, the same normalized counterparty, amounts within 0.01 account-currency units, and a maximum three-day span for the full group.

For a group with `k` transactions, possible duplicate exposure is at most `k - 1` extra payments. Do not sum pair combinations.

## Payment outlier

Require at least five earlier payments to the normalized counterparty. Compare the payment with the historical median available before that payment.

Flag a payment only when it is at least three times the historical median and above materiality. If the median is zero, report the pattern without a ratio.

## Vendor increase

Compare equal-length complete periods. Require current-period spend of at least 500 account-currency units, growth of at least 25%, and an absolute increase above materiality.

Label a counterparty absent from the comparison period `new in period`. Do not divide by zero.

## Recipient identity

Use these confidence levels:

- High: an explicit recipient ID or linked identifier matches.
- Medium: the exact normalized name matches and transaction metadata provides independent support.
- Low: only name similarity supports the match.

Do not merge low-confidence records. Put them in the review queue. Do not use bank account or routing numbers as displayed evidence.

## Concentration

Always state the denominator. Use a user-defined policy threshold when supplied. Otherwise, show top 5 and top 10 shares without declaring a breach.

## Materiality

Use the larger of 250 account-currency units or 0.5% of review-period external outflow. State the selected value and denominator.
