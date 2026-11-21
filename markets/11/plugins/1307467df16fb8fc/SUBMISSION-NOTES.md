# SmartReply 1.0.7 — preparation status

Package fixes completed:
- Added Agent Plugins 1.0 plugin.json and portable mcp.json.
- Moved portable listing fields to extensions.com.openai.interface.
- Set portable MCP transport to streamable-http; retained the older client overlay.
- Preserved plugin identity, MCP endpoint, icons, prompts and skill.
- Added five positive and three negative review cases and release notes.

Review cases: NOT RUN. They are based on the supplied skill and available SmartReply Development tool contracts; production tool parity and behavior remain unverified.

Before submission:
- Supplied walkthrough URL is included as extensions.com.openai.review.demo_recording_url: https://youtu.be/qyEE1D3FlAY. Playback, permissions and coverage still need confirmation.
- Confirm intended country targeting and applicable commerce declarations; set them in the ZIP or available portal fields. Unknown values were deliberately omitted.
- Confirm the selected verified publisher identity and supported portal category.
- Provide dedicated reviewer access only in secure portal fields, never in this ZIP.
- Verify OAuth, actual production tool schemas and boolean readOnlyHint, openWorldHint and destructiveHint annotations.
- Run the included cases against the actual saved submission version and fix any failures.
- Complete portal verification, scans and attestations.

Suggested demo: show account setup status, persisted Facebook connection status, configuration conflict search, an instruction preview without saving, a completed sandbox response, and the unsupported public-post request. Keep credentials and real customer data off screen.

The ZIP is a corrected package, not a claim that live validation or public review has passed.

## New submission package

Package name: smartreply-customer-service
Version: 1.0.7
This is a separate author-supplied package, not an update to the app-6aa08b41ee108191b403de0e16e1c269 package. There are no app binding declarations. The MCP endpoint remains https://app.smartreply.io/api/mcp and OAuth is declared for the new connection. The portal assigns any new backend plugin/app IDs; a package rename does not itself create a submission or guarantee acceptance. Configure and verify the new connection in the intended submission flow, including the supported OAuth client/callback. No online submission has been performed and no existing app or connection was changed.

## Listing update

Updated both manifests with the AI customer service automation subtitle and platform-specific description. Hosted tools, MCP configuration, skills, and review cases are unchanged. This metadata revision has not been uploaded or submitted for review.

## Listing title update

Set displayName to SmartReply AI Customer Service and shortDescription to Automate customer replies in both manifests. Long description and all runtime components are unchanged. This package has not been uploaded or published.
