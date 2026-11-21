# Pricing Adequacy Calculator

Answers: Do my prices cover the whole business, including my own pay?
Learn more: https://omnyra.ai/wiki/business/pricing-adequacy

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Annual revenue | $ a year | none, ask for it | Total sales for the year. |
| Direct costs | $ a year | none, ask for it | Materials, direct labor and subcontractors for the year. |
| Annual overhead | $ a year | $0 | Rent, office staff, insurance, vehicles, software and the like, not counting the owner's pay. Use 0 if there is none. |
| Owner's salary | $ a year | $0 | What the owner needs to be paid for the year. Use 0 only if the owner truly takes nothing. |
| Target net margin | choose one | 15% - Healthy | The share of revenue the owner wants left as profit after every cost and their own pay. One of: 5% - Survival; 10% - Stable; 15% - Healthy; 20% - Strong; 25% - Excellent. |

## Before you calculate

- Annual revenue must be above 0.
- Direct costs must be above 0.

## Formula

1. Gross profit = annual revenue - direct costs, and gross margin = gross profit / annual revenue x 100
2. Operating profit = gross profit - annual overhead, and operating margin = operating profit / annual revenue x 100
3. Net profit = operating profit - owner's salary, and net margin = net profit / annual revenue x 100
4. Total costs = direct costs + annual overhead + owner's salary
5. If the net margin is at or above the target: margin above the target = net margin - target net margin. Stop there; no increase is needed.
6. If the net margin is below the target: revenue needed for the target = total costs / (1 - target net margin / 100)
7. If the net margin is below the target: price increase needed = (revenue needed - annual revenue) / annual revenue x 100
8. Adequacy score = net margin / target net margin x 100, never below 0 or above 100

## Rounding

Give dollars to the nearest whole dollar, percentages to one decimal place, and the adequacy score to the nearest whole number.

## Worked example

Inputs: Annual revenue $500,000; Direct costs $300,000; Annual overhead $100,000; Owner's salary $80,000; Target net margin 15% - Healthy.

1. Gross profit = $500,000 - $300,000 = $200,000, a gross margin of 40.0%
2. Operating profit = $200,000 - $100,000 = $100,000, an operating margin of 20.0%
3. Net profit = $100,000 - $80,000 = $20,000, a net margin of 4.0%
4. Revenue needed = ($300,000 + $100,000 + $80,000) / (1 - 15 / 100) = $564,706
5. Price increase needed = ($564,706 - $500,000) / $500,000 x 100 = 12.9%
6. Adequacy score = 4.0% / 15% x 100 = 27

Result for these inputs:

- Adequacy score: 27 out of 100
- Net margin: 4.0%
- Gross margin: 40.0%
- Operating margin: 20.0%
- Revenue needed for the target: $564,706
- Price increase needed: 12.9%

Rule of thumb for this result: Pricing is inadequate.

## The Playbook's rule of thumb

- The net margin is at or above the target: **Pricing is adequate.** Current prices meet the target. There is room to absorb cost increases or to invest in growth.
- The net margin is at least 70% of the target but below it: **Pricing is tight.** Close to the target. The price increase worked out above would close the gap, by raising rates on new work or by lowering costs.
- The net margin is below 70% of the target: **Pricing is inadequate.** Prices do not cover the business at the target margin. The owner needs to raise prices by the increase worked out above, cut costs, or accept a lower margin. Carrying on at current rates wears down the business's finances.

## Notes

- The owner's salary is a cost here, not part of the profit. A business that only looks profitable because the owner is unpaid has prices that are too low.
- The Playbook's own calculator offers these five targets. The formula works for any target under 100.
