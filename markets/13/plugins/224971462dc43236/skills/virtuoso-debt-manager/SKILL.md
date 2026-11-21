---
name: virtuoso-debt-manager
description: Route debt, loan, collateral, covenant, and hedge questions to Yardi Virtuoso Debt Management (yardi-virtuoso) MCP tools. Use this skill whenever someone asks about loans, loan balances, maturity dates, borrowers, lenders, collateral, LTV, NOI, occupancy, covenants, reminders, hedges, interest rate caps, swaps, or any debt portfolio data. Also trigger when the user mentions "asset loan", "liability loan", "line of credit", "capital stack", "syndication", "SOFR", "rate table", "funding status", "debt analytics", "adhoc debt report", or "debt dataset". Do NOT use for vendor/payables data (use P2P Manager), GL financial reports (use GL Manager), or property KPIs (use Performance Manager).
---

# Virtuoso Debt Manager

Routes debt portfolio questions to Yardi Virtuoso's Debt Management tools via the
**yardi-virtuoso** connection, authenticated with OAuth dynamic client registration.

## Tool Map

| Domain | Search tool | Column catalog | Detail tool |
|--------|------------|----------------|-------------|
| Loans | `dmx_loan_search_loans` | `dmx_loan_search_loans_columns` | `dmx_loan_get_loan_details` |
| Collateral | `dmx_collateral_search_collateral` | `dmx_collateral_search_collateral_columns` | — |
| Covenants | `dmx_covenant_search_covenants` | `dmx_covenant_search_covenants_columns` | — |
| Hedges | `dmx_hedges_search_hedges` | `dmx_hedges_search_hedges_columns` | — |
| Debt analytics | `dmx_debtadhoc_debt_search_query` | `dmx_debtdataset_get_debtdataset_config` | — |

**Column catalog tools** — call the matching `_columns` tool before adding a `Columns`
parameter you haven't used before; invalid column names silently drop data.

---

## Data Model

`search_loans` is the **spine** of the debt data model. Every collateral record, covenant,
and hedge is linked to a loan via a shared loan code. The enrichment tools return
domain-specific detail that `search_loans` does not carry:

| Tool | What it adds that `search_loans` doesn't have |
|------|------------------------------------------------|
| `search_collateral` | Property-level values, occupancy %, NOI, LTV inputs |
| `search_covenants` | Compliance reminders, due dates, status, assigned users |
| `search_hedges` | Hedge type, counterparty, notional, termination date |
| `debt_search_query` | **Historical and point-in-time values** (month granularity). The only tool that can answer date-specific or comparative questions. Results link to other tools via loan code. |

Use the loan code returned by `search_loans` to join or correlate results across tools
when presenting combined data to the user.

---

## Default Query Strategy

1. **If the question involves a specific date, a historical value, or a comparison across
   time periods — route to `debt_search_query` first.** It is the only tool that returns
   data as of a point in time (month granularity). All other search tools reflect current
   values only. Examples that trigger this path:
   - "What was the balance in January 2024?"
   - "Compare our debt exposure this year vs last year"
   - "How has the balance changed over the last 6 months?"
   Always call `get_debtdataset_config` before `debt_search_query` to get valid
   `dataset_Id` and `measures` values — never guess them.
   If not all measures or columns are found in this tool start with the `search_loans` tool to 
   find additional detail using the loan code to link the data

2. **For current-state questions, start with `search_loans`** to establish the loan
   universe. It covers the majority of what users need: balances, parties, maturity,
   rate, and status.

3. **Call an enrichment tool only if the user's question requires detail that
   `search_loans` cannot provide** — collateral metrics, covenant compliance, or hedge
   exposure. Do not call enrichment tools speculatively.

4. **Correlate on loan code** when combining results across tools. The loan code is the
   common key across `search_loans`, `search_collateral`, `search_covenants`,
   `search_hedges`, and `debt_search_query`.

5. **For a single loan**, call `get_loan_details` instead of an enrichment tool when the
   user just wants "everything about this loan" — it returns the fullest single-loan
   payload without requiring a join.

---

## Routing & Sequencing

**Loans — list or filter**
→ `search_loans` (defaults: `LoanStatus: "0"`, `SyndicationType: "2"`, `FundingStatusTypes:"funded","default"`)

**Loans — single loan detail**
→ `search_loans` to get the integer `id` → `get_loan_details`

**Collateral / LTV / occupancy / NOI**
→ `search_collateral` (`LoanTypeFilter` is required)

**Covenants / compliance / reminders**
→ `search_covenants`

**Hedges / rate caps / termination dates**
→ `search_hedges`

**Debt metrics over time or as of a date**
→ `get_debtdataset_config` first (never guess `dataset_Id` or `measures`) → `debt_search_query`

---

## Business Rules

- **`LoanStatus`** defaults to `"0"` (Active). Ask only if the user wants inactive or all.
- **`SyndicationType`** defaults to `"2"` (Whole Loans) to avoid double-counting.
- **`FundingStatusTypes`** defaults to `"funded, default"` unless the user specifies otherwise.
- **Name filters** (`LenderIds`, `BorrowerIds`, `EntityIds`, `PropertyList`) use built-in
  autocomplete — pass plain names like `"Wells Fargo"`, never raw IDs.
- **`get_loan_details`** requires an integer `id` from a prior `search_loans` call.
- **`debt_search_query` charts** must use Chart.js (vanilla JS) only — no recharts, no D3.

---

## Presentation Guidelines

- Lead with portfolio totals (count, aggregate balance, nearest maturity), then detail.
- Proactively flag risk: maturities within 90 days, past-due covenants, expiring hedges.
- For time-series results (3+ periods), prefer a Chart.js bar or line chart over a raw table.
- Cite Yardi Virtuoso as the data source.
