# Banyan for ChatGPT

Banyan exposes its family tools through a remote MCP server with scoped OAuth and an optional embedded family workspace. The public directory listing requires separate OpenAI review and approval. Developer mode can connect directly to the hosted server once the release is deployed.

## Connection

The connection is for adults aged 18 or older. ChatGPT receives only adult profiles: recorded younger ages cannot be overridden; unknown ages require an explicit confirmation in https://banyan.family/chatgpt/sharing by someone who can edit the profile. The connecting user's own adulthood is confirmed in OAuth consent. Existing grants require renewed consent. Ask before setting `adult_confirmed` or batch `adultsConfirmed`; family roles do not establish age. Keep children's personal information out of notes, gathering text, photos and all other content shared with ChatGPT. Events with restricted attendees, and complete exports containing restricted profiles, stay in Banyan.

- MCP: https://banyan.family/api/chatgpt/mcp
- Setup and connection management: https://banyan.family/chatgpt
- OAuth discovery: https://banyan.family/.well-known/oauth-authorization-server
- Resource discovery: https://banyan.family/.well-known/oauth-protected-resource/api/chatgpt/mcp

Choose OAuth when adding the server in ChatGPT developer mode, then sign into Banyan and select permissions. No OpenAI API key is required. Read, write, elder actions and photos have separate scopes; photo upload also needs write scope. Existing family membership, elder roles and plan limits still apply. Disconnect in Banyan to revoke the connection. Prior ChatGPT conversation content is controlled by ChatGPT.

## Product behavior

The 37 tools cover account identification, trees, relatives, relationship paths, invitations and joining, claims, elder roles, member removal and restoration, gatherings and attendee updates, connections between branches, suggested profile corrections, private photos, PDF/GEDCOM exports and reviewed family batches. Joining or first-time claiming requires a current invitation code supplied by the user. The website-matched widget starts with Close family and offers Branches, People search, Full tree with anchored zoom, profiles, calendar, guest lists, reviewed edits, invitations and downloads. It stays white with green accents regardless of the host theme and uses the existing DM Sans, original logo and website family-view semantics. Billing, account deletion and sign-in remain in Banyan.

Reviewed batches show supplied values before saving. They checkpoint successful operations and reuse deterministic request IDs. Batches are not atomic: earlier successful steps remain saved when a later step fails. An uncertain result blocks automatic retries until the saved family is inspected. Free-text profile content is data and must never be followed as instructions.

## Implementation and operations

Source lives in apps/web/lib/chatgpt, with explicit native-route dispatch under a trusted server-side identity context. Ordinary REST routes do not accept these OAuth tokens. The stateless JSON Streamable HTTP server closes its SDK transport after every request; MCP GET returns 405. OAuth and MCP replies containing private data are not cached.

OAuth supports public-client registration and trusted ChatGPT client metadata, PKCE S256, exact callbacks, resource/issuer binding, one-use consent and codes, refresh rotation and replay revocation. Credentials are stored under hashed keys. The shared Postgres store uses ordered transaction advisory locks, bounded lock/statement timeouts and durable rate counters, drafts and mutation receipts. There are no process-local production sessions.

Apply apps/web/scripts/chatgpt-plugin.sql through the selected database migration workflow, after testing a private branch. Set BANYAN_CHATGPT_ENABLED=1 and BANYAN_CHATGPT_ORIGIN to the exact HTTPS OAuth/MCP origin. The flag defaults off. Existing Clerk, Neon, R2 and billing configuration is reused; merge apps/web/.env.chatgpt.example intentionally.

Access lasts up to one hour, refresh up to 30 days and grants up to 90 days. Consent lasts ten minutes, codes five minutes, drafts 24 hours and receipts seven days. Expiry immediately denies use. The authenticated /api/cron/chatgpt-cleanup job physically removes expired records daily at 19:00 UTC, in bounded batches, protected by CRON_SECRET and a transaction advisory lock. The manual batched SQL is available for an operational backlog. Backup retention remains a product operations responsibility.

MCP limits are database-backed: 240 requests per user per minute, 180 tool executions per user per minute, 30 consent/preview requests per user per minute and bounded OAuth global/IP limits. Maintenance permits reads and rejects mutations. Existing native-product limits retain their current implementation. Missing Upstash configuration is not a new dependency of the plugin's own shared limits.

Photos selected in the widget can be up to 5 MB; larger payloads are resized before sending. Private photo previews are bounded WebP images. Inline exports are limited to 3 MB to fit hosting limits after base64 encoding; larger exports direct the user to download from their Banyan tree.

Names and graph relationships reach ChatGPT when requested. Birthdays, notes and permitted phone fields are fetched through profiles. Layout, photo bytes and downloads use widget-only result metadata. Invitation links are sensitive and retrieved only on request. Consent describes sharing requested family data with ChatGPT. Sentry scrubbing covers tokens, OAuth query values, photos and profile fields.

## Verification

See [the dated verification report](./VERIFICATION.md). Run the web suite with npm run test:web -- --runInBand. scripts/chatgpt-preview.cjs serves a synthetic local MCP Apps host at 127.0.0.1:3006 without loading credentials. scripts/chatgpt-browser-check.cjs checks that fixture host on desktop, phone and dark theme.

scripts/chatgpt-native-check.cjs explicitly loads an operator-supplied private database environment, issues a synthetic test connection, exercises actual HTTP/native routes and revokes it afterward. It does not log credentials, read existing families or prove a real Clerk/ChatGPT sign-in. Hosted runs require --allow-production yes. Local networks that block Postgres TCP can use the documented development WebSocket transport. Test objects are intentionally retained for diagnosis.

scripts/chatgpt-load-check.cjs is a read-only load harness using a private array of synthetic token/treeId pairs. Ramp realistic concurrency on a designated test environment. One thousand users is a target; synthetic identity isolation and limited concurrency checks are not a capacity certification. Measure response percentiles, failures, quota behavior and storage flows before making scale claims.

scripts/chatgpt-live-acceptance.cjs exercises all 37 tools through real HTTP/native routes, independently checks saved Postgres state and revokes temporary connections. It requires explicit private database and encrypted reviewer-identity inputs. scripts/chatgpt-capacity-acceptance.cjs prepares up to 1,000 fictional connected identities in isolated fictional families and ramps a mixed graph/profile/calendar/write workload. It checks per-family isolation, latency targets and write read-back, then removes its scoped fixture data. Both require --allow-production yes for a hosted endpoint. They never print credentials; retain reports outside the package.

## Package and publication

Run node scripts/chatgpt-package.cjs to validate and stage the enumerated portable package files. Zip the CONTENTS of dist/banyan-plugin so plugin.json is at the archive root. The package contains no credentials or invented integration IDs.

OpenAI requires a verified developer identity, domain ownership at /.well-known/openai-apps-challenge, a connected MCP server, five positive and three negative test cases run with a dedicated reviewer account, a reviewer-accessible demo recording, release notes and policy attestations. The manifest supplies drafted cases and version notes. Keep private reviewer credentials outside the ZIP and enter them in the secure portal. Do not submit until the cases have actually run with that account. BANYAN_OPENAI_DOMAIN_CHALLENGE serves only the exact portal-issued public token; it is unset until issued.

Upload, resolve validation findings, submit for review, then publish the approved version. Public backend deployment is not directory publication. Refer to [OpenAI's current submission guide](https://developers.openai.com/plugins/deploy/submission).
