# Remindlo public submission draft — incomplete

The supplied listing text is preserved verbatim. Publisher: Bizmut Piotr Bednarek (operator of Remindlo). All available countries: publication.countries=[] deliberately removes restrictions. No translations requested.

## Verified information
All four listing URLs were accessible through public web retrieval on 2026-09-29. Public integration documentation confirms the supplied endpoint and OAuth. Tool schemas exposed by the connected Remindlo app support the stated conversational operations. No direct email-sending tool is exposed; the opening paragraph describes the Remindlo service.

## Remaining preparation
- Icon: DONE. assets/icon.png (512x512 PNG, same file as the site favicon) is used as both logo and composerIcon.
- Optional dark-mode assets and brand colours may be added if requested.
- Verify Streamable HTTP transport and live OAuth connection for this exact submission; transport in mcp.json is provisional pending direct protocol validation.
- Tool annotations: DONE. Verified against supabase/functions/_shared/mcp-tools.ts: all five tools set readOnlyHint and openWorldHint; the two write tools also set destructiveHint=false and idempotentHint (true for upsert_contact, false for send_message).
- Category and commerce selector must be mapped to supported target-portal values. Commerce description records allowance use AND possible off-platform automatic charges; this must not be represented as unconditionally free usage.
- Publisher identity and domain verification are not verified by accessible policy pages.
- All 5 positive and 3 negative review cases are NOT RUN. Seed a dedicated test account, validate date filter boundaries, rehearse and run cases. Do not use real customer numbers for test sends.
- Demo recording: DONE, https://youtu.be/hJS3cMFbvkg (unlisted), recorded on the test account peter+anthropic@remindlo.co.uk. Reviewer account access belongs only in secure dashboard fields, never this ZIP.
- Privacy policy covers platform processing but does not explicitly document the ChatGPT/MCP integration, OAuth permission/revocation, or associated contact/message disclosures. Confirm actual practices and extend the published policy where needed; policy completeness is not certified.
- Help article uses support@remindlo.co.uk while the supplied primary contact and terms use contact@remindlo.co.uk. Confirm both work or update the article.
- Complete target validation and saved-portal metadata verification before calling the package ready.

## Suggested demo (about 3 minutes)
Use the existing working ChatGPT development connection with a dedicated account and sample data. Show: campaign listing; search for Jasmine Bleep; date-filtered customer listing; update its due date and enrol it in the existing Vehicle Service campaign with confirmed consent; send one SMS to an operator-controlled phone after reviewing the recipient, text and charge; ask to create a campaign and show the unsupported-operation explanation.

Disable auto top-up on the test account, ensure adequate SMS allowance, and rehearse before recording. Start a screen recorder, show real prompts and readable tool results, then stop. Play back the recording and remove any exposed secrets or unrelated customer data. Host the recording at a reviewer-accessible HTTPS URL and verify playback without a private login. A script is not a completed demo.

Archive prepared only. Nothing uploaded, submitted for review, or published.
