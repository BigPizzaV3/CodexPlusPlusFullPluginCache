# Lukka tool inventory

This is the original Claude plugin operation list with three unavailable
operations removed. It contains **66 operations**. No new product operations
have been added to this edition.

Tool names and required input types below use the verified Global catalog.
Optional parameters and actual host dispatch names follow the connected schema.

[README](../README.md) · [CONNECTORS](../CONNECTORS.md)

## Pricing (20)

| Operation | Required inputs |
|---|---|
| `pricing___get_candles` | `pairCode`: string, `sourceId`: integer |
| `pricing___get_derivative_source_details` | `productType`: string, `sourceId`: integer |
| `pricing___get_historical_derivative_trades` | `sourceId`: integer |
| `pricing___get_historical_index_prices` | `sourceId`: integer |
| `pricing___get_historical_prices` | `pairCode`: string, `sourceId`: integer |
| `pricing___get_latest_derivative_trades` | `sourceId`: integer |
| `pricing___get_latest_index_prices` | `sourceId`: integer |
| `pricing___get_latest_market_caps` | None in schema |
| `pricing___get_latest_markets` | `marketType`: string |
| `pricing___get_latest_prices` | `sourceId`: integer |
| `pricing___get_market_capitalization` | `pairCode`: string |
| `pricing___get_market_depth` | None in schema |
| `pricing___get_market_variances` | `pairCode`: string, `sourceId`: integer |
| `pricing___get_order_book_snapshot` | None in schema |
| `pricing___get_source_details` | `sourceId`: integer |
| `pricing___get_source_details_by_product` | `productType`: string, `sourceId`: integer |
| `pricing___get_spot_trades` | `pairCode`: string, `sourceId`: integer |
| `pricing___get_vwap` | `from`: string, `to`: string, `pairCode`: string |
| `pricing___list_pricing_sources` | None in schema |
| `pricing___list_sources_by_product` | `productType`: string |

## Reference Data (20)

| Operation | Required inputs |
|---|---|
| `refdata___get_asset_by_id` | `assetLid`: string |
| `refdata___get_asset_crypto_actions` | `assetLid`: string |
| `refdata___get_asset_exposure` | None in schema |
| `refdata___get_asset_mappings` | None in schema |
| `refdata___get_core_asset_scores` | None in schema |
| `refdata___get_crypto_actions` | None in schema |
| `refdata___get_derivative_by_id` | `lukkaDerivativeLid`: string |
| `refdata___get_entity_by_code` | `code`: string |
| `refdata___get_enums` | `enumName`: string |
| `refdata___get_legal_entity_mappings` | None in schema |
| `refdata___get_market_scores` | None in schema |
| `refdata___get_pair_mappings` | None in schema |
| `refdata___get_reference_assets` | None in schema |
| `refdata___get_reference_derivatives` | None in schema |
| `refdata___get_reference_pairs` | None in schema |
| `refdata___get_sectors` | None in schema |
| `refdata___list_assets` | None in schema |
| `refdata___list_derivatives` | None in schema |
| `refdata___list_entities` | None in schema |
| `refdata___list_vasps` | None in schema |

## AML (4)

| Operation | Required inputs |
|---|---|
| `AML___generateAmlEnhancedReport` | `address_type`: string, `address`: string |
| `AML___generateAmlScoringReport` | `address_type`: string, `address`: string |
| `AML___generateAmlSimplifiedReport` | `address_type`: string, `address`: string |
| `AML___generateAmlStandardReport` | `address_type`: string, `address`: string |

## UDA (6)

| Operation | Required inputs |
|---|---|
| `UDA___Get_newest_block_blockheight` | `blockchain`: string |
| `UDA___Get_transaction_for_txhash` | `blockchain`: string, `txhash`: string |
| `UDA___get_address_assets` | `address`: string, `blockchain`: string |
| `UDA___get_address_balance` | `address`: string, `blockchain`: string |
| `UDA___get_address_transactions` | `address`: string, `blockchain`: string |
| `UDA___get_block` | `block`: integer, `blockchain`: string |

## Analytics (3)

| Operation | Required inputs |
|---|---|
| `analytics___getImpliedRates` | `curveType`: string, `lukkaEntityCode`: string, `pairCode`: string, `rateType`: string, `source`: string |
| `analytics___getImpliedRatesOtcFx` | None in schema |
| `analytics___getImpliedVolatilitySurface` | `lukkaEntityCode`: string, `moneyness`: string, `underlyingAssetLukkaCode`: string |

## News (2)

| Operation | Required inputs |
|---|---|
| `news___getDailySummaries` | None in schema |
| `news___getNews` | None in schema |

## Prediction Markets (11)

| Operation | Required inputs |
|---|---|
| `prediction-markets___GetExchanges` | `limit`: string, `offset`: string |
| `prediction-markets___GetMarketNews` | `publishDateFrom`: string, `publishDateTo`: string |
| `prediction-markets___GetMarketOverview` | `from`: string, `interval`: string, `to`: string |
| `prediction-markets___GetMarketRecap` | None in schema |
| `prediction-markets___GetOpenInterest` | `from`: string, `interval`: string, `to`: string |
| `prediction-markets___GetPMCSstats` | None in schema |
| `prediction-markets___GetPredictionMarketTotalVolume` | `from`: string, `interval`: string, `to`: string |
| `prediction-markets___GetPredictionMarkets` | None in schema |
| `prediction-markets___GetPredictionMarketsTaxonomy` | None in schema |
| `prediction-markets___GetPriceHistory` | `event`: string, `exchangeId`: string |
| `prediction-markets___GetSimilarMarkets` | `event_ticker`: string, `limit`: string, `offset`: string |
