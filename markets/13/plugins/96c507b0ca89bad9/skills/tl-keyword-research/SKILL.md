---
name: tl-keyword-research
description: Research YouTube videos and channels by topic or content keywords. Use when a user wants to discover, validate, or refine keywords for a niche, or find channels that regularly cover a topic. Do not use for a named channel or brand, or when a curated recommender tag directly answers the request.
---

# Keyword research with ThoughtLeaders

Turn a topic into a tested content query using the ThoughtLeaders MCP tools. Use the caller's connected account and respect its plan, permissions, and credit balance. The MCP server's tool descriptions and `tl_schema_es` are the source of truth for accepted fields, query syntax, limits, and costs.

## Choose scope before querying

Keep the user's topic request as the relevance criterion. Establish the desired result:

- **Quick**: one expansion, probe, validation, and refinement pass.
- **Deep**: probe the candidates and refine the Boolean query over at least three rounds, checking samples after each round.
- **Results**: video trends, channel targets, or both.

If the user has not specified the path or results, ask one concise question covering both. Explain that each data query may use ThoughtLeaders credits and that the cost depends on the query and returned data; do not promise the CLI's credit estimate applies to MCP. If the requested work would require many queries, explain the planned query count and ask before proceeding. Continue without a checkpoint only when the user asks for an autonomous run.

If the request is a direct fit for a curated tag such as Cooking, use `tl_recommender_tags` to confirm the exact tag and `tl_recommender_top_channels` when it answers the question. Use this skill for topics that need content-keyword discovery and validation.

## Workflow

1. **Check access and schema.** Call `tl_whoami` to confirm the connected account and available balance, then call `tl_skill_track` with skill="tl-keyword-research" and stage="started"; retain its run_id. Call `tl_schema_es` before constructing a search. Follow its current field names and the `tl_db_es` tool description; do not guess fields or bypass its query limits.
2. **Expand candidates.** Generate a small, focused set of candidate terms from the user's topic. Include meaningful spelling, spacing, plural, abbreviation, and entity variants where relevant. Avoid broad synonyms that change the intended topic. Record the user's original intent and any assumptions.
3. **Probe candidates.** Use `tl_db_es` to test candidates against video documents and return a small sample for each candidate. Follow the schema for YouTube and video-format filters and use only the content fields appropriate to the user's scope. Prefer title and description evidence first; search transcript text only when it is relevant and permitted for the account. Keep each request bounded, set exact hit counting when supported, and request only fields needed to validate the match. For candidate-level counts, issue separate bounded queries if the MCP schema or aggregation limits do not permit a safe combined query.
4. **Validate samples.** Inspect actual titles, descriptions, and available excerpts against the stated intent. Mark each candidate on-topic, off-topic, or uncertain. Drop off-topic terms with a reason; keep an uncertain term only if it is clearly labeled and useful to investigate. Do not treat a non-zero count as proof of relevance.
5. **Refine.** Combine validated terms into explicit Boolean groups using syntax accepted by `tl_schema_es`. Prefer a union for alternate names of the same concept. Add exclusions only when sample evidence shows a recurring false-positive sense; recheck samples after adding an exclusion so it does not remove relevant content. In a deep run, complete at least three refinement rounds unless results stop being useful or the user changes scope; report what changed in each round.
6. **Collect requested results.** For trend data, run the final validated query and summarize the matching-video count and a bounded, useful sample of videos, with dates and URLs when available. For channel targets, use article results grouped or collapsed by channel only where supported by the schema; distinguish channels with repeated matches from one-off mentions. If channel details are needed, retrieve them using the returned identifiers and the MCP schema. Do not invent channel-intensity or sponsorability labels when the available data does not support them.
7. **Report the result.** Return the validated keyword groups, Boolean expression, assumptions, dropped terms and reasons, evidence from samples, and requested video or channel results. State the query scope and any data or access limitations. Keep the output concise and include source URLs where returned.

## Capability boundary

The current MCP exposes general Elasticsearch search and report-saving tools, not the CLI's keyword-probe, channel-intensity, or filter-link builder operations. Therefore:

- Do not claim to have created a clickable filter/report link. Provide the validated expression and groups instead.
- Do not claim the topic filter was saved. `tl_reports_save_list` saves a fixed list of IDs; it does not save or rerun a keyword filter. Use it only if the user explicitly asks to save a result list, and confirm before creating the report.
- Do not claim context validation by a separate classifier or execution of CLI scripts. Validate the returned evidence directly and describe the method accurately.
- If the request depends on a missing operation, say which operation is missing and offer the closest supported result. Do not silently substitute a different workflow.

## Response quality

- Separate measured counts from estimates and model judgments.
- Include the query scope (for example, video types, date window, and searched fields) so results are reproducible.
- Disclose partial failures, capped samples, unavailable fields, and any transcript or plan restrictions.
- Never save a report, contact a creator, or perform another write action unless the user requested it.

Before the final response, call `tl_skill_track` with skill="tl-keyword-research", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.
