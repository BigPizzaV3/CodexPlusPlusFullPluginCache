---
name: halan-draft-limit-order
description: Prepare a Halan Borsa draft buy or sell limit order after resolving the EGX symbol, validating required account details, and obtaining explicit user confirmation. Use only when the user asks to draft an order for later mobile-app review; never represent it as an executed trade.
---

# Halan Draft Limit Order

Collect and validate the order before taking the single write action.

1. Establish the side, EGX symbol or ISIN, limit price, quantity, and validity. Only buy and sell limit orders are supported; do not convert a market-order request into a limit order without the user's direction.
2. Resolve a company name or ticker with `search_symbols`. Never guess an ISIN.
3. For a sell, call `get_portfolio_details` and use a returned custodian ID and settlement cycle whose available units cover the quantity. Do not guess either value. T+0 and T+1 sells are day orders, so call `is_market_open`; stop if the market is closed.
4. For `GOOD_TILL_DATE`, require a `validTill` Unix-millisecond timestamp. Explain that T+0 and T+1 sells are forced to `GOOD_TILL_TODAY`.
5. Immediately before calling `create_temp_order`, show side, company and ISIN, limit price, quantity, custodian and settlement details when applicable, validity, and currency. Ask for an explicit confirmation of those exact details.
6. Call `create_temp_order` only after that confirmation. If any material detail changes, ask for confirmation again.
7. Return the draft identifier and state that the draft still requires separate review and confirmation in the Halan Borsa mobile app before it can reach the exchange.

Do not claim a draft was submitted, filled, or executed. Do not call the tool when required data is missing, holdings are insufficient, or the user has not explicitly confirmed the final summary.
