---
name: water-contract-research
description: Answer questions about what US water/wastewater utilities decided, awarded or approved, and which companies won or bid — "who won X", "what has firm Y won", "what did utility Z approve", competitor win/loss tracking. Uses the Water Investment Navigator MCP tools and cites the source meeting documents.
---

# Water contract research

Use the `water-investment-navigator` MCP tools. The data is decisions taken by utility governing
bodies (boards, councils, commissions), extracted from their agendas, minutes and
meeting video, with companies attributed to the contract events in each decision.

## Workflow

1. **Resolve the entities first.**
   - Utility named → `find_utilities(q=...)` to get `utility_id`. Several rows can
     match (a city and its water department); pick the one whose name fits the
     question, or say which you chose.
   - Company named → `find_companies(q=...)` to get `company_id`. Joint ventures are
     separate companies (e.g. "Florida Water Partners (Garney / Wharton-Smith)");
     include them when the question is about a parent firm, and say you did.
2. **List candidates.** `search_decisions` with the ids and filters (`state`,
   `date_from`/`date_to` by publication date, `min_value_millions`,
   `decision_type`), or `company_decisions(company_id)` for a firm's history.
   Follow `next_cursor` until you have the whole window; don't answer "all of X"
   from the first page.
3. **Read before you claim.** For each decision you report,
   `get_decision(decision_id, include=["companies","bid_tabulations","documents"])`.
4. **Quote the source** for any number or winner you state:
   `get_decision_source_text(decision_id)` gives the verbatim agenda/minutes text.
5. **Look inside the documents** when the decisions do not answer the question
   (what was said in the debate, a firm that only a transcript names, a page of
   a packet):
   - `search_documents(q, utility_id)` finds words on the pages of agendas,
     packets, minutes, staff reports and video transcripts. Each hit has a
     snippet, the `resource_id`, the page and a `document_url` for that page.
   - `list_meetings(utility_id)` lists every meeting with its documents, also a
     meeting with no decision yet. `get_meeting(meeting_id)` adds its decisions.
   - `get_document_text(resource_id, start_page, end_page)` reads the pages;
     follow `next_page` for a whole transcript.
   - A transcript is machine speech-to-text with no speaker names. Say when a
     quote is from the transcript, and check names and numbers against the
     packet or minutes.

## Reading the fields correctly

- `decision_type` is one of: Contract Awards, Contract Amendment, Capital Projects,
  Finance, Operations & Maintenance, Presentation/Report, People, Procedural, Other.
  Only Contract Awards / Contract Amendment are contract actions. A
  Presentation/Report decision with a big number is usually a plan or study, not
  money awarded.
- A company's `role` says what it did: `contractor`, `consultant`, `engineer`,
  `vendor`, `supplier`, `cmar`, `design_build`, `subcontractor`, `recipient` —
  and **`bidder`, which means it bid, not that it won.** For who won, look for
  a winning role or `is_winner` on the bid tabulation rows.
- `event_type` separates awards (`award`, `bid_award`, `task_order`, `gmp_set`)
  from `amendment`, `change_order`, `scope_change`, and from money that is not a
  won contract: `opex_payment`, `intergov_payment`, `finance_payment`,
  `financing`, `grant`, `acquisition`. `award_unverified` is a lower-confidence award.
- `evidence_role`: `final_vote` means the body acted on it in this decision;
  `reference` means the decision only mentions an earlier action.
- Money: `value_millions` is **millions of USD** and is null when the source
  gave a range or no figure. `delta_value` on a company event is in whole units
  of `value_currency`.
- Joint awards: when several firms share an award with no stated split, each
  firm is shown with the full value. Never add those across firms, and don't
  total a firm's wins across a JV and its members without saying so.
- `get_company` totals (`total_committed_value`) exclude opex payments.

## Answer format

Lead with the answer. For each decision: utility, date, what was approved, value,
winner/bidders, and a one-line quote from the source text. Say when data is
thin (few decisions, no bid tab) rather than filling the gap. The data refreshes
daily around 09:15 UTC and can change as quality review runs.

After the text, show the source once: `show_decision_source(decision_id)` when
the answer rests on one decision, or `show_decision_list(decision_ids, title)`
for 2 to 10 decisions, in the order of your answer. Never call both.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
