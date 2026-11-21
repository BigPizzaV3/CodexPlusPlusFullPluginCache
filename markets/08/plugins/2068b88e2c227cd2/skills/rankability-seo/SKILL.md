---
name: rankability-seo
description: Use connected Rankability evidence for SEO and AI visibility analysis, keyword research, content workflows, and audits. Applies when the user asks to work with Rankability or its client workspaces.
---

# Work with Rankability

Use the connected Rankability MCP server at `https://app.rankability.com/mcp`. Discover the actual tool schemas in the current session; tool availability follows the account's scopes. If the connection is missing, explain how to connect through OAuth using the [setup guide](https://www.rankability.com/mcp-for-seo/).

Resolve the requested client and organization before reading its records. Use saved client Knowledge and evidence where relevant. Do not guess record IDs, mix organizations, or treat absent/stale/partial data as zero or a verified negative result. Cite the saved record, report, capture time, or source supporting a finding.

For an analysis request, start with saved records and read tools. Keep traditional search rankings, AI answer mentions, and AI citations distinct. A cited page alone does not prove that it mentions the tracked brand.

Before starting a paid or consequential operation, read the current usage contract and the applicable estimate/preflight tool. Explain the requested operation, target, and usage impact; obtain the user's approval unless this exact action is already authorized. Use `confirm_cost: true` only when the current tool requires it and that cost is authorized. Do not invent per-action prices for pooled usage accounts.

Use one stable idempotency key for retries of the same logical action. Treat returned job/run IDs as accepted work, not completed results. Poll the provided status route with bounded backoff; honor `Retry-After` and any returned `retry_at`. Stop on an actionable authentication, scope, subscription, validation, or terminal job error. Do not launch a duplicate job after an ambiguous response.

Publishing, deleting records, sending outreach, creating schedules, and triggering fresh scans are separate actions from reading evidence. Keep each within the user's authorization. Never include API keys, OAuth tokens, private customer content, or internal identifiers in public output unless the user explicitly requests an appropriate data export.

Answer with the finding, its evidence and uncertainty, and the next useful action. Describe missing prerequisites plainly. A custom MCP connection or locally installed package is not a platform directory endorsement.
