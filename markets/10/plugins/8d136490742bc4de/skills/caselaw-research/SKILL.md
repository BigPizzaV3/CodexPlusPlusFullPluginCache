---
name: caselaw-research
description: Search U.S. federal and state caselaw in LawDiver with a required jurisdiction, then summarize hits with real citations and good-law flags. Use when the user wants case research, case law search, or authorities on a legal issue. Do not use for non-legal web search, drafting filings, or inventing citations.
---

# Caselaw research (LawDiver)

Use LawDiver MCP tools only. Never invent case names, citations, holdings, or good-law status.

## When to use

- User asks to find cases on an issue, doctrine, or fact pattern
- User wants jurisdiction-scoped caselaw (state, circuit, SCOTUS, federal, etc.)
- User asks “what cases say about …” or “search caselaw for …”

## Steps

1. If jurisdiction is missing or ambiguous, ask once for the court scope (e.g. California state, Ninth Circuit, all federal). Do not run an unscoped national search.
2. Call `list_jurisdictions` only when the user needs help choosing a jurisdiction code.
3. Call `search_cases` with:
   - `query`: the user’s legal issue in plain language or keywords
   - `jurisdiction`: required object (`type`, plus `state` / `circuit` when needed)
   - `searchType`: `auto` unless the query is clearly a citation or case name
   - `limit`: 5–15 unless the user asks for more
4. Prefer search hit fields (name, citation, court, date, snippet, good-law flags). Do not treat search snippets as the full opinion.
5. If the user needs the full opinion text for a hit, call `retrieve_case` (if needed) then `get_opinion_text` with that `caseId`. Paginate with `nextOffset` until you have enough text.
6. Answer with cited authorities from tool results only. Flag negative treatment / not-good-law when tools report it.

## Do not

- Fabricate citations or quote language that did not come from LawDiver tools
- Use LawDiver for restaurants, news, or general web browsing
- Draft or e-file court documents
- Claim you deleted or edited anything in the corpus (tools are read-only)
