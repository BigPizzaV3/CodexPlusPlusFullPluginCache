---
name: intakra-account-opportunities
description: "Prioritize owned Intakra accounts, review dated buying signals and changes, find relevant contact evidence, or prepare a daily account brief."
---

# Review accounts worth attention

Use the connected workspace at https://intakra.com/mcp through normal OAuth with `accounts:read`. The old /api/mcp resource requires a fresh connection; never repurpose its token. Setup guidance is https://intakra.com/mcp-guide. Resolve missing scopes through normal consent, not pasted secrets.

Start with `list_accounts` or `get_daily_brief` according to the question. Use `prioritize_accounts` to rank owned candidates from saved opportunities. Preserve missing domains, quiet results, pagination, check dates and source links. An empty or quiet brief is valid and does not establish no activity. Present the most useful finding first, then why it matters and its evidence.

Use `get_account`, `get_account_changes`, `list_opportunities` and `get_project_updates` for selected accounts and opportunities. Separate the public event date from when Intakra recorded it; a newly found record can describe an older event. Saved evidence is not fresh research, and public signals do not prove need, budget, authority or purchasing intent. Do not claim changes since the previous visit without an actual dated comparison.

Use `get_best_contact` only when relevant. Preserve its source and coverage limits; a suggested role is not a verified decision maker, and a missing email is not permission to invent one. Share only relevant business contact information. Return watch status and material before/after claims as recorded; reading them does not create a notification.

For an empty workspace, offer the supported setup workflow with the user’s offering and target companies. Conversation drafts are possible when requested; Intakra does not write or send outreach. Supplied-evidence review is available separately without a workspace.
