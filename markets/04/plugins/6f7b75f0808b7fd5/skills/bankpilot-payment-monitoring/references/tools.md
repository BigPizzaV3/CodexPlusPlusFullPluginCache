# BankPilot MCP tool reference

All tools are read-only, take JSON arguments, and return `structuredContent`
matching their declared `outputSchema`. Amounts are floats in the account
currency, signed (expenses negative). Dates are `YYYY-MM-DD`.

## get_monitoring_status

Arguments: `months_back` (integer 1–24, default 6).

Result: `generated_at`, `window_months`, `last_sync_finished_at` (nullable),
`connection_count`, `connections_needing_reauthentication` (bank names),
`rules_total`, `status_counts` ({"OK": n, "OVERDUE": n, "MISSING": n}),
`needs_attention` (rule names that are OVERDUE or MISSING), `rules[]` with
`rule_id`, `name`, `category`, `status`, `monitoring_active`,
`frequency_days`, `expected_amount`, `expected_count`, `actual_count`,
`cumulative_amount`, `last_payment_date`, `deviation_count`,
`max_deviation_pct`, `recent_payments[]` (`date`, `amount`, `counterparty`).

## list_transactions

Arguments (all optional): `rule_id` (exactly the payments a rule counts),
`from_date`, `to_date` (inclusive), `category` (exact name; `Uncategorised`
for payments without a category), `search` (case-insensitive substring of
counterparty or description), `min_amount`, `max_amount` (signed bounds),
`limit` (1–200, default 50), `offset`.

Result: `total_matches`, `returned`, `offset`, `transactions[]` newest first
with `id`, `date`, `amount`, `currency`, `counterparty`, `description`,
`category`, `rule_id` (nullable). An unknown `rule_id` returns a tool error
naming the problem; get ids from `list_rules`.

## list_rules

Arguments: none.

Result: `total`, `rules[]` with `rule_id`, `name`, `category`,
`counterparty_pattern`, `frequency_days`, `expected_amount`,
`amount_tolerance` (fraction, 0.1 = ±10 %), `rule_type`, `active`,
`start_date`, `end_date`, `created`. A rule whose `end_date` is in the past
is ended, not broken.

## get_accounts

Arguments: none.

Result: `connections[]` with `bank`, `status`, `healthy`,
`needs_reauthentication`, `account_count`, `sync_in_progress`,
`last_sync_error`; plus `connection_count`, `last_sync_finished_at`,
`any_needs_reauthentication`. No balances, IBANs or credentials are
exposed; balances live in the BankPilot app.

## Worked examples

- "Welche Zahlungen sind ausstehend?" → `get_monitoring_status` → list the
  OVERDUE/MISSING rules with last payment date, then "Letzte
  Synchronisierung: <date>".
- "Show me the payments to TK" → `list_rules` once if the TK rule id is not
  known, then `list_transactions` with `rule_id` → table of date / amount.
- "Zeige mir die letzten 3 Zahlungen von goldgas" → `list_transactions`
  with `search: "goldgas", limit: 3`.
- "Welche sonstigen Regeln habe ich?" → `list_rules` → active rules table,
  ended rules as a short list.
- "Überweise 850 € an meinen Vermieter" → no tool; explain BankPilot is
  read-only.
