# Version 1.0.6 package validation - November 11, 2026

The supplied screenshot requires exactly five positive test cases. Version 1.0.5 contains seven in both manifests. This is a confirmed count mismatch consistent with the displayed Test cases error; individual green case checks do not establish that the collection has a valid count.

Version 1.0.6 contains exactly five positive cases and three negative cases in each synchronized manifest. Cases cover brand/profile discovery, scheduled content retrieval, inbox retrieval, cross-channel analytics, and a self-contained schedule/edit workflow. All required case fields are nonempty strings. The write case specifies a timezone, uses server-returned IDs, verifies persisted content, and requires owner cleanup before the scheduled time. It retains edit_post as supplied by the publisher, rather than replacing it with an older documented name.

Validation scope: ZIP integrity, JSON parsing, portable plugin/MCP JSON schemas, case counts/field types, manifest consistency, listing limits, referenced asset existence, icon dimensions, and forbidden app binding checks. Public listing pages and OAuth discovery are accessible. The MCP initialization probe returns the expected unauthenticated 401 with a resource_metadata challenge. YouTube oEmbed metadata resolves; hosted playback is not verified.

All five positive cases and three negative cases: NOT RUN during this packaging review. Authenticated tool definitions, annotations, token exchange, live execution and the portal importer remain UNVERIFIED. The publisher's 1.0.5 release notes describing server analytics fixes are preserved as supplied, not independently certified. The prior recording observations below remain historical evidence, not proof that the current server is broken or fixed.

After uploading: verify version 1.0.6 and exactly five positive/three negative cases in the saved portal draft. Recheck preserved reviewer credentials, countries/translations and demo link. Complete any attestations reset by upload, run required scans/tests, and verify the Test cases status clears. If it does not, capture the current saved-version validation details; do not add extra test cases.

# Recording review and remaining submission requirements

Recording: review/eclincher-demo.mp4; duration 355.96 seconds, 1912 x 1032, no audio stream. Visual sampling at 30-second intervals and inspection of the final analytics response. This is not exhaustive frame-by-frame verification.

Observed: successful-looking user-visible results for brands, connected profiles, scheduled posts and unanswered inbox items. Underlying tool-call details remain collapsed, so exact arguments/results cannot be independently verified from this recording. No passwords or tokens were visible in sampled frames; social handles and message content are visible, so confirm they are acceptable sample data before sharing.

Analytics: final response says cross-channel and built-in reports completed with empty results ({}) and no reach, engagement or follower metrics. Analytics success is not demonstrated. Investigate report retrieval/async result handling or prepare a test account with valid metrics; record successful analytics results.

Negative cases: not observed in sampled recording. Record the submitted unsupported-action cases.

Hosted video URL: https://www.youtube.com/watch?v=ohfJo1xatFY. YouTube oEmbed returned the title Eclincher - OpenAI MCP Submission and publisher tal mikaelovich without credentials. Browser playback was not verified. Keep the video unlisted or public, not private.

Review case names: the supplied 1.0.5 package states these names were checked against tools/list. Version 1.0.6 preserves those supplied names, including edit_post. This packaging review did not independently authenticate or retrieve current tools/list. Re-verify in the connected submission before submission.

Remaining dashboard setup: verify reviewer credentials, current MCP scans, developer/domain verification, country targeting and applicable commerce declarations. Preserve credentials in secure portal fields only.

Package status: required demo URL is now populated. Analytics success, negative-case execution and expanded tool-call evidence remain unverified; review the notes above before final submission.
