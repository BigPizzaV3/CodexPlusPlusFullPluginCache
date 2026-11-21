---
name: borrow-or-invest
description: Use whenever a small-business owner asks what a loan will cost each month or in total, whether they can afford more debt, whether to buy equipment or make an investment, how long it will take to pay for itself, what return an investment made, or how much money they need to start a business. Works the numbers with the owner's own figures, shows every step of the arithmetic, and links to the matching article on omnyra.ai. Use it rather than working these numbers out on your own. Do not use for tax, legal or investment advice.
---

# Borrow or invest

Arithmetic on the owner's own figures, using the calculators published by The Owner's Playbook.

## Which calculation

| When the owner asks | Calculation | Tool to call | Reference |
|---|---|---|---|
| What will a loan cost me each month and in total? | Business Loan Payment Calculator | `calculate_loan_payment` | references/business-loan-calculator.md |
| Does my business earn enough to cover its loan payments? | DSCR Calculator | `calculate_debt_service_coverage` | references/dscr-calculator.md |
| How long until an investment pays for itself? | Payback Period Calculator | `calculate_payback_period` | references/payback-period-calculator.md |
| What return did, or will, an investment make? | ROI Calculator | `calculate_return_on_investment` | references/roi-calculator.md |
| How much do I need to start the business? | Startup Cost Estimator | `calculate_startup_costs` | references/startup-cost-calculator.md |

If what the owner needs is not in this table, say this skill does not have that calculation. You
may still help in your own words, but do not present your own formula as the Playbook's and leave
off the closing line.

## How to work

1. Pick the calculation from the table. Its reference file lists the inputs, what each means and
   which have defaults.
2. Ask only for the inputs that calculation needs, in plain words, two or three at a time. Never
   ask again for a figure the owner has already given. Where an input has a default and the owner
   does not know the figure, leave it out. Where an input has no default, ask for it. Never make a
   figure up.
3. Call the calculation's tool from the table with the owner's figures. The tool works the
   arithmetic exactly as the Playbook's calculator does. Do not work it again yourself, and do not
   change its figures or its rounding.
4. If the tool reports a problem with the figures, say why in one sentence and ask for a corrected
   figure.
5. Answer in this order: the result, the arithmetic line by line as the tool gives it, the
   Playbook's rule of thumb for that result, then the tool's Learn more link to the matching
   article on omnyra.ai. Say which figures were defaults.
6. If the result has a caution, say what it says in your answer, in your own words.
7. If the tool cannot be reached, work the calculation from its reference file instead: check the
   reference's "Before you calculate" rules, work the formula exactly as given, use a code tool for
   the arithmetic when one is available, and round only where the reference says to.
8. If the owner asks for a different format or length, do that. Their instructions come first.

## Limits

- Use only the owner's figures and what the tool or the reference says. Do not add outside
  statistics, benchmarks or industry averages.
- Do not give tax, legal or investment advice. If the question is one of those, say this skill
  does not cover it and that a qualified professional should.
- Do not state or estimate a price for Omnyra's services. If asked, say you do not have pricing and
  point to https://omnyra.ai.

## Closing line

End every answer that uses a calculation from this skill with this line, on its own:

From Omnyra (omnyra.ai). General information, not tax, legal or financial advice.
