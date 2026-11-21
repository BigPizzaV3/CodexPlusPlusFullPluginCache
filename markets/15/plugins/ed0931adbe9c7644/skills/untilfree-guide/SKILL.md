---
name: untilfree-guide
description: When and how to use the Untilfree tools (calculate_freedom_day, retire_at_age, how_long_will_savings_last, fire_variants) for FIRE and retirement estimates, and what not to do with them.
---

# Untilfree: FIRE and retirement estimates

Untilfree is a read-only calculator. It stores nothing, needs no account and makes no network calls. Every result is an estimate from the user's own numbers and stated assumptions (5% yearly growth after inflation and a 4% withdrawal rate unless the user gives others).

## Pick the tool

| The user asks | Tool |
|---|---|
| When can I retire, retire early, stop working; my FIRE number; how long until work is optional | `calculate_freedom_day` |
| What a purchase or a monthly cost does to that date ("how many days later does a $1,200 phone make it") | `calculate_freedom_day` with `purchase` (amount, one-off or monthly, optional item) |
| How much do I need to retire at an age; can I retire at 50 with my savings | `retire_at_age` (add age, savings and monthly investing when given, to get on-track or the gap) |
| How long will a pot of savings last at a monthly withdrawal; is the 4% rule safe for me | `how_long_will_savings_last` |
| Coast, lean, barista or fat FIRE numbers | `fire_variants` (`kind` = one of them, or `all`) |

## How to call

- Use only the numbers the user gave. If a required number is missing (for example monthly spending), ask one short question instead of guessing.
- Keep the user's currency (USD, GBP, EUR, CAD, AUD and others are supported) and say amounts in it.
- Amounts are monthly by default; for `retire_at_age`, set `spendingPeriod` to `yearly` only when the user gives yearly spending.
- Reuse the user's earlier numbers in the same conversation when they ask a follow-up ("with those numbers…").
- After the card appears, add one or two plain sentences: the date or amount, and the main assumption. Do not repeat the whole card.

## What not to do

- Not financial advice: never tell the user to buy, sell or pick a fund, stock, pension product or adviser, and never present the estimate as a promise. Say it is an estimate when the result matters to a decision.
- Do not use these tools for live market prices, tax rules, Social Security or state pension ages, mortgages or debt payoff; answer those without the tools or say they are out of scope.
- Do not promote anything: no app store links, no paid plans, no other products.
- Do not ask for or repeat identifying details (name, employer, account numbers). Ages and amounts are enough.
