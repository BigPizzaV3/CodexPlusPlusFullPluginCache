---
name: channlworks-workflows
description: Use when a user asks to find, summarize, create, update, or review Channlworks partner relationships, customer accounts, contacts, deals, campaigns, MDF requests, receivables and payables claims, notes, or programs through the connected Channlworks MCP server.
---

# Channlworks workflows

Use the connected Channlworks server's discovered tools and schemas for supported workflows. Tool availability depends on the deployed server, the user's role, and the organization's MCP Access subscription feature.

## Connect and establish context

The production endpoint is `https://mcp.channlworks.com/v2/mcp`, using Streamable HTTP and OAuth. Follow the client's supported connection and OAuth consent flow and the metadata advertised by the server. Do not ask for an API key, construct bearer tokens, or copy credentials into chat or files. Leave OAuth client credentials unset unless the discovered provider flow explicitly requires them. The server advertises `profile`, `email`, and `offline_access` scopes.

For a new organization-scoped task, use the discovered `get_user_details` tool to identify the active organization and role when this context is needed. Use `get_tenants` to resolve organization ambiguity. Do not assume an organization ID from its name or claim a read changes the globally active organization. Inspect each business tool's actual schema for organization scoping.

## Find and summarize records

- Discover current tools and argument schemas. Resolve account, contact, partner, deal, campaign, and other identifiers from returned records. Ask for clarification when multiple records match.
- Apply the user's requested filters. List responses contain summaries; use available single-record tools for full details where the task needs them.
- Respect pagination types and defaults in each schema. Page sizes are capped at 50; offsets at 10,000 and page numbers at 1,000. Narrow filters or page size if a result exceeds the roughly 80 KB response cap.
- Traverse pages when needed for a complete answer. If only part of a result set is available, state the coverage. Do not present a partial page as a complete total or ranking.
- Base summaries, metrics, currencies, statuses, and dates on returned data. Keep different currencies separate unless the user supplies an explicit conversion basis. Do not invent empty-result records or expose unrelated personal information.

## Prepare and execute supported changes

Read the current record, resolve identifiers, and describe the proposed change and relevant side effects. Obtain explicit authorization for concrete writes; an existing authorization for that exact operation is sufficient. A request for a report or a suggested change does not authorize a write.

Follow the discovered schema rather than guessing required fields or statuses. For a requested draft deal, set `isDraft: true`; for a requested draft MDF request, set `state: DRAFT` explicitly because its default is SUBMITTED. Confirm required values when they are missing. Avoid sending placeholder IDs.

Pay attention to tool descriptions and annotations. Deleting a deal removes associated mappings, tags, and proof-of-value records. Rejecting a deal can close pending approval requests, cancel a running proof of value, and withdraw a renewal reminder. Completing a proof of value is final. Archiving a program stops new enrollment. Notes, comments, accounts, contacts, deals, campaigns, and financial workflows can send notifications; account and contact creation can enqueue outbound CRM synchronization. Describe applicable side effects before executing them.

Claim payment recording stores a settlement that occurred outside Channlworks; it does not transfer money. Use the discovered payment-recording tool and verified settlement details. The plugin has no general-purpose email, banking, payroll, or travel-booking tools.

Report success only from the actual tool result. Do not blindly retry a write after an uncertain result; first inspect whether it succeeded. Present the resulting record identifiers and changed fields that matter to the user.

## Recover from errors

- `forbidden`: explain the relevant role permission or MCP Access entitlement; do not retry with another identity or bypass it.
- `not_found`: check the identifier and visibility within the intended organization.
- `validation_failed`: use the schema and error to correct arguments or narrow results.
- `rate_limited` or `dependency_unavailable`: retry reads within reasonable limits. For writes, verify whether an earlier call completed before retrying.
- `internal_error`: report the failure with tool name, error code, and approximate time; do not claim completion or disclose backend details.

For connection help, use [Channlworks MCP setup](https://mcp.channlworks.com/docs). For permission or subscription questions, use [Channlworks support](https://channlworks.ai/contact-us).
