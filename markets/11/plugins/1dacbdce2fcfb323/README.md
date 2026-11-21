# Seistream Blockchain Data

Version 0.1.7. Read-only Sei mainnet data plugin using Streamable HTTP.
Endpoint: https://api.seistream.app/mcp/plugin (no authentication).
Original service: https://api.seistream.app/mcp (unchanged).

The plugin exposes 130 data tools with concise descriptions and preserves argument validation. It rejects transaction broadcasting/preparation, wallet generation, and contract-verification submission or import tools before forwarding requests. Those excluded tools remain available only through the original service.

Responses come from the existing Seistream APIs. Report error:true responses as failures and distinguish incomplete/stale indexing from fresh chain data. Public wallet addresses are sufficient for lookups; this plugin cannot retrieve existing private keys or seed phrases.

Support: https://stakeme.pro/
Privacy: https://stakeme.pro/privacy-notice
Terms: https://stakeme.pro/terms

The review recording demonstrates real ChatGPT Work catalog discovery, five read calls and three clarification/refusal cases. This is not a test of every operation or a guarantee of acceptance by OpenAI.
