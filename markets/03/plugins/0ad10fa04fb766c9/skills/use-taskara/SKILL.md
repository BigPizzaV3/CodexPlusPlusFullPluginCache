---
name: use-taskara
description: Operate the signed-in Taskara web app for cleaning and facility-service back-office work. Use when the user asks to inspect or manage Taskara customers, objects, employees, schedules, tasks, time entries, absences, field reports, articles, documents, quotes, invoices, settings, or the Taskara assistant; asks what is happening today or this week in Taskara; or wants help using Taskara in German or English.
---

# Use Taskara

Operate Taskara through the `taskara` MCP server whenever its tools cover the request. The MCP server is the source of truth for live Taskara data and supported writes. Use the web interface at `https://taskara.de/app` only for workflows not exposed by MCP; prefer semantic browser control and use computer control only when browser control is unavailable. Never claim an action succeeded without a tool result or visible confirmation.

## Start safely

1. Call `list_organizations` before organization-scoped MCP work unless the exact organization ID is already established in the conversation.
2. If MCP requires authentication, ask the user to complete Taskara OAuth. Never request, read, or store their password, access token, session token, or Firebase token.
3. Select the organization the user named. If more than one organization is available and the choice is unclear, ask one focused question.
4. Read exact customers, objects, employees, tasks, or schedule occurrences through MCP before referencing their IDs in a write.
5. If MCP does not expose the requested operation, open `https://taskara.de/app`, verify the active organization, and continue through the UI.
6. Reply in the user's language. Default to German when the user writes in German.

Read [references/product-map.md](references/product-map.md) when choosing a route, explaining a feature, or handling a plan limitation.

## Choose the workflow

- For summaries or questions, use the MCP list tools and answer only from their returned records. When falling back to the UI, mention when pagination, a filter, or limited visibility may make the answer incomplete.
- For supported task or schedule creation explicitly requested by the user, use MCP and verify the returned ID and link. For other ordinary creations or edits, use the UI and verify the saved state.
- For vague requests such as "manage tomorrow," inspect first, present the concrete proposed changes, and ask what to apply.
- For bulk changes, deletion, sending an invoice or quote, sending invitations or messages, changing roles or ownership, subscription changes, or other externally consequential actions, show the exact target and effect and obtain confirmation immediately before the final action.
- Prefer creating quotes and invoices as drafts. Do not send them unless the user explicitly asks and confirms the final recipient and document.
- If MCP does not cover the operation and no control tool is available, provide precise navigation and field-by-field guidance; do not pretend to operate the app.

## Resolve records before writing

Resolve every named customer, object, employee, or document through MCP first and use the exact returned ID. For UI-only entities, search Taskara and use the exact visible record. If more than one record matches, ask one focused clarification. If none matches, state that and ask whether to create it.

For schedule entries, obtain the object, date, start time, and employee assignment before saving unless the user explicitly requests an unplanned entry. Preserve recurrence, duration, notes, and assignment details given by the user. Check the visible schedule for conflicts and report any warning.

For quotes and invoices, verify the customer, optional object, line descriptions, quantities, units, net prices, VAT, and due date. Report totals shown by Taskara instead of calculating a competing total. Keep unsent documents in draft status unless explicitly instructed otherwise.

## Use Taskara's assistant

Use `/app/assistant` only when the user's request spans Taskara areas not covered by MCP or needs Taskara's in-app document/image context. Give it the user's intent without adding facts. Review proposed actions against live records and observe the same confirmation rules above.

## Finish

After a write, report the returned record ID or verified visible change, the organization, and any draft or unsent state. Include the returned Taskara link when useful. If MCP or Taskara reports an error or permission restriction, relay it accurately and suggest the smallest next step; use `support@taskara.de` only when normal troubleshooting cannot resolve the issue.
