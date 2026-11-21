# Onramp Money buy and sell quotes

Onramp Money provides crypto buy estimates and crypto-to-fiat sell estimates
through `/mcp/chatgpt`. Swap is unavailable. Runtime availability
follows the server's advertised tools; this package does not change server flags.

| Tool | Amount choices |
| --- | --- |
| `onrampPriceQuote` | Fiat to spend or crypto to receive |
| `offrampPriceQuote` | Crypto to sell or target net fiat proceeds |

Choose the asset, ISO fiat currency and a supported network, then provide one
positive amount. Network discovery is specific to buy or sell. Quotes return
text and structured data, with optional MCP Apps cards/forms. When a card is
displayed, the assistant acknowledges it briefly; a full text quote is available
when the card cannot render or the user requests details. Crypto display uses
`balanceFloatPlaces` while numeric quote and checkout inputs retain full precision.

The service reads public country, v3 buy/sell network configuration and v4 pricing
endpoints at `https://api.onramp.money/onramp/`. Requests contain asset, currency,
network and amount choices, `appId=1` and `paymentType=1`. It accepts no payment
credentials, identity documents, wallet addresses, private keys or seed phrases.
Service/upstream APIs may have operational access logs. UI assets are inline in
MCP resources. Checkout links point to `https://onramp.money/main/buy/` or
`https://onramp.money/main/sell/` and include ChatGPT source/campaign attribution.

The user obtains a fresh quote and completes verification and any payment or
transfer on Onramp Money. This MCP never creates orders, executes trades, signs
transactions or moves funds. Estimates are free; hosted transactions may carry
disclosed fees. Preparing this package does not establish marketplace approval.
Use [Onramp support](https://onrampmoney.freshdesk.com/support/home) for assistance.
