---
name: research
description: Use for Klue questions that need fresh evidence beyond a sufficient curated answer: competitive research, source-backed claims or quotes, account and opportunity investigation, recent changes, win/loss analysis, counts, trends, or comprehensive comparisons.
---

# Klue Research

Gather the minimum sufficient evidence for the user's question, then stop.
Use [citation-instructions](../citation-instructions/SKILL.md) when turning
that evidence into an answer.

## Select the current platform workflow

Inspect the tools available in the current session and their descriptions. A
client exposes one platform surface; never infer its platform from the user's
wording and never combine workflows.

| Tool signals | Workflow |
| --- | --- |
| `Search Klue` / `klue-search-content` with Smart Answers or 2.0 deal-support tools | **Compete 2.0** |
| `Search Klue` / `klue-search-content` limited to win/loss, without 2.0 Smart Answer/deal-support tools | **Klue 1.0** |
| Neither recognizable surface | Use only tools whose descriptions clearly fit the request; explain the limitation if none do. |

Search content is the default research path on both surfaces. Its result-source
labels, including Stack Cards, are not platform signals. The categories and
filters in its live description are an access boundary.

### Compete 2.0

- Use `Search Klue` / `klue-search-content` as the default research path. Use
  its live description for supported sources, filters, and parameters.
- Check Smart Answers first when available. They can answer a stable,
  well-matched question directly, but are not sufficient alone for a
  time-sensitive, account-specific, source-specific, conflicting, or partially
  covered request.
- For a named account, opportunity, buyer, prospect, renewal, or recent deal:
  resolve the opportunity when needed, then retrieve the available buyer
  requirements, competitors, and recent deal evidence. Supplement with unified
  search when it materially answers the requested angle.

### Klue 1.0

- Use the exposed `Search Klue` / `klue-search-content` capability for
  competitive research. Klue 1.0 exposes win/loss content only; use only the
  categories, filters, and fields documented by that live tool description.
- A rejected category is an access boundary, not a query to retry. Do not
  borrow 2.0-only fields or parameters.

## Plan the evidence

Before searching, silently identify the required entities, requested source
types, date window, deal context, and deliverable. Preserve the user's angle;
do not expand a focused question into adjacent topics merely to collect more
material.

- **Targeted research:** one or two named angles, a specific claim, a focused
  source request, or a single account/deal.
- **Broad research:** an open comparison, multiple competitors, several
  independent angles, a pattern, roster, ranking, or explicitly comprehensive
  request.
- **Follow-up research:** only to close a named evidence gap, verify recency,
  resolve a conflict, or retrieve a requested quote/detail.

Run independent searches together when the connector supports it. Keep
dependent steps ordered: resolve an opportunity before requesting its details;
confirm a filter value before relying on it when the tools provide metadata
enumeration.

## Retrieval rules

- Query each source type the user explicitly requests. If the request asks for
  buyer voice, search for buyer evidence rather than only enablement material
  or a competitor's own claims.
- Use primary source material to validate decisive claims when available.
  Summaries and synthesized insights can orient research but do not turn into
  verbatim buyer evidence.
- For a "latest" claim, compare explicit dates within the requested scope and
  check for a newer candidate when the capability supports it. Otherwise say
  "newest found," not "latest."
- For a trend or change claim, obtain evidence from both the earlier and later
  periods. One time slice does not prove a trend.
- Do not guess tool parameters, filter names, category values, IDs, or source
  coverage. Current tool descriptions and returned schema are authoritative.
- If a valid filtered search returns no results, widen one level at a time:
  remove the narrowest subcategory filter, then the category filter, then run
  the query unfiltered. Preserve the user's query and stop once evidence is
  sufficient. Do not widen a rejected category, invalid parameter, or
  permission-bound query.
- Use public web research only when the user asks for public sources or a
  current public fact is unavailable in Klue. It never substitutes for
  proprietary deal, call, message, or win/loss evidence.

## Stop conditions

Stop when the core question has enough citable evidence and any material caveat
is known. More search is not automatically better.

If a required part remains unsupported after a bounded gap-fill, answer the
supported parts and name the missing evidence. Do not manufacture a complete
answer from near matches.
