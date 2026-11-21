---
name: get-started
description: "Connect to Heffl and identify the selected CRM workspace when onboarding or when account or workspace context is unclear."
---

# Start using Heffl

Heffl uses OAuth to connect the user's account and selected workspace. Direct the user through the plugin connection UI; never ask for passwords, tokens or API keys. If context is unclear call heffl_whoami to report the actual user, workspace, scopes and timezone. Do not change workspace implicitly. Read-only scopes hide write tools; module and record permissions still apply.

For a concrete known-object read, go directly to the relevant tool without unnecessary identity/schema calls. Discover unfamiliar tasks with heffl_search_actions and unknown objects with records_catalog. If authorization fails, report the permission/scope/billing requirement and stop retrying.

Available workflows include CRM records and follow-ups, deals and quotations, field-service jobs and visits, forms and submissions, client documents and internal wiki, synced email, and workspace configuration. Use the matching bundled skill when needed. Every MCP write executes immediately; validation is available via heffl_validate_action. Successful results are receipts, not pending approvals. See ../heffl-crm/references/operating-rules.md for writes and recovery.
