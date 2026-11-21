# Chat-guided authentication design

Public package reconciliation: 22 October 2026. This is a server/operator contract and implementation status. Public discovery and an unauthenticated transport challenge were checked; no fresh-install authenticated user journey was completed in this rebuild. Historical authenticated tests are retained separately as dated review evidence.

## Intended user experience

The first DoctillaQM interaction checks trusted link state without launching unwanted sign-in. Already-linked users continue after a read-only identity check. Otherwise the exact two-option chooser is shown. After Get me connected, an actual authenticated profile/read tool requests account linking through ChatGPT's native OAuth card. The user completes provider login/consent, the host resumes the workflow, the profile is retrieved and the original task continues. Standalone requires neither linking nor private record access.

## Changes owned by this package

- Remote HTTPS Streamable HTTP declaration remains in mcp.json.
- OAuth now prefers CIMD; DCR remains available under host fallback policy. Earlier retrieved provider metadata advertised both. Preserve working saved DCR registrations.
- Keep PKCE/OAuth managed by the host, with OIDC disabled until the provider actually supports the required OIDC identity contract.
- Discover OAuth endpoints rather than hard-coding overrides for endpoints already supplied by discovery.
- Keep existing Doctilla read/write scopes for the record-maintenance use case; the host's consent and server authorisation still govern access. A startup check is read-only.
- Guide Get me connected through an actual authenticated read tool/native OAuth card before generic setup instructions. No credential collection, fabricated URLs or invented tools.

## Server changes required for the native card

1. Publish protected-resource and authorisation metadata and declare each private tool's oauth2 securitySchemes with its actual scopes. Mirror securitySchemes in tool _meta for compatibility where applicable.
2. Return MCP tool error results containing _meta["mcp/www_authenticate"] challenges when authentication is missing/expired or scopes need upgrading. Include resource_metadata plus error and error_description; do not return a normal success payload saying "not connected". Use an appropriate HTTP 401 WWW-Authenticate challenge for transport-level failures. Handle actual denied permissions separately.
3. Prefer an authenticated profile tool designated by _meta["openai/profile"]: true. Accept an empty object, resolve the profile from validated credentials and return the standard profile schema in structuredContent. Use a stable opaque id; optional display name/email/nickname may help identify the selected connection. Never accept a caller-supplied user ID to choose the identity. Obtain tenant/permissions through a separate trusted context contract where needed.
4. If both optional linking and automatic status checks are required, provide public protocol/tool discovery and a deliberately public or optional-auth status operation. It must disclose no private records without valid credentials. Its anonymous result is only "unlinked/available", not an authenticated profile. Only then consider auth.type=mixed in the package; do not flip the manifest to mixed while the server requires authentication for all discovery. Private tools remain OAuth-protected.
5. Preserve an existing provider web login where possible. Carry the OAuth request through password login/organisation selection, then return to the exact validated callback. Let the host manage token refresh. Enforce issuer, audience/resource, expiry and actual scopes. Advertise issuer identification only if every authorisation response really includes the matching iss value.
6. Keep discovery/tool auth metadata reachable by legitimate OpenAI clients through the edge/WAF, without exposing business records or bypassing token checks.

The profile/status names above describe capabilities; they are not assertions that Doctilla currently exposes those tools. Runtime skills must discover actual tools before invoking them.

## Host and distribution wiring

For private ChatGPT use, a verified registered MCP App may be mapped into the plugin via .app.json and extensions.com.openai.apps. A portable mcp.json declaration and a registered host connection are distinct. The author-supplied public ZIP intentionally contains only the portable declaration. A private development App mapping must not be carried into a customer distribution package.

For public distribution, submit through the With MCP path, complete server connection/domain verification there, and keep private .app.json references out of the public ZIP. Ordinary customers should receive that completed MCP integration; they should not each have to register a custom server manually. Public submission currently does not support adding MCP later to an existing skills-only listing. Preserve the existing public submission draft and package name. Let the Portal create the public connection binding; do not copy an owner-only App ID into the upload or create a replacement listing.

## Implementation status

| Layer | Status after this package update |
| --- | --- |
| Exact chooser, standalone and task continuity | Implemented as skill instructions |
| CIMD preference / DCR fallback | Configured in both MCP manifests |
| Call actual read tool to invoke native OAuth card | Implemented as skill routing, conditional on exposed tools |
| securitySchemes, authentication challenge, profile/status handlers | Requires current MCP server source; not verified or modified here |
| Provider login/callback and refresh implementation | Requires server/application source; not verified or modified here |
| Registered ChatGPT App or public With MCP setup | Separate host configuration; not changed by this package update |

Current MCP/OAuth server source was not included in this package rebuild. Do not present a package reference document as deployed server code.

## Official references

- https://developers.openai.com/plugins/build/auth — native OAuth challenges, tool auth policy, profiles, refresh and client identification.
- https://developers.openai.com/plugins/build/plugins — portable MCP, CIMD preference/DCR fallback and registered App mappings.
- https://developers.openai.com/plugins/deploy/submission — With MCP connection and public package requirements.

## Non-technical customer release requirement

[Customer connection guide](customer-connection.md) is mandatory for setup wording. Customers must be able to use the included sign-in flow with their existing Doctilla account; a custom MCP registration is owner setup. If customer linking is absent, show a clear owner-help message and standalone option. Do not present server configuration as an end-user workaround or describe these documentation changes as completing backend deployment.
