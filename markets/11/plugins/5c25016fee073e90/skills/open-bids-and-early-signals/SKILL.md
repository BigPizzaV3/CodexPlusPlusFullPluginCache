---
name: open-bids-and-early-signals
description: Find work that is not yet awarded in the US municipal water market — open solicitations and the earlier signs of a procurement — "what water treatment bids are open in Texas", "which utilities are about to bid a pump station", "find projects going to CMAR or progressive design-build", "what is coming to market in the next year", "who is planning a rebid". Uses the Water Investment Navigator MCP search, bid, capital plan and meeting document tools.
---

# Open bids and early signals

Use the `water-investment-navigator` MCP tools. Work reaches the market in stages, and each
stage shows up in a different place. Say which stage each item is at; do not
call a planned project an opportunity to bid, or a discussion a commitment.

| Stage | Where it shows | Tool |
|---|---|---|
| In a capital plan, years away | CIP project with future spending | `capital_projects` |
| Design or study under way | design / study contract decisions | `search_decisions` |
| Board told a procurement is coming | staff reports, transcripts | `search_documents` |
| On the street | open solicitation | `search` → `bid:<id>`, `fetch` |
| Bids in, award pending or rejected | bid tabulations, debate | `get_decision`, `search_documents` |

## Workflow

1. **Open solicitations.** `search(query="<work type> <place>")` returns open
   bids as `bid:<id>` beside decisions and CIP projects. `fetch("bid:<id>")`
   gives the due date, pre-bid meeting (and whether it is mandatory), question
   deadline, estimated value and the link to the solicitation. With a utility,
   `search_decisions(utility_id=...)` lists `open_bids` on its first page.
   Sort what you report by due date and drop anything already past due.
2. **Told to the board.** `search_documents` finds the pages where staff or the
   board say a procurement is coming. Useful queries (add `state`, or
   `utility_id`, and `date_from` of the last 3-6 months):
   - `"request for qualifications" OR "request for proposals"` plus a work word
   - `"authorization to advertise" OR "advertise for bids"`
   - `"progressive design-build"`, `"construction manager at risk"`, `CMAR`,
     `"guaranteed maximum price"`
   - `rebid OR "reject all bids"` (a failed procurement usually returns)
   - `"engineer's estimate"` plus the project name
   Without `utility_id` a common phrase can come back partial
   (`matches.capped` true): narrow it and say so. Read around a hit with
   `get_document_text` before you report it.
3. **Planned, not yet bought.** `capital_projects(q=..., state=...,
   min_total_musd=..., covers_year=<next year>)` finds funded projects with
   spending ahead. `get_capital_project(cip_id)` shows yearly spending and
   linked `decisions`: a design award with no construction award is the
   classic lead. CIP amounts are planned spending.
4. **Design awards that lead to construction.** `search_decisions(q="design",
   state=..., date_from=<18 months ago>, min_value_millions=..., sort="value")`:
   a large design or owner's-advisor contract names the construction work
   that follows and often its delivery method.

## Reading it correctly

- A decision that awards the work is closed. A decision that selects a
  shortlist, approves a budget, executes a grant or buys land for a project is
  still open work.
- Work that another party will buy (a developer, a state DOT, another agency)
  is not the utility's procurement.
- A statement in a transcript ("we will rebid in the spring") is an intention.
  Report it with its date and say it is from a transcript.

## Answer format

A table, soonest first: utility, state, project, stage, value (and what kind:
estimate, planned, bid), next date (due date, pre-bid, expected advertisement),
and the `document_url` or solicitation link. Then two or three lines on what to
watch. State the geography and window you searched.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
