---
name: app-analytics
description: "The person's own app numbers: revenue and proceeds, subscriptions, users, retention, installation cohorts, lifetime value, publishing figures and product analytics, read and compared correctly. Use when the person says things like \"how is my revenue doing?\", \"did the new paywall work?\", \"why did my users drop?\", \"what is my LTV?\" or \"compare this month with last month\". Not for competitors' numbers (market-research) or ratings and reviews (reviews)."
---

# App analytics

## When this applies

Reading the person's own numbers: store revenue and proceeds, subscriptions, users and retention, installation cohorts, lifetime value, publishing revenue and spend, and product analytics from MWM's SDK. Competitors' figures belong to market-research; ratings and reviews to reviews.

## The job and what good looks like

Every number is named: which metric, a period flow or an installation cohort, gross or net, which currency, which window and how mature the data is. Comparisons put like with like. Figures come from the reads, with their date and their limits; an absent value is unknown, never zero. A change is explained only as far as the data supports it, and a guess is labelled as one.

## How a pro decides

- **Which revenue.** When the answer differs between gross revenue and proceeds, or between store and publishing figures, ask which one; otherwise use proceeds and say so.
- **Cohort or period.** A cohort follows the users who installed on a date; a period counts what happened on calendar days. They answer different questions and never share a comparison.
- **Is it mature.** A cohort or a bucket still filling up is not a drop. Compare windows of equal length and equal maturity.
- **One dimension at a time.** Split by one dimension, read it, and narrow before splitting again.
- **Before and after.** For a paywall or a release, compare equal windows around the change, and say what else changed in the same days when the data shows it.

## Do

- Name each number fully the first time you give it.
- Keep each currency in its own column.
- Explain only what the data shows, and mark the rest as a hypothesis.
- Ask when two readings of the question would give different answers.
- Write a note on a chart when the person asks for one, with facts from the data read.

## Don't

- Don't mix cohort and period figures, two currencies, or store and publishing revenue in one table.
- Don't read an immature cohort as a fall.
- Don't treat a missing value as zero.
- Don't call search visibility traffic, visits or conversion.
- Don't add a chart note nobody asked for.

## Pitfalls

- Monthly recurring revenue normalises plans to a month; it is not what was booked.
- User retention, subscription renewal and SDK event retention are different measures with similar names.
- Reports can lag, so the latest days may be incomplete.
- Lifetime value forecasts are predictions, in their own currency, with fewer filters than store figures.

## Store facts

Tool results carry the store rules and limits they depend on, each with its source and the date it was checked. `get_publishing_knowledge` answers questions on this skill's topics the same way (topics: `mwm/analytics-metric-definitions`). When you use one of these facts, give its source and date.
