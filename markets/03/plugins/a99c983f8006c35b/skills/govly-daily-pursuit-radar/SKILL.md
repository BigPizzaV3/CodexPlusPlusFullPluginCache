---
name: govly-daily-pursuit-radar
description: Create an on-demand or scheduled, read-only digest of Govly opportunity saved-search matches, deduplicate results, and rank them with a customer-provided scoring rubric. Use for daily or weekly pursuit radar, capture-team digests, saved-search scoring, and identifying new or materially changed matches. Do not use for SLED meeting intelligence or recompete monitoring.
---

# Govly Daily Pursuit Radar

Produce a concise, evidence-backed digest of the best opportunity matches from the user's Govly saved searches. Keep scheduled runs read-only.

## Prepare the run

Collect or recover these settings from the current chat:

- Saved-search scope: exact saved-search IDs, exact names, or all visible opportunity saved searches.
- Scoring rubric: weighted criteria, scoring anchors, hard disqualifiers, and minimum reporting score.
- Coverage limits: maximum matches to inspect per search and maximum finalists to open in detail.
- Reporting preference: daily or weekly window, desired result count, and output detail.

For interactive use, ask one concise question for any setting that materially changes the result. For a scheduled run, do not guess missing saved-search scope or rubric rules; return a short setup-needed message naming the missing settings.

Read [references/templates.md](references/templates.md) when setting up a rubric, scheduled prompt, or final report.

## Build the candidate set

1. Call `list_opportunity_saved_searches` and follow `meta.nextCursor` until it is null.
2. Match configured names exactly. If multiple searches share or closely resemble a requested name, ask the user during an interactive run; skip the ambiguous search and report it during a scheduled run.
3. For every selected search, call `list_opportunity_saved_search_results` and follow `meta.nextCursor` until it is null or the configured coverage cap is reached.
4. Treat these as cached saved-search matches, not a live replay of the search.
5. Deduplicate matches by canonical opportunity ID. Preserve every saved search that matched each opportunity.
6. Exclude clearly closed, expired, cancelled, or otherwise inactionable records unless the user explicitly requested historical review.
7. If any pagination or coverage cap prevents a complete pull, label the report `Partial coverage` and state which searches were truncated.

## Detect changes

Compare the current candidate set with the most recent successful report in the same chat when that context is available.

- Label an unseen opportunity `New`.
- Label an existing opportunity `Changed` only when a material field changed, such as status, deadline, buyer, scope summary, value, set-aside, or attachments.
- Suppress unchanged opportunities when the scheduled prompt requests changes only.
- Label the report `First run` when no reliable prior snapshot is available.

Do not claim durable cross-chat state. A standalone scheduled run may not have the prior chat context needed for change detection.

## Apply the scoring rubric

1. Evaluate hard disqualifiers before weighted criteria.
2. Use the scale and anchors supplied by the customer. If the rubric uses 0-5 ratings and weights totaling 100, calculate each contribution as `weight * rating / 5`.
3. Require weights to total 100 unless the customer explicitly defines another calculation. Do not silently normalize a malformed rubric.
4. Score only from returned Govly evidence and customer-provided context.
5. Mark unavailable evidence `Unknown`. Do not convert missing evidence into zero unless the rubric explicitly says to do so.
6. Keep score and confidence separate:
   - `High`: most high-weight criteria have direct evidence.
   - `Medium`: the score depends on some summaries or unresolved fields.
   - `Low`: one or more high-weight criteria lack evidence.
7. Use the saved-search result's opportunity payload and `aiSummary` for the first scoring pass.
8. Call `show_opportunity` only for the highest-ranked candidates that could make the final report. Default to at most 10 detail reads unless the user configures another cap.
9. Use `document_read` only when the rubric requires evidence from an attachment and the user has asked for that depth. Cite the document or page used.

When an AI summary conflicts with source metadata or a document, prefer the source and disclose the conflict.

## Produce the digest

Lead with the result, not the retrieval process. Include:

1. Run status: complete, partial coverage, first run, or setup needed.
2. Number of saved searches reviewed, candidate matches found, unique opportunities scored, and finalists reported.
3. A ranked table with status, score, confidence, opportunity, buyer, deadline, matched searches, and one-sentence rationale.
4. A short score breakdown for each finalist with evidence, risks, unknowns, and recommended next action.
5. A `Not reported` note for disqualified or below-threshold candidates, using aggregate counts rather than a noisy list.

If nothing qualifies, say so plainly and include the coverage summary. Do not pad the report with low-scoring results.

## Preserve safety and scope

- Use only read tools during a scheduled run.
- Never call `follow_entity`, `mark_not_interested`, inbox mutation tools, saved-search update tools, workspace mutation tools, or comment tools from this workflow.
- Treat the original scheduling request as authorization to read and report, not authorization for future mutations.
- Do not send results to email, Slack, or another destination unless the user explicitly requests it and an authorized connector is available.
- Do not present model judgment as a source fact. Show the evidence behind every material score.
- Do not report a first page as the complete result set.
