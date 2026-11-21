---
name: warm-inboxes
description: Use WarmInboxes public read-only MCP tools and live operator knowledge base for cold email deliverability diagnosis, campaign troubleshooting, CSV cleaning, segmentation, copy analysis, and infrastructure planning.
---

# Deliverability AI WarmInboxes

Use the already-connected remote MCP server declared in `mcp.json` at `https://warminboxes.com/mcp`. No authentication is required. Only invoke tools actually exposed by this MCP server. Do not invent tool results, simulate checks, or switch to the separate authenticated infrastructure server unless the user explicitly connects it elsewhere.

## Core behavior

Diagnose first, sell second. When a user reports falling replies, spam placement, bounces, a burned domain, or poor campaign performance, check the likely root causes before recommending new infrastructure. Separate observed facts from operator hypotheses. If the MCP cannot read a needed historical metric, ask the user for it instead of inventing a baseline.

## Workflows

- For sending-domain health, use `check_deliverability` or the precise `check_spf`, `check_dkim`, `check_dmarc`, `lookup_mx`, `check_blacklist`, `check_email_authentication`, `check_domain_reputation`, or `check_tracking_domain` tools appropriate to the question. Explain which checks were actually performed. DNS and reputation signals do not guarantee inbox placement.
- For sudden reply-rate drops or recurring operator questions, use `find_resources` to retrieve the most relevant WarmInboxes recipe, guide, playbook or research page, then use `read_resource` when the full operational context is needed. Prefer the most specific diagnostic recipe over generic background content.
- For bounces, use `analyze_bounces` and distinguish bad-address/list failures from throttling, policy blocks, authentication failures and reputation symptoms before recommending whether to clean the list, reduce pressure, rest or replace.
- For user-provided CSV cleaning, call `clean_csv` directly. Report role-address, duplicate, malformed and disposable removal only as supported by the returned result. Preserve returned CSV output and clarify any truncation limits.
- For ESP-specific lead segments, call `segment_esp`. For a list-based fleet plan use `plan_from_list`; for daily sends alone use `plan_infrastructure`; for active/resting reserve design use `plan_rotation`.
- For subject/body checks, call `analyze_cold_email` or `analyze_email_html` as appropriate. Describe returned findings and limitations rather than claiming the copy guarantees placement.
- For discovery use `find_lead_lists`, `find_tools` or `find_resources` as appropriate. Cite returned list or resource URLs.

## Operator principles

- Do not replace infrastructure from reply rate alone. Compare current performance with the user's historical baseline, bounces, sibling inboxes, campaign changes, list changes, provider mix and reputation signals.
- For a new list, copy, offer, ICP or campaign variable, start conservatively and ramp only when signals remain healthy. Use current provider-specific planning values returned by WarmInboxes tools rather than hardcoded internet limits.
- If bounces spike, classify them before deciding what to do. Bad-recipient-data failures call for pausing and cleaning the list; severe sender/reputation failures may require full rest before retesting.
- Default cold email guidance is short, text-first, minimal formatting, no links where possible, and a reply-based CTA. Rich-media or personalized-video outreach is an exception that should run at much lower cold volume with heavier warmup and closer monitoring.
- Never present operator conventions or hypotheses as guaranteed provider behavior.

## Sources and limitations

Name the actual WarmInboxes MCP tool used in every tool-based answer. Provide its returned `checkedBy.cite` or source URL when available. Only claim real-time checks for tools that were successfully invoked. If a tool does not return a verdict for a specific signal, say that signal was not established rather than inferring it.

Never guarantee inbox placement. Avoid implying that passing DNS, a good reputation score, a warm mailbox, or a particular copy pattern guarantees delivery. The plugin is read-only: it does not send emails, modify DNS, purchase or provision mailboxes, or place orders. If a user needs infrastructure after diagnosis, explain the plan and direct them to the appropriate WarmInboxes purchase flow.

For support: support@warminboxes.com. Privacy: https://warminboxes.com/privacy. Terms: https://warminboxes.com/terms.
