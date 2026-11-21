---
name: tl-creator-brief
description: Prepare an evidence-led profile of a YouTube creator from their own public video statements, or turn that profile into a creator-facing brief. Use for creator profiles, self-references, or talking points; use tl-brand-creator-connection when the central question is the fit between a named brand and creator.
---

# Creator profile and brief (MCP)

Build only from evidence returned by ThoughtLeaders tools. This MCP version lacks the CLI skill's local transcript-mining scripts, quote verifier, HTML renderer, and external web-research pipeline.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-creator-brief" and stage="started"; retain its run_id. Resolve the channel with tl_channels_find. Resolve a named brand with tl_brands_find. Ask the user to disambiguate multiple plausible records.
2. Read tl_schema_es and tl_describe. Make a bounded, channel-scoped tl_db_es query for relevant uploads and transcript highlights. Use pricing=true before an expensive query and include only a few candidate videos.
3. Create an evidence table with theme, excerpt as returned, title, URL, and timestamp only when provided. Mark paraphrases as paraphrases; do not turn partial highlights into complete quotes or infer personal facts.
4. For a named brand, use available brand and sponsorship evidence. Ask for the brand brief or identify missing context; the MCP has no general web-search tool.
5. Produce a concise internal profile and, if requested, a separate creator-facing brief. Ground each talking point, include source links, disclose thin evidence, show unresolved contradictions, and omit unnecessary sensitive details.

Do not claim every relevant video was reviewed or a quote was verified against a full timestamped transcript unless the returned data supports it. This workflow cannot create the CLI skill's reusable evidence ledger or rendered HTML artifact.

Before the final response, call tl_skill_track with skill="tl-creator-brief", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.

