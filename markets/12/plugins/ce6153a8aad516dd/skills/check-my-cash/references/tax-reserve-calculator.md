# Tax Reserve Calculator

Answers: Roughly how much should I be setting aside for taxes?
Learn more: https://omnyra.ai/wiki/business/tax-reserve

## Caution

This is a rough set-aside estimate from flat assumed rates. It is not a tax calculation and it is not tax advice. Tax situations vary a great deal, and a tax professional should work out the real figure. Say this whenever you give a result.

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Projected profit for the year | $ a year | none, ask for it | What the business expects to make this year before taxes. |
| Profit so far this year | $ | $0 | Profit from the start of the year to now. Use 0 if it is not known, and the result will only cover the full year. |
| Business structure | choose one | Single-Member LLC | How the business is set up. It decides which assumed rates are used. One of: Sole Proprietorship; Single-Member LLC; Multi-Member LLC; S-Corporation; C-Corporation. |
| State income tax rate | % | 5% | The owner's state income tax rate. Use 0 for a state with no income tax. |
| Set aside so far | $ | $0 | What is already put away for taxes. Use 0 if nothing is. |
| The current month | a number from 1 to 12 | none, ask for it | Work this out from today's date. Do not ask the owner for it. |
| The owner's own total rate | % | optional, leave out if not known | If the owner or their accountant has a total effective tax rate, use it in place of the assumed rates and say that you did. |

## Before you calculate

- Projected profit for the year must be above 0.
- The current month must be a whole number from 1 to 12.

## Formula

1. Assumed federal income tax rate: 22% for a sole proprietorship or single-member LLC, 24% for a multi-member LLC or S-corporation, 21% for a C-corporation
2. Assumed self-employment tax rate: 15.3% for a sole proprietorship or an LLC, 0% for an S-corporation or C-corporation
3. Total rate = assumed federal rate + assumed self-employment rate + state income tax rate. If the owner gave their own total rate, use that instead.
4. Estimated tax for the year = projected profit for the year x total rate / 100
5. Quarterly estimate = estimated tax for the year / 4
6. Tax owed on profit so far = profit so far this year x total rate / 100
7. Reserve gap = tax owed on profit so far - set aside so far. Above 0, the reserve is short by that much.
8. Months left in the year = 13 - the current month, so the current month counts
9. To set aside each month from now = (estimated tax for the year - tax owed on profit so far) / months left

## Rounding

Give dollars to the nearest whole dollar and rates to one decimal place.

## Worked example

Inputs: Projected profit for the year $100,000; Profit so far this year $50,000; Business structure Single-Member LLC; State income tax rate 5%; Set aside so far $15,000; The current month 6.

1. Total rate = 22 + 15.3 + 5 = 42.3%
2. Estimated tax for the year = $100,000 x 42.3% = $42,300
3. Quarterly estimate = $42,300 / 4 = $10,575
4. Tax owed on profit so far = $50,000 x 42.3% = $21,150
5. Reserve gap = $21,150 - $15,000 = $6,150
6. To set aside each month = ($42,300 - $21,150) / 7 = $3,021

Result for these inputs:

- Estimated tax for the year: $42,300
- Total rate used: 42.3%
- Quarterly estimate: $10,575
- Tax owed on profit so far: $21,150
- Reserve is short by: $6,150
- To set aside each month from now: $3,021

Rule of thumb for this result: Reserve underfunded.

## The Playbook's rule of thumb

- The amount set aside covers the tax owed on profit so far: **Reserve on track.** Enough is set aside for the year so far. Keep adding the monthly amount.
- The amount set aside is at least 90% of the tax owed on profit so far, but short of it: **Almost there.** The reserve is slightly behind. Adding the gap brings it back on track.
- The amount set aside is under 90% of the tax owed on profit so far: **Reserve underfunded.** The reserve is short for the profit already made. A catch-up amount into the tax reserve closes the gap.

## Notes

- The assumed rates are flat and apply to every dollar of profit. Real income tax is charged in brackets, and the estimate ignores deductions, credits, the limit on earnings subject to Social Security tax, and the payroll taxes an S-corporation pays on the owner's salary.
- Do not use this to decide how to set a business up, and do not compare structures with it.
