---
name: currency-converter
description: Convert money with dated European Central Bank reference rates (convert_currency) and show the exchange rate history for a date range with a CSV download (rate_history).
---

# Zovo Currency Converter

Use `convert_currency` when the user wants a currency converter, an exchange rate today, a rate on a date, or to convert usd to eur (and other pairs). Use `rate_history` when the user wants a historical exchange rate, an exchange rate history, or a CSV of rates over a date range.

1. `convert_currency`: give `amount`, `from`, `to` (one to ten codes separated by commas) and an optional `date` (YYYY-MM-DD, 1999-01-04 or later, not in the future). Call it right away when the request has an amount and two currencies. Omit `date` for the latest published rate.
2. `rate_history`: give `base`, `quote` (one to five codes separated by commas), `start` and `end` (at most 366 days). It returns min, max, average and the first-to-last change in percent plus a CSV download link.
3. Share the converted amount, the rate, the rate date and any note (for example that the ECB did not publish on a weekend or holiday) from the result. Include the CSV link for `rate_history`.
4. Rates are European Central Bank euro reference rates for about 30 currencies, published on working days around 16:00 CET. They are indicative mid-market rates, not a bank or card rate, and there is no cryptocurrency.

Do not use this skill for crypto, metals, stock prices, or financial advice.
