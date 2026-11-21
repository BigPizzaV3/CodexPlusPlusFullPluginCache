# Example: First-time connection + existing CRM boards

## User prompt
"Set up monday CRM"

## Expected behavior
1. Skill asks if user has a monday account → yes.
2. Calls `get_user_context` → succeeds (OAuth already configured).
3. Triage: calls `search` for CRM-shaped boards → finds "Deals" board (42 items), "Contacts" board (87 items).
4. Prints connected-user message with existing boards listed.
5. Suggests operate-mode skills: morning-briefing, forecast-dashboard, board-diagnosis.

## Expected output
> monday MCP is connected. You're signed in as **Jane Doe** (jane@acme.com).
>
> I found existing CRM boards in your workspace:
> - Deals (42 items)
> - Contacts (87 items)
>
> You're all set. Here are the skills that work with your existing boards:
> - the `morning-briefing` skill — daily pipeline digest
> - the `forecast-dashboard` skill — commit / best-case / pipeline view
> - the `board-diagnosis` skill — structural audit of your CRM board
> - the `bulk-data-hygiene` skill — clean and normalize your CRM data
> - the `update-crm` skill — review customer conversations and propose updates to one record or a batch
