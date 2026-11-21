---
name: wealth-simulation
description: Use when the user asks whether their savings, income and spending will reach a goal, when they can retire, whether their money will last, or wants a Monte Carlo projection of household net worth. Guides gathering a few numbers, calling the WealthStoryLine quick_simulation tool and explaining the result.
---

# WealthStoryLine retirement and savings check

## When to use
The user wants a probabilistic answer about their household finances: "Can I retire at 60?", "Will my savings last until 90?", "Will I have $1 million by 50?". Use the `quick_simulation` tool rather than estimating by hand.

## What to ask (only what is missing)
1. Age and country (ISO code such as US, TW, JP; amounts are in that country's currency).
2. Household income per year now, and the age when work income stops.
3. Living expenses per year now.
4. Savings and investments today.
5. Pension or other income after retirement (0 if none).
6. Optional: a target amount and the age to reach it; an expected investment return.

Do not ask for names or account details. If the user gives only some numbers, run with what you have; the tool fills sensible defaults and lists them in `assumptions_used`.

## How to explain the result
- Lead with the success probability in plain words ("about 7 in 10 futures reach your goal").
- Mention the bankruptcy rate and the worst-10% net assets so the user sees the downside.
- All amounts are inflation-adjusted, in today's money.
- Name the defaults that matter (investment return, target used) and offer to rerun with the user's own numbers.
- Offer one or two what-if variations (retire later, spend less, save more) and rerun if the user agrees.

## Limits
Home purchases, mortgages, several incomes and fund portfolios are not modelled here; say so and point the user to https://wealthstoryline.com. Taxes and insurance are not modelled. Results are projections for planning discussions, not financial advice.
