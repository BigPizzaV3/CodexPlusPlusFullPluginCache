# Churn Rate Calculator

Answers: How fast am I losing customers?
Learn more: https://omnyra.ai/wiki/business/active-customers

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Customers at the start | customers | none, ask for it | Customers the business had at the start of the period. |
| Customers lost | customers | none, ask for it | Customers who left during the period. New customers do not count here. |
| Period | choose one | Monthly | How long the period was. One of: Monthly; Quarterly; Annually. |

## Before you calculate

- Customers at the start must be above 0.
- Customers lost must be 0 or more, and no more than the customers at the start.

## Formula

1. Churn for the period = customers lost / customers at the start x 100
2. Monthly churn: for a monthly period, the same. For a quarter, 1 - (1 - quarterly churn / 100)^(1/3), x 100. For a year, 1 - (1 - yearly churn / 100)^(1/12), x 100.
3. Yearly churn = 1 - (1 - monthly churn / 100)^12, x 100
4. Months until half the customers are gone = ln(0.5) / ln(1 - monthly churn / 100)
5. Average customer lifespan in months = 1 / (monthly churn / 100)
6. Retention = 100 - churn

## Rounding

Give percentages to one decimal place. Give months to one decimal place, years to one decimal place from 24 months up, and "10+ years" from 1,200 months up.

## Worked example

Inputs: Customers at the start 500; Customers lost 25; Period Monthly.

1. Churn for the period = 25 / 500 x 100 = 5.0%
2. Yearly churn = 1 - (1 - 0.0500)^12 = 46.0%
3. Average lifespan = 1 / 0.0500 = 20.0 months

Result for these inputs:

- Monthly churn: 5.0%
- Yearly churn: 46.0%
- Monthly retention: 95.0%
- Half the customers gone in: 13.5 months
- Average customer lifespan: 20.0 months

Rule of thumb for this result: Manageable, worth improving.

## The Playbook's rule of thumb

- Monthly churn is under 2%: **Strong retention.** Customers stay a long time, which gives room to build the relationship and grow what each one spends.
- Monthly churn is 2% to 5%: **Manageable, worth improving.** A common range for small businesses, but it compounds over a year. Finding out why customers leave pays off.
- Monthly churn is over 5%: **The customer base is eroding fast.** New customers are needed just to stand still. Finding and fixing why customers leave comes before spending more on winning new ones.

## Notes

- Count only customers who stopped buying. A business that also wins new customers in the period should not net them off here.
