---
name: legisratio-caselaw
description: Search Italian court judgments by theme, retrieve full text and official shareable PDF links, and list jurisprudence on a statutory article via LegisRatio MCP. Use for case-law research and filing citations; not for legislation text.
license: MIT
metadata:
  version: "0.1.0"
---

# LegisRatio Caselaw Skill

Locate and pull Italian court judgments — search by topic/court/date, retrieve full text, produce official shareable PDF links, and surface jurisprudence attached to a specific statutory article.

See [litigation package prompt](references/litigation-package.md) for a ready-to-use citation-ready filing workflow.

## When to Use

- Find court judgments/verdicts on a dispute theme or legal point
- Retrieving a judgment's full text or an official PDF URL for citation/filing
- Compile the jurisprudence interpreting a given law article
- Don't use for: legislation search or law text (use `legisratio-research` / `legisratio-law-text`)

## Prerequisites

- LegisRatio MCP server connected and available to the agent. Tool names below are the base MCP tool names; depending on the MCP client they may appear with a prefix (e.g. `mcp_legisratio_judgment_search`).

## How to Run

The agent calls the MCP tools directly.

## Procedure

1. Search judgments: call `judgment-search` with `searchString` (topic/phrase), optionally `section` (array of courts, e.g. `CASSAZIONE_CIVILE`, `CASSAZIONE_UNITE`, `TAR_LAZIO`, `CORTE_GIUSTIZIA_UE`) and `startDate` (YYYY-MM-DD). `k` defaults 100; lower it for a focused set.
2. For each relevant result, note its verdict ID, formatted like `SENTENZA-CASS:2017:10413:CIV` (Cass. civ. sez. unite, 27 Apr 2017, n. 10413).
3. Full text: call `get-judgment-text` with `idJudgment`.
4. Official shareable PDF: call `get-judgment-url` with `idJudgment` — use this URL for citations/filings, not a guessed link.
5. Jurisprudence on an article: call `judgment-related-to-article` with `articleId` in article format (see `legisratio-law-text` for the ID patterns).
6. Present each judgment with court, date, number and the official PDF URL.

## Pitfalls

- Pass the verdict ID exactly as returned — `SENTENZA-...` IDs encode court/type/year/number and don't tolerate reformatting.
- `section` is an array; pass courts as a list.
- `TRIBUNALE` and `CORTE_APPELLO` in `section` mean merit ('sentenze di merito') cases.
- `get_judgment_url` returns a shareable official PDF link (e.g. `.../view_pdf/<ID>?token=...`) — use it for citations/filings. A past 401 (the PDF endpoint wanting its own key) was fixed server-side; if it ever errors again, don't invent a URL — say it's unavailable and offer the full text via `get_judgment_text` instead.
- `get_judgment_text` already embeds the same shareable PDF link inline in its output — when you've already fetched the text you can skip the separate `get_judgment_url` call.

## Verification

- Every cited judgment has a real `idJudgment` from a search result, and the PDF URL you give is the one returned by `get_judgment_url` (official), not a constructed link.
