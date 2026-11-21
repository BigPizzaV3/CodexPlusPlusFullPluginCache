# Current connection contract

The package declares the remote Streamable HTTP MCP endpoint https://mcp.doctilla.co.uk/mcp in root mcp.json and the compatibility .mcp.json. It uses OAuth with Client Identifier Metadata Documents (CIMD) preferred and host-supported DCR fallback, OIDC disabled, and doctilla:read / doctilla:write scopes. No API key, password, token or client secret belongs in the package or ordinary chat.

Use host-supported account linking. Never decrypt local credentials, inspect token stores, construct raw authorisation URLs, invent an OAuth client, or use REST as an alternative to a failed MCP connection. The old Python API-key adapter is not required.

## Connection routine

Use [the server and packaging contract](authentication-design.md) when maintaining the integration; instructions alone cannot implement server-side authentication challenges or host registration.

Read [customer connection guide](customer-connection.md) before any user-facing setup instructions. It governs the wording, explicit fallback steps and escalation for non-technical customers. Keep the protocol details in this file internal unless technical help is explicitly requested.

Run this after "Get me connected", an equivalent explicit request to connect, or a relevant reconnect request. The initial harmless probe is governed by [startup routine](modes.md#startup-routine).

1. Preserve the current task and draft. Discover the actually exposed Doctilla tools and trusted host connection metadata. If an authenticated read already succeeded in this chat and the account has not changed, reuse it and continue without another login.
2. After connection is chosen, invoke an actually exposed authenticated, read-only profile/context tool with its real schema; otherwise use doctilla_overview with no arguments if exposed. This is the preferred chat-guided linking trigger: the tool's OAuth descriptor and server authentication challenge let ChatGPT present its native sign-in card. If it succeeds immediately, establish organisation context and continue. If it returns _meta["mcp/www_authenticate"], allow the host to handle that challenge and show its native card; never print the raw challenge, construct a URL or treat it as plain task failure. Use generic connection settings only if no callable tool/native linking flow is available. Do not create a record as a connection trigger.
3. If no tools are exposed, inspect actual host connection controls or an available supported plugin-management action. Use an existing registered Doctilla MCP connection where available. A skill selection is not account linking. Do not invent a connect tool, display a fake sign-in button, or repeatedly tell the user to type "connected".
4. Open the actual host connection/sign-in control when supported. Otherwise follow customer-connection.md: give the existing plugin details link and conditional plain-language sign-in steps, ask one simple question about what the page shows if needed, then verify internally. Let the customer complete credentials, MFA and consent on the provider page.
5. If no customer connection option exists, treat it as owner/administrator setup work. Use the guide's support note and standalone recovery. Do not ask an ordinary customer to add a custom server, change OAuth settings or obtain technical IDs. The owner-only registration and packaging requirements are in authentication-design.md and are not part of customer onboarding.
6. After sign-in, rediscover tools through the host and perform one authenticated read with an actual identity/context tool, otherwise `doctilla_overview` with no arguments if present. An installation check, OAuth callback, successful protocol handshake, public metadata response or user statement alone does not establish authorised record access. If tools become available only in a fresh chat, explain that host limitation and carry the task/draft into that chat; do not claim the present session is connected.
7. On successful authenticated retrieval, state briefly that the connection is verified, establish the organisation as far as trusted returned context allows, and resume the original task. Read-only access is sufficient; effective write permission is unverified until an authorised supported write succeeds. Follow change control for any later save.
8. If cancelled, unavailable or unsuccessful, explain the specific blocker once and continue useful standalone drafting in the same plugin, clearly unsaved. Keep live-record requests pending. Do not loop login, promise automatic repair, switch accounts silently, substitute an API key or weaken authentication. For 403 preserve the permission/entitlement distinction.

The onboardingSkill declaration offers setup after installation. It does not itself sign the user in, register an App dependency, or run a global new-chat hook. OAuth consent and host policy remain necessary. Fresh-install linking must be tested in the intended host; a valid package alone is insufficient evidence.

## OAuth settings and diagnostics

The server's public authorisation metadata was fetched on 22 October 2026 and advertised:
- issuer: https://mcp.doctilla.co.uk
- authorisation endpoint: https://app.doctilla.co.uk/oauth/authorize
- token endpoint: https://mcp.doctilla.co.uk/oauth/token
- registration endpoint: https://mcp.doctilla.co.uk/oauth/register
- PKCE: S256
- grant types: authorization_code and refresh_token
- scopes: doctilla:read and doctilla:write
- client metadata documents supported, alongside DCR
- token endpoint methods: none, client_secret_post and client_secret_basic

Use current discovery as the authority; these values are a diagnostic cross-check. The manifest requests CIMD preference with OIDC off; DCR remains a host-supported fallback. CIMD is supported by the metadata retrieved earlier in this authoring session and avoids the dynamic client-registration step. Existing working DCR links should be reused rather than reconnected solely to change the registration method. A working saved host connection may retain a prior client registration method after an update. Do not disconnect it unnecessarily. If `invalid_client` appears, record the exact error/time, try a supported DCR reconnect once if appropriate, then refer the server operator if it still fails. Do not invent client credentials.

On 22 October 2026, the server operator disabled the Cloudflare Browser Integrity Check for the MCP subdomain after an earlier browser-signature denial. Subsequent Python urllib checks retrieved both OAuth discovery documents with HTTP 200; unauthenticated MCP initialize returned HTTP 401 with the protected-resource challenge, as expected. This verifies discovery reachability and the transport challenge only. It does not verify completed OAuth, exposed tools, an authorised record read, optional linking or refresh. No authenticated Doctilla tools were exposed in the rebuild chat. Use [connection evaluations](connection-evals.md) against the exact public host release before claiming seamless installation.

## Connected record access

The observed MCP tools on 14 October 2026 were doctilla_overview, doctilla_search, doctilla_describe, doctilla_list, doctilla_get, doctilla_create, doctilla_update and doctilla_link. Discover the currently exposed tools. Names proposed in a specification, including doctilla_connection and batch/version tools, are NOT available unless discovery actually returns them.

Before connected work, use an actual identity/context tool if present. Otherwise use trusted authenticated connection metadata and returned organisation IDs from read-only domain calls; explicitly say which user/name/permission details are not exposed. An overview count is not proof of identity or write permission. Confirm an ambiguous target organisation with the user. If no organisation binding can be established, do not write.

Use IDs returned by authorised retrievals for that connection, not another organisation, a supplied name, or a fabricated UUID. A caller-supplied ID must first be retrieved and checked. For a new-record batch, bind the approved plan to the verified current organisation. Changing accounts invalidates the pending plan.

Server authentication and permissions are authoritative. A scoped, user-approved write may be attempted through an actual available write tool; do not claim effective write access before it is established. On 403 stop affected/systemic work and explain the limitation, rather than trying REST or privileged access. Missing a proposed identity-tool name is not itself a reason to invent a new server API.

Describe each resource before its first write and refresh after schema changes. The live tool schema is authoritative for fields. Lifecycle decisions in human-decisions.md are additional workflow boundaries: if a schema appears to allow a prohibited decision, do not use it and report the inconsistency.

Follow next_cursor and relevant native filters. get(include_links=true) supplements, but does not replace, native children such as car-steps, audit-findings or actions. Bound broad traversals; track visited IDs; disclose partial visibility and incomplete pagination.

Owner IDs are Doctilla assignable-user IDs. Personnel records are different. Use a supported authorised lookup if present; otherwise leave optional owners unresolved or ask for a verifiable ID. Never substitute a personnel ID.

The existing connection contract reports that the endpoint challenges unauthenticated initialize and tools/list; recheck this against the submitted host connection. OAuth metadata is reachable, but a manifest does not change this behaviour. The single package's skills must run without protected calls when standalone is chosen. Do not ask users to download or install a separate edition. If the intended host blocks installation or skill use until linking, record this as a release blocker to fix in that host/integration setup; it does not justify splitting the product. Do not claim anonymous MCP support. Full ChatGPT optional-linking/write verification is a separate release gate.

401: reconnect through the host. 403: permissions/entitlements. 404: missing or inaccessible, not proof of absence. 409: conflict/final state, reread. 422: correct against descriptor; renew approval if meaning changes. 429: honour retry guidance. Timeout: reconcile the previous operation before retrying writes.
