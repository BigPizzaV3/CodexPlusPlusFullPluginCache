---
name: jurnie
description: Connect Codex to a user's Jurnie account to review and manage personal or shared Journeys, projects, assigned tasks, habits, daily intentions, calendar events, consistency, and scheduled actions. Use when the user mentions Jurnie, asks to plan or review their day from Jurnie data, wants to turn a conversation into tracked actions, assign work to a Journey member, or wants Codex to read or update their goals and plans through Jurnie's MCP tools.
---

# Jurnie

Use Jurnie's MCP tools to turn goals into clear next actions while preserving the user's control over their account.

## Work with Jurnie

1. Use Jurnie tools for account data. Do not bypass them with direct database access or browser automation.
2. Start with the smallest read that answers the request. For daily planning, inspect relevant tasks, overdue work, calendar events, and the daily intention rather than loading every Journey.
3. Resolve names to current Jurnie records before writing. When multiple records match, ask the user which one they mean.
4. Treat the user's explicit request as authorization for the requested non-destructive write. Confirm before deletions, bulk changes, or a materially broader mutation.
5. Use the user's Jurnie timezone for dates and calendar times. Ask when a time or date remains ambiguous.
6. Report what changed only after the tool succeeds. Keep recommendations distinct from state actually saved in Jurnie.

## Choose the right capability

- Review goals or projects: inspect Journeys, then fetch tasks only for the relevant Journey.
- Plan today: combine current tasks, overdue tasks, calendar events, and the daily intention; propose a short ordered plan.
- Capture follow-through: create or update the smallest useful task, preserving the user's wording where practical.
- Assign work: first list the accepted members of the relevant shared Journey. Match the requested person to exactly one returned member, then pass that member's `userId` as `assigneeId` when creating or updating the task. Ask when names are ambiguous. Use `assigneeId: null` to unassign. Pending invitees are not assignable until they accept.
- Track routines: inspect habits before logging completion; do not infer completion from discussion alone.
- Set an intention: keep it concise and aligned with the user's stated priority.
- Schedule follow-up: distinguish a Jurnie scheduled action from a calendar event and use the one the user requested.
- Delete: explain the exact target and obtain confirmation immediately before using a destructive tool.

## Respect capability boundaries

Jurnie has no tools for sending email, buying subscriptions or charging cards, or reading Google Drive files.

- For an email request, explain that Jurnie cannot send it and offer to draft the message. Do not send it or create a substitute scheduled action.
- For a subscription upgrade or payment request, direct the user to the Jurnie app's billing settings. Do not collect card details or claim that a charge or plan change happened.
- For Google Drive requests, explain that those files are not available through the Jurnie connection. Do not claim to have listed or read them.

Do not silently substitute another service when the user explicitly asks Jurnie to perform an unsupported action.

## Handle connection and scope limits

If Jurnie tools are unavailable, tell the user to connect the Jurnie plugin and resume after OAuth authorization. If a tool reports a missing scope, name the capability that needs permission and ask the user to update the Jurnie connection; do not work around the denied scope.

Never request, reveal, or store access tokens in chat. Jurnie's OAuth connection and server-side audit trail are the source of truth.
