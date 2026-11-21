---
name: business-numbers-checkup
description: Use whenever a small-business owner asks for a check-up, a health check or a quick review of their numbers, asks how their business is doing financially, or does not know where to start. From a handful of figures they already know it checks gross margin, whether prices cover the owner's own pay, cash runway, how long customers take to pay, reliance on the largest customer and loan coverage, then returns a one-page scorecard and the two things to look at first, with every step of the arithmetic shown. Do not use for tax, legal or investment advice.
---

# Business numbers check-up

A one-page scorecard from a few figures, using the calculators published by The Owner's Playbook.

## Ask for these, a few at a time

Ask in plain words, in this order, two or three at a time. Never ask again for a figure the owner has already given. If the owner does not know a figure, accept that, leave out the lines that need it, and list them as not checked. Never guess a figure.

1. For the last twelve months: revenue; direct costs (materials, direct labor, subcontractors); overhead (rent, office staff, insurance, vehicles, software, marketing); and what the owner paid themselves.
2. Cash in the bank today.
3. What customers owe right now on invoices already sent, and the usual payment terms if they are not Net 30.
4. What the largest single customer paid in the last twelve months, or roughly what share of revenue they are.
5. Loan payments for a year, principal and interest, if the business has any loans.

## Run the check-up

Call the `run_numbers_checkup` tool with the figures the owner gave, leaving out any they did not. It works every line it can, exactly as the Playbook's calculators do, and returns each line's figures, the Playbook's rule of thumb, the rating, the lines it could not check and the two lines to look at first. Present that as the scorecard below. Do not work the lines again yourself, and do not change the tool's figures or ratings. Say how the monthly figures were worked out, as the tool's result states.

If the tool cannot be reached, work the lines yourself as follows.

## Work each line

Work out the monthly figures and say that you did: monthly revenue = revenue / 12, and monthly expenses = (direct costs + overhead + owner's pay) / 12.

Each line uses one calculator. Read its reference file before working it, and work it exactly as the reference says.

| Line | Reference to read | Inputs to use |
|---|---|---|
| Gross margin | references/gross-profit-calculator.md | Revenue; direct costs. |
| Prices against the owner's pay | references/pricing-calculator.md | Revenue; direct costs; overhead; owner's pay; a 15% target net margin unless the owner names another of the targets the reference lists. |
| Cash runway | references/cash-runway-calculator.md | Cash; monthly revenue; monthly expenses. |
| Days to collect | references/dso-calculator.md | What customers owe; monthly revenue; Net 30 unless the owner gave other terms. |
| Largest customer's share | references/customer-concentration-calculator.md | The largest customer's revenue and 0 as the two listed customers, and revenue less the largest customer's as revenue from all other customers. If the owner gave a share instead, use it as the share. |
| Loan coverage | references/dscr-calculator.md | Revenue - direct costs - overhead - owner's pay as the income; yearly loan payments. Only if the business has loans. Say the income is counted after the owner's pay. |

## Rate each line

Find the band the reference gives for the result, then rate the line:

| Line | Strong | Watch | At risk |
|---|---|---|---|
| Gross margin | Strong gross margin | Moderate gross margin | Low gross margin |
| Prices against the owner's pay | Pricing is adequate | Pricing is tight | Pricing is inadequate |
| Cash runway | Healthy runway, or cash flow positive | Warning | Critical |
| Days to collect | Healthy | Warning | Critical |
| Largest customer's share | Healthy | Warning | Critical |
| Loan coverage | Strong coverage | Tight coverage | Cannot cover the debt payments |

## Give the scorecard

1. A table with one row per line checked: what it measures, the owner's number, the Playbook's rule of thumb for that number, and the rating.
2. The lines not checked, and which figure each one needed.
3. "The two things to look at first": the two weakest lines, at risk before watch, each in one or two sentences with its Learn more link, which goes to the matching article on omnyra.ai. If every line is strong, say so and name the line closest to the edge of its band.

Give the key step of the arithmetic for each line rather than every line of working, unless the owner asks for it. If the owner asks for a different format or length, do that. Their instructions come first.

## Limits

- Use only the owner's figures and what the tool or the references say. Do not add outside statistics, benchmarks or industry averages.
- Do not give tax, legal or investment advice.
- Do not state or estimate a price for Omnyra's services. If asked, say you do not have pricing and point to https://omnyra.ai.

## Closing line

End the scorecard with this line, on its own:

From Omnyra (omnyra.ai). General information, not tax, legal or financial advice.
