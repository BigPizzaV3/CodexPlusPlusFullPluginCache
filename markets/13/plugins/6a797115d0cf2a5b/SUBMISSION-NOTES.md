# Rockhopper submission preparation

Target OpenAI organization: org-b19JygUJbjVe6HMwHAfJHu39
Select this organization in https://platform.openai.com/apps-manage. Organization ownership is selected in the portal, not set by the ZIP.

Included: supplied listing description; square 512x512 PNG logo (original centered with transparent padding); MCP endpoint; OAuth dynamic client registration; read-write scope to support the supplied commit, review, comment, and rename workflows; support email in author metadata; verified public website, privacy, contact, and terms URLs.

The supplied documentation URL https://docs.rockhopper.co/it-setup/mcp-server redirects to sign-in. The listing uses the public contact page, which provides support@rockhopper.co.

STATUS: Draft package, not yet ready for final submission. No portal upload or submission has been performed. The organization and publishing identity are not verified by preparing this ZIP. Capabilities come from the creator's description; authenticated tool discovery, schemas, annotations, and behavior remain unverified.

Remaining before final submission:
- Confirm the selected verified publisher identity (package currently says Rockhopper).
- Specify supported countries and whether purchases/payments are involved; omitted rather than guessed.
- Verify playback and reviewer access for the supplied demo recording URL.
- Prepare a dedicated reviewer account with sample files through secure portal fields; do not put credentials in this ZIP.
- Discover actual tools after OAuth; check boolean readOnlyHint, openWorldHint, and destructiveHint annotations.
- Verify test fixtures and run the five positive and three negative cases included in plugin.json. No cases have been run during this update.
- Complete domain verification, scans, and required declarations in the portal.

Review materials added October 26, 2026:
- Exactly five positive and three negative cases are in plugin.json at extensions.com.openai.review.test_cases.
- User-supplied walkthrough URL: https://www.loom.com/share/1f96544e5c944b2fb38040b2ae300795
- Playback and reviewer access could not be verified: the retrieval tool could not access the Loom URL.
- All eight cases: Not run during this ZIP update. This update does not approve any actual review.
- Cases 1–4 share conversation context; case 5 enumerates all files visible to the reviewer.
- Required fixtures: enrolled Review Test file; comments and reviews; pending href review assigned to the reviewer; at least two committed versions with a recorded expected change list; recorded unresolved threads across accessible test files. Fixture availability has not been verified.
- Tool names and arguments were checked against the connected Rockhopper Test 2 tool descriptions; parity with the packaged endpoint and tool annotations remains unverified.
- Historical comparison requires sufficient returned version/cell history. get_unattributed_changes describes changes since the last saved version and must not be treated as a diff between two committed versions.
- Keep reviewer credentials only in secure portal fields.

Optional: separate dark-mode icons and brand colors can be added; neither is required. The supplied logo is used unchanged apart from transparent square padding.
