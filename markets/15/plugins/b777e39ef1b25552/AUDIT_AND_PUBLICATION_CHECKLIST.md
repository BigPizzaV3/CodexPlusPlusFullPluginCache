# Voico v0.3.0 — Independent package audit (2026-11-03)

## Conclusion
**Package is ready for a dashboard upload and automated validation, but NOT certified ready for public review or publication.** The publisher must complete MCP connectivity/authentication, domain verification, reviewer materials, and privacy checks.

## Corrections made
- Reduced positive test cases from eight to exactly five; retained three negative test cases, as required for initial review of a single MCP server.
- Removed the subscription reference from the public long description in response to the screenshot warning; no prices, promotions, or offers are advertised.
- Added publisher support email and company website to author metadata.
- Declared the existing Voico skill as an onboarding skill.
- Preserved the exact visual pixels of the uploaded 140x140 Voico favicon; PNG encoding differs from source but RGBA pixels are identical.
- Preserved MCP endpoint `https://mcp.voico.ai/mcp` and all bundled skill references.

## Verified locally
- Plugin manifest and MCP manifest parse as JSON.
- Exactly one plugin root, one MCP server, one skill, five positive and three negative cases.
- All relative image and skill paths resolve; icon is square 140x140 and below 5 MiB.
- All bundled skill reference Markdown files exist.
- ZIP integrity and unencrypted entries checked.
- Website, legal privacy, terms and Impressum pages were found publicly accessible during web review; Impressum is a legal contact page, not a dedicated technical support page.

## Publisher actions before submitting for review
1. Upload ZIP as new version to the **existing** Voico plugin, not a second plugin.
2. Inspect portal metadata findings and confirm icon preview.
3. Complete MCP domain verification and Connect; server authentication is not configured in bundled `mcp.json`. **Do not assume unauthenticated access is suitable.** If server requires OAuth, add correct OAuth settings and upload a new version. Do not put secrets in ZIP.
4. Run the MCP tool scan and verify all actual tool names, input schemas, authorization and side-effect controls. The ZIP cannot prove server-side permissions.
5. Provide dedicated reviewer account, representative non-sensitive test data, opt-in phone test number and accessible demonstration video in the portal.
6. Have the Voico privacy/legal owner confirm that the privacy notice adequately describes the ChatGPT/MCP integration and data disclosures. An automated policy assessment was previously inconclusive.
7. Confirm `https://www.voico.ai/impressum` is accepted as supportURL; a dedicated public support page may be preferable.
8. Wait for all required automated checks to finish; fix blocking findings before clicking Submit for review.

## Limits
The ZIP contains instructions and metadata, not the running MCP implementation. Live endpoint, OAuth, tenant isolation, telephony consent, call billing, real tool execution, review acceptance, and OpenAI approval cannot be guaranteed from this package. The previous portal screenshot is evidence of outstanding issues, not a fresh scan.

## Source documentation
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors
- https://developers.openai.com/plugins/build/plugins
