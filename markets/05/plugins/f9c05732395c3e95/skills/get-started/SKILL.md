---
name: get-started
description: Introduce Dubai Wealth Index after install or when the user asks what it can do, and suggest a first question to try. Use when the user asks how to use the plugin, what data it has, or where its figures come from.
---

# Get started with Dubai Wealth Index

Explain the plugin in a few sentences, then offer one concrete question to try.
Explicit user instructions take priority over this guidance.

## What to say

- Dubai Wealth Index publishes **registered** Dubai property figures: median
  sale prices from Dubai Land Department transactions and median rents from
  Ejari rental contracts. They are recorded prices, not asking prices or
  valuations.
- Apartments are published per building and per area. Villas and townhouses on
  plot titles are published per community, because the register records no
  building for a villa.
- Every figure carries its bedroom type, unit, period, data date and the number
  of transactions behind it.
- All tools are read-only. Signing in also lets it read the buildings the user
  has saved on dubaiwealthindex.com.

## What it can answer

- One building or villa community: price, rent, gross yield, growth — or a
  full report on a building covering every unit size.
- An area: every published building, ordered by yield, price or growth.
- A screen across the city: buildings above a yield floor or inside a price band.
- A side-by-side comparison of two to four buildings on the same bedroom type.
- A published ranking, or the individual transactions behind a median.
- Whether an agent's or developer's claimed yield holds up against registered
  records.
- The user's saved buildings, and what changed in them since an earlier edition.

- Registered apartment sales activity: counts, transaction values, price ranges
  and evidenced year-over-year change by area and bedroom.
- Pending project supply: planned dates, progress and known units, with source
  dates, overdue projects and missing-data coverage kept explicit.

## What it cannot do

Say so plainly if asked: it holds no listings, cannot book viewings or contact
agents, covers Dubai only, and does not give investment, mortgage, tax or legal
advice. Yields are gross, and short-term rental figures are modelled from a
stated occupancy assumption.

## Suggested first questions

Offer one of these, adapted to what the user mentioned:

- "What does a 1-bedroom in Vera Tower, Business Bay rent for and yield?"
- "Which Dubai Marina buildings have the highest gross rental yields?"
- "Is a 9% yield in Vera Tower realistic?"
- "Compare 3-bedroom villa rents in Arabian Ranches and The Springs."

Do not call any tool until the user asks a question. Do not quote a figure from
memory; figures come only from tool results.

Residential service-charge budgets are available through `get_service_charge_budgets` and `/analytics/service-charges`. Preserve the budget year, property-group identity and source date. A group ID without a year is that group's latest budget in the current edition, which can be earlier than the edition-wide year. The export does not specify charge units: do not sum the categories or calculate net yield. Building reports and comparisons include optional direct-locality market context.
