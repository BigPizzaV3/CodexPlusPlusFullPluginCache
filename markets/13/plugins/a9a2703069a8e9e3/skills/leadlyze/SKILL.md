---
name: leadlyze
description: Review and manage leads, contacts, companies and deals in a connected LeadLyze CRM workspace.
---

Use the bundled LeadLyze MCP connection. Its OAuth grant is bound to the workspace selected during consent. Discover available tools and schemas; scope categories select tool families, not a read-only role. Never claim a grant is read-only merely because the current request only reads data.

Resolve records through list/search tools before using IDs. Tool names replace gateway dots with underscores: leads.list is leads_list, contacts.search is contacts_search, deals.list is deals_list. Pagination and filter arguments vary; use each advertised schema. Lead priority questions can use lead score filters when available; do not invent a priority field.

For pipeline summaries, distinguish returned facts from recommendations, retain currencies and dates, and disclose pagination or unavailable history. Cite record URLs only when returned by the service.

For authorized changes, preserve other fields and verify the result. Creating a lead may trigger configured automation, including calls; inspect the tool description and clarify the intended behavior before executing. Calling, sending outreach, enrolling sequences, deleting records, spending credits and external enrichment are separate actions, not implied by a request to review CRM data. Respect server denials and approval requirements. Never expose tokens or retrieve secrets for a summary.
