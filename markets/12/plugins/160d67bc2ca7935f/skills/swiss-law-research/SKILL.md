---
name: swiss-law-research
description: Research Swiss law with the iusLink MCP tools. Use when a user asks about a Swiss federal or cantonal statute, an article (e.g. Art. 28 ZGB, Art. 337 OR), a Federal Supreme Court or cantonal court decision (BGE, BGer, docket numbers), or how courts interpret a provision. Always retrieves the current official text instead of answering from memory.
---

# Swiss law research with iusLink

iusLink gives read-only access to three official Swiss legal databases: Fedlex
(federal statutes), LexFind (cantonal and federal enactments) and Entscheidsuche
(court decisions). Results are legal information from official sources, not
legal advice; tell the user to consult a qualified lawyer for their specific
situation.

## Source-of-truth rule

Never cite, quote or summarize a Swiss statute or decision from memory. Fetch
the current text with an iusLink tool first, even for well-known provisions
(BV, OR, ZGB, StGB) and famous BGE decisions. If retrieval fails, say that the
text could not be verified instead of guessing. Quote the fetched wording and
include the official source link from the result.

## Pick the tool family

- **Fedlex** for the text of a federal law or ordinance (SR number, abbreviation
  such as OR/ZGB/BV/StGB/DSG, or ELI URI).
- **LexFind** to find a cantonal law, or to search all Swiss jurisdictions at
  once. LexFind returns metadata and official links, not the consolidated text.
- **Entscheidsuche** for case law: BGE/ATF/DTF citations, dockets such as
  6B_123/2022, and keyword search across federal and cantonal courts.
- For "how do courts interpret Art. X": fetch the article with Fedlex, then
  search Entscheidsuche for the citation.

## Fedlex workflow

1. `resolve_fedlex_statute` with a compact identifier (`OR`, `SR 220`,
   `Datenschutzgesetz`, or an ELI URI). Skip this when you already hold the ELI.
2. `get_fedlex_article` for one article (preferred), `get_fedlex_outline` when
   the article number is unknown, `get_fedlex_text` for broad, paginated context.
3. Historical wording: pass `as_of` (YYYY-MM-DD) to `get_fedlex_article` or
   `get_fedlex_text`, or `list_fedlex_versions` then `version_uri` (choose an
   entry with `has_text=true`). `as_of` and `version_uri` are mutually exclusive.

## Case-law workflow

1. `search_entscheidsuche` with short legal keywords, exact terms or citations;
   the search is lexical, not semantic. Apply canton, date and language filters
   first. Use `sort=relevance` for topics and `sort=date_desc` for recent cases.
2. `get_entscheidsuche_document` with the returned signature. Use `format=text`
   to read the decision, `format=json` for metadata only. Paginate with
   `next_offset` while `has_more` is true.
3. `get_entscheidsuche_citations` to follow the citation chain of a decision.

If a known citation is not found, retry through `search_entscheidsuche` with the
exact signature. Narrow, then widen: start with a focused query, tighten with
filters, and simplify again if nothing matches.

## Cantonal-law workflow

1. `search_cantonal_law` with the search text and canton codes (`ZH`, `BE`, ...;
   `CH` for the Confederation; omit to search everywhere).
2. `get_cantonal_law` to inspect one entry and obtain the official publication link.

## Answering

- Quote the retrieved wording, name the source (statute, article, decision
  signature, date) and give the official link from the tool result.
- Pass the user's language explicitly (`de` default, `fr`, `it`; Fedlex also
  `rm`, `en`).
- Never infer legal content from empty results or metadata-only responses.
- Do not present results as advice and do not offer upgrades, plans or checkout
  links; if a tool reports `no_active_plan`, relay its message and `info_url`.
