---
name: get-started
description: Use when the user asks about or wants to change their Referly affiliate program (affiliates, referrals, sales, commissions, payouts, coupons, links, announcements, tracking setup). Explains how the Referly tools fit together and the safety rules for writes and payouts.
---

# Working with Referly

Referly is affiliate-program software. Every Referly tool acts on one affiliate program, identified by `programId`.

## Finding things

1. If the connection covers more than one program, call `list_programs` first and ask the user which program they mean.
2. For a quick picture of the program, use `get_program_overview` for a period, or `list_top_affiliates` for a ranking.
3. To find a specific affiliate, customer, sale, link or coupon, use `search`, then `fetch` to open one result.
4. Plan, group, webhook, domain and notification ids come from their `list_` tools.

## Making changes

- Bulk and destructive actions return a preview first. Show the user the preview, and only call the tool again with `confirm: true` after the user agrees.
- Prefer deactivating or disabling over deleting when history matters.
- Drafts (announcements, popups, contests, content rewards, performance bonuses) stay drafts until their `set_*_state`, `set_*_status` or `set_*_enabled` tool turns them on. Do not publish a draft unless the user asks.

## Money

- Referly never sends money from chat. Payout tools prepare batches; the user reviews and sends them in the Referly dashboard. `get_payout_execution_link` returns that dashboard link.
- Amounts are in the program's currency. Dates are ISO 8601.

## Tracking setup

Start with `get_integration_setup_status`, then `get_tracking_snippet` and `verify_tracking_script`.
