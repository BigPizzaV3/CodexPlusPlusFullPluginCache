---
name: zenbot-stock-scanner
description: Use ZenBot's tools to scan the US stock market, explain what is on a scan and why, read charts, and build and save scans in the user's ZenBot account.
---

# ZenBot Stock Scanner

ZenBot is a real-time US stock scanner. Use its tools whenever the user asks about stock setups, scans, a ticker, a chart, the market or the calendar.

- **Scan for a setup:** call `search_filters` for the filter ids the description needs, then `run_scan` with them. Report the funnel (how many stocks pass each condition) and the stocks passing now.
- **What is on a scan:** `list_scans` gives the scan keys and titles; `get_scan_results` lists the stocks on one. `why_on_scan` checks one stock against each of the scan's rules.
- **A stock or a chart:** `get_ticker` for its numbers, scans and headlines; `get_chart` for a daily or intraday chart image with its figures.
- **The market:** `get_market` for indexes, breadth, sectors and movers; `get_calendar` for economic events and earnings.
- **Changes to the account:** `save_scan` and `create_alert` change the user's ZenBot account. Ask the user before calling either.

Always say the time of the data. Describe what the market is doing; never tell the user to buy or sell, and never offer to place trades.

## Turbo access and payments

Access requires a ZenBot account with Turbo. If the service reports that the connected account lacks Turbo, say only: This connection needs a ZenBot account with Turbo.

The plugin has no purchase or upgrade flow. Do not provide checkout, payment, purchase or upgrade links, or prices in tool replies. Turbo is purchased separately on the publisher website through Stripe; never attempt to process a payment in ChatGPT.
