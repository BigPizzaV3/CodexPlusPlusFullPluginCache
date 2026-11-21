# Submission kit

Prepared 2026-10-02. Scenarios are prepared for review; do not mark them as executed until the named host actually passes them. This file contains no reviewer credentials.

## Public listing fields

- Publisher: Greg Eland
- Support: https://shareout.io/support
- Contact: hello@gregeland.com
- Privacy: https://shareout.io/privacy
- Terms: https://shareout.io/terms
- Website: https://shareout.io
- Connection guide: https://shareout.io/agents
- Hosted endpoint: https://shareout.io/mcp
- Repository: https://github.com/geland/shareout-integrations
- Public product example: https://shareout.io/d/cujufgdheurd
- Category: Productivity
- Account required: yes. Current browser sign-in uses an email link.
- Intended for under-18s: no; publishing accounts are intended for adults 18+.
- Commerce: the current self-service service is free with usage limits; no purchase flow is part of the plugin.

## Data-handling answers

**Reads or stores personal information:** Yes. Shareout stores account emails, publisher-selected document content and metadata, invitations, comments, connection/permission metadata, viewing events, support information, and security/audit records. Uploaded documents and comments can contain personal information chosen by users.

**Data destinations:** The declared Shareout MCP service receives tool requests. Hosted publishing transfers file bytes directly to a short-lived Shareout HTTP upload. Cloudflare supplies hosting, storage, database, security and email infrastructure; the marketing site also uses its cookie-free Web Analytics. Email reaches the recipient's provider; support email reaches Gmail. A document can load scripts/fonts from the allowlist described in the privacy policy. A connected AI host processes returned information under its own policies. Do not answer a portal's “other services” question with an unconditional “no”; use its exact definition and disclose these destinations.

**Retention:** Documents default to no scheduled deletion, unless the owner chooses a retention deadline. Links expire independently. Detailed viewing events are pruned after 30 days; daily deduplication rows roughly two days. Aggregate counts remain with the document. Deletion denies access immediately and queues storage cleanup. Audit, support and some collaboration records can remain after account deletion. See the policy for limitations.

**Training/advertising:** Shareout does not sell personal information, use it for targeted advertising, or train AI models on documents. A user's selected AI provider has its own policies.

**Permissions:** The OAuth connection requests the selected Shareout read/publish/manage permissions. Connections are revocable. Reviewer access must be restricted to a dedicated account containing fictional material.

## Review cases and fixture files

The portable manifest's `extensions.com.openai.review.test_cases` contains five positive and three negative cases. The Codex compatibility manifest carries the same cases. They cover catalog discovery, first publication, stable-link revision, feedback reading, link revocation, missing file transfer, unauthorized access, and malicious comment instructions.

Two fictional files in `examples/review/` provide the first and revised weekly update. The only substantive revision adds “Owner: Avery.” Serve the file as `index.html` in its upload bundle. These are downloadable fixtures, not skill content, and are not loaded into model context automatically.

Use the same workflow to record each host: normal connection UI, catalog lookup, publish, open the recipient page, update, reopen the original link, review comments, and revoke the named link. Include negative cases. Keep credentials, private account details, and unrelated workspace content out of recordings. A recording must show an actual host run; screenshots, a script, or an API smoke test are not a substitute.

## Submission gates

- Public policy/support URLs are live and identify Greg Eland. Verified 2026-10-02.
- Run the cases in each target host, with its production connection. An API-key test does not establish interactive OAuth acceptance.
- Enter reviewer credentials only in the portal's private review fields. Do not add credentials or reviewer sign-in instructions to a manifest, this repository, or a ZIP.
- OpenAI requires a dedicated account that works without email/SMS codes, magic links, or MFA approval. An isolated demo account now meets that requirement: production login was verified and its credentials saved only in the private portal on 2026-10-03. Customer email-link authentication remains unchanged. Do not put demo credentials in a package or inject browser sessions.
- A recorded walkthrough URL is intentionally absent until an actual recording exists.
- Portal sign-ins are complete. OpenAI confirmed individual developer verification and accepted the initial draft upload on 2026-10-03. Claude directory submission is deferred at the owner’s request because the current personal account is Free.
- Track submission IDs and decisions in `docs/distribution.md`. A valid ZIP and a public repository do not establish directory approval.

Sources: [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [OpenAI authentication](https://developers.openai.com/plugins/build/auth), [Claude submission](https://claude.com/docs/plugins/submit).
