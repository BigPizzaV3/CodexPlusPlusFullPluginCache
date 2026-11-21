# TrustSEO

TrustSEO is a remote MCP plugin for ChatGPT. Its existing OpenAI plugin identity
is `app-6aa3a8524fc88191be91389c5180d647`; its display name remains TrustSEO.
It connects to the production TrustSEO server at https://trustseo.club/api/mcp
using OAuth with PKCE.

The connection uses TrustSEO's multi-site consent flow. Users can authorize only the Google Search Console properties they select. Tools do not change SEO or site data and are limited to the authorized TrustSEO account and selected sites. The service may record internal request telemetry and API-key last-used timestamps.

The package contains no API keys, access tokens, demo credentials, or private environment values. Legal and support pages are hosted at https://trustseo.club/privacy-policy, https://trustseo.club/terms-of-service, and https://trustseo.club/contact.

See REVIEW-TEST-CASES.md for the reviewer test plan.

## Package layout

The portable package keeps `plugin.json`, `mcp.json`, and `assets/` at the
package root. The `.codex-plugin/` and `.mcp.json` files are compatibility
fallbacks for Codex clients. The MCP transport is `streamable-http` and points
to `https://trustseo.club/api/mcp`.

The package exposes 17 read-only tools, including `get_current_search_console_metrics` for current Search Console metrics, `extract_schema` for reading
existing JSON-LD and `get_schema_generation_context` for returning page HTML and schema definitions. It
does not include `get_site_dashboard`.

The plugin publication manifest uses an empty country allowlist, which removes
country restrictions for public distribution.

## Validation and packaging

Run the deterministic submission contract check and build the root-level
release archive with:

```sh
pnpm trustseo:validate
pnpm trustseo:package
```

The current release archive is generated at
`packages/trustseo/releases/trustseo-1.0.4.zip`.

The validator checks tool parity, all package manifests, transport, endpoint,
annotations, stale tool names, and exactly five positive plus three negative
submission cases. The web/mobile reviewer cases in
`REVIEW-TEST-CASES.md` still require execution in clean ChatGPT conversations
with the dedicated reviewer account.
