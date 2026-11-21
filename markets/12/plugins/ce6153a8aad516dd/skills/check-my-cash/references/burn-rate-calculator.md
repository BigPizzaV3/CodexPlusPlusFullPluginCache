# Burn Rate Calculator

Answers: How fast am I burning cash, and what will I have left in 3, 6 and 12 months?
Learn more: https://omnyra.ai/wiki/business/burn-rate

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Total monthly expenses | $ a month | none, ask for it | Everything the business spends in a month. |
| Monthly revenue | $ a month | $0 | What comes in during a month. Use 0 if there is none yet. |
| Cash on hand | $ | none, ask for it | What is in the bank now. |

## Before you calculate

- Total monthly expenses must be above 0.
- Cash on hand must be above 0.

## Formula

1. Gross burn = total monthly expenses
2. Net burn = total monthly expenses - monthly revenue
3. If the net burn is 0 or less, the business is cash flow positive: it adds that amount each month and has no runway to count
4. Weekly burn = net burn / 4.33
5. Runway in months = cash on hand / net burn
6. Cash left in 3, 6 and 12 months = cash on hand - net burn x 3, x 6 and x 12. A negative figure means the cash has run out before then.
7. Month the cash runs out = today's date + runway in months x 30.44 days

## Rounding

Give dollars to the nearest whole dollar. Give months to one decimal place, years to one decimal place from 24 months up, and say "10+ years" from 120 months up. Give the month the cash runs out as a month and a year.

## Worked example

Inputs: Total monthly expenses $45,000; Monthly revenue $30,000; Cash on hand $90,000.

1. Net burn = $45,000 - $30,000 = $15,000
2. Weekly burn = $15,000 / 4.33 = $3,464
3. Runway = $90,000 / $15,000 = 6.0 months
4. Cash left in 3 months = $90,000 - $15,000 x 3 = $45,000

Result for these inputs:

- Net burn a month: $15,000
- Gross burn a month: $45,000
- Weekly burn: $3,464
- Runway: 6.0 months
- Cash left in 3 months: $45,000
- Cash left in 6 months: $0
- Cash left in 12 months: none, the cash has run out before then

Rule of thumb for this result: Warning.

## The Playbook's rule of thumb

- The net burn is 0 or less: **Cash flow positive.** Revenue covers expenses. Keep tracking it: growth, a slow season or a large purchase can turn it negative.
- The runway is under 6 months: **Critical.** Cut non-essential spending now, collect outstanding invoices faster, and consider whether more capital is needed. Each week of delay leaves fewer options.
- The runway is 6 to 12 months: **Warning.** There is room to breathe but little margin for error. A bad month, a lost client or a surprise cost could make it critical. Close the gap between revenue and expenses while the choices are still considered ones.
- The runway is over 12 months: **Healthy runway.** There is time to make considered decisions. A comfortable runway is not the same as being profitable: the business is still spending more than it earns.

## Notes

- This calculation calls a runway under 6 months critical. The cash runway calculation uses 3 and 6 months. Use the bands of the calculation the owner asked for, and say which one it is.
- The answer assumes revenue and expenses stay as they are.
