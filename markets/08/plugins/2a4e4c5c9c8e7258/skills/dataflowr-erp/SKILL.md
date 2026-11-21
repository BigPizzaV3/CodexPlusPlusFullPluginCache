---
name: dataflowr-erp
description: How to work in an Exact Online administration through the DataFlowr MCP server — resolving the division, choosing between the reporting tools and raw ledger tools, staying inside the query guardrails, and confirming before anything is written. Use whenever a request touches bookkeeping figures, customers, suppliers, invoices, VAT, projects or assets.
---

# Working in Exact Online through DataFlowr

## Overview

DataFlowr exposes one Exact Online administration as MCP tools. Reads are safe to
run; writes create real records in a live administration.

Tool names below are the MCP names. Your client may show them with a server
prefix (`mcp__…__exact_online_divisions`) — same tools.

## Resolve the division first

Almost every tool takes a `division`. It is Exact Online's internal division
**Code**, which is not the number users see.

1. Call `exact_online_divisions` before anything else.
2. Match on the company name or the HID the user mentions — never guess a Code.
3. One division? Use it without asking. Several and the request is ambiguous?
   Ask which company they mean.

## Reach for the reporting tools before the ledger

The reporting tools aggregate server-side against the RGS template tree and
return far less data than pulling lines yourself:

- `financial_report` — trial balance / balance sheet / P&L, with prior-year and
  budget columns.
- `financial_period_report` — the same figures per period, for trends.
- `financial_gl_data` — RGS-scoped GL aggregates. Use it as a **pre-check**
  before any line-level pull, to find out which accounts are worth opening.
- `financial_drilldown` — the transactions behind a report line.
- `financial_kpis`, `financial_query` — ratios and ad-hoc questions over the
  same tree.

Only drop to `exact_online_transaction_lines` and friends when you need
individual postings that a report line cannot answer.

## Query guardrails

These are enforced server-side; hitting them is a failed call, not a slow one.

- `exact_online_transaction_lines` must filter on **both** `FinancialYear` and
  `FinancialPeriod`. A year-only filter is expanded into per-period calls.
- Year and period field names differ per entity and are preserved verbatim:
  `ReportingYear`/`ReportingPeriod` on purchase and sales entries,
  `FinancialYear`/`FinancialPeriod` on transaction lines and bank, cash and
  general journal entries, `FinYear`/`FinPeriod` on financial periods.
- There is no `_get`: fetch a single record with `_list` plus an ID filter.
- Ask for the fields you need. Wide entities have a trimmed default `$select`;
  widening it costs bandwidth on every row.

## Before you write

Creates and updates hit the live administration.

1. Validate the required fields — the tool schema lists them.
2. Echo a plain-language summary of the draft (who, what, how much, which
   division) back to the user.
3. Wait for an explicit "yes". Never chain a write off an assumption, and never
   batch several writes behind one confirmation.

## Answering

State the figures you retrieved, name the period and the administration they
came from, and say when a number could not be tied out. Never compute a
financial figure from memory or fill a gap with a plausible-looking value — if a
call failed, say so.
