# signageOS public submission draft

Not ready for public submission. No private plugin was created and no public submission was uploaded.

## Confirmed configuration
- Endpoint: https://mcp.root.signageos.io/mcp
- Transport: Streamable HTTP (supplied by publisher; authenticated handshake not yet tested).
- OAuth: provided client, no client secret, scopes openid profile email offline_access.
- Endpoint returned 401 with protected-resource metadata advertising https://auth0.signageos.io/ as authorization server and https://mcp.root.signageos.io/ as resource.
- Authorization-server discovery returned authorize and token endpoints and S256 support.
- All supplied listing URLs were accessible; PDF contents identify signageOS and its services. Actual MCP data-practice coverage remains to be confirmed.

## Remaining preparation
- Publisher confirmed OAuth audience: https://mcp.root.signageos.io/. Record this value in the supported connection setup; no undocumented audience field is added to mcp.json. Authenticated audience behavior remains untested.
- Live checks through the connected signageOS Root plugin succeeded: docs_search, graphql_context, inventory_search, inventory_focus, inventory_details, and a read-only graphql_query listing three device records. These checks do not verify the saved public submission or every tool annotation. No devices were changed.
- Confirm intended verified legal publisher identity in the submission portal. signageOS business entity was requested; legal documents identify signageOS s.r.o. No unverified developer-name override is encoded.
- Country targeting confirmed: all available countries (publication.countries is an explicit empty array). MCP has no payments or purchases; sign-up and payments occur separately in the signageOS web console. Commerce description is encoded; the final portal commerce selector must be checked.
- Branding complete: publisher-preferred navy-blue square from signageOS-square-bw copy 2.png, copied unchanged to assets/signageos-blue.png (PNG, 2001x2001, 54,421 bytes). Used for both listing logo and composer icon. Optional dark-mode assets and colors omitted.
- Five positive and three negative review cases are now encoded in plugin.json based on discovered tools. Underlying read-only tool checks succeeded; full conversational routing cases and dedicated reviewer-account runs remain Not run. Verify all top-level tools have correct readOnlyHint, openWorldHint, and destructiveHint booleans before submission.
- Recording supplied: signageOS-Root-MCP-preview.webm, 75.937 seconds, VP8/Opus, 1058x720, 1,028,870 bytes. Full media decode passed. Sampled frames show installation/connection and an online-device count grouped by applicationType; final table is readable. This is evidence of that recorded workflow, not a verification of tool arguments or a current fleet count. No credentials were visible in inspected frames; audio and every frame have not been manually reviewed. Demo hosting verified: Drive permission is anyone/reader; anonymous download succeeded and SHA-256 matches the reviewed attachment. The verified Drive view URL is recorded in review.demo_recording_url. An unsupported-request boundary example is not present in this recording.
- Prepare a dedicated reviewer account and secure dashboard access instructions. Never include credentials in this archive.
- Verify OAuth redirect configuration, developer/domain verification and portal requirements. Final draft upload, review submission and publication are distinct steps.

## Listing draft
Name: signageOS
Subtitle: Digital signage operations
Description: Connect ChatGPT to the signageOS MCP service using your signageOS account. Available operations depend on the connected service and your account permissions.

Listing description and prompts updated using the connected signageOS Root tool inventory. The public display name remains signageOS as requested; the demonstrated development connection is named signageOS Root.
