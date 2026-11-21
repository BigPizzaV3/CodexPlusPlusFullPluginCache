# Diagnose or connect idea.ai MCP

The endpoint is `https://mcp.idea.ai/mcp`, using Streamable HTTP and OAuth. The package declares explicit authorization and token URLs. Keep passwords, bearer tokens, client secrets, presigned upload URLs, and local credential files out of the package.

Check installation/enabling, actual tool discovery, OAuth sign-in, and a successful read-only `list_models` separately. An installed badge alone does not prove the server started. A 401 from an unauthenticated request advertises OAuth and is not proof the endpoint is down. Use the host's supported connection or refresh controls first. Let the user complete sign-in and consent in the provider's normal flow without extracting tokens.

On 13 November 2026 a fresh runtime inventory returned 20 tools, including `preview_3d`, an app-only status helper, and two deprecated compatibility tools. `list_models` returned 127 models. The earlier empty dependency rules for VEED Subtitles and Topaz Proteus were absent, and Nano Banana 2.1 returned a numeric `maxMb=60` limit. The upload-session description now distinguishes changing a picker selection from overwriting or deleting stored files. These observations describe advertised contracts and authenticated reads, not verification of paid generation, upload implementation, or OpenAI approval.

The host can retain older tool definitions during an existing chat. After server changes, use the supported refresh or fresh-conversation flow and inspect the current schema before supplying new fields such as quote_cost.prompt or calling a newly exposed tool. Do not infer current capability from old instructions alone. If an operation such as create_audio or preview_3d is unavailable in a published connection, explain the missing capability rather than silently using a deprecated paid executor. Tool discovery on a development connection does not establish portal approval; the publisher must inspect the current scan and review status separately.

For user-requested direct Codex setup or diagnostic work, inspect existing entries before using:

```sh
codex mcp add idea-ai --url https://mcp.idea.ai/mcp
codex mcp login idea-ai
codex mcp list
```

`mcp add` may start sign-in, so use `mcp login` only if needed. Refresh or open a fresh conversation when required, then verify discovery and a read-only call. A direct connection may bypass a packaged-plugin loading problem; it does not prove the loader was repaired and is not a universal installation prerequisite.

On `paid_subscription_required`, explain the connected account requirement and do not retry. Respect rate-limit guidance, wait before a bounded read retry, and avoid concurrent discovery bursts. Keep diagnosis on MCP rather than automating the idea.ai website or desktop app, which would not test this connection.

Documentation: https://www.idea.ai/mcp/docs
