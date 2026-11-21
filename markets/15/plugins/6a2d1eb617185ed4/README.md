# SecProbe MCP submission

Server: https://secprobe.io/mcp
Transport: Streamable HTTP (stateless JSON responses).
Authentication: None.
Tools: batch_filings and research_answer.
Privacy: https://secprobe.io/api/v1/privacy/
Support: staff@secprobe.io

Tool discovery requires no credentials. Each invocation requires contact_email explicitly supplied by the user; it is self-reported contact information, not verified identity. Do not fabricate or infer a private email. Optional agent defaults to SecProbe MCP client. Tool calls reuse REST admission, quotas, and admin audit logs.

Annotations: both tools are read-only (public filing retrieval or generated research; no modifications to user data), non-destructive, idempotent in their user-visible effects, and bounded to SecProbe's stored public correspondence. Operational logs, quota reservations, and temporary research caches are implementation side effects.

Test prompts (replace the placeholder contact with the reviewer's approved contact):
1. My contact is reviewer@example.com. Find two Apple SEC letters or responses since 2024, returning source URLs. Expected: batch_filings with supplied contact_email and filters.tickers=[AAPL], bounded page_size; sources or an explicit empty result with coverage.
2. Using that same contact, which revenue recognition disclosure concerns appear significant in Apple's SEC correspondence since 2024? Expected: research_answer with question and filters, findings with source IDs and quotes, subjective assessment criteria, and coverage limitations; no assertion that SEC questions prove violations.
3. Fetch the next page using the previous manifest.next_cursor. Expected: same filters and continuation token, or a clear error if expired.
4. A request missing contact_email must ask the user to supply it, not infer one. Rate-limit errors must be surfaced with retry_after_seconds.

Directory status: OpenAI draft created; domain verified and both tools discovered. Not yet submitted or approved. The owner explicitly chose to retain mandatory email after OpenAI flagged the server instructions for requesting information beyond the stated operation. This finding is retained for human review, not hidden or bypassed. Complete OpenAI developer identity verification, select the intended verified publisher and project, upload the ZIP, verify secprobe.io using the portal's challenge, scan tools, resolve required findings, and submit. Country availability and policy attestations must reflect the publisher's actual choices. Do not invent domain challenges, credentials, verification status, approvals, or organization identities.

Review material: plugin.json contains five executed positive cases, three negative cases, release notes, and a public walkthrough URL. The video condenses actual official-SDK call results, rather than simulating a ChatGPT UI.
