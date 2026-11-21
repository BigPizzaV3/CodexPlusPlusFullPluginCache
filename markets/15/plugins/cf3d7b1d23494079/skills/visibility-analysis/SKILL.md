---
name: visibility-analysis
description: Use Cituna to inspect measured AI answers, brand mentions and citations, compare engines and competitors, review audit history, or run a visibility scan when requested.
---

# Analyze AI visibility with Cituna

Read [connection and evidence rules](../../references/connection-and-evidence.md).
Use this workflow for answers and audits. Use the sibling prompt-tracking skill
to edit tracked questions, citation-sources for cited pages, and search-console
for Google performance.

## Current visibility and actual answers

1. Establish the account and brand using the shared rules.
2. Call `get_visibility` with the returned brand ID or bare domain. Identify the
   latest measurement day and the exact strings in `prompts[].prompt`.
3. Call `get_engine_answers` for each requested prompt, copying its exact text.
   If no prompt is specified, start with the most relevant prompts and disclose
   the sample. Retrieve all requested prompts if the user requests full coverage.
   If `availablePrompts` is returned, select from that list instead of guessing.
4. Engine keys are `chatgpt`, `perplexity`, `gemini`, `claude`, `grok`,
   `aioverviews`, and `aimode`. Google AI Overviews and Google AI Mode are distinct
   surfaces. Omit the engine filter for a cross-engine comparison.
5. Report prompt, engine, date, measurement status, answer summary, brand mention
   or citation and cited position when returned, and source links. Mark answers
   with `truncated: true` as incomplete. Never infer an absent citation merely
   from text that may have been truncated.

## Audits, trends and competitors

- Use `list_audits` with a domain filter, then `get_audit` for the needed scan IDs.
  Explain score components and show the citation matrix without counting missing
  measurements as misses. Inspect `scoring_epoch` before score comparisons.
- For a weekly review, use actual dated audits that bracket the requested window.
  If history is insufficient, report the available snapshot and missing baseline.
  The daily visibility and answer tools return the latest stored day; they are
  not historical time-series endpoints.
- Use `competitor_discovery` to find candidates observed in engine answers and
  GSC that are absent from the tracked competitor list. Distinguish configured
  competitors from newly observed candidates, and show the evidence source.
  This tool discovers rivals; it does not edit the competitor list.
- For "why am I not cited", join the visibility grid and answer receipts with
  citation sources and, when connected, GSC evidence. Classify observed gaps
  without asserting that absent GSC rows prove non-indexation. Clearly label
  explanations about source selection as hypotheses.

## Requested fresh scan

First read recent audits to determine whether existing data answers the request.
Use `run_scan` only for an authorized fresh measurement with a clear target and
known quota effects. Accept the URL/domain and up to eight explicit competitor
domains supported by its schema. A scan can add an untracked brand. Respect
backend plan and write-scope checks.

An untracked domain without competitors can return a recent shared measurement
instead of a new run. MCP v1.7.2 trims the scan response and does not reliably
expose its measurement date, replay status or quota effect. Never invent those
fields or label every successful response fresh. Compare `list_audits` before
and after the requested run and use a returned scan ID/date when available.
If there is no new history entry, state that freshness could not be confirmed;
this alone does not prove a replay. Use account usage only when returned and
avoid attributing concurrent usage changes to this scan. Do not automatically
repeat a scan to resolve an uncertain result.

## Relevant tools

`whoami`, `list_brands`, `gsc_status`, `get_visibility`, `get_engine_answers`,
`list_audits`, `get_audit`, `competitor_discovery`, `run_scan`.
