# Vincent connection

This plugin connects to an already-running Vincent MCP server. It does not launch the backend, bundle the Vincent codebase, or provision credentials.

## Configured transport: Clio's MCP gateway

The plugin's `.mcp.json` declares one remote server over streamable HTTP:

```json
{
  "mcpServers": {
    "vincent": {
      "type": "streamable-http",
      "url": "https://staging.mcp.api.clio.com/mcp"
    }
  }
}
```

The gateway terminates OAuth and forwards the caller's identity to Vincent, so the host signs the user in and no token is stored anywhere in this plugin. This is the sanctioned configuration: it targets staging deliberately, because that is where the gateway runs. Do not copy credentials into plugin files, ask for cookies or bearer tokens in chat, or bypass authentication and feature flags. If the user asks for a different environment, use their approved credential setup rather than improvising one.

Conversation, workflow, collection, file, and export tools use private routes such as `/workflows` and `/document_conversation`. Only citation matching uses `/api/v2/authority-match`; do not prepend `/api/v2` globally.

## Alternate transport: local stdio

`.mcp.stdio.json` holds the developer configuration, which runs `./bin/vincent-mcp` against a local checkout. It is not active unless someone has copied it over `.mcp.json` and reinstalled. In that mode the launcher resolves the backend from the `vincent-local` marketplace `source` recorded in `config.toml` and execs `uv --directory <backend> run --no-sync python mcp_server.py`; `VINCENT_BACKEND_DIR` and `VINCENT_UV` override the resolved backend and `uv` binary, the intended backend runs `EDITOR_DEV=1`, and `VINCENT_LT_TOKEN` supplies a bearer when it does not. If dependencies are missing or stale, report that prerequisite and obtain authorization before synchronizing them.

## Connection diagnosis

- Missing tools: confirm the plugin is installed and enabled, then test in a new Codex task after reinstalling. Reinstalling refreshes the plugin's packaged instructions, not the server.
- Not signed in: a remote server that has never completed OAuth surfaces as an authentication prompt or a 401 on the first call. Ask the user to complete the host's sign-in for the `vincent` server; do not attempt to supply a token yourself.
- Stale skill metadata: if a task advertises a deleted versioned skill path or wording that differs from the installed plugin, it is using an old skill catalog. Reinstalling alone may not refresh the running desktop host. Ask the user to fully quit and reopen Codex, then start a new task. Do not explain the missed activation as a requirement to name Vincent; legal advice is already sufficient. Do not restore obsolete cache directories as a workaround.
- Tool surface narrower than this skill describes: the gateway forwards to whatever Vincent build is deployed. If turn-running, interruption or document tools are absent, report that the deployed server predates them instead of substituting another service.
- Launch failure (stdio mode only): `bin/vincent-mcp` reports the specific cause on stderr — a missing `[marketplaces.vincent-local]` entry, an unresolvable backend directory, or `uv` not found. Relay it and, for a missing marketplace entry, direct the user to re-run `mcp-plugin/install.sh`. Do not modify the repo or install dependencies as part of ordinary legal work.
- Backend failure: use `list_collections` as a read-only connection check. A successful list verifies connectivity and auth, not research, uploads, or exports. Do not restart services or edit `.env` without authorization.
- 401/403: report the returned authentication or account requirement. An expired session must be renewed through the host's sign-in for this server. Do not retry it indefinitely or treat a denied/empty list as success.
- `start_research` refused with a 4xx naming the workflow: the agentic agent is gated on `vincent:research_assistant:agentic_default_agent`, and the error names it. Report that the flag is needed for the user's organization; retrying will not help, and there is no other workflow to fall back to.
- Upload/status 403: the staged-upload API requires `vincent:research_assistant:new-file-upload`. Distinguish this account gate from an S3 upload permission failure.

## Long turns and cards

The server drives a turn for up to `VINCENT_MCP_TURN_TIMEOUT` (default 240 seconds, kept under the host's own 300s tool timeout) per call, then returns `still_running`. Resume with `watch_conversation`. `VINCENT_MCP_REQUEST_TIMEOUT_SECONDS` (default 30) is a separate HTTP request timeout. `VINCENT_MCP_STREAM_READ_TIMEOUT` (default 35) must exceed the backend's roughly 20-second stream window. Do not interpret a normal stream reconnect as failed research.

If stream establishment repeatedly fails and the tool explicitly recommends snapshot polling, use `get_conversation_messages` with backoff from about 5 to 30 seconds as a limited fallback. A snapshot cannot expose an external-tool request; report that limitation if the run remains stuck. Preserve the conversation ID rather than restarting or resubmitting a turn. A 409 on continuation means wait for the existing turn.

The server bundles its card renderer by default. `VINCENT_MCP_CDN_RENDERER` is a local-only opt-out; the default avoids hosts blocking the CDN fetch. If cards do not render, report the host/renderer issue rather than claiming the MCP lacks task-selection or document tools. Attaching a document needs no card at all. Approvals and clarifications need no card — see [interruptions.md](interruptions.md); use the direct document tools the drafting skill describes.

## Upload limits

`attach_document` carries the bytes inside the tool call, so the host's own argument limit is the ceiling — well under the 25 MiB the staged-upload API accepts. For anything larger, the user uploads through Vincent for the same backend/account and gives you the file ID; verify it with `get_file_status`. Do not invent a local-path upload tool.

Local uploads can fail with S3 403 because the backend's AWS role lacks upload-bucket write permission. Explain the storage blocker and use an already accessible file if the task permits. Do not change AWS permissions or silently send the document to another environment. Pending upload, failed ingest, missing account access, and storage denial are distinct outcomes.
