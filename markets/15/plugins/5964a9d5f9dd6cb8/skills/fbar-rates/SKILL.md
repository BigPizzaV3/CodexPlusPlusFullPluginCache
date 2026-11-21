---
name: fbar-rates
description: Convert foreign account maximum balances to US dollars at the Treasury December 31 rate for FBAR (FinCEN 114) and Form 8938 with convert_foreign_balances, or look up Treasury Reporting Rates of Exchange with list_treasury_rates.
---

# Zovo FBAR Currency Converter

Use `convert_foreign_balances` when the user has foreign bank accounts and needs each account's maximum balance in US dollars for an FBAR or Form 8938. Pass `tax_year` (e.g. 2025) and up to 25 `accounts`, each with a short `label` (no account numbers), `currency` (ISO code such as EUR, GBP, INR, or the exact Treasury description such as Euro Zone-Euro) and `max_balance` in that currency. Add `year_end_balance` per account and `filing_status` (+ `lives_abroad`) only when the user gives them and asks about Form 8938.

Use `list_treasury_rates` when the user asks for the Treasury rate itself: `year`, optional `currency` filter, optional `all_quarters`.

Show the aggregate maximum value and the FBAR threshold result first, then each account's Treasury row (country-currency, rate, effective date) and rounded-up USD value, then the PDF, CSV and Excel links (they expire in about one hour). Quote the source line with its retrieval time.

Rates are foreign units per 1 US dollar from the U.S. Treasury Reporting Rates of Exchange for December 31 of the tax year; each account is rounded up to the next whole dollar and a negative maximum is 0, as the FinCEN instructions describe. An account whose currency has no December 31 Treasury rate is shown as not converted: tell the user the FinCEN instructions call for another verifiable rate with its source. A year that has not ended has no December 31 rate yet. Form 8938 thresholds are published figures shown for information. Do not present results as tax advice, and do not use these tools for today's market exchange rate or to file a form.
