# Eli — OpenAI plugin submission checklist

## What is already verified
- Public MCP endpoint: https://www.hireeli.io/api/mcp-public/mcp
- Public tools visible in ChatGPT:
  - test_company_for_ai
  - scan_visibility
  - get_started
- `test_company_for_ai` successfully returned live public evidence.
- `scan_visibility` successfully returned a live public scan.
- `get_started` successfully returned Eli onboarding URLs.
- Privacy policy is live: https://www.hireeli.io/privacy

## User-only account step
1. Keep using your current OpenAI login. Your sign-in email does not have to become the public publisher name.
2. In OpenAI Platform, select the API organization that should permanently own Eli.
3. Complete **Business verification** in that organization using the exact legal company name and official records.
4. In the plugin submission portal, select that verified business identity as Developer Identity.

## Before uploading/submitting
- Publish https://www.hireeli.io/support using SUPPORT_PAGE_COPY.md.
- Publish https://www.hireeli.io/terms using TERMS_PAGE_DRAFT.md after replacing:
  - [LEGAL ENTITY NAME]
  - [GOVERNING JURISDICTION]
- Add a real square Eli logo/app icon in the portal or package.
- Confirm every public MCP tool has correct annotations:
  - test_company_for_ai: readOnlyHint=true, openWorldHint=true, destructiveHint=false
  - scan_visibility: readOnlyHint=true, openWorldHint=true, destructiveHint=false
  - get_started: readOnlyHint=true, openWorldHint=false, destructiveHint=false

## Upload
1. Open the OpenAI plugin submission portal.
2. Choose the organization that owns Eli.
3. Create/upload plugin.
4. Upload `eli-openai-plugin-submission.zip`.
5. Choose the verified business identity.
6. Connect the MCP server from the package.

## MCP connection
- URL type: Universal
- URL: https://www.hireeli.io/api/mcp-public/mcp
- Public V1 authentication: none
- Complete the domain-verification challenge shown by OpenAI.
- Host the exact token as plain text at the exact URL OpenAI gives you:
  https://<challenge-base-host>/.well-known/openai-apps-challenge
- Click Scan Tools.
- Confirm the public tool list is exactly what you intend to publish.

## Review materials
- Exactly 5 positive test cases: already in plugin.json.
- Exactly 3 negative test cases: already in plugin.json.
- Release notes: already in plugin.json.
- Commerce: false.
- Demo video: record with REVIEW_VIDEO_SCRIPT.md and add the reviewer-accessible URL.
- Reviewer credentials: none for the public V1.

## Final checks
- Website, support, privacy, and terms URLs are public HTTPS pages.
- Tool responses contain no auth secrets, unnecessary personal data, debug payloads, or internal IDs.
- Tool metadata accurately describes real behavior.
- Run all five positive cases yourself immediately before submission.
- Complete OpenAI policy attestations.
- Submit for review.
