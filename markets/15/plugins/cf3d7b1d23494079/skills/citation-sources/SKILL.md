---
name: citation-sources
description: Find the source sites and pages cited in Cituna's measured AI answers, compare engines, identify verified coverage gaps, and update requested outreach statuses.
---

# Inspect citation sources and outreach

Read [connection and evidence rules](../../references/connection-and-evidence.md).

1. Call `list_citation_sources` with the target domain. Match the requested
   `range` (`today`, `7d`, `30d`, `all`) and `engine` where relevant. The default
   range is 30 days; state it rather than implying all-time coverage.
2. Use `search` for a brand name, source host or URL fragment. Search can return
   cited pages excluded from outreach targets; preserve `excludedAs` and do not
   conflate all cited sources with suitable pitch targets.
3. Use `limit` and returned `nextOffset` to paginate targets. For a complete
   requested inventory, continue until `nextOffset` is null. Disclose truncation
   of other lists; pagination of targets does not establish completeness of
   search pages or `yourPagesEnginesCite`.
4. Report source hosts, sample page URLs, citation counts, engines, associated
   prompts and rivals. Use `get_engine_answers` for exact answer context, keeping
   its latest-day scope distinct from the source aggregation window.
5. Interpret `youOnThisSite` precisely: `linked` means linked to the brand,
   `mentioned` means named without a backlink, and `absent` means a completed
   page check found no brand. `unknown` and `unreachable` are not verified gaps.
   `gapsOnly: true` filters verified gaps and may undercount unexamined sources.
6. Show `yourPagesEnginesCite` to explain which owned pages already receive
   citations. Its 50-item cap can truncate results; absence from a capped list
   does not prove a page is never cited. Use `whatEachEngineReads` for engine
   comparisons and disclose that it covers all engines even when targets are
   filtered to one engine.
7. Prioritize observed source gaps by relevance and repeated citation evidence.
   Do not guarantee inclusion, recommendations or ranking improvements.

## Requested outreach status changes

Read the target list first. Call `set_outreach_status` with the exact returned
`host`, target domain, and one of `planned`, `pitched`, `placed`, `declined` or
`none` (clear). Use `planned` for a requested plan, not `pitched` unless the user
says outreach happened. Read `list_citation_sources` again to verify the change.

Updating a status does not send an email or obtain a placement. Draft outreach
copy if requested; this MCP has no tool for sending messages.

## Relevant tools

`list_citation_sources`, `get_engine_answers`, `get_visibility`,
`set_outreach_status`.
