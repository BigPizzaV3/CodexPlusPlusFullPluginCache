# Troubleshooting

First identify the product. ChatGPT uses Box MCP only; Codex may use configured MCP, CLI, or REST paths as routed by the main skill.

## Triage

Capture the acting identity, tool or endpoint, Box object type and ID, minimal request, and complete error response. Most failures are an actor, object-ID/type, endpoint, scope, or permission mismatch.

## Common Box errors

- **401/403:** Expired or wrong token, missing scope or app permission, or an actor without access.
- **404:** Wrong object ID/type, or an object hidden from the current actor.
- **409:** Duplicate item name, existing collaboration, or metadata-template/instance conflict.
- **Timeout/5xx after a mutation:** Read the target before retrying because the write may already have completed.

## 429 rate limits

1. Stop requests using the same actor or token.
2. Read `Retry-After`, wait at least that duration, then retry the same request.
3. Do not send other requests with that identity during the cooldown.
4. For bulk work, keep CLI commands serial and pace large batches by 200–500 ms after recovery.
5. If `Retry-After` is absent or throttling repeats, use exponential backoff with jitter.

## Webhook verification failures

- Verify the signature against the unmodified raw request body with the correct signing secret.
- Reject stale or replayed events, and record an idempotency key before downstream work.
- If logging or middleware parses or normalizes the body first, preserve the original bytes for verification.

See `references/webhooks-and-events.md` for implementation and verification guidance.

## Search quality problems

Use `references/mcp-search.md` for search selection, scoping, metadata schemas, and ambiguous results.

## MCP connection or authentication

Use the official-plugin troubleshooting path in `references/auth-and-setup.md`. Use custom OAuth setup only when the user explicitly requests custom MCP. In ChatGPT, do not fall back to CLI or REST; in Codex, follow the main skill's configured fallback routing.

## MCP tool missing

Check the [maintained tool list](https://docs.box.com/en/box-mcp/tools). If the tool is documented but absent, it may have been disabled by their Box Admin through [Box Admin controls](https://docs.box.com/en/box-mcp/admin-controls). If the user confirms the tool is not disabled, reconnect Box, and start a new session if the client cached its tool list.

## CLI auth problems

CLI is Codex-only. Use `references/box-cli.md` for login, safe authentication checks, actor overrides, and token precedence.

## Codex sandbox network access

Box CLI commands that worked in a regular terminal fail inside Codex with `getaddrinfo ENOTFOUND api.box.com` or a generic "Unexpected Error" with no HTTP body. Auth checks like `box users:get me --json` may still pass because they use cached local credentials, making it look like auth works but API calls do not.

**Cause:** Codex sandboxes block outbound network access by default. The CLI cannot reach `api.box.com`, `upload.box.com`, or any other Box endpoint.

**Fix for Codex CLI:** Add to `~/.codex/config.toml`:

```toml
[sandbox_workspace_write]
network_access = true
```

Then restart the Codex CLI session.

**Fix for Codex web (cloud):** In the environment settings, turn agent internet access **On** and add `box.com` and `boxcloud.com` to the domain allowlist.

**How to tell this is the problem:** If `box users:get me --json` succeeds but `box files:get <ID> --json` fails with a DNS or connection error, the sandbox is blocking outbound network access. The same commands will work in a regular terminal outside of Codex.