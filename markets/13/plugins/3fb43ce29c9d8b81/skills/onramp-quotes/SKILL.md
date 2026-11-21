---
name: onramp-quotes
description: Get Onramp Money crypto buy estimates and crypto-to-fiat sell estimates, supported networks, itemized fees, and hosted checkout links.
---

# Onramp Money buy and sell quotes

Use this ChatGPT connection at `/mcp/chatgpt`. Read its advertised tool schemas.
`onrampPriceQuote` estimates purchases; `offrampPriceQuote` estimates crypto-to-fiat
sales. Swap is unavailable. If a tool is disabled or unavailable, explain that;
do not switch to another endpoint to bypass this connection's scope.

1. Preserve details already supplied. Ask for the missing asset and fiat currency
   using ISO codes; never guess a country or currency. The server resolves
   `fiatType` internally; never pass it as an argument.
2. Select the flow from the user's intent. Buying a target crypto quantity is a
   buy; selling crypto for a target fiat receipt is a sell. Never change flow to
   obtain a different quote or use buy networks for a sell.
3. Omit a missing network to discover the complete available list for the selected
   flow. Let the user choose. Numeric networks are Onramp configuration keys, not
   public EVM chain IDs. Never substitute a mainnet for a test network.
4. Request exactly one positive amount. For buy, use `fiatAmount` to spend or
   `coinAmount` to receive. For sell, use `coinAmount` to sell or `fiatAmount` for
   target net fiat proceeds. Clarify conflicting inputs; never pass both amounts.
5. A displayed quote widget already contains the amounts, network, price, fees,
   and checkout button. Respond with one short acknowledgement. Do not repeat a
   quote table, fee breakdown, or checkout link below it unless explicitly asked.
   When no widget is available or rendering fails, show the complete returned text
   quote and checkout link. Always show errors and requests for missing choices.
6. Preserve the API's exact numeric amounts for calculations, edits and checkout.
   For display, use the returned text quote or `balanceFloatPlaces` for crypto
   quantities. Sell fiat proceeds already include fees: do not subtract them again
   or reconstruct them using another rate. Show tiny nonzero prices/fees visibly.
7. Use the returned `actionUrl` / `buyUrl` / `sellUrl` unchanged so the selected
   amount, network and ChatGPT attribution remain intact. Checkout obtains a fresh
   quote; final rates, eligibility and fees may change.

The user completes wallet details, verification, payment or crypto transfer and
confirmation on Onramp Money. These tools only fetch estimates. Never create
orders, execute trades, sign transactions, transfer funds, or claim completion.
Do not collect payment credentials, identity documents, passwords, private keys
or seed phrases. Do not present personalized investment recommendations.

Examples:
- “How much USDT can I buy for 5000 INR on Polygon?”
- “How much USD do I need to buy 0.05 ETH on Ethereum?”
- “What would I receive in INR for selling 100 USDT on Polygon?”
- “How much USDT must I sell on Polygon to receive 5000 INR after fees?”
- “Which networks support selling USDT for INR?”
