# Evaluation rubric

Use this rubric to keep NBA deal recommendations consistent.

## 1. Comp match confidence

- **Exact / 0.90-1.00:** Same year, product, card number, parallel, serial tier, auto or memorabilia configuration, grader, and grade.
- **Strong / 0.75-0.89:** Exact card with a small non-price-defining difference, or multiple highly comparable copies with a defensible adjustment.
- **Near / 0.50-0.74:** Adjacent serial tier, different grade, or related parallel. Separate these from exact sales.
- **Uncertain / below 0.50:** Variant or condition cannot be resolved, or evidence is mostly active listings and estimates.

Do not issue Buy below 0.75 confidence.

## 2. Liquidity

- **High:** At least five useful sales in the last 90 days and the latest within 30 days.
- **Medium:** At least three useful sales in the last 180 days and the latest within 60 days.
- **Low:** Fewer than three useful sales in 180 days, or the latest reliable sale is older than 90 days.
- **Unknown:** No reliable completed-sale evidence.

Use exact sales for the primary count. Near comps can support judgment but must not inflate the exact-sale count.

For fast resale, prefer High. Accept Medium only when the pricing edge and player demand are strong. Do not issue Buy for Unknown liquidity.

## 3. Price estimate

1. Normalize currencies to EUR using a stated rate and date.
2. Start with the median of up to five most recent reliable exact sales.
3. Keep accepted best-offer sales only when the actual accepted price is known.
4. Exclude a sale as an outlier only with a concrete reason such as a mislabeled card, obvious lot, damaged copy, shill concern, or materially different attributes.
5. If exact sales are sparse, provide a range and lower confidence.
6. Do not treat an algorithmic value estimate as a completed sale.

## 4. All-in cost

Include when applicable:

- Listing or winning price.
- Buyer premium or marketplace fee.
- Seller-to-warehouse or domestic shipping.
- Allocated international or combined shipping.
- Import tax, customs, and carrier handling.
- Payment and currency-conversion charges.

If combined shipping is unknown, show both a card-only result and a conservative allocated-shipping result.

## 5. Resale economics

Use the user's actual resale channel. Include:

- Expected sale price, not the highest possible asking price.
- Selling fee percentage and fixed fee.
- Promoted-listing cost when normally used.
- Outbound postage, packaging, insurance, and other predictable costs.
- Taxes only when the user supplies the relevant business treatment.

Default thresholds for this skill:

- All-in cost between EUR 10 and EUR 250.
- Expected ROI at least 20% on all-in acquisition cost.
- No separate minimum euro-profit gate unless the user supplies one.

Classify financially acceptable but less liquid opportunities as Watch rather than Buy.

## 6. Candidate quality

Use a 100-point explanation aid, not a claim of mathematical certainty:

- Valuation edge: 35 points.
- Liquidity: 25 points.
- Comp match confidence: 20 points.
- Player and card demand: 10 points.
- Listing and condition risk: 10 points.

Suggested interpretation:

- **80-100:** Strong candidate if hard financial gates also pass.
- **65-79:** Watch or secondary candidate.
- **Below 65:** Pass unless missing information could materially change the result.

The hard financial, liquidity, and confidence gates override the score.

## 7. Risk flags

Flag explicitly:

- Unclear parallel, serial number, grade, or autograph authentication.
- Patch premium based only on visual appeal without comparable sales.
- Population scarcity mistaken for demand.
- One anomalous high sale driving the estimate.
- Player news, injury, trade, or short-lived hype affecting recent sales.
- Seller restrictions, poor condition, returns risk, or unclear shipping.
- Currency, customs, or combined-shipping uncertainty large enough to erase the margin.

Never describe a card as guaranteed profit or an investment certainty.
