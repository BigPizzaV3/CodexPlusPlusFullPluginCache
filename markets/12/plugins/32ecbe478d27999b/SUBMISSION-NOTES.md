# Submission preparation status — 0.1.8

Not ready for submission. All eight review cases are drafts and have status: Not run.

Public listing URLs are included. The support URL uses the public Filament homepage, which exposes support@filament.dm. The listing category is Communication; dashboard acceptance has not been verified.

The existing requested description is preserved and extended with concrete collaboration capabilities and access limits. Icon references use documented ./-prefixed paths.

## Demo setup and recording

Demo environment:
- Login server: https://chat.filament.dm
- MCP endpoint: https://api.filament.dm/mcp/agents
- Use a dedicated production demo principal and agent with sample data in a demo community, isolated from unrelated users' content through normal account and channel permissions.
- Enter the demo account credentials and exact sign-in instructions in the dashboard's secure reviewer-access fields. No login phone number, auth code, or other credentials are bundled in this package.
- Reviewers must be able to complete sign-in using the supplied account without access to the creator's phone or inbox.
- Authenticate the plugin against the declared production MCP endpoint. Ensure the Review Demo channel and sample messages are accessible through that same account and endpoint.
- Record the walkthrough using this production demo account and connection. Do not claim account readiness or passing test results until they have been verified.

Prepare a dedicated test principal and agent, a community with a unique Review Demo channel, and the two sample messages specified in the test cases. Keep unrelated private channels inaccessible. Run each case in a development connection using this test account. Record Passed, Failed, or Blocked privately with actual tool evidence. No cases have been run by this package-generation step.

Record the actual identity, channel listing, summary, search, and test-principal message flows, plus the three negative cases. Keep credentials and unrelated personal content off screen. Host a playable recording accessible to reviewers; then add its real URL as extensions.com.openai.review.demo_recording_url in both manifests.

Enter reviewer credentials, exact login URL, demo workspace details, and sign-in instructions only in secure dashboard fields. Do not place credentials in the ZIP. Reviewers need working access without relying on the creator's phone or mailbox.

Still needed: tested cases, demo recording URL, reviewer access, confirmed verified publisher identity, supported countries, commerce declaration, final domain/OAuth connection checks, and legal/policy attestations.
