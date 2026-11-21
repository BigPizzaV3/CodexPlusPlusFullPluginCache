# Clarity4D public ChatGPT review candidate — 30 October 2026

This ZIP creates a developer-portal draft. It has not been uploaded, submitted, approved or published to the ChatGPT directory. Official MCP Registry publication is already complete and separate.

Upload the ZIP at https://platform.openai.com/plugins using a verified Clarity4D developer identity. Root plugin.json, mcp.json and the existing official 128px PNG icon are included. No application source, credentials, participant records or questionnaire answers are bundled.

In MCP setup, enter the existing clarity4d-chatgpt secret only in the portal. Do not paste it into chat or edit it into the ZIP. Confirm the portal-displayed exact OAuth redirect against the Keycloak client before connecting. The currently verified custom connector callback is https://chatgpt.com/connector_platform_oauth_redirect; do not assume the public submission uses the same callback. If different, add only the portal's exact callback while preserving the working connector's callback.

Run metadata checks and MCP discovery/scan, then copy the Issues output for correction. Category Productivity is a draft selection and may need matching to an available dashboard category. Developer identity, country availability, reviewer access and any legal acknowledgments require the owner's confirmation in the portal. Do not start a payment for review testing.

IMPORTANT COMMERCE REVIEW ISSUE: the ZIP truthfully declares commerce=true. The running server still exposes all nine tools including begin_checkout, and the browser journey still has Upgrade to Full Profile. Current OpenAI guidelines restrict digital sales and upgrade promotion, including indirect freemium upsells. Adding a free snapshot or renaming a button does not remove this issue. This candidate is for draft validation and identifying review findings; do not treat it as ready for final submission until commerce issues are resolved or OpenAI provides an applicable permitted route. No production behavior has been hidden or changed to influence review.

The review metadata contains exactly five positive and three negative cases. These describe expected behavior; they are not a claim that all cases have been run against this candidate. Existing browser/production MCP snapshot tests passed. New assessment, unauthorized-access and negative-scenario review tests remain outstanding. Reviewer access must be provided through the secure portal, not this file. Email-code login may require a dedicated reviewer-access arrangement.

Official references:
https://developers.openai.com/plugins/deploy/submission
https://developers.openai.com/plugins/plugin-guidelines

Version 1.0.3: user-supplied privacy PDF URL selected; public release notes updated; verified hosted walkthrough URL included. Privacy PDF automated accessibility and coverage remain unverified. Reviewer credentials remain outside this ZIP.

Version 1.0.4: Education & Research category selected with owner agreement. Privacy URL now points to the unchanged PDF hosted on mcp2.clarity4d.com; server-side public HTTP, MIME and checksum checks passed. OpenAI metadata rescan remains pending. Assessment-specific policy coverage remains outstanding.

Version 1.0.5 uses an HTML transcription of the same privacy document. Deploy the HTML route before uploading this version. No assessment-policy coverage has been added or claimed.
