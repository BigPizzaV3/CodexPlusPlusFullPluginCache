---
name: box
description: "Foundation skill for working with Box in ChatGPT or Codex. Use whenever a request involves Box files, folders, search, sharing, metadata, AI, Hubs, Doc Gen, authentication, MCP, Codex CLI or REST access, SDK code, webhooks, or Box errors. Start here to select the available tool path and relevant domain reference."
---

# Box

## Overview

This skill targets OpenAI products. In ChatGPT, use Box MCP only and ignore all CLI and REST paths. In Codex, MCP, CLI, and REST are available as described below. When building application code in Codex, preserve the repository's existing Box SDK or REST architecture.

## Route The Request

### Identify the product and authenticated tools

- **ChatGPT:** Use only Box MCP. Call `who_am_i`; a successful response confirms the connected Box user. If it fails with an authentication error, complete the client-provided Box OAuth flow and retry. If MCP is not configured, use `references/auth-and-setup.md`. Do not check for or use CLI or REST.
- **Codex:** Check the available Box paths:
  - **MCP:** Call `who_am_i`. A successful response confirms the connected Box user.
  - **CLI:** Run `box users:get me --json`. A successful response confirms that Box CLI is installed, authenticated, and identifies the active CLI actor.
  - **REST:** Confirm `BOX_ACCESS_TOKEN` is present without printing it, then call `GET https://api.box.com/2.0/users/me` to validate the token and identify its actor.

In Codex, use authenticated MCP when available. If a check fails, use `references/auth-and-setup.md`, `references/box-cli.md`, or `references/rest-calls.md` for the relevant path.

Tool definitions and current Box documentation are authoritative for live parameters, supported operations, and limits.

### Domain routing

Choose the matching domain reference regardless of tool path:


| Request                                                                              | Reference                           |
| ------------------------------------------------------------------------------------ | ----------------------------------- |
| Authentication, actor selection, or initial setup                                    | `references/auth-and-setup.md`      |
| Uploads, downloads, previews, files, folders, moves, copies, properties, or metadata | `references/content-workflows.md`   |
| Collaborations, shared links, comments, or access changes                            | `references/collaboration.md`       |
| Keyword, folder-name, or metadata search                                             | `references/mcp-search.md`          |
| Box AI Q&A, extraction, summarization, or document retrieval                 | `references/ai-and-retrieval.md`    |
| Box Hubs creation, curation, or Q&A                                                  | `references/mcp-hubs.md`            |
| Box Doc Gen templates or generated documents                                         | `references/mcp-doc-gen.md`         |
| Bulk organization, folder trees, migrations, moves, or metadata writes               | `references/bulk-operations.md`     |
| Webhooks, events, ingestion, or catch-up synchronization                             | `references/webhooks-and-events.md` |
| 401, 403, 404, 409, 429, missing content, missing tools, or wrong-actor errors       | `references/troubleshooting.md`     |


### Codex-only CLI and REST fallbacks

Ignore these paths in ChatGPT.

- **Use CLI in Codex** only after `box users:get me --json` confirms it is configured and authenticated. Use it when the required operation is unavailable through MCP, the user explicitly requests CLI, or the deliverable requires a local reproducible command. For bulk actions, prefer CLI only when this availability check succeeds. Read `references/box-cli.md` in addition to the domain reference.
- **Use REST in Codex** when building or debugging application code that calls the Box API, or when neither MCP nor CLI can perform the required operation. Use it only after confirming REST authentication is configured. Read `references/rest-calls.md` in addition to the domain reference. Prefer an existing official Box SDK or HTTP abstraction in application code.

## MCP

The Box MCP server is the only Box tool path in ChatGPT. It provides structured operations for content, search, collaboration, AI, metadata, Hubs, and Doc Gen.

### Tool availability and documentation

The maintained list of Box MCP tools is at [https://docs.box.com/en/box-mcp/tools](https://docs.box.com/en/box-mcp/tools). If an expected tool is absent, check that list first, then use the MCP-tool section of `references/troubleshooting.md` for client and Box Admin Console enablement steps.