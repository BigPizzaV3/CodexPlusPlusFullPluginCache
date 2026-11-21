# Nova public tool guide

The public endpoint is `https://ai.nov.ag/mcp/solana-intelligence`. It exposes 47 individually named, model-visible read-only operations. Version 0.3.0 retains the 0.2.5 public parameter contracts below and adds app-only UI reads described separately. The host’s advertised schema remains authoritative. Do not call legacy grouped tools or pass hidden operation selectors.

All exact addresses are public Solana base58 addresses, never secrets. Optional cursors are opaque values returned by the same tool and dataset; never invent one or substitute a URL. Do not auto-paginate. Parameters marked required below are the tool’s required inputs; other listed parameters are optional.

## nova_capabilities

Report implemented tool coverage, bounded limits, provenance and live-stream limitations. No provider call.

Parameters:
- None. Call with an empty object.

## nova_token_profile

Token metadata, pools, risk and market context from Nova. Missing values remain missing; no safety guarantee.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_stats

Computed token stats via the current stats resource, not deprecated events; preserve each reported window and missing metric.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_ath

Reported token all-time-high price and context; indexed historical coverage is provider-defined.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_safety

Canonical token authorities, Token-2022 flags, holder concentration and developer attribution candidates via Nova. Attribution is evidence, not proven identity; never declares a token safe.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_holders

Bounded top-holder snapshot with public wallet labels and concentration analysis. Not an exhaustive holder census; no holder cursor is invented.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_bundlers

Reported bundler aggregate and bounded wallet cohort. Holdings changes do not establish sales or dollar flows.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_first_buyers

Bounded PnL V2 first-buyer cohort (up to 50), with arbitrage and zero-buy exclusions. No deprecated first-buyer endpoint or invented pagination.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_cohorts

Nova holder-intelligence snapshot: reported developer, insider/sniper/bundler evidence where available. Labels can overlap or be unavailable; do not infer an identity or sale from balance changes.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_token_traders

One PnL V2 trader page ranked by token PnL, excluding arbitrage and zero-buy rows. pnl.token and pnl.wallet have different scopes. This endpoint does not accept pnlMode.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_trades

One cursor page of normalized indexed token trades via Nova, with sample buy/sell flow and explicit missing amounts. Use returned nextCursor; no auto-pagination.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_kol_trades

One cursor page of token trades attributed to the provider KOL cohort. Labels do not prove identity or future performance.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_whales

Thresholded large trades from one bounded history page, not a universal whale registry. Cursor advances through sampled input, even if no trades match.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.
- `minTradeUsd`: optional; number; minimum 1000; maximum 1000000000; default 10000

## nova_token_flows

Aggregate deduplicated observed buy/sell USD notional in one cursor page. This is sampled swap flow, not complete transfers, exchange flow, liquidity or realized PnL.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_liquidity

One opaque cursor page of token LP activity. Exact token amounts stay strings; no USD/PnL is invented. Keep this cursor separate from swap cursors and do not signature-deduplicate multiple actions.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_chart

Bounded OHLCV history with return and volume analysis. Provider is reported from actual points. Missing volume is not zero; no guaranteed finality or exhaustive history.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `interval`: optional; string; one of 1s, 5s, 15s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1mn; default "1m"
- `candles`: optional; integer; minimum 1; maximum 300; default 100
- `metric`: optional; string; one of price, marketCap; default "price"
- `toTimestampMs`: optional; integer; minimum 1; maximum 4102444800000

## nova_token_prices

Batch prices for up to 20 exact mints, via one Nova read. Not an executable quote or trading tool.

Parameters:
- `mints`: required; array; minItems 1; maxItems 20; unique items

## nova_token_positions

Read PnL V2 positions for up to 20 public wallets in one provider batch. Explicitly reports notFound and invalid; does not infer complete cohort ownership.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `wallets`: required; array; minItems 1; maxItems 20; unique items
- `pnlMode`: optional; string; one of strict, adjusted; default "adjusted"

## nova_wallet_holdings

Indexed Solana wallet holdings and portfolio concentration. Tracker is the wallet-data source. Unpriced, stale or absent values are explicit; no balance claim suitable for signing.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_wallet_summary

Read wallet PnL V2 summary in the selected accounting mode and currency. Provider-adjusted accounting is not claimed to be FIFO.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `pnlMode`: optional; string; one of strict, adjusted; default "adjusted"
- `currency`: optional; string; one of usd, sol, eur; default "usd"

## nova_wallet_positions

One cursor page of PnL V2 positions, with sample profitability analysis. Period applies to provider positions semantics; never presented as complete all-wallet profit.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `pnlMode`: optional; string; one of strict, adjusted; default "adjusted"
- `period`: optional; string; one of 1d, 7d, 14d, 30d, 90d, all; default "30d"
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.
- `filter`: optional; string; one of all, holding, active, sold, profitable, losing; default "all"
- `sort`: optional; string; one of last_trade, pnl, realized, unrealized, roi, value, holding, invested, cost, proceeds, buys, sells; default "value"
- `direction`: optional; string; one of asc, desc; default "desc"

## nova_wallet_token_position

Read one public wallet-token PnL V2 position; missing cost basis remains absent.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `pnlMode`: optional; string; one of strict, adjusted; default "adjusted"

## nova_wallet_trades

One provider cursor page of indexed wallet swaps. Not accounting-complete transfer or transaction history; no arbitrary deep page or force-refresh.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_wallet_pnl_chart

Provider daily wallet PnL snapshots; token one-second chart coverage does not apply here.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `time_from`: optional; integer; minimum 0; maximum 4102444800
- `time_to`: optional; integer; minimum 0; maximum 4102444800

## nova_wallet_pnl_history

Bounded daily cumulative PnL and activity, not an exact cash ledger.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `currency`: optional; string; one of usd, sol, eur; default "usd"
- `period`: optional; string; one of 1d, 7d, 14d, 30d, 90d, all; default "30d"
- `limit`: optional; integer; minimum 1; maximum 100; default 30

## nova_wallet_performance

Provider rolling PnL, activity, streaks and drawdown. Evidence is historical; ranking does not predict returns.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `currency`: optional; string; one of usd, sol, eur; default "usd"
- `period`: optional; string; one of 1d, 7d, 14d, 30d, 90d, all; default "30d"
- `days`: optional; integer; minimum 1; maximum 90; default 30

## nova_wallet_highlights

Provider standouts, including winners and losers, under selected PnL V2 accounting.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `pnlMode`: optional; string; one of strict, adjusted; default "adjusted"

## nova_wallet_risk

Provider concentration, exposure and PnL mix; risk analytics are not a security clearance.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.

## nova_wallet_dca

One cursor page of indexed public wallet DCA orders. Reads only; never creates or cancels orders.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_kol_directory

Paginated Nova curated public KOL directory. Directory identity and trade profitability are different evidence.

Parameters:
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_kol_resolve

Resolve one Nova directory profile by handle or public address; a directory label is not cryptographic identity proof.

Parameters:
- `query`: required; string; minLength 1; maxLength 100

## nova_kol_leaderboard

Paginated monitored KOL 24h gain ranking. The current Nova contract supports only 24h/gain; no fabricated alternative windows.

Parameters:
- `limit`: optional; integer; minimum 1; maximum 50; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_kol_trades

One cursor page of Nova indexed KOL trades with source labels and sampled flow, not every KOL trade.

Parameters:
- `limit`: optional; integer; minimum 1; maximum 50; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_smart_money

Bounded Nova smart-money signals feed. Uses Nova evidence filters; standalone smart-money discovery is unavailable. Missing evidence never becomes a smart-trader claim.

Parameters:
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_whale_signals

Whale-labelled observations from one bounded Nova smart-money feed page. No guarantee of complete large-trade coverage.

Parameters:
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_dca_flow

Read active DCA flow and remaining orders for one exact Solana mint, in one bounded cursor page. Indexed intentions are not executed volume or guaranteed future demand; missing data remains unknown.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_dca_buyers

Read the active DCA buyer cohort for one exact Solana mint, in one bounded cursor page. Indexed intentions are not executed volume or guaranteed future demand; missing data remains unknown.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_dca_sellers

Read the active DCA seller cohort for one exact Solana mint, in one bounded cursor page. Indexed intentions are not executed volume or guaranteed future demand; missing data remains unknown.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_token_dca_users

Read the active DCA user cohort for one exact Solana mint, in one bounded cursor page. Indexed intentions are not executed volume or guaranteed future demand; missing data remains unknown.

Parameters:
- `mint`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `limit`: optional; integer; minimum 1; maximum 100; default 25
- `cursor`: optional; string; minLength 1; maxLength 1024; Opaque nextCursor returned by this same tool; never a URL.

## nova_search_tokens

Search Solana token observations by a user-supplied name, symbol or exact public mint. Return at most the requested limit under Nova's research-access policy. Results are not a screened recommendation or proof of sellability; preserve missing data and promotion flags.

Parameters:
- `query`: required; string; minLength 1; maxLength 100
- `limit`: optional; integer; minimum 1; maximum 100; default 25

## nova_trending_tokens

Read one bounded Nova-filtered trending Solana token ranking for the selected interval. Preserve promoted true/false/unknown; an unknown flag does not mean organic. Ranking is an observation, not a recommendation or complete market scan.

Parameters:
- `interval`: optional; string; one of 1h, 6h, 24h; default "1h"
- `limit`: optional; integer; minimum 1; maximum 100; default 25

## nova_most_traded_tokens

Read one bounded Nova-filtered Solana token trading-volume ranking for the selected interval. Preserve promotion flags and missing volume; a ranking is not a recommendation or complete market scan.

Parameters:
- `interval`: optional; string; one of 1h, 6h, 24h; default "1h"
- `limit`: optional; integer; minimum 1; maximum 100; default 25

## nova_new_pairs

Read one bounded Nova-filtered list of recently indexed Solana token pairs. Indexing may lag launches; preserve promotion and missing-data flags. This is not an exhaustive launch feed or proof of sellability.

Parameters:
- `limit`: optional; integer; minimum 1; maximum 100; default 25

## nova_token_gainers

Read a bounded Nova-filtered gainers ranking for newly launched Solana tokens over the selected interval. Provider-defined launch coverage is incomplete; no extra page or cursor is available. Historical gains do not predict future returns.

Parameters:
- `interval`: optional; string; one of 1h, 6h, 24h; default "1h"
- `limit`: optional; integer; minimum 1; maximum 100; default 25

## nova_deployer_tokens

Read one bounded page of indexed token deployments for an exact public Solana wallet. Provider-reported pages and totals can be incomplete. A deployer signer can differ from a metadata creator; history does not establish legal identity or a screened recommendation.

Parameters:
- `wallet`: required; string; minLength 32; maxLength 44; Exact public Solana base58 address; never a secret key.
- `page`: optional; integer; minimum 1; maximum 20; default 1
- `limit`: optional; integer; minimum 1; maximum 100; default 25

## nova_signals_snapshot

Read one short observation window of Nova's Solana signals, capped at 10 seconds and 25 events, then release the temporary subscription. Empty windows are valid. No durable watch, replay, complete coverage, finality or guaranteed event delivery.

Parameters:
- `seconds`: optional; integer; minimum 1; maximum 10; default 5
- `maxEvents`: optional; integer; minimum 1; maximum 25; default 10

## nova_kols_snapshot

Read one short observation window of Nova's KOL relay events, capped at 10 seconds and 25 events, then release the temporary subscription. Empty windows are valid. No durable watch, replay, complete coverage, finality or guaranteed event delivery.

Parameters:
- `seconds`: optional; integer; minimum 1; maximum 10; default 5
- `maxEvents`: optional; integer; minimum 1; maximum 25; default 10

## Interpretation and limits

- Identify the service as Nova in normal responses and the user interface. Preserve original provenance in raw tool results, without visible operational provider names, provider breakdowns or Details/Data notes panels. Material warnings and data limits remain meaningful; the presentation does not add independent verification.
- Source observation freshness is unknown whenever status is unknown or observedAt is absent. Retrieval/source-fetch timestamps alone cannot establish current on-chain observations.
- Missing values, notFound and invalid do not establish zero. Preserve reduced, partial, stale, indexing and unavailable states.
- PnL V2 coverage starts in December 2023 and excludes SOL/stablecoin positions where the provider reports that limitation. Preserve strict versus adjusted accounting and requested currency; do not claim FIFO.
- KOL leaderboard covers monitored 24-hour gain only. Labels do not prove legal identity, wallet wealth or future performance.
- DCA flow, buyers, sellers and users describe indexed intentions, not executed or guaranteed future demand.
- Each live snapshot ends after at most 10 seconds/25 events. No durable monitoring, replay, complete coverage or guaranteed finality.
- No trading, signing, transaction construction/broadcast, broad news/social sentiment, complete wallet cash ledger, unrestricted provider passthrough or private-identity graph.


## Interactive result UI

Public research results can render the associated `ui://nova-solana-intelligence/v3.html` component automatically. `nova_token_chart` supplies the chart directly; do not invoke an opener such as a legacy chart/board tool. Expand, Price/Market Cap and history-range controls use the supported chart schema above with the same exact mint. Available observations, null volume and gaps are preserved. A bounded same-mint transaction-history read may accompany an expanded chart without replacing it. No continuing live-feed or complete-history claim follows from rendering a component.

A wallet card can expand into a public identity header and the canonical Positions, Closed and Activity views. These are explicit user interactions through app-only tools, not additional model-visible research operations:

- `nova_ui_wallet_profile`: accepts only required `wallet`, one exact public Solana address. Returns bounded public identity metadata separately from the accounting result; no private account data or follow action.
- `nova_ui_wallet_view`: required `wallet`, `view` (`positions`, `closed` or `activity`) and `limit` (integer 1–25); optional `cursor` is the opaque same-wallet, same-view cursor returned by this operation, maximum 4096 characters. Do not apply a public-model-tool cursor to this view or automatically fetch every page.

On explicit wallet expansion, read the profile once and the requested initial tab. Switching tabs keeps the same public wallet and profile header. Preserve the original summary’s requested strict/adjusted mode and currency; canonical expanded views carry their own accounting and do not inherit a strict label from the summary. Preserve the API’s row order and roster without extra SOL/stablecoin/dust filtering. Closed rows describe token-lifetime aggregates with unavailable close/reopen episode history. Activity is a bounded indexed-execution sample; transfer-only history and per-fill realized PnL can be unavailable.

The user interface identifies Nova and avoids visible provider/source breakdowns and Details/Data notes panels. Original provenance stays in the raw result. Preserve material warnings, unknown observation freshness, incomplete coverage and missing-versus-zero distinctions. Public names, avatars and verification evidence do not prove legal identity, wallet control, token safety or future returns.
