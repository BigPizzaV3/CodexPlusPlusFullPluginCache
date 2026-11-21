# Brief template

Fill only what the tools returned. Drop a section with nothing in it, and list it
under Unknowns if the reason is a missing tool or no access.

```markdown
# Trading brief: <workspace name>, <Mon DD Mon> to <Sun DD Mon YYYY> (<AEST/AEDT>)
<Focus: <category / supplier / remit>, if given>

**Headline.** <One or two sentences: the main call this week, with its figure.>

## Actions
Overdue (<n>)
- <title>, <owner or "unassigned">, due <date>
Due this week (<n>)
- <title>, <owner>, due <date>
Source: twelfth_list_open_actions, as of <time>. <"List capped at 100" if full.>

## Suppliers awaiting action
| Supplier | Open recommendations | Catalogue products |
| --- | ---: | ---: |
Source: find_supplier (order_by open_recommendations), as of <time>.

## Stock and cover
Lowest cover
| SKU | Product | Stock | Cover | On order | Units L4W |
Top sellers at risk
| SKU | Product | Units L4W | Cover | On order |
<n> lines have no cover measure and are not ranked.
Source: twelfth_list_products, as of <time>.

## Market
Price index by competitor (<4/8/12>-week average; 100 = parity, above 100 we are dearer)
| Competitor | Index |
This week's moves
- <headline> (<SKUs>)
Prices are observed, not live. As of <time>.
Source: price_intel_summary, price_intel_observations.

## Projects / Routines / Calendar / Since last week
<Only if offered and non-empty.>

## Unknowns
- <Tool not offered on this connection: ...>
- <Figures null or unmeasured: ...>
- <Possible gaps from remit scope: ...>

## Three things first
1. <Action>, because <figure>. Owner: <name>.
2. ...
3. ...
```

## Writing notes

- Use dates and times in the workspace timezone, labelled.
- One currency, the workspace's, unless a tool returned another; then label it.
- Prefer counts and dollars over adjectives. "12 actions overdue, 5 unassigned"
  beats "a lot of overdue work".
- A blank owner is worth saying: unowned work is often the real finding.
- Do not pad. A quiet week can be a short brief.
