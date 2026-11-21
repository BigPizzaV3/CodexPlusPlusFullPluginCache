# Owner-operated production release checks

Status: package static validation passes with the documented OAuth extension checked separately from the published base schema. The public protected-resource, authorization-server and OIDC metadata return HTTP 200; the unauthenticated MCP endpoint returns HTTP 401 with a Bearer resource-metadata challenge. The checks below remain unverified unless separately recorded. No plugin source code was executed by the repair tools.

## Authentication and service

- Verify the production endpoint supports MCP Streamable HTTP initialize, tools/list, and the five documented tools with valid input/output schemas. Record host/protocol versions, dates, and results.
- Complete an actual OAuth 2.1 flow. Public metadata advertises dynamic registration and PKCE S256, but this does not prove registration, callbacks, consent, code exchange, or refresh behavior works. The supplied `email` scope is advertised; confirm it is the intended permission for note access.
- Confirm each request validates token signature, issuer, audience/resource, expiry, and intended scopes. Reject missing, expired, forged, revoked, and wrong-audience credentials; document reconnect/revocation behavior.
- Verify every note/folder query authorizes the authenticated user. With two test users, attempt another user's note ID and search/overview/folder requests. No cross-account content, counts, or snippets may leak.
- Verify Supabase row-level security or equivalent explicit authorization, especially when service-role credentials bypass RLS. Store secrets only on the server or in the secure connection flow.
- Check pagination, empty libraries, missing notes, malformed arguments, rate limits, timeouts, and service errors. Avoid exposing tokens or transcript contents in logs/errors; document retention and deletion policies.
- Verify tool annotations reflect behavior. For genuinely read-only library tools, readOnlyHint should be true and destructiveHint false; justify openWorldHint based on actual external interaction. Provide required annotation justifications and a current production tool scan.

## Review and publishing

- Run all five positive and three negative cases declared in the manifest in supported hosts and save results. Negative prompts alone do not prove backend isolation.
- Verify website, support, privacy, and terms pages are accessible and accurate; confirm provider identity and support contact.
- Record a walkthrough showing connection and principal tools. Enter a reviewer-accessible video URL in the secure dashboard or add review.demo_recording_url to BOTH manifests' extensions.com.openai.review. Replace any previously imported homepage demo URL in the dashboard; omission may preserve prior values.
- Supply reviewer test credentials through the secure dashboard form only. Never put credentials or reviewer access instructions in this ZIP.
- Complete domain verification for the MCP host and confirm ownership/control of its Supabase domain or migrate to a controlled custom domain and update BOTH MCP files together.
- Confirm the imported publication targeting removes plugin-specific country restrictions, as requested by the owner. Verify the intended business publisher (Notely Voice Pro) and release version.
- No custom UI is declared and no screenshots are shipped. If a future tool scan reports custom UI, provide one genuine plugin screenshot per starter prompt, exactly 706 pixels wide and 400-860 pixels tall, and update both listing interfaces.
- Obtain host skill/security scan success, developer verification, policy attestations, and dashboard validation. Local JSON schemas do not validate OpenAI extension semantics or certify security.

## Controlled install acceptance

- Validate a clean install and install during an existing conversation. Confirm setup invokes the packaged skill and account connection works.
- Exercise the documented five tools with synthetic test notes; compare returned results to known account data.
- Confirm transcript prompt injection cannot make the host disclose secrets, bypass account permissions, or execute unrelated actions.
- Confirm reconnect, disconnect, provider revocation, disable, and uninstall behavior. Confirm authorization revocation independently of package removal.

After completing these checks, rebuild/version the package if configuration changes, repeat static validation, and record the successful dashboard/tool-scan evidence.
