---
name: retrieve-opinion
description: Resolve a U.S. case citation or name in LawDiver and load the full opinion body text for quoting and pin cites. Use when the user wants the full case, opinion text, or quotes from a known citation. Do not use for free-form topic search (use caselaw-research) or non-legal lookups.
---

# Retrieve full opinion text (LawDiver)

Use LawDiver MCP tools only. Never invent opinion language.

## When to use

- User provides a reporter citation or case name and wants the opinion
- User asks for quotes, pin cites, or a summary of a specific case’s reasoning
- Prior search returned a `caseId` and the user needs the full body

## Steps

1. Call `retrieve_case` with `query` set to the citation or case name.
2. If the result is ambiguous (did-you-mean list), present candidates and confirm before continuing — or call again with the chosen `caseId`.
3. Call `get_opinion_text` with the confirmed `caseId`.
4. If `truncated` is true, call again with `offset` / `nextOffset` until you have the needed passages (or the full body).
5. Quote only text returned by `get_opinion_text`. Prefer that tool over PDFs or search excerpts.
6. Optionally call `get_good_law` or rely on treatment fields from prior tools when the user asks whether the case is still good law.

## Do not

- Invent pin cites or quote language not present in the returned body
- Treat search `includeOpinionText` excerpts as a substitute for `get_opinion_text`
- Claim the full opinion was retrieved if the body is still truncated and you stopped early without saying so
