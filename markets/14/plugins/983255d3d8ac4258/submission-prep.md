# Sellerity Roleplay public plugin: submission prep

Package: `sellerity-roleplay`, version `1.0.5`  
Form factor: public ChatGPT plugin using Sellerity's hosted Streamable HTTP MCP endpoint. It does not depend on Codex desktop or a local server.

## Completed

- Portable Agent Plugins manifest and remote MCP configuration, scoped to `/mcp/roleplay`.
- OAuth configuration is included in `mcp.json` for the hosted MCP server. The public client ID and standard token endpoint auth method are packaged; the client secret is intentionally not in the ZIP and must be entered only in the OpenAI portal's secure connection setup.
- Backend routes now include the OpenAI challenge-token endpoint and a protected-resource metadata endpoint that normalizes the Clerk issuer identifier. Local tests passed; these changes are not deployed.
- Public website, support, privacy, and terms URLs verified in Chrome on 2026-10-22:
  - https://sellerity.co/
  - https://sellerity.co/support
  - https://sellerity.co/privacy
  - https://sellerity.co/terms
- Listing icon copied from the Sellerity website's 512 × 512 web app manifest icon.
- Five positive and three negative test cases drafted from `backend/mcp/roleplay_server.py`.
- Review fixtures are set up specifically for review: use `admin@test.com` for the demo and manifest cases (account, bots, bot creation, scorecard creation, and inaccessible-company boundaries). The reviewer should open Sellerity from the ChatGPT connection flow and sign in at Sellerity's app (`https://app.sellerity.co/`) with that admin account. Enter credentials only in the portal's secure reviewer-access fields; do not add passwords to this package or the demo recording.
- Tool annotations in the local server source now explicitly include boolean `readOnlyHint`, `openWorldHint`, and `destructiveHint` values. The production MCP service needs a deployment of this source update and a fresh portal scan before its annotations are verified.
- Worldwide publication targeting is set with an empty `publication.countries` allowlist.

## Still required before review submission

- Confirm the verified publisher identity in the OpenAI portal. The manifest currently names Litemind Labs, matching Sellerity's published policies.
- Confirm the published product flow meets current plugin guidelines before submission.
- The published privacy policy says Sellerity is not directed to people under 18; current plugin guidelines say plugins must be suitable for general audiences including ages 13–17. Confirm eligibility language and age handling with the policy owner/legal reviewer before submission.
- Record and host an actual reviewer-accessible demo video, then add its URL as `extensions.com.openai.review.demo_recording_url`.
- In the portal's secure reviewer-access fields, provide the review account credentials (at minimum `admin@test.com` for manifest and demo cases). The cases are already written in the correct manifest location; run them against the saved review connection and record outcomes during the portal test step, after the demo walkthrough is agreed.
- Add an actual reviewer-accessible demo video URL. No recording has been made or verified yet.
- Upload and connect the MCP in the plugin dashboard, check the scan and imported metadata, complete publisher/domain verification, and resolve any portal findings.
- The current portal draft is still version `1.0.0`; `plugins/releases/sellerity-roleplay-v1.0.5.zip` is prepared but not uploaded. The portal's challenge token must be set as `OPENAI_APPS_CHALLENGE_TOKEN` in the production backend and deployed before domain verification can succeed. No active `gcloud` account is configured in this workspace, so production deployment is pending owner action/access.
- The upload dialog currently selects the verified business identity “Sellerity”; the manifest developer name is “Litemind Labs.” Confirm that this is the intended publisher identity before replacing the draft.
- After upload and domain verification, enter the Clerk OAuth client secret only in the portal's secure connection setup, connect, and verify the sign-in and tool scan. Do not put the secret in source, the ZIP, or the backend environment.
- The user reports that Chrome is now signed in to the requested `hello@sellerity.co` ChatGPT account; confirm publisher identity in the portal before submission.
- The authorized developer must personally complete required legal/policy attestations and the final submit-for-review action in the portal.

## Demo recording plan

See [`demo-script.md`](demo-script.md) for the full recording flow, narration, prompts, fixture safeguards, and post-recording checks. The script covers all eight manifest cases (five positive, three negative) on the admin account only; it is not a recording or evidence that those cases have passed.

The available CUA controls provide browser interaction and screenshots but no video recording. Start a macOS screen recording (for example, QuickTime Player or Screenshot) after the dedicated test session is ready; I can then operate the browser walkthrough, stop once the result is shown, and help verify the saved playback. Do not grant macOS screen-recording permissions or capture private data without the user controlling that permission.
