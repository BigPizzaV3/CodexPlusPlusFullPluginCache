# Public Research Decision Contract — Version 1.0.4

This contract makes the public Lifetime Core Championship output machine-readable without creating order intent, brokerage authorization, execution authority, or personalized financial calculation.

The original canonical source remains preserved for lineage. For the publicly distributed plugin, `public-compliance-overlay.md` controls wherever the original source requests personal account truth, personalized sizing, transaction directives, account-specific execution guidance, or conflicting ranking semantics.

## Public decision classes

Emit one `decision_class` for the security research object:

- `TICKER_SPOTLIGHT` — highest-ranked current security research candidate. Research priority only.
- `WATCHLIST` — ranked candidate worth continued research.
- `WAIT` — potentially interesting, but current conditions do not justify Spotlight status.
- `RISK_ELEVATED` — material contradiction/event/liquidity/valuation/technical/data-quality risk weakens the candidate.
- `NO_SPOTLIGHT` — no security earns Spotlight status.

Separately emit one `championship_result`:

- `TICKER_SPOTLIGHT` — the #1 security clears the cash hurdle.
- `CASH_WAIT` — cash/wait wins overall.

## Prohibited personalization

The public Decision Envelope must never contain account balances/buying power, holdings/average cost, account concentration, planned dollar risk, share/contract count, personalized allocation, security-specific purchasing-capacity math derived from user finances, BUY/ADD/HOLD/TRIM/EXIT/SELL directives, order intent, or transaction authorization.

## Required separation

Keep these fields independent: `decision_class`, `championship_result`, `spotlight_rank`, `market_permission`, `structural_thesis_quality`, `watchlist_competition`, `technical_state`, `data_freshness`, and `evidence_confidence`.

## Public Research Envelope

```json
{
  "decision_class": "TICKER_SPOTLIGHT | WATCHLIST | WAIT | RISK_ELEVATED | NO_SPOTLIGHT",
  "championship_result": "TICKER_SPOTLIGHT | CASH_WAIT",
  "ticker": "TICKER | NONE",
  "spotlight_rank": 1,
  "market_permission": "GREEN | SELECTIVE GREEN | YELLOW | RED | BLACKOUT | UNKNOWN",
  "structural_thesis_quality": "HIGH | MEDIUM | LOW | UNKNOWN",
  "watchlist_competition": "SPOTLIGHT_1 | WATCHLIST_2 | WATCHLIST_3 | WATCHLIST_OTHER | NOT_RANKED",
  "technical_state": "UNCONFIRMED | DEVELOPING | CONFIRMED | EXTENDED | DAMAGED | UNKNOWN",
  "data_freshness": "FRESH | DEGRADED | STALE | UNKNOWN",
  "current_price": null,
  "price_source": null,
  "price_timestamp": null,
  "catalyst": null,
  "structural_thesis": null,
  "strongest_contradiction": null,
  "technical_confirmation_threshold": null,
  "support_reference": null,
  "resistance_reference": null,
  "no_chase_reference": null,
  "technical_invalidation": null,
  "thesis_invalidation": null,
  "upside_scenario": null,
  "downside_scenario": null,
  "evidence_confidence": "HIGH | MEDIUM | LOW",
  "demotion_conditions": [],
  "research_note": null
}
```

If `decision_class` is `NO_SPOTLIGHT`, set `ticker` to `NONE`, `spotlight_rank` to null, and `championship_result` to `CASH_WAIT`. A `TICKER_SPOTLIGHT` security may coexist with `championship_result=CASH_WAIT` when it is the best security candidate but does not clear the cash hurdle.


## Transaction-language firewall

The envelope is descriptive research output only. It must not contain affirmative or negative transaction recommendations, including `buy`, `do not buy`, `sell`, `do not sell`, `hold`, `add`, `trim`, `exit`, `enter`, `deploy`, `do not deploy`, or equivalent action advice. It must not contain execution-readiness states, entry zones, stops, profit targets, order types, order prices, order timing, or execution plans.
