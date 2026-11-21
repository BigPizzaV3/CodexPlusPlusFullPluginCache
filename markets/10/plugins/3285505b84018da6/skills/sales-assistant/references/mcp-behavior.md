# MCP behavior

Configured endpoint: `https://mcp.sybill.ai/mcp`, using Streamable HTTP and OAuth. The host handles sign-in. Never add credentials to the package.

## Route requests

- `ask_sybill`: send the scoped sales question in `message`.
- `get_ask_sybill_result`: continue a pending analysis, if available.
- `list_conversations` / `get_conversation`: find meetings and retrieve a selected meeting's evidence.
- `list_deals` / `get_deal`: resolve an opportunity or check its returned fields.
- `list_accounts` / `get_account`: resolve account identity when those tools are exposed.

Use IDs returned by searches or supplied by the user. Preserve opaque IDs exactly. A similar name is not a substitute for an exact identity. Tool names may have a host namespace; select the matching connected Sybill tool.

## Complete an analysis

`ask_sybill` may return final text immediately. A JSON envelope with `status: "running"` is a pending job, not an answer. Pass its `threadId` as `thread_id` and `runId` as `run_id` to `get_ask_sybill_result`. Reuse that job instead of submitting the same question again.

Follow host timing constraints and any server retry delay. If none is supplied, use bounded backoff between polls. At `completed`, use the returned `output`. At `failed`, `stopped`, an unknown status, or malformed data, describe the failure without inventing an answer. If the poll tool is unavailable or the host's wait budget ends, report that the analysis remains pending. Do not spin in a tight loop or claim success.

## Retrieve enough evidence

List endpoints paginate. Preserve filters and pass the returned cursor for subsequent pages when the requested scope needs them. Do not assume the first page is the whole pipeline or that returned records are sorted by recency unless the schema guarantees it. Use date filters or compare returned timestamps for a "latest" request. If coverage is partial, label the result as partial and avoid complete totals or rankings.

## Recover proportionately

Expired or missing authorization requires the host's reconnect flow. Do not substitute a broad organization API key. Respect access-denied responses. For rate limits, honor the retry delay and avoid repeated analysis submissions. If Sybill remains unavailable, preserve useful retrieved context, disclose the interruption, and do not guess at missing records.

Source: [Sybill MCP documentation](https://api.sybill.ai/docs/mcp.html).
