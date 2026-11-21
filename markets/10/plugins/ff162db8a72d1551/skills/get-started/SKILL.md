---
name: get-started
description: Connect DB Investing in ChatGPT and use MT5 desk tools safely.
---

# Get started with DB Investing in ChatGPT

## Who this is for

DB Investing clients with linked MT5 accounts—the same account on [dbinvesting.ai](https://dbinvesting.ai) (web) or the DB Investing desktop app—who want snapshots, quotes, positions, and **proposed** trades in ChatGPT. Not investment advice.

## Before you connect

1. Use your existing DB Investing CRM login (web or desktop). OAuth for ChatGPT runs through [dbinvesting.ai](https://dbinvesting.ai).
2. Open **AI Settings → Permissions**:
   - Accept **MT5 access** consent if prompted.
   - Set trading mode to **Propose trades** (not analyze-only) if you want draft/confirm flows.
3. In ChatGPT, add the DB Investing app and complete **OAuth** when asked.

## In ChatGPT after connect

- Ask for **your** accounts: “List my MT5 accounts.”
- Read desk data: equity, margin, quotes, open positions.
- To open a trade: ask for a **draft** (e.g. “Draft buy 0.01 XAUUSD on login …”). Review the inline **Confirm & send** card; approve the tool when ChatGPT asks.
- To cancel a **draft** before MT5: use **Cancel** on the card (not “close my position” after execution).

## Approvals

In the app settings in ChatGPT, use **Configure → Allow all actions** (or approve each confirm) so `confirm_trade_instruction` can run after you agree.

## Disconnect

- **dbinvesting.ai** → AI Settings → Permissions → **Revoke connection**, or `/settings/connected-apps`.
- Or remove the app in ChatGPT.

## Trade workflows

For draft → confirm → cancel/close/modify sequences, follow **`trade-workflow`** skill in this plugin.

## Limits

- Tools only access data and trading actions allowed for **your** connected CRM user.
- This is not personalized investment advice. Trading involves risk.
