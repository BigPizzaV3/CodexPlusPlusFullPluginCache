## Submission identity

This is a new plugin package (`wowseru-ai-affiliate-storyboard-remote`, version `1.0.0`). In the OpenAI Plugins portal, create a **new plugin draft** for this archive. Do not use Reupload ZIP / update on the older command-MCP plugin; the portal does not permit replacing that plugin's MCP server configuration.

# Reviewer Guide

## Package transport configuration

The submission transport is the remote Streamable HTTP endpoint declared in the root `mcp.json`:
`https://ai-affiliate-storyboard.infowowseru.workers.dev/mcp`.
The local stdio entrypoint is retained only for development and is not the submission connection.

## Local core test

1. Install Node.js 18 or later.
2. Open a terminal in `mcp-server/`.
3. Run `npm test` for the shared core tests.
4. `npm start` runs the optional local stdio development entrypoint; it is not used by the submitted remote MCP configuration.

## Remote MCP test

1. The Cloudflare Worker is already deployed at `https://ai-affiliate-storyboard.infowowseru.workers.dev`.
2. Verify `GET https://ai-affiliate-storyboard.infowowseru.workers.dev/health`.
3. Open MCP Inspector, choose **Streamable HTTP**, and connect to `https://ai-affiliate-storyboard.infowowseru.workers.dev/mcp`.
4. Production checks run on 2026-11-01 returned HTTP 200 for initialize, tools/list, and tools/call for all three tools.
5. Recorded Cloudflare version ID: `4b31e74d-0fb1-4101-8ac5-ed24c8fc0b60`. The reviewer may independently repeat these checks.

## Conversational test

Use the five positive and three negative cases in `test/`. Record actual results and environment details separately. Do not mark a test passed until it has been executed in the target host.

## OpenAI submission

Upload the ZIP through the OpenAI Plugins submission flow, connect the remote MCP server, complete the domain-verification challenge shown in the portal, inspect the automated tool scan, and complete the applicable metadata and review fields. A demo plan is not a demo recording; provide an actual reviewer-accessible recording URL. Website, support, privacy policy, and terms URLs must be supplied and verified before submission; they are not fabricated in this package.
