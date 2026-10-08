---
name: bankpilot-payment-monitoring
description: Answer questions about a user's recurring bank payments with the BankPilot MCP tools (get_monitoring_status, list_transactions, list_rules, get_accounts). Use when the user asks whether monitored payments arrived, what is pending, overdue or missing (ausstehend, überfällig, fehlend), for payments to a specific counterparty or rule, for their monitoring rules, or whether a bank connection needs renewing. Read-only; German-first users.
---

# BankPilot payment monitoring

Use this skill when the BankPilot app is connected and the user asks about
their monitored recurring payments, their transactions, their monitoring
rules, or the health of their bank connections. BankPilot is read-only: it
can report, it can never move money, change rules or touch bank logins.

## Workflow

1. Pick the one tool that answers the question (see the table below). One
   call is almost always enough; do not "warm up" with other tools.
2. Call it with the narrowest arguments that fit the question (`rule_id`,
   `search`, date range, `limit`).
3. Answer in the user's language (German by default), in the format rules
   below, and state the last bank sync date whenever timing matters.
4. If the user asks for something BankPilot cannot do, say so in one
   sentence and point to the BankPilot app (see Limits). Do not call a tool
   to "try anyway".

## Which tool

| Question | Tool | Notes |
| --- | --- | --- |
| Did all monitored payments arrive? What is pending / overdue / missing? Which payments are due? | `get_monitoring_status` | Already includes the last sync time and connections needing re-authentication. Never add `get_accounts` or `list_rules` for a status question. |
| Payments to / from X, the last N payments of X, how much did I pay X | `list_transactions` | If X is a rule name, pass its `rule_id` (from a previous `list_rules` or status call); otherwise use `search`. Use `limit` for "the last N". |
| Uncategorised payments, payments in a category, payments in a period, payments over/under an amount | `list_transactions` | `category: "Uncategorised"`, `from_date`/`to_date`, `min_amount`/`max_amount` (signed). |
| What rules do I have? What is monitored? | `list_rules` | Show ended rules (`end_date` in the past) separately. |
| Do I need to renew a bank connection? Which banks are linked? | `get_accounts` | Only for questions about connections themselves. |

## Reading the data

- Amounts are signed: negative = money out, positive = money in. Show them
  the way the user reads them (e.g. "1.214,24 €" for an outgoing payment,
  "+1.000 €" for income). Never flip a sign.
- Rule status: `OK` = payments arrived as expected; `OVERDUE` = the last
  payment is later than the cadence allows; `MISSING` = no matching payment
  in the window at all. `expected_count` vs `actual_count` says how many
  were due vs. seen.
- `last_sync_finished_at` is when BankPilot last pulled data from the
  banks. Payments after that date cannot be visible yet; say so instead of
  calling something "missing".
- `connections_needing_reauthentication` (status) or `needs_reauthentication`
  (accounts): the bank link must be renewed in the BankPilot app before new
  data can arrive. Mention it whenever it is non-empty.
- `total_matches` vs `returned`: if more rows exist than were returned,
  say how many there are in total.

## Answer format

- Lead with the answer in one sentence ("Aktuell ist keine überwachte
  Zahlung überfällig." / "Two rules are overdue: …").
- Lists of payments: a table with date, counterparty, amount; newest first.
  For a single counterparty, a column with the billing month ("Beitragsmonat")
  is helpful when the description carries it.
- Rules: name, expected amount ("ca." when a tolerance applies), cadence
  (`frequency_days` 30 = monatlich, 90 = alle 3 Monate, 365 = jährlich).
- Point out changes the data shows (an amount that rose, a payment that
  came early or late) in one short sentence after the table.
- Do not invent categories, dates or reasons. If a field is null, leave it
  out rather than guessing.

## Limits (say these plainly, then stop)

- No transfers, no payments, no standing orders: "BankPilot kann keine
  Überweisungen ausführen."
- No creating, editing or deleting rules, categories or connections: these
  are done in the BankPilot app (Regeln / Bankverbindungen tabs).
- No bank credentials, IBANs beyond what a row shows, or data of other
  people.
- Questions unrelated to the user's payments do not use BankPilot at all.

See `references/tools.md` for the exact tool arguments and result fields.
