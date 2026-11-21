## New plugin package — Remote MCP edition

- Created a separate package identity: `wowseru-ai-affiliate-storyboard-remote` version `1.0.0`, for submission as a new plugin draft.
- Keeps the already deployed and production-tested Streamable HTTP endpoint; does not attempt to replace the MCP server configuration of the older command/stdio plugin.

# Release Notes — 0.1.0

## WOWSERU AI AFFILIATE STORYBOARD

Initial development package for creating AI UGC affiliate storyboards and video prompts.

### Included
- Product and USP brief collection.
- Audience and emotional insight analysis.
- Three connected storyboard prompts, each specifying a 2×3 grid of six panels.
- Three connected video prompts with time-coded action and optional narration.
- Character, product, and scene continuity locks.
- Context-aware negative prompt.
- Story summary, production specifications, and checklist.
- MCP tools for brief validation, production-output validation, and production-manifest generation.
- Local stdio MCP entrypoint and Cloudflare Worker Streamable HTTP entrypoint using Cloudflare Agents SDK.
- Five positive and three negative acceptance scenarios.

### Known limitations
- This package generates production plans and prompts; it does not render images or videos.
- The Streamable HTTP Worker is deployed at `https://ai-affiliate-storyboard.infowowseru.workers.dev/mcp`; production health, initialize, tools/list, and all three tools/call operations returned HTTP 200 on 2026-11-01.
- The included root `mcp.json` targets the deployed public Streamable HTTP endpoint. The local stdio entrypoint remains available for development testing.
- Cloudflare Worker uses the stateless Streamable HTTP handler. Recorded deployed version ID: `4b31e74d-0fb1-4101-8ac5-ed24c8fc0b60`.
- Public listing URLs, privacy policy, terms, verified publisher identity, demo recording, and portal attestations must be completed before public submission.
