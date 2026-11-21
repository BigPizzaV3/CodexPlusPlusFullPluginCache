---
name: win-intelligence
description: General guide to the Water Investment Navigator MCP tools for questions about US municipal water and wastewater investment — utilities, capital plans, projects, governing-body decisions, contract awards, companies, unit prices, open bids, meeting documents and transcripts. Use when no more specific skill fits, or to choose one.
---

# Water Investment Navigator: general guide

Use the `water-investment-navigator` MCP tools. The data comes from the governing-body
meetings of US water, wastewater and stormwater utilities (agendas, packets,
minutes, video transcripts) and from their capital improvement plans.

## Pick the route

| The user asks about | Start with | Skill |
|---|---|---|
| Who won, what was approved, a firm's awards | `search_decisions`, `company_decisions` | water-contract-research |
| A firm against its rivals, win/loss | `find_companies`, `company_decisions` | competitor-intelligence |
| One project, end to end | `capital_projects`, `search_decisions`, `search_documents` | project-pursuit-brief |
| One utility, before a meeting | `latest_capex`, `search_decisions` | utility-account-brief |
| Work not yet awarded, open bids | `search`, `search_documents`, `capital_projects` | open-bids-and-early-signals |
| What was said or written in a meeting | `search_documents`, `get_document_text` | meeting-documents-and-transcripts |
| Planned capital spending | `latest_capex`, `capital_plans` | utility-capital-plans |
| Unit costs | `pricing_benchmarks` | water-pricing-benchmarks |

## Rules that apply everywhere

- Resolve names to ids first: `find_utilities` for `utility_id`,
  `find_companies` for `company_id`.
- Keep four kinds of money apart: **planned** (capital plan), **estimated**
  (engineer's estimate), **bid** (a tabulation row) and **awarded** (a contract
  decision). Say which one each number is.
- Keep decided, discussed and proposed apart. A decision record is what the
  body acted on; a transcript is what was said.
- Cite each fact with the `document_url` of its decision or page. An article
  (`search_articles`) is our summary of a meeting, not a source.
- Show the source once, after the text: `show_decision_source(decision_id)`
  when the answer rests on one decision; `show_decision_list(decision_ids,
  title)` for a list or comparison of 2 to 10 decisions. Never call both, and
  not for capital plans, prices or open bids.
- State the geography and the date window of every list and total. An empty
  result means "not in this data"; say what you searched.
- Ids are strings of digits. Pass them back exactly as returned.
- Lists page with `next_cursor`. Use the totals a tool gives (`totals`,
  `top_companies`) instead of paging through every record to add them up.

## Usage limits

- An account can have daily and monthly limits on records, source texts
  (`get_decision_source_text`, `get_document_text`) and document downloads.
- When the user asks how much they have used or have left, call `usage`. It is
  free. Report each limit with the amount used, the amount left and the reset
  time (UTC).
- When a result has a `quota_notice` field, tell the user once that they are
  near a limit. An error that starts with `429 quota_exceeded` means a limit is
  reached: say which limit and when it resets, and do not retry before then.

## Style

Be concise, commercially useful and factual. Lead with the answer, then the
evidence. Say when the data is thin instead of filling the gap.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
