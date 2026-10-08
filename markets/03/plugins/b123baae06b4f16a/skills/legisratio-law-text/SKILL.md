---
name: legisratio-law-text
description: Retrieve authoritative full text of an Italian/EU law, single article, or secondary act as in force on a date via LegisRatio MCP. Use when the law, article, or act ID is already known for a clause or compliance check; not for topic search.
license: MIT
metadata:
  version: "0.1.0"
---

# LegisRatio Law-Text Skill

Retrieve the authoritative full text of a law, a single article, or a secondary act exactly as it stood in force on a given date. Use this when the document ID is already known; search first (`legisratio-research`) when it isn't.

See [clause deep-dive prompt](references/clause-deep-dive.md) for a ready-to-use clause/compliance validation workflow.

## When to Use

- Need the full current or historical text of a specific Italian/EU/regional law
- Need the text of one article to cite in an opinion or brief
- Need a `Consob`/`Bankitalia`/`IVASS` secondary act's full text
- Don't use for: finding which documents exist on a topic (use `legisratio-research`)

## Prerequisites

- LegisRatio MCP server connected and available to the agent. Tool names below are the base MCP tool names; depending on the MCP client they may appear with a prefix (e.g. `mcp_legisratio_get_law_text`).

## How to Run

The agent calls the MCP tools directly.

## Procedure

1. Confirm the document ID and the target `dateInForce` (YYYY-MM-DD; use today's date when the intent is "current").
2. Law text: call `get-law-text` with `idLaw` = `YEARPUBLICATION|LAWNUMBER` (e.g. `2023|123`), `dateInForce` = target date. Regional laws append `:<region>` (e.g. `2023|123:lombardia`).
3. Article text: call `get-article-text-by-id` with `idArt` = `YEARPUBLICATION|LAWNUMBER#ARTICLENUMBER` (e.g. `2023|123#45`; regional adds `:lombardia`). For Constitution and codes use the exception names: `costituzione`, `codice_civile`, `codice_penale`, `codice_procedura_civile`. For EU laws use the CELEX ID from a prior search.
4. Secondary act: call `get-secondary-act` with `idAct`.
5. Verify the returned text matches the requested in-force date; quote it verbatim in the deliverable.

## Pitfalls

- Always pass `dateInForce` explicitly — the tool requires it and the text is date-sensitive.
- Unknown ID → search first; the tool will not guess. IDs come from search results, not memory.
- `#BIS` / `#TER` articles have no separate ID — their text is inside the main article (e.g. the base article number).
- Code/Constitution and regional IDs use special forms; don't force the generic `YEAR|NUM` pattern on them.
- Full law text for codes is NOT available via `get_law_text` with the `YEAR|NUM` id — e.g. `idLaw 1942|262` (civil code RD) returns "No text found". Read codes/Constitution at the article level with `get_article_text_by_id` (`codice_civile#NNNN`), which returns verbatim text.
- `get_secondary_act` accepts the exact `idAct` returned by `secondary_act_search` (e.g. `BANKIT:CIRC:229-...:9#1`) with no trimming.

## Verification

- The returned text begins with the correct document/act header and reflects the requested in-force date; you can quote it directly.
