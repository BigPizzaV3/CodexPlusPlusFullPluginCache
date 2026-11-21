---
name: get-started
description: First-run tour of the Skipo plugin. Confirms the connection to the user's Skipo account works and shows what they can ask about it. Use right after Skipo is installed or connected.
---

# Get started with Skipo

Use this the first time someone connects their Skipo account.

1. Call `check_api_health`. If the status is `MAINTENANCE`, tell the user Skipo is in maintenance and to try again later, and stop here.
2. Call `get_balances`. Summarize the assets with a non-zero balance and the total in USD (the sum of `balanceUSD`). Keep every amount exactly as returned; do not round it. If the call fails with an authorization error, ask the user to reconnect Skipo.
3. Briefly explain what they can ask about:
   - balances, and how a balance changed over time
   - deposits and withdrawals
   - convert orders, fills and the ledger
   - where to send crypto or a CLP bank transfer to fund the account
   - supported assets and markets, minimums and withdrawal fees per network
   - indicative prices
4. Say clearly that this plugin is read-only. It cannot trade, convert, withdraw or send funds, and an indicative price is not an executable quote. Those actions are done in the Skipo app.
5. Offer two or three example questions that fit what they hold.

Do not call `get_account` during this tour: the tour does not need it.
