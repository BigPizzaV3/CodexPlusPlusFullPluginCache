---
name: legisratio-research
description: Discover relevant Italian/EU laws, court judgments, and secondary regulation by topic via LegisRatio MCP search. Use when finding which sources exist on a fact pattern or legal question for a memo or opinion; not for fetching text of an already-known ID.
license: MIT
metadata:
  version: "0.1.0"
---

# LegisRatio Research Skill

Find which Italian/EU legal documents are relevant to a question, using the LegisRatio MCP search tools. This skill answers "what exists on this topic" — picking up specific texts and judgments belongs to `legisratio-law-text` and `legisratio-caselaw`.

See [research-brief prompt](references/research-brief.md) for a ready-to-use first-pass memo workflow.

## When to Use

- User asks to find laws, articles, court judgments, or secondary regulation on a topic or fact pattern
- Building the starting set of sources for a legal opinion, memo, due-diligence, or compliance check
- Don't use for: retrieving a specific known law/article/judgment by ID (use the text/caselaw skills)

## Prerequisites

- LegisRatio MCP server connected and available to the agent. Tool names below are the base MCP tool names; depending on the MCP client they may appear with a prefix (e.g. `mcp_legisratio_hybrid_search`).

## How to Run

The agent calls the MCP tools directly. Run the searches, then synthesize.

## Procedure

1. Identify the document type(s) the question targets.
2. Search legislation: call `hybrid-search` with `searchString` = the topic/phrase. Set `k` ~80 (recommended for coverage; max 100). Add `levels` to widen from default `['EU','National']` to regions as needed (e.g. `['RegionalLombardia']` for a Lombardy question; `RegionalAll` only when spanning all regions).
3. Search case law: call `judgment-search` with `searchString`. Narrow with `startDate` (YYYY-MM-DD) and `section` (e.g. `CASSAZIONE_CIVILE`, `TAR_LAZIO`, `CORTE_GIUSTIZIA_UE`). `k` defaults 100.
4. Search secondary regulation: call `secondary-act-search` with `searchString`, `entity` as an array (e.g. `['Bankitalia']` or `['Consob','IVASS']`), `k` high, optional `articleOfLaw` reference.
5. Report sources grouped by type, each with its stable ID for follow-up retrieval.

## Pitfalls

- `levels` and `entity` are arrays — pass them as lists or the call fails.
- `entity` values are case-sensitive: use `Bankitalia`, `IVASS`, `Consob`, `CCNL`, `EDPB`, `ConsiglioNotarile` (lowercase 'ob' in `Consob` — the tool's own description shows the wrong capitalization and errors out with `-32602`).
- Default search scope is EU + National only; regional law requires explicitly adding regional `levels`.
- Search results give IDs in `YEAR|NUM` / `SENTENZA-CASS:...` form — hand those to the text/caselaw skills, don't retype from memory.
- Query phrasing decides relevance: state the topic in 2–4 concrete terms tied to the actual question (object, sector, transaction), not a generic doctrinal phrase and not a full sentence. "non concorrenza lavoratore" hits art. 2125 c.c.; "patto di non concorrenza del lavoratore codice civile" and the broad "adempimento obbligazioni" both returned off-topic laws. If the first pass lands off-topic, re-search with the concrete fact-words of the query. 

## Verification

- Every source you cite was returned by a real search call and carries an ID you can pass to a text-retrieval tool (`get-law-text`, `get-article-text-by-id`, `get-judgment-text`, `get-secondary-act`) to fetch the authoritative text.
