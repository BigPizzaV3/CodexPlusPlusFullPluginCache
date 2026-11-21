# Customer Lifetime Value Calculator

Answers: What is a customer worth to me over the whole time they stay?
Learn more: https://omnyra.ai/wiki/business/customer-lifetime-value

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Average purchase | $ | none, ask for it | What a customer spends on a typical purchase or job. |
| Purchases a year | purchases | none, ask for it | How many times a typical customer buys in a year. |
| Years a customer stays | years | none, ask for it | How long a typical customer keeps buying. |
| Gross margin | % | none, ask for it | The share of each sale left after direct costs. |

## Before you calculate

- Average purchase must be above 0.
- Purchases a year must be above 0.
- Years a customer stays must be above 0.
- Gross margin must be above 0.

## Formula

1. Revenue a year from a customer = average purchase x purchases a year
2. Lifetime revenue = revenue a year x years a customer stays
3. Lifetime profit (the lifetime value) = lifetime revenue x gross margin / 100
4. Revenue a month = lifetime revenue / (years x 12)
5. Profit from each purchase = average purchase x gross margin / 100
6. The most to spend winning a customer = lifetime profit / 3, the Playbook's 3 to 1 rule of thumb

## Rounding

Give dollars to the nearest whole dollar, except profit from each purchase, which is to the cent.

## Worked example

Inputs: Average purchase $150; Purchases a year 4; Years a customer stays 3; Gross margin 40%.

1. Revenue a year = $150 x 4 = $600
2. Lifetime revenue = $600 x 3 = $1,800
3. Lifetime profit = $1,800 x 40 / 100 = $720
4. The most to spend winning a customer = $720 / 3 = $240

Result for these inputs:

- Lifetime profit (lifetime value): $720
- Lifetime revenue: $1,800
- Revenue a year from a customer: $600
- Revenue a month from a customer: $50
- Profit from each purchase: $60.00
- The most to spend winning a customer: $240

Rule of thumb for this result: Moderate lifetime value.

## The Playbook's rule of thumb

- Lifetime profit is over $2,000: **Strong lifetime value.** Customers are worth a lot over their lifetime, which leaves real room to spend on winning them.
- Lifetime profit is $500 to $2,000: **Moderate lifetime value.** There is some room for paid marketing, with discipline over what each customer costs to win. Raising how often customers buy, or how long they stay, moves this most.
- Lifetime profit is under $500: **Low lifetime value.** The budget for winning each customer is very tight. Repeat business, higher prices or cheaper ways of finding customers matter more than paid advertising.

## Notes

- This is lifetime value on gross profit. Some sources use revenue instead, which gives a much larger figure; say which one this is.
