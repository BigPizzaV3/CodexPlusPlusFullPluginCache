---
name: parse-brokerage-screenshots
description: Parse E*TRADE, Robinhood, and other brokerage screenshots into validated position or transaction tables and structured JSON. Use when screenshots show portfolios, holdings, stocks, options, transactions, orders, balances, gains, market values, quantities, prices, or cost basis.
---

# Brokerage Screenshot Parser

Convert attached brokerage screenshots into accurate structured data. Read [references/output-schema.json](references/output-schema.json) when producing JSON.

## Parse safely

- Extract only information visible in the screenshots.
- Never guess, extrapolate, calculate, or reconstruct cropped, obscured, or ambiguous values.
- Use `null` for unavailable values.
- Preserve negative signs and displayed decimal precision.
- Normalize monetary values to JSON numbers without currency symbols or thousands separators.
- Treat color as sign evidence only when the interface makes that meaning unambiguous.
- Normalize complete dates to `YYYY-MM-DD`. Preserve incomplete date text separately and leave the normalized date `null`.
- Add a warning for every cropped, ambiguous, or low-confidence field.
- Do not provide investment advice, predictions, recommendations, or performance interpretations unless separately requested.

## Protect sensitive data

Redact passwords, PINs, authentication codes, API keys, recovery codes, full account numbers, bank details, and authentication QR codes as `"[REDACTED]"`. Redact personal and account identifiers from output unless the user explicitly requests their inclusion.

## Classify the screen

Identify the broker, screen type, account type, currency, and screenshot sequence. Use one of:

- `portfolio_positions`
- `transaction_history`
- `order_history`
- `balances`
- `unknown`

## Parse instruments

Classify each instrument as `stock`, `option`, `etf`, `cash`, `cryptocurrency`, or `unknown`.

For stocks and ETFs, extract visible symbol, description, quantity, last price, average price, cost basis, market value, day gain, total gain, and percentages.

For options, also extract the underlying symbol, expiration date, strike price, call or put type, and contract count. Do not infer quantity, cost basis, market value, or gains from other values unless the user explicitly requests calculations.

For transactions and orders, extract visible dates, symbol, instrument type, action, quantity, price, amount, fees, status, order type, limit or stop price, option details, and description. Keep multiple fills separate.

## Merge screenshots

When screenshots overlap:

1. Match rows using symbol, instrument details, expiration, strike, option type, and visible values.
2. Merge complementary columns from matching rows.
3. Do not duplicate overlapping rows.
4. Preserve conflicting readings and flag them instead of choosing silently.
5. Never combine rows merely because they share a ticker.

## Respond

1. Provide a concise Markdown table of the most important visible fields.
2. Provide JSON conforming to `references/output-schema.json`.
3. Briefly state what was extracted, what was missing or cropped, and what screenshot would complete the data.
4. Remind the user to verify extracted values before relying on them.

Set confidence from `0.0` to `1.0`, reducing it for blurry, cropped, covered, or ambiguous text.
