---
name: project-pursuit-brief
description: Build a pursuit brief on one water or wastewater project — "tell me everything about the Northside wastewater treatment plant expansion", "where does this project stand and who is involved", "what is the budget, schedule and delivery method", "who is the engineer and who bid", go/no-go research for a contractor, engineer or supplier chasing a specific plant, pipeline or program. Uses the Water Investment Navigator MCP capital plan, decision, bid, meeting document and transcript tools.
---

# Project pursuit brief

Use the `water-investment-navigator` MCP tools. One project leaves traces in four places: the
capital plan (budget and timing), the decisions (contracts already placed), the
documents and transcripts (scope, estimates, delivery method, politics) and the
open bids (what is on the street now). A brief joins them in date order.

## Workflow

1. **Utility and project names.** `find_utilities(q=...)` for `utility_id`.
   Note the names the owner uses for the project (a plant name, a program
   name, a project number): each source spells it differently.
2. **Budget and timing — the capital plan.**
   `capital_projects(q="<project words>", utility_id=...)`, then
   `get_capital_project(cip_id)`: total planned cost, yearly spending, funding,
   `versions` (the same project in earlier plans: cost growth, slipped years)
   and linked `decisions`. CIP amounts are **planned**, not awarded.
3. **Contracts already placed — the decisions.**
   `search_decisions(q="<project words>", utility_id=..., sort="date")`.
   Read each relevant one with
   `get_decision(decision_id, include=["companies","bid_tabulations","documents"])`:
   the engineer, owner's representative, CMAR or design-builder, amendments,
   bid tabulations with every bidder and price, rejected bids, terminations.
4. **The story behind the votes — documents and transcripts.**
   `search_documents(q="<project name or a distinctive word>", utility_id=...)`
   and again with `document_type="transcript"`. Look for: the engineer's
   estimate, the delivery method and why it was chosen, schedule drivers
   (consent decree, permit, funding deadline), funding (SRF, WIFIA, bonds,
   rates), bid results and what the body said about them, a planned rebid,
   packaging into phases. Read around each hit with `get_document_text`.
5. **What is open now.** `search(query="<project words>")` returns open
   solicitations as `bid:<id>`; `fetch("bid:<id>")` gives the due date, pre-bid
   meeting, estimate and link. `search_decisions` with `utility_id` also lists
   `open_bids` on its first page.
6. **Latest position.** `list_meetings(utility_id, date_from=<90 days ago>)`
   and search the newest meetings (`meeting_id`) for the project, so the brief
   ends with the most recent thing said, not the most recent award.

## What the brief contains

1. **Snapshot** — owner, project, scope in one line, planned cost, stage.
2. **Timeline** — dated events, oldest first, each with its `document_url`.
3. **Money** — planned (CIP), estimated (engineer's estimate, if stated),
   awarded so far, bid results. Keep the four apart; never present a planned
   amount as a contract.
4. **Who is on it** — firms and roles, with the decision that placed each.
5. **Delivery and procurement** — method, packages, what is awarded, what is
   still to buy, any open or expected solicitation.
6. **Risks and signals** — cost growth between plan versions, rejected bids,
   terminations, funding gaps, board disagreement (quote the transcript and say
   it is a transcript).
7. **Gaps** — what the data does not show (no packet for a meeting, no
   transcript, no bid tab). An honest gap is more useful than a guess.

After the brief, call `show_decision_list(decision_ids, title)` once with the
decisions of the **Timeline**, oldest first (at most 10). When the project has
only one decision, call `show_decision_source(decision_id)` instead.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
