# Hyperliquid PnL & NAV Auditor

Read-only tools for a public Hyperliquid address:

- account snapshot: perpetual equity and open positions, raw spot balances, and vault equity;
- portfolio history: Hyperliquid's own timestamped portfolio and PnL series;
- recent activity: returned fills and up to 90 days of funding with coverage boundaries.

## Safety and limitations

No wallet connection, credentials, signing, or trading. Spot tokens, perpetual account value, and vault equity remain separate. Recent fills are capped and outputs are not a full-history guarantee, total wallet NAV, accounting opinion, or tax advice.

The hosted server calls only Hyperliquid's documented public Info API. Submitted public addresses are not stored by this service. See the linked privacy policy, terms, and support pages in the public listing.
