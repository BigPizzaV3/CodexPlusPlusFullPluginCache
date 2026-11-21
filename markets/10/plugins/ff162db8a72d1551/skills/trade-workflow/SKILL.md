---
name: trade-workflow
description: Draft, confirm, cancel, close, or modify MT5 trades in ChatGPT with the inline confirm card and CRM permissions.
---

Use this skill when the user wants to **propose** or **change** trades on their linked MT5 logins—not for investment advice.

## Preconditions

1. User connected DB Investing via OAuth in ChatGPT.
2. CRM **Propose trades** (not analyze-only) and **MT5 consent** enabled on dbinvesting.ai.
3. ChatGPT app **Allow all actions** (or approve each confirm tool).

## Connection check (before trading)

OAuth success does **not** prove MT5 works. Run:

1. `list_mt5_accounts` — only use logins returned here.
2. `get_account_snapshot` or `get_risk_status` on the chosen login — if this fails, stop and explain reconnect / permissions; do not draft trades.

Use `get_trading_permissions` when confirm is blocked or mode is unclear.

## Account and symbols

- Ask which login or pick one **explicitly** from `list_mt5_accounts`; do not guess “main” account.
- For symbols: `search_symbols` or `get_quotes` with `login` — **never** guess broker suffixes (`.s`, `.b`, `.m`, etc.).

## Tool sequence

| User goal | Tools (in order) |
|-----------|------------------|
| Open market order | Connection check → `draft_trade_instruction` (once) → user confirms on card → `confirm_trade_instruction` |
| Close position | `get_positions` → `draft_close_position_instruction` with **ticket** → confirm → `confirm_trade_instruction` |
| Change SL/TP | `get_positions` → `draft_modify_position_instruction` with **ticket** → confirm → `confirm_trade_instruction` |
| Cancel before MT5 | `cancel_trade_prepare` |
| Refresh quote on card | `refresh_trade_quote` |

## Rules

- One `draft_*` call per user intent; no `render_trade_confirm_card` in the same turn.
- No `confirm_trade_instruction` without explicit user approval on the card.
- After `executed: true`, reply with execution markdown only — no second confirm or new draft in that turn.
- If confirm **fails** or times out: **do not** immediately retry confirm or re-draft. Call `get_trade_activity` (channel chatgpt_mcp) and/or `get_positions` first; only draft again if nothing filled.
- `cancel_trade_prepare` voids a draft only; after fill use close flow with a real ticket.

## Read-only follow-ups

`get_risk_status`, `get_positions`, `get_quotes`, `get_trade_activity`.

See `../get-started/SKILL.md` for connect and revoke.
