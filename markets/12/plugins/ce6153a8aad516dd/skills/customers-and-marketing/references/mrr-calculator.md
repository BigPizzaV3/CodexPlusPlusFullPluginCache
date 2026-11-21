# MRR Calculator

Answers: Is my recurring revenue growing, and how fast?
Learn more: https://omnyra.ai/wiki/business/building-recurring-revenue

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Recurring revenue at the start of the month | $ a month | none, ask for it | Monthly recurring revenue from memberships, subscriptions or service plans at the start of the month. |
| New recurring revenue | $ a month | $0 | Monthly revenue added by new customers this month. Use 0 if none. |
| Expansion | $ a month | $0 | Monthly revenue added by existing customers upgrading or buying more. Use 0 if none. |
| Churned | $ a month | $0 | Monthly revenue lost from customers who left. Use 0 if none. |
| Contraction | $ a month | $0 | Monthly revenue lost from customers who downgraded. Use 0 if none. |

## Before you calculate

- Recurring revenue at the start of the month must be above 0.

## Formula

1. Net new recurring revenue = new + expansion - churned - contraction
2. Recurring revenue at the end of the month = start + net new
3. Growth for the month = net new / start x 100
4. Annual run rate = end of month x 12
5. Months to double, if growing = 72 / monthly growth. This is the rule of 72, an approximation.
6. Quick ratio = (new + expansion) / (churned + contraction). Revenue gained for each dollar lost.

## Rounding

Give dollars to the nearest whole dollar, growth to one decimal place, the quick ratio to one decimal place and months to double to the nearest whole month.

## Worked example

Inputs: Recurring revenue at the start of the month $50,000; New recurring revenue $5,000; Expansion $2,000; Churned $3,000; Contraction $1,000.

1. Net new = $5,000 + $2,000 - $3,000 - $1,000 = $3,000
2. End of month = $50,000 + $3,000 = $53,000
3. Growth = $3,000 / $50,000 x 100 = 6.0%
4. Quick ratio = ($5,000 + $2,000) / ($3,000 + $1,000) = 1.8

Result for these inputs:

- Recurring revenue at the end of the month: $53,000
- Net new recurring revenue: $3,000
- Growth for the month: 6.0%
- Annual run rate: $636,000
- Months to double: about 12 months
- Quick ratio: 1.8 to 1

Rule of thumb for this result: Strong growth.

## The Playbook's rule of thumb

- Growth is over 5% a month: **Strong growth.** A strong trajectory. Keep an eye on the quick ratio to make sure growth is not hiding customers leaving.
- Growth is 0% to 5% a month: **Slow growth.** Growing, slowly. Look at both sides: more new and expansion revenue, and less churn and contraction.
- Growth is below 0%: **Recurring revenue is shrinking.** More is being lost than added. Reducing churn and contraction comes first.

## Notes

- Recurring revenue means revenue that repeats each month without a new sale: memberships, subscriptions, maintenance plans. One-off jobs do not belong here.
