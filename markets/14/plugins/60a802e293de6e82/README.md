# Domi Ops household

Connect to https://app.domi-ops.com/api/mcp for:
shared household shopping items, shared household chores, adding shopping items, medication group times and logging status, recording a medication group as taken, busy times on chosen calendars. This
package contains one remote HTTPS MCP connection and two skills: the household briefing and household actions.
It runs no local commands or background programs. Each ability must be offered by the server's operator, approved when you sign
in and switched on for this connection in Domi Ops under Settings, AI
Connections. Reading shopping and chores starts on; everything else starts off,
and you can switch any of it off at any time. Actions finish in chat with no
second confirmation in Domi Ops, though ChatGPT may ask you to confirm. Nothing
here can edit, check off, remove, skip, undo or delete a record, or create a
calendar event. Approved reads send household labels/timezone and chores and shopping items to ChatGPT. Adding a shopping item sends back the item you asked for; it cannot edit, check off or remove one. Medication group access sends a label you choose, the group's times and whether it was logged. Medication name, strength, instruction and history fields are never sent, but the label is sent as you wrote it, so choose one that does not name a medication. Timing and logging status are still personal health information. Recording a group as taken only fills gaps for medications you approved; it cannot skip, undo or change an entry, and Domi Ops notifies you each time. Calendar availability sends merged busy times for calendars you choose. Event titles, locations, people and calendar names are never sent, and events imported from Google Calendar are left out.
There is no School, Drive or attachment access.

Install using ChatGPT's supported plugin flow, choose OAuth with published
identity (CIMD), sign in to Domi Ops and review your household and permissions.
The operator and household administrator must enable AI connections first.
No client ID, client secret, API key or request header is required. Account and
workspace policies apply. Review provider privacy settings before consenting;
do not share copied Google-derived, health, child or other excluded content.
Disconnect in Domi Ops AI Connections to stop future access; provider copies
remain governed by your ChatGPT settings and terms. Standard integration is
included in hosted pricing and free for self-hosting; a separate ChatGPT account
is required. Self-hosters use their own reachable HTTPS server and package.

Ask for a household briefing using only approved permissions. The skill reports
missing coverage and links to source records. See
[setup](https://github.com/mwhobrey/domi-ops/blob/main/docs/MCP_CHATGPT.md),
[privacy](https://domi-ops.com/privacy) and
[support](https://github.com/mwhobrey/domi-ops/issues/new/choose).
This MIT-licensed package does not establish directory approval or live
connectivity. Stop and check the endpoint/settings on a connection error instead
of sharing credentials or disabling authentication.
