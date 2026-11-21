# Troubleshooting Notes

## Statuses

- `queued`: accepted, waiting for processing.
- `processing`: running upstream.
- `succeeded`: inspect `result.assets`.
- `failed`: inspect `errorCode` and `errorMessage`; this is not an HTTP error.
- `canceled`: terminal; do not keep polling.

## Web Connector Checks

In a chat without shell access, connect or reconnect Givon through the host's
plugin/connector settings and browser sign-in. Use `givon_list_models`,
`givon_get_balance` and `givon_get_generation_status` for the corresponding
reads. Do not ask a web user to run local diagnostics.

## CLI Checks (with shell access)

Use the installed client:

```bash
givon mcp doctor --client codex
givon mcp doctor --client claude-code
givon mcp doctor --client claude-desktop
givon mcp doctor --client cursor
```

Use REST for direct API checks:

```bash
givon model list --kind video
givon asset list --kind image
givon balance
givon generate get <generation-id>
```

## Boundaries

The public API/CLI exposes asset upload, import, list, get and soft archive.
MCP exposes ChatGPT native file-param upload, base64 upload, URL/data import,
list, get and soft archive. Local file upload still requires the CLI for
generic MCP clients because the remote MCP server cannot read local disk.
Cost quotes and OAuth connector sign-in are supported. Generation listing and
webhooks are outside the current public surface.
