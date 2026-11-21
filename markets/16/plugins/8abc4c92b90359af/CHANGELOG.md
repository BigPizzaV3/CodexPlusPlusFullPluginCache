# Changelog

## 1.0.5
- Added a regression test that fails unless every MCP tool publishes explicit boolean values for readOnlyHint, destructiveHint, and openWorldHint in the tools/list annotations object.
- Kept the three tool registrations read-only and non-destructive; no tool behavior or product-brief fields were removed.


## 1.0.4
- Corrected the MCP URL to the active Cloudflare Worker hostname.
- Updated the OpenAI domain verification challenge value for the new plugin draft.
- Retained explicit MCP annotations on all three read-only tools: readOnlyHint=true, destructiveHint=false, openWorldHint=false.


## 1.0.3
- Added explicit MCP tool annotations for all three tools: readOnlyHint=true, destructiveHint=false, openWorldHint=false.
- Preserved existing tool behavior and Worker endpoint.


## 0.1.0 — Initial development package

- Added independent WOWSERU AI Affiliate Storyboard identity.
- Added product brief, audience, emotional insight, storytelling, storyboard, video prompt, continuity, and production checklist workflow.
- Added three MCP tools for brief validation, output validation, and production manifest creation.
- Added local stdio and Cloudflare Worker MCP entrypoints.
- Added five positive and three negative acceptance scenarios.
- Added draft reviewer and release documentation.

This is an initial development package. Cloudflare deployment, host integration, and all runtime acceptance tests remain to be completed by the operator.
