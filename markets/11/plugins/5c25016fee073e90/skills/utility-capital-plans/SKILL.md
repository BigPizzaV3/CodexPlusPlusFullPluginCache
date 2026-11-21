---
name: utility-capital-plans
description: Answer questions about water utility capital improvement plans (CIPs) and planned capex — "which utilities have the biggest capital plans in Texas", "what is Houston planning to spend on water treatment", "find planned reservoir projects in California", "how has this project's cost changed" — using the Water Investment Navigator MCP capital-plan tools.
---

# Utility capital plans

Use the `water-investment-navigator` MCP tools. A capital plan (CIP) is a utility's published
multi-year budget of planned projects. **CIP amounts are planned spending, not
awarded contracts or money spent.** Don't present them as wins or as actuals.

## Which tool

| Question | Tool |
|---|---|
| Rank/screen utilities by planned capex | `latest_capex(state=..., min_total_musd=...)`: one row per utility, its newest plan |
| All plans for a utility, or older vintages | `capital_plans(utility_id=..., latest_only=false)` |
| One plan's totals, sector split, funding | `get_capital_plan(file_id, spending_group_by="sector")` |
| Projects in one plan | `capital_projects(file_id=..., sort="total_desc")` |
| Projects across utilities | `capital_projects(q=..., state=..., sector=..., min_total_musd=...)`: newest plan per utility by default |
| One project, cost drift, linked decisions | `get_capital_project(cip_id)` |

## Reading the numbers

- Every `*_musd` field is **millions of USD** (`source_currency` shows what the
  plan was published in).
- A plan covers `cip_start_year`–`cip_end_year`. `spending.by_year` is the
  yearly profile; `prior_years_musd` is spend before the window and
  `future_years_musd` is spend after it. Say which of these your total includes.
- `expenditure_status` (e.g. Ongoing, Complete) and `new_in_cip` flag
  whether a project is new in this vintage.
- `get_capital_project` → `versions` is the same asset across plan vintages. Use
  it for "how has the cost/timing changed". `decisions` lists the governing-body
  decisions linked to the project, which is the bridge from planned to awarded
  (use the water-contract-research skill from there).
- For what the board said about a planned project (estimate, delivery method,
  schedule, funding), `search_documents(q="<project name>", utility_id=...)`
  searches the meeting packets and transcripts (see the
  meeting-documents-and-transcripts skill).
- Plans are published at different times, so comparing utilities means
  comparing different plan years. Mention `publication_year` when ranking.

Cite the plan with its `file_name`, `publication_year` and `documentlink`
(a public link to the source PDF).

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
