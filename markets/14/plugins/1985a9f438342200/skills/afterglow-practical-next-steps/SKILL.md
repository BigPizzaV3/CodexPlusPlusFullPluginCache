---
name: afterglow-practical-next-steps
description: "Turn a linked Afterglow checklist into manageable next steps, review saved progress, or update an exact confirmed item. Use for practical separation, moving, money and coparenting tasks."
---

Afterglow’s public website is https://withafterglow.com. Use its connected API at https://api.withafterglow.com/mcp through the client’s normal OAuth connection. `get_connected_profile` identifies the connected account and actual verification state. If unavailable, use https://api.withafterglow.com/developers for the connection handoff. Linking supplies account access; saving a checklist status still follows the user’s requested item and choice.



# Practical next steps

Read the relevant legal, money, home or coparenting checklist with `get_checklist`. Keep its actual audience filtering, saved statuses and scope statement. A weekly plan is your suggestion based on the returned tasks and the user's time and priorities; do not present suggested effort, due dates or dependencies as stored Afterglow facts.

For a first visit, select the relevant module from the user's situation. If account linking, onboarding or access is required, give the returned next step and preserve the user's task. Empty or completed checklists are valid outcomes; do not invent tasks or silently substitute another audience. Coaching history, stories, health data and personal notes are outside this connection.

For a return visit, reread the checklist, summarize remaining work and confirmed completed items, and suggest the next manageable action. Without an earlier dated snapshot, do not claim which items changed since the last visit. A plan in this conversation does not create reminders or calendar events.

Call `set_checklist_status` only with an exact item ID returned by the checklist and the user's confirmed done, todo or na (not applicable) choice. A request to complete a clearly identified item supplies that confirmation; do not ask again unnecessarily. If the item is ambiguous, identify it before writing. For an uncertain write, reread or repeat the same item and status; never choose another item. Repeating the same status should preserve its completion timestamp. State the actual saved outcome.

Connections are bound to the MCP resource URL. When moving a connection from a legacy hostname, complete a fresh normal OAuth connection for https://api.withafterglow.com/mcp instead of reusing a token issued for another resource.
