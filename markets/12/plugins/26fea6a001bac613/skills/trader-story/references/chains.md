# Chain ids, asset keys and units

Rows from portfolios and activity identify assets by `asset_key`. `get_token` and
`get_token_candles` want a chain **slug** plus an address. Prefer a row's own
`chain_slug` when present; otherwise map the numeric prefix with this table.

| chain_id | slug |
| --- | --- |
| 1 | ethereum |
| 10 | optimism |
| 56 | bsc |
| 137 | polygon |
| 988 | stable |
| 999 | hyperevm |
| 4663 | robinhood |
| 5042 | arc |
| 8453 | base |
| 42161 | arbitrum |
| 57073 | ink |
| 792703809 | solana |

`1337` is Hyperliquid's HyperCore ledger: a route destination (cash moved to perps), not a
token chain.

## asset_key shapes

| Shape | Meaning |
| --- | --- |
| `4663:0xff08…` | `<chain_id>:<address>` token. Call `get_token(chain=robinhood, address=0xff08…)` |
| `hyperliquid:BTC` | a Hyperliquid perp position on coin `BTC` |
| `polymarket:0x…:yes` | a Polymarket outcome position (`<condition_id>:<side>`) |
| bare `polymarket` / `hyperliquid` on an activity leg | cash moved into that venue, not a trade of a named market |
| `KNOWN-…` as a `symbol` | an instrument id with no ticker: call it an unlisted token and show its `asset_key` |

## Units

| Field | Unit |
| --- | --- |
| discover `stats.change_24h_pct` | percent (`1.06` = +1.06%) |
| `get_token` `stats.activity.price_change_24h`, `stats.windows[].change` | fraction (`-0.0316` = -3.16%) |
| `list_traders` `return_pct`, `hit_rate` | percent, as strings |
| prediction outcome `price`, `best_bid`, `best_ask`, `history[].p` | YES probability 0..1 |
| USD amounts as long decimal strings | exact; round for display (2 dp, or 3 significant digits for small prices) |
| `get_perp_candles` `from`/`to` | unix **milliseconds**; returned `t` is seconds |
| `get_token_candles` `from`/`to` | unix **seconds** |
