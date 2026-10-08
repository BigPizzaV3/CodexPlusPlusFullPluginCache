---
name: ask-embat
description: Answer questions about the user's own live treasury and finance data in Embat — cash position, account balances, bank fees, debt schedules, WACD, cash forecasts and scenario variance, payables and payment batches, journal entries, reconciliations, PSP reconciliation (Stripe, Adyen, Redsys, PayPal), intercompany balances and interest, users, roles and automation rules. Use whenever the user asks about their company's or group's financial position, payments, debt, accounting or forecasts. Read-only — it cannot execute payments, post entries, approve batches or change configuration. Do not use for general finance theory, public market data, or companies other than the user's own.
---

# Ask Embat

Embat is a treasury management platform. This skill queries the signed-in user's
own Embat data through the `ask_tellme` MCP tool, which routes each question to
a supervisor agent and eight domain specialists.

## When to use

Use this skill whenever the question concerns the user's own financial data in
Embat. Typical triggers by domain:

| Domain | Ask about |
|---|---|
| **Cash** | Cash position, account balances, bank fees, transactions, balance movements, bridge analysis, abnormal movements |
| **Debt** | Debt schedules, loan terms, WACD / cost of debt, amortization, drawdowns, repayments, maturities, interest costs, credit line headroom |
| **Treasury forecasting** | Cash forecasts, forecasted position on a future date, forecast-vs-actual variance, scenarios and projections, drill-downs, cash risks, unexpected transactions, client billed volume |
| **Payments** | Payables, invoices to pay, payment batches, approval status, pre-funding transfers, payment orders, rejected payments, supplier payment history, failure reasons |
| **Accounting** | Journal entries, settlements, pending postings, reconciliations, chart of accounts, GL accounts, ERP sync, single-transaction status trace |
| **PSP reconciliation** | Stripe, Adyen, Redsys, PayPal; reconciliation bundles, order-to-transaction matching, unmatched items, manual vs automatic matches, PSP connection health |
| **Intercompany / In-House Bank** | Relation balances between group entities, accrued and paid interest, netting and settlement proposals, interest income/expense by entity |
| **Settings & automation** | Users, roles and permissions, category tree, automation rules (errored / stale / affecting accounting), approval flows, dashboards, widgets, scheduled reports |

## When not to use

- General finance, accounting theory or "how does treasury work" questions.
- Public market data, FX rates or benchmarks not held in the user's Embat account.
- Any other company's data — the tool only ever sees the signed-in user's own
  group, scoped by their Embat permissions.
- Requests to **change** anything (see the read-only boundary below).

## How to call it

Pass the user's question through essentially verbatim as `query`. Do not
decompose it into sub-questions or pre-translate it — the supervisor handles
routing, multi-domain fan-out (e.g. liquidity = cash balances + credit
headroom) and language detection itself. `query` is the only parameter;
conversation continuity is bound to the MCP session automatically, so
follow-ups like "and last month?" work without passing any thread identifier.

The tool answers in the user's own language.

## What to expect back

A text answer plus `structuredContent` carrying the rendered `components` and
the `tool_calls` the agent made. Relay the answer as given; don't recompute
figures from the components.

Two clarifying behaviours are **correct and expected** — relay them to the user
rather than guessing:

- **Scope selectors.** The agent may ask which companies a rule or query
  applies to. Answering it ("only Acme SL", "all companies in my group") is the
  second step of the same request, not a new one.
- **Projection picklist.** For a forecast question when more than one scenario
  exists, the agent asks the user to pick one. Dates, companies and currencies
  have safe defaults and are never asked about.

## Read-only boundary

`ask_tellme` is annotated `readOnlyHint: true` / `destructiveHint: false`. It
looks up and analyses data; it cannot post journal entries, make or approve
payments, create, edit or delete records, change configuration, or connect
integrations. If the user asks for one of those, say it must be done in the
Embat app.

One nuance worth knowing: the agent *can* record "customization contexts" —
recurring instructions the user teaches it, such as how a class of transactions
should be matched or which payables to discard. These change the assistant's
future behaviour, not any Embat record, which is why the tool remains read-only.

## Authentication

The connector uses OAuth; the tool resolves the user's identity and Embat
permissions from their token on every call. If the user sees a message about
verifying access, they should reconnect the connector.
