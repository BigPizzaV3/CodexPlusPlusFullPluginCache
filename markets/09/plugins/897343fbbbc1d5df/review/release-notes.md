# Release notes — initial submission

GovPeak connects ChatGPT and Codex to an authenticated GovPeak federal business development workspace through the existing production MCP server.

This initial public-plugin package exposes the same narrow MCP surface already implemented by GovPeak:
- read pipeline pursuits, action items, pursuit notes/history/events, upcoming events, and federal opportunities;
- optionally create or update pursuits, add pursuit notes, and create or update action items after the user explicitly grants Read & write access;
- no delete tools.

The connection is tenant-scoped from the GovPeak OAuth token. Read-only is the default permission, and GovPeak re-checks account/workspace eligibility on tool calls.

Submission-readiness additions include RFC 8707 resource-bound OAuth tokens, OpenID/email scopes with a verified-email UserInfo endpoint for workspace domain restrictions, a dormant OpenAI domain-verification challenge route, and public privacy, terms, and support pages.
