---
version: 3
---

# Price analysis: Patina tool map

One `get_market_snapshot` with `include` of `estimate`, `comps` and `context` answers every question below. Read it once and work from it.

- **"What's it worth?"** Lead with the `estimate` section, and back it with the strongest recent rows in `comps.sold_comps`.
- **"Is this ask fair?"** Put the ask against `comps.sold_comps` first, then against `comps.active_asks` to show the competition it stands next to. Say where it sits against both stacks.
- **"Why is X higher than Y?"** Contrast attribute by attribute: full set against head-only, condition, year and dial variant, bracelet against strap, market of sale, auction against private. Point at the rows that carry the difference.
- **"Should I wait?"** Answer from the trend and liquidity copy in `context`, plus the evidence depth. Do not forecast a price.
- **Another reference or a loose description.** Pin it with `search_watch_references` (free), ask the user to pick when more than one candidate fits, then call `get_market_snapshot` once with that `reference_id`.
- **"Show me every data point."** Only then call `get_market_points`. It is charged, and its counts are pool sizes you never state.

None of the Patina tools searches the web. A web search here is your own, and its results are not Patina evidence. Patina holds no stored evidence for the watch on `not_found`, on `no_data`, when the snapshot's `resolved_watch` brand or model is not the watch the user described, and when the price-analysis rules find none. Say so, then search the web for the price: run your web search tool on the exact brand, model and reference plus `sold`, `auction result` and `price`. Present each find as an unverified web observation, with one citation per page, in that page's currency. Never merge a web price into Patina's band, never present one as Patina's estimate, and never run the dealer-decision playbook on it. If the host gives you no web search tool, say so and say what is missing; do not fill the gap from memory.

Thin evidence earns the same search. When `context.sample_size.band` is `thin` or `estimate.confidence` is `low`, keep the snapshot's band and comps as the read, say it is thin, then search the web for the price the same way and add the finds beside Patina's read as unverified web observations. They never move the band and never enter the dealer-decision playbook.
