Five-Minute Math: public draft package, version 1.0.3

Purpose
Prepare a NEW public submission draft for the verified anonymous MCP endpoint:
https://five-minute-math-worksheets.techancedmarketing.com/mcp
Keep the two existing public drafts and the working private Sites plugin unchanged.
This ZIP does not update those drafts, submit anything for review, or publish a listing.

Changes from the selected 1.0.2 draft
- MCP endpoint changed to the public anonymous bridge.
- Package version and release notes updated to 1.0.3.
- Two review-case setup descriptions no longer require a separate service sign-in.
- README replaces obsolete OAuth-blocker and replacement-upload instructions.
All listing text, icon bytes, starter prompts, case prompts/expected outputs, eight-case coverage, policy URLs, existing recording URL, publisher, free-use declaration, and unrestricted country targeting are preserved.

Authentication and service
The new public MCP endpoint needs no separate service sign-in or OAuth client credentials. Do not add guessed OAuth fields, tokens, secrets, or private .app.json/apps bindings to the upload. The host still manages its own account and plugin installation. The anonymous bridge calls fixed ordinary public math APIs; it does not proxy the protected Sites /mcp endpoint. Worksheet generation, PDFs, and the embedded workspace remain provided by the existing Five-Minute Math Site. No student profiles, scores, account database, or paid AI generation are introduced.

Preparation evidence
Eleven live anonymous MCP/PDF/resource checks on the new endpoint were reported passed on October 5, 2026. This package has local archive/schema/static validation; it has not been uploaded or validated by the new submission draft. New-draft domain verification, exact-saved-version tool scans, review cases, and actual ChatGPT host behavior remain separate checks.

Existing recording
https://drive.google.com/file/d/1rlRMx-WUn7ReoFC1-Ld2BbANQ6NCDF4H/view?usp=sharing
The existing real five-minute recording is retained as workflow evidence. It predates this endpoint change and is not a newly recorded anonymous-endpoint demo. Its prior anonymous download, full decode, and user-reported incognito playback were verified. Confirm current reviewer access and suitability for the submitted version before review; refresh it if the earlier connection steps would mislead reviewers.

Required before final public submission
- Review/update the linked privacy policy to distinguish the retained private Sites login from the new anonymous bridge and accurately cover Cloudflare processing/logging based on the actual account settings. Existing v11 policy text says tool calls check a Site user ID and describes OpenAI hosting/authentication; that text does not yet clearly cover the new public path. The published policy has not been changed by this ZIP.
- Verify all four published listing/policy links and the retained demo remain reviewer-accessible and accurate.
- Complete domain verification for this new MCP hostname; do not reuse or overwrite either old draft's challenge token.
- Connect the actual new saved draft, confirm anonymous authentication, run its current tool scan and review cases, and inspect imported metadata and country targeting.
- The authorized publisher must complete legal/policy attestations. Any requested reviewer-access fields should accurately say that the endpoint requires no separate service login; never supply the publisher's credentials.

Public upload structure
The ZIP contains one folder matching the unchanged package name, with plugin.json, mcp.json, README.txt, and the original assets/five-minute-math-icon.png. It contains no private app bindings or credentials. The original selected 1.0.2 draft export is preserved separately.

Official references
https://developers.openai.com/plugins/build/plugins
https://developers.openai.com/plugins/deploy/submission
https://agent-plugins.org/schemas/1.0.0/mcp.schema.json
