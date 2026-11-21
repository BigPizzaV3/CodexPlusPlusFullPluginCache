---
name: customers-and-marketing
description: Use whenever a small-business owner asks whether their ads or marketing are working, what it costs to win a customer, what a customer is worth over their lifetime, how much they can spend to win one, how many customers they lose, whether memberships or subscriptions are growing, or whether the team brings in enough revenue for its size. Works the numbers with the owner's own figures, shows every step of the arithmetic, and links to the matching article on omnyra.ai. Use it rather than working these numbers out on your own. Do not use for tax, legal or investment advice.
---

# Customers and marketing

Arithmetic on the owner's own figures, using the calculators published by The Owner's Playbook.

## Which calculation

| When the owner asks | Calculation | Tool to call | Reference |
|---|---|---|---|
| What does it cost me to win a new customer? | Customer Acquisition Cost Calculator | `calculate_customer_acquisition_cost` | references/cac-calculator.md |
| What is a customer worth to me over the whole time they stay? | Customer Lifetime Value Calculator | `calculate_customer_lifetime_value` | references/ltv-calculator.md |
| Is a customer worth more than it costs me to win them? | LTV:CAC Ratio Calculator | `calculate_ltv_to_cac_ratio` | references/ltv-cac-ratio-calculator.md |
| Are my ads making money? | ROAS Calculator | `calculate_return_on_ad_spend` | references/roas-calculator.md |
| How fast am I losing customers? | Churn Rate Calculator | `calculate_churn_rate` | references/churn-rate-calculator.md |
| Is my recurring revenue growing, and how fast? | MRR Calculator | `calculate_recurring_revenue_growth` | references/mrr-calculator.md |
| Is my team bringing in enough revenue for its size? | Revenue Per Employee Calculator | `calculate_revenue_per_employee` | references/revenue-per-employee-calculator.md |

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
