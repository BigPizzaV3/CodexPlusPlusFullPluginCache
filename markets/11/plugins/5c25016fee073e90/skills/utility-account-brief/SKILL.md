---
name: utility-account-brief
description: Prepare an account brief on one water, wastewater or stormwater utility before a meeting, a proposal or a territory review — "brief me on Miami-Dade Water and Sewer", "what is this utility spending on and who works for it", "what has their board approved lately", "who are the incumbents", key-client planning. Uses the Water Investment Navigator MCP utility, capital plan, decision, company, article and meeting tools.
---

# Utility account brief

Use the `water-investment-navigator` MCP tools. The brief answers five questions about one
owner: what it plans to spend, what it has just approved, who works for it now,
what is coming to market, and what its board is talking about.

## Workflow

1. **Resolve the utility.** `find_utilities(q=..., state=...)`. A city and its
   water department can be separate rows; pick the row with decisions and a
   capital plan, and say which you used.
2. **Planned spending.** `latest_capex(q="<utility name>")` for the newest plan
   total and yearly profile; `get_capital_plan(file_id, spending_group_by="sector")`
   for the split; `capital_projects(file_id=..., sort="total_desc", limit=10)`
   for the largest projects. Planned spending, not awards.
3. **Recent approvals.** `search_decisions(utility_id=..., date_from=<12 months
   ago>, sort="value", limit=20)`: the largest items first, so ceremonial items
   do not crowd out contracts. The first page also carries `top_companies`
   (who won the most here) and `open_bids`.
4. **Incumbents.** From `top_companies` and each row's `awarded_companies`,
   name the engineer(s), contractors and suppliers with repeat work. For a firm
   that matters, `company_decisions(company_id, utility_id=...)` shows its
   history with this owner and `totals`.
5. **Coming to market.** The `open_bids` from step 3; the large CIP projects of
   step 2 with spending in the next two years and no construction award yet;
   and `search_documents(q='advertise OR solicitation OR "request for
   qualifications"', utility_id=..., date_from=<6 months ago>)` for items the
   board has been told are coming.
6. **What the board is talking about.** `search_articles(utility_id=...,
   limit=5)` gives our summary of the latest meetings (an article is a summary,
   not a source: cite the decisions it covers). `list_meetings(utility_id,
   limit=5)` shows the latest meetings and which documents we hold; search the
   newest transcript for the user's topic when they named one.

## Answer format

One page, in this order: **Snapshot** (utility, state, newest plan total and
window) · **Capital plan** (top projects, sector split) · **Recent approvals**
(top items with value, firm and `document_url`) · **Who works here** (firms and
roles) · **Coming to market** (open bids, planned projects not yet awarded) ·
**Board themes** (two or three, each with a dated source). State the date
window of every number, and say where the data is thin (few meetings, no
capital plan, no transcripts).

After the brief, call `show_decision_list(decision_ids, title)` once with the
decisions of **Recent approvals** (at most 10), so the user can open each
source page.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
