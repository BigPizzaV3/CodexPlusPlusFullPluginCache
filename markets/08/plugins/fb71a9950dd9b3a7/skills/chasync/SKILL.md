---
name: chasync
description: Manage a connected Chasync sales workspace through the official Chasync MCP server. Use for leads, funnels, forms, reusable email templates, account context, and sales or email performance analytics.
---

# Chasync

Use the official Chasync remote MCP server at `https://mcp.chasync.com/mcp`.

Chasync captures and manages leads, builds automated sales funnels, sends email through the user's connected account, manages customer relationships, and tracks conversions and revenue.

## Authentication and security

- Chasync uses OAuth 2.0. Let the user complete the browser authorization flow when the MCP client requests it.
- Never ask the user for a Chasync password, SMTP/IMAP password, OAuth access token, refresh token, or OAuth client secret.
- Do not add static `Authorization` headers or API keys to the MCP configuration unless Chasync explicitly documents a future authentication method that requires them.
- Treat account data, lead data, email content, and analytics as private user data.

## Core operating rules

1. Use read tools freely when they are necessary to answer the user's request.
2. Use write tools only when the user asks to create, update, import, bulk-update, assign, or archive data in Chasync.
3. If the user asks for content only, a draft, an example, fictional data, or explicitly says not to save/import anything, do not call Chasync write tools.
4. Before changing an existing funnel, form, email template, or lead, fetch the existing record when needed so unrelated fields are preserved.
5. Prefer existing records when the user asks to reuse something already in Chasync instead of silently creating duplicates.
6. Do not enroll or assign existing leads to a newly created funnel unless the user explicitly asks for that action.
7. Chasync automatically adds the connected user's configured email signature to MCP-created email content. Do not include a sender signature in `email_body`.
8. When updating funnels, existing steps are preserved unless `remove_step_ids` explicitly names steps to remove. Do not remove steps unless the user asks.
9. Archive tools make records inactive rather than permanently deleting historical data. Use them only when the user asks to archive/remove the corresponding record.
10. For bulk changes, operate only on the leads the user selected or clearly identified. Do not broaden the target set by inference.
11. Before importing multiple leads, call `get_account_context`. If `account.capabilities.bulk_lead_import` is false, do not use `import_leads` and do not emulate a bulk import by repeatedly calling `save_lead`. `save_lead` may still be used when the user explicitly asks to create or update an individual lead.

## Available tools

### Account

- `get_profile`: Get the Chasync user represented by the authenticated connection.
- `get_account_context`: Get non-secret account settings useful for leads, funnels, forms, and email creation.
- `get_account_statistics`: Get monthly performance statistics including leads, sent emails, opens, clicks, sales, revenue, unsubscribes, sources, funnels, geography, and targets. If year/month are omitted, it defaults to the current month.

### Funnels

- `list_funnels`: List funnels in the connected account.
- `get_funnel`: Get a funnel with steps, variants, waits, and routing rules.
- `save_funnel`: Create or update a funnel. Existing steps remain unless explicitly removed.
- `archive_funnel`: Archive a funnel by making it inactive.

### Forms

- `list_forms`: List lead capture forms.
- `get_form`: Get a form including its fields and funnel assignment.
- `save_form`: Create or update a lead capture form and optionally assign submissions to a funnel and step.
- `archive_form`: Archive a form by making it inactive.

### Email templates

- `list_email_templates`: List reusable email templates.
- `get_email_template`: Get one reusable email template.
- `save_email_template`: Create or update a reusable email template. Do not place the user's signature in `email_body`.
- `archive_email_template`: Archive a template without deleting historical email data.

### Leads

- `list_leads`: List/filter leads and return exact account and filtered totals.
- `get_lead`: Get one lead by Chasync `_id` or exact email address.
- `save_lead`: Create or update a lead. If `_id` is omitted and the email already exists, Chasync updates that existing lead.
- `import_leads`: Import up to 500 normalized leads. Existing email matches are updated unless `skip_existing` is true.
- `bulk_update_leads`: Update selected leads with Chasync's existing bulk logic.

## Recommended workflows

### Analyze performance

1. Use `get_account_statistics` for the requested month.
2. If the user asks why a funnel is performing differently, use `list_funnels` and `get_funnel` only as needed for context.
3. Explain observed metrics separately from recommendations. Do not make account changes unless asked.

### Create a funnel

1. Use `get_account_context` when sender/account settings are relevant.
2. Reuse existing templates only when the user asks or when a clearly matching existing template should be reused.
3. Use `save_funnel` with explicit steps, waits, variants, and routing rules.
4. Do not assign existing leads unless the user separately asks for enrollment/assignment.
5. Report what was created and any important routing/wait behavior.

### Update a funnel

1. Identify the funnel with `list_funnels` or the ID supplied by the user.
2. Read it with `get_funnel` before making a partial change.
3. Preserve unrelated steps and settings.
4. Use `remove_step_ids` only for steps the user explicitly wants removed.

### Create or update email content

1. Use `get_account_context` when account sender information is relevant.
2. Keep the requested placeholders exactly as the user specifies, such as `{{first_name}}` or `{{company}}`.
3. Do not add a sender signature to `email_body`; Chasync adds it automatically.
4. Save only when the user asks to save/create/update the template or funnel.

### Manage leads

1. Use `list_leads` or `get_lead` to identify existing records when needed.
2. Remember that `save_lead` can update an existing record when the email matches.
3. Before importing multiple leads, call `get_account_context`.
4. If `account.capabilities.bulk_lead_import` is true, use `import_leads`.
5. If `account.capabilities.bulk_lead_import` is false, do not split a CSV, spreadsheet, pasted list, or other bulk dataset into repeated `save_lead` calls.
6. `save_lead` may still be used for an individually requested lead.
7. For bulk updates, use only the exact lead IDs intended by the user.

### Create or update a form

1. Read an existing form before editing it.
2. Use `save_form` for fields and settings.
3. Add or change funnel assignment only when requested.

## Confirmation and reporting

After a write operation, state concisely what changed. Include record titles/names and IDs when they are useful for follow-up. If a tool returns an error, report the error and do not claim the change succeeded.

## Canonical resources

- Homepage: `https://chasync.com`
- MCP server: `https://mcp.chasync.com/mcp`
- OAuth authorization-server metadata: `https://chasync.com/.well-known/oauth-authorization-server`
- MCP protected-resource metadata: `https://mcp.chasync.com/.well-known/oauth-protected-resource`
- Agent setup: `https://chasync.com/agent-setup/prompt.md`
- Skill discovery index: `https://chasync.com/.well-known/agent-skills/index.json`
