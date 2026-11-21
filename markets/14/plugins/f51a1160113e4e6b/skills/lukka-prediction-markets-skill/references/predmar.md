# Lukka Prediction Markets Data MCP — hosted workflows

Adapted from the publisher-provided `lukka-mcp-hosted` product reference. Old deployment observations must be checked against current discovery and returned data.

## Discover the actual event and venue

Use `prediction-markets___GetPredictionMarkets` for listings and retain the returned event identifier, venue and outcomes. Use `prediction-markets___GetPredictionMarketsTaxonomy` and `prediction-markets___GetPMCSstats` for the returned taxonomy and classification counts; use `prediction-markets___GetSimilarMarkets` for related markets.

Preserve the deployed `prediction-markets___` prefix and casing. The old entrypoint also mentioned a different prefix and an AWS gateway; this package uses its declared public Lukka endpoint and current host tool handles.

## Interpret activity and history

Use the available market overview, recap, volume and open-interest tools for their distinct measures. For `prediction-markets___GetPriceHistory`, take `event` and `exchangeId` from discovery and inspect required argument types. Use a window overlapping the event's actual trading period; an empty window is not proof that history is broken.

`prediction-markets___GetExchanges` is reference/VASP context, not proof of all active trading venues. Source observations report ignored filters and bare-array response shapes, so inspect returned fields and apply supported filters locally when necessary. An unscored venue must not be assigned a fabricated score.

Keep dates explicit, use millisecond intervals where required, and honor string-versus-number distinctions in live inputs. Return actual observation times, venue identifiers, labels and missing coverage. Observed prices are not guaranteed event probabilities and this plugin does not place wagers or trades.
