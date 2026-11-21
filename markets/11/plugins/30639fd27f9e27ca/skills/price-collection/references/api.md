# CardRouter Collection Pricing MCP server reference

Live routed pricing server for the `price-collection` skill. The plugin connects to it through the `cardrouter` entry in the package's `mcp.json`.

## Endpoint and transport

- URL: `https://cardrouter.com/api/mcp`
- Transport: MCP Streamable HTTP, stateless — one JSON response per POST, no long-lived SSE stream.

## Authentication

OAuth 2.0 Authorization Code with PKCE (S256). No credentials are needed from the user beyond sign-in:

- Client registration: OAuth Dynamic Client Registration (DCR) with a public client and `token_endpoint_auth_method: none` — the `mcp.json` declares this with `client.mode: "dcr"`.
- Discovery: OAuth Protected Resource Metadata and OAuth Authorization Server Metadata.
- Token binding: RFC 8707 `resource` is required at authorization and at token exchange.
- Reviewer access: the consent flow mints an anonymous per-browser OAuth identity — no reviewer credentials, no manually shared token. The consent page shows the requested permissions and the active quota before Allow.

## Tools

The server exposes exactly two tools.

### `price_card_collection`

Prices line items against live buylists and routes each card to the best-paying vendor.

Input schema (verbatim):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "items": {
      "type": "array",
      "minItems": 1,
      "maxItems": 100,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "qty": { "type": "integer", "minimum": 1 },
          "card_name": { "type": "string", "minLength": 1, "maxLength": 255 },
          "set": { "type": "string", "minLength": 1, "maxLength": 255 },
          "collector_number": { "type": "string", "minLength": 1, "maxLength": 20 }
        },
        "required": ["qty", "card_name", "set", "collector_number"]
      }
    }
  },
  "required": ["items"]
}
```

- `set` accepts the set code (`A25`, `LEA`, `VOW`) or the canonical set name.
- All four fields are required on every item.
- Split larger collections into batches of at most 100 items and sum the batch totals.

### `get_price_freshness`

Reports how current the pricing dataset is. Takes no input — call it with an empty object:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {}
}
```

## Rate limits

Per OAuth identity, enforced server-side:

- 20 pricing calls per hour.
- 500 line items per hour.
- Maximum 100 items per call.
- The defaults are set by the `MCP_RATE_LIMIT_CALLS` and `MCP_RATE_LIMIT_ITEMS` environment variables.

Over-limit behavior: the request is blocked and returns JSON-RPC error code `-32026` with HTTP status `429`, a `Retry-After` header, and quota headers. Surface the retry window to the user instead of retrying immediately.

## Vendors and coverage

Vendors are limited to CardRouter's covered buylists and may change. Prices are near-mint, non-foil, in USD, because the collection input carries no condition or finish.
