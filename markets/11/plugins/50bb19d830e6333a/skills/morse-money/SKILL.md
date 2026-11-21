---
name: morse-money
description: Use when someone asks about sending money abroad, what a transfer costs or what the recipient gets, an exchange rate between two currencies, or whether Morse can send money from or to a country.
---

# Morse

Three read-only tools answer questions about sending money abroad. No account is needed and
nothing is sent.

## How to use the tools

1. For a rate between two currencies, call `get_exchange_rate`. The rate is mid-market and
   says nothing about whether Morse can send in those currencies.
2. Before calling `quote_send`, call `list_send_destinations` with the sender's country of
   residence to check the destination country and currency are offered.
3. Always pass the sender's country of residence as `from_country`. If the user has not said
   where they live, ask before quoting.
4. For a quote, call `quote_send` with the amount, `from_country` and `to_country`. Only set
   `from_currency` or `to_currency` when the user asks for a currency other than the default.

## How to present results

- Show the amounts, the fee and the exchange rate as returned, and repeat the `disclaimer`
  field in your own words or verbatim.
- When a result includes `get_started_url`, show it as the way to continue in the Morse app.
- When `list_send_destinations` returns an empty list, tell the user what the returned
  `disclaimer` says: either that Morse is not available to people living in that country, or that
  sending to other people's bank accounts is not offered from there yet. Do not speculate about why.
- When `quote_send` returns "Morse cannot quote that transfer yet", say so and offer
  `list_send_destinations` for the sender's country to show what is offered.

## What never to say

- Never say a transfer was made, scheduled or can be made from this chat. The tools only read
  data; money is sent in the Morse app after the user signs up and confirms the final rate and fee.
- Never claim to know anything about the user's Morse account, balance or history. The tools
  have no access to accounts.
