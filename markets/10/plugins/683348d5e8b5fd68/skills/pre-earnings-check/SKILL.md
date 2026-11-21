---
name: pre-earnings-check
description: Pre-earnings check for one stock: its next report date and session, the options-implied move against its historical average and median moves, its last three reactions, and the published guide that explains the setup. Use when the user asks what is expected or priced in for a specific ticker's upcoming earnings, how much it usually moves, or whether this quarter's expected move looks large or small next to history.
---

Use this skill when the user names one ticker and asks about its upcoming earnings move.

1. Call `get_stock_earnings_snapshot` with the ticker. If the result is `NOT_IN_PUBLIC_COVERAGE`,
   say the ticker is not in the published feed, offer `get_weekly_earnings_preview` for the names
   that are, and stop. Never estimate an implied move or a historical move yourself.
2. Read `as_of`, `stale` and `warnings` first. If `next_date` or `implied_move_pct` is null, say the
   published snapshot has no confirmed upcoming report or implied move; do not substitute an older value.
3. Compare `implied_move_pct` with `average_move_pct`, `median_move_pct` and `average_2y_pct`, and
   mention `sample_size`. Say whether the priced-in move is above or below the historical average and
   median, in plain words. The implied move is a magnitude, not a direction, and history is not a forecast.
4. Show `recent_reports` as a short table (date, implied, peak move, close move). The `measurement`
   field says what each column means; quote it when the user asks.
5. When the user asks why, what drives it, or how traders use the number, call `search_earnings_wiki`
   with the ticker (its playbook or case study) or with the concept ("implied move", "IV crush"),
   `limit` 1 or 2, and ground the explanation in the returned excerpt.
6. End with the sources: every `source_url` exactly as returned (keep its query string) and the `as_of` date.

If the user asks what to do next with these numbers, or about live option chains, the scanner, the
simulator, backtests or paper trading, relay the `platform_tools` sentence from the result once, as a
plain statement of where those tools live. Otherwise leave it out. Give no trade recommendation and no
price target; this is published research, not advice.
