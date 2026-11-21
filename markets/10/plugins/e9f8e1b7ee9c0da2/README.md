# WisBot plugin package

This package connects ChatGPT to the supplied WisBot MCP endpoint:
`https://agents.wisbot.ai/mcp`.

## Before public submission

This is a connection package, not a public-submission-ready listing. Confirm the MCP transport and authentication in the Developer Portal, and complete the public listing and review requirements:

- Verified publisher identity
- Public plugin website, support page, privacy policy, and terms of service URLs (the current support URL points to the home page, which offers a booking/contact path; a dedicated support page would be stronger)
- Square app icon suitable for the listing
- Supported countries and commerce declaration
- Five positive and three negative review cases based on the server's actual tools
- A reviewer-accessible demo recording and reviewer access, if authentication is required

Do not claim these are complete unless they have been verified.

## Public upload and publication steps

1. Open the OpenAI Developer Portal's Plugins area and choose to create or upload a plugin.
2. Upload this ZIP as a draft and select the intended verified publisher identity.
3. Review the imported name, descriptions, server endpoint, and publisher identity.
4. Convert/connect the remote MCP server. Confirm the endpoint uses the supported transport, complete OAuth or other authentication if prompted, and verify tool discovery.
5. Add the verified public listing URLs, icon, country targeting, release notes, commerce declaration, review cases, demo recording, and reviewer access.
6. Run every review case against the saved draft. Fix connection or validation errors and verify the saved values.
7. Complete the portal's required legal and policy attestations as the authorized publisher, then submit the draft for review.
8. After approval, verify the approved version and country targeting, then publish it from the portal.

Uploading creates a draft; it does not itself submit, approve, or publish the plugin.
