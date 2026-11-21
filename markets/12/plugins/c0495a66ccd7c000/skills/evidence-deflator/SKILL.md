---
name: evidence-deflator
description: Check whether a Hyperliquid trader's record is skill or could be luck before anyone copies, ranks or cites it. Use when a user asks about a Hyperliquid wallet or trader, shares a leaderboard rank or PnL as proof, or wants to copy-trade someone.
---

# Evidence Deflator

A leaderboard ranks by profit. Among tens of thousands of accounts, someone is always on a streak, so a high rank is not evidence by itself. This skill answers one question: **is the record long and strong enough to tell apart from luck, once you allow for how it was picked?**

## How to check a wallet

Call the `hyperliquid_wallet` tool with the address (`0x` followed by 40 hex characters). It is read-only: it fetches the wallet's public history from Hyperliquid and scores it. If the user only wants to look for themselves, link `https://evidencedeflator.com/wallet/?a=0xADDRESS`.

### Before you call it

Ask how the user found the wallet, or state your assumption. If it came from sorting a leaderboard, pass `picked_from` as the size of that board (Hyperliquid ranks about 47,000 accounts). Leaving it out treats the wallet as the only one anyone looked at, and the bar drops from about 4.9 to 2.

### How to report the result

| verdict | say |
|---|---|
| `too_short` | Fewer than 8 measurable weeks. "This record cannot tell you yet." Not "no skill". |
| `luck` | Cannot be told apart from luck at this length. Give `months_more_to_clear` if present. |
| `clears_single` | Passes for one wallet picked blind, not for one picked off a board. |
| `clears_board` | Passes the best-of-`picked_from` bar. |
| `loses` | t at or below -2: losing, and not by chance. |

Always report the `flags` next to the verdict:

- `no_losing_week`: consistent with selling tail risk; t measures consistency, not the loss that has not happened yet.
- `one_week_majority`: one week made most of the gains.
- `pnl_outside_record`: most of the PnL was booked while the account held under $1,000, so it cannot be turned into a return. The verdict covers only the weeks that can be measured.

## What not to do

- Do not turn a passing verdict into a recommendation, and do not give buy or sell advice. A past record is the trader's fills, not the user's returns after fees, latency and slippage.
- The tool cannot trade, copy trades, or read exchange accounts. It only reads public Hyperliquid wallets. Say so when asked for anything else.

## Method, in one paragraph

Weekly returns come from PnL, so deposits and withdrawals are not counted as returns. t is Sharpe times the square root of years, with the n - 1 variance and Student's t on effective degrees of freedom, put back on the normal scale so short records are not over-read. One record picked blind needs t >= 2; the best of N needs the Bonferroni bar (4.90 for about 47,000). Details: https://evidencedeflator.com/method/
