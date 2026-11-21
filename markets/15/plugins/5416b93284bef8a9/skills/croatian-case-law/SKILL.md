---
name: croatian-case-law
description: Research how Croatian courts applied the law to a legal issue, find sudska praksa or Supreme Court practice, and read a particular decision by case number or ECLI. Retrieve the decision before quoting its reasoning and distinguish its facts from a statutory rule. Does not cover Constitutional Court, ECHR or other national court corpora.
license: Proprietary — see https://eulex.ai/legal
metadata:
  compatibility: Requires the EULEX.AI MCP connector (https://mcp.eulex.ai/mcp) to be connected and authorised. Without it none of the retrieval steps can run.
  author: Augment Ltd
  version: "1.3.14"
---

# Croatian case law research

The `@hr` corpus holds decisions of Croatian courts from odluke.sudovi.hr
(count, with its stats_as_of date, via `about`). Constitutional Court decisions are not in it as case law;
they appear as Narodne novine publications. EU (CJEU) judgments live in the
`@eu` corpus and are reached differently — see the end of this skill.

Use the tools of the EULEX.AI connection (`https://mcp.eulex.ai/mcp`) with
the exact names the host shows. If it is unavailable, say retrieval needs it;
never cite a decision from memory.

## Known case number or ECLI: open it directly

`get_decision(uri: "Rev-1356/2024-2")` — no search first. It accepts spaces
instead of hyphens, missing diacritics (`Gz`), two-digit years
(`Revr-615/08`), a missing final suffix, an ECLI, or `@hr/decision/{uuid}`.
If several courts use the number, the response has `candidates[]`; pick by
court and date, or ask.

## Topic: search, then open

**1. Search** with `case_law_search(query: ...)` in Croatian legal terms —
the decisions are Croatian and the search is semantic over their reasoning
and operative part. Filters:

- `court_codes` — comma-separated, for example `"vs"` (Vrhovni sud). Other
  codes appear in `court_code` of the results; reuse them.
- `reference_only: true` — VSRH reference decisions, for settled positions.
- `date_from` (inclusive) / `date_to` (**exclusive**), `YYYY-MM-DD`.

Each `decisions[]` entry has `decision_number`, `court_name`,
`decision_date`, `ecli`, `citation` and up to three matching passages in
`segments`. Its URI is in `sources[].id` (`@hr/decision/{court_decision_id}`).

**2. Triage on the passages,** then open only the decisions that matter.
`get_decision` returns the full text by default (often 50–70 KB); to check
several decisions cheaply, pass `include_text: false` and
`include_citations: true` first.

**3. Follow the law the court applied.** With `include_citations: true`,
each `citations[]` entry has `cited_title`, `article_ref_raw`,
`resolution_confidence` and, when resolved, `article_uri` and
`resolved_regulation_version_id`.

- `article_uri` alone returns **today's** wording.
- For the wording the court applied, call
  `get_article(uri: <article_uri>, version_id: <resolved_regulation_version_id>)`.
- Citation resolution can point to the wrong act. If `cited_title` and the
  resolved title disagree, trust `cited_title` and address that act yourself
  (`@hr/<official title>`).

**4. Check that the rule is still the same.** Fetch the article without a
version and compare, or use the `point-in-time-law` skill. A decision applying
since-amended wording may no longer reflect the law.

**5. Instance chain (optional).** `include_related: true` lists earlier and
later decisions in the same matter. The source links them by case number
across courts, so a `chronology_warning` or an odd court pairing means the
link may be wrong — open the decision before relying on it.

## Inspect a decision in the source viewer

When the user asks to open the source, call `view_source` with the returned
`@hr/decision/...` source ID. The card contains retrieved decision wording.
Keep the official citation and disclose any missing text or source link; the
viewer does not validate cited legislation or resolve conflicting case metadata.

## Coverage to disclose

- Few or no results do not mean the courts have not ruled; the search covers
  the decisions indexed so far. Say so.
- `finality_date` is always empty; use `finality_status`.
- Count what you found. One decision is not settled case law.

## EU judgments (CJEU)

`case_law_search` and `get_decision` are `@hr` only. For CJEU judgments use
`search(query: ..., scopes: ["@eu"], in_force_only: false)` — judgments are
dropped when `in_force_only` is true — or
`get_related(uri: <EU act>, relation_type: "related_case_law")`, which lists
judgments concerning an act (metadata, not text).

## Output

- What the courts held, as a proposition, and how many decisions support it.
- Each decision: court, case number, date, ECLI when present, link from
  `source_url`.
- The provisions applied, quoted from `get_article` in the version the court
  used, and whether that wording is still in force.
- An explicit note when coverage is thin.

## Do not

- Do not generalise one decision into a settled position.
- Do not treat a related-decision link as agreement; it may be an appeal, a
  correction or a later instance.
- Do not present case law as predicting the outcome of the user's matter.
- Do not put the user's party names or confidential facts into the query.
