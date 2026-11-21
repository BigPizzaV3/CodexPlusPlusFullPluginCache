---
name: competitor-intelligence
description: Profile a contractor, engineer or supplier in the US municipal water market — "what has Kiewit won this year", "where does Garney work and who do they lose to", "who beats us in Texas", "which firms win CMAR and progressive design-build work", "is firm X active at utility Y", win/loss and head-to-head analysis. Uses the Water Investment Navigator MCP company, decision, bid tabulation and document search tools.
---

# Competitor intelligence

Use the `water-investment-navigator` MCP tools. Build the picture of one firm (or a head-to-head
between firms) from three layers: what it **won**, what it **bid and lost**, and
where it is **named in the documents** before any award exists.

## Workflow

1. **Resolve the firm.** `find_companies(q=...)`.
   - Take every row that is the same firm: a parent, its regional entities and
     its **joint ventures** are separate companies ("Garney Construction",
     "Florida Water Partners (Garney / Wharton-Smith)"). Say which you included.
   - `unlisted_firms` in the same result lists firms with awards but no
     `company_id` (smaller firms, some JVs), with totals and their latest
     awards. Use those rows directly; there is no `company_decisions` for them.
2. **Wins.** `company_decisions(company_id, role="awarded", date_from, date_to)`.
   - The first page carries `totals` over **all** matching decisions (won value,
     new awards vs amendments, decision count). Use `totals` for "how much";
     do not page through every decision to add them up.
   - Add `state` or `utility_id` to cut by geography or client. `sort="value"`
     puts the largest first.
3. **Losses and rivals.** `company_decisions(company_id, role="bidder")` lists
   bids that did not win. For each one that matters,
   `get_decision(decision_id, include=["bid_tabulations","companies"])` shows
   every bidder, the amounts, and `is_winner`. Count who won against the firm
   and by what margin: that is the head-to-head.
4. **Market view (no firm named).** `search_decisions(state=..., date_from=...,
   min_value_millions=..., sort="value")`: the first page carries
   `top_companies` (firms ranked by won value over all matching decisions) and
   each row carries `awarded_companies`. Use it for "who wins the most in X".
5. **Early presence.** `search_documents(q="<firm name>", utility_id=... or
   state=..., date_from=...)` finds the firm on pages with no award yet: a
   shortlist, a presentation, a design contract that precedes construction, a
   council member naming the firm in debate (`document_type="transcript"`).
   Read around a hit with `get_document_text`.

## Reading it correctly

- `company_role` on each row says what the firm did. **A `bidder` row is not a
  win.** Winning roles: `contractor`, `consultant`, `engineer`, `vendor`,
  `supplier`, `cmar`, `design_build`, `subcontractor`, `recipient`.
- Joint awards with no stated split show the full value on each firm. Never add
  those across firms, and say so when a firm's total includes JV awards.
- Amendments and change orders are money on an existing contract, not a new
  win. Report new awards and amendments apart (the `totals` do).
- Delivery method (CMAR, progressive design-build, design-bid-build) is in the
  decision text and the staff report, not a field. Confirm it with
  `get_decision_source_text` or `search_documents` before you classify a win.
- Coverage is the utilities and meetings in the dataset. "No wins found" means
  none in this data, not none in the market. State the window and geography.

## Answer format

Lead with the headline (won value, number of awards, window). Then a short
table: utility, date, project, value, role, `document_url`. Then rivals (who
won when this firm lost), then early signals from the documents. Mark anything
that comes from a transcript.

After the text, call `show_decision_list(decision_ids, title)` once with the
decisions of the table (at most 10, in table order), so the user can open each
source page.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
