# Business Loan Payment Calculator

Answers: What will a loan cost me each month and in total?
Learn more: https://omnyra.ai/wiki/business/business-loans

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Loan amount | $ | none, ask for it | How much is being borrowed. |
| Annual interest rate | % | none, ask for it | The rate the lender quotes, as a yearly percentage. |
| Loan term | choose one | 60 months (5 years) | How long the loan runs. One of: 12 months (1 year); 24 months (2 years); 36 months (3 years); 48 months (4 years); 60 months (5 years); 84 months (7 years); 120 months (10 years). |
| Origination fee | % | 0% | A one-off fee taken from the loan, as a percentage of it. Use 0 if there is none. |

## Before you calculate

- Loan amount must be above 0.
- Annual interest rate must be above 0.
- Loan term must be above 0.

## Formula

1. Monthly rate = annual interest rate / 100 / 12
2. Monthly payment = loan amount x monthly rate x (1 + monthly rate)^months / ((1 + monthly rate)^months - 1)
3. Total paid = monthly payment x months, and total interest = total paid - loan amount
4. Fee = loan amount x origination fee / 100, and true cost = total interest + fee
5. Interest as a share of the loan = total interest / loan amount x 100
6. Effective APR, only when there is a fee: the yearly rate at which the payments are worth exactly the loan amount less the fee. It needs an iterative solve, so only give it when a code tool is available to work it out. Otherwise give the payment, the total interest and the fee, and say the effective APR needs a financial calculator or a spreadsheet to solve.

## Rounding

Give the monthly payment to the cent, other dollars to the nearest whole dollar, and rates to one decimal place.

## Worked example

Inputs: Loan amount $100,000; Annual interest rate 8.5%; Loan term 60 months (5 years); Origination fee 2%.

1. Monthly rate = 8.5 / 100 / 12 = 0.007083
2. Monthly payment = $100,000 x 0.007083 x (1 + 0.007083)^60 / ((1 + 0.007083)^60 - 1) = $2,051.65
3. Total paid = $2,051.65 x 60 = $123,099
4. Total interest = $123,099 - $100,000 = $23,099, which is 23.1% of the loan
5. Fee = $100,000 x 2 / 100 = $2,000, so the true cost is $25,099

Result for these inputs:

- Monthly payment: $2,051.65
- Total paid: $123,099
- Total interest: $23,099
- Interest as a share of the loan: 23.1%
- Fee: $2,000
- True cost (interest and fee): $25,099
- Effective APR: 9.4%

Rule of thumb for this result: Reasonable cost of capital.

## The Playbook's rule of thumb

- Total interest is 25% of the loan or less: **Reasonable cost of capital.** A competitive cost for a small business loan. Check that what the loan pays for will earn back more than its true cost.
- Total interest is over 25% and up to 50% of the loan: **Moderate cost, shop around.** Not unusual for small business lending, but worth comparing offers. A shorter term, a smaller amount or an SBA-backed loan may cost less.
- Total interest is over 50% of the loan: **High cost, proceed with caution.** The business will pay back much more than it borrowed. This is common with high-rate online lenders and very long terms. Look at other kinds of lender, or at funding the need from cash flow.

## Notes

- The payment assumes a fixed rate and equal monthly payments for the whole term.
