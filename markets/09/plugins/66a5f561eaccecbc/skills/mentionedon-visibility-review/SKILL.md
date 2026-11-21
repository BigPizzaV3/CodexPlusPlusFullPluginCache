---
name: mentionedon-visibility-review
description: "Review a connected MentionedOn business’s saved AI visibility, competitors and comparable changes, or identify the next action from its existing report."
---

# Review saved AI visibility

Use https://mentioned-on.com/mcp through normal OAuth with `brands:read`. If not connected, preserve the task and give https://mentioned-on.com/developers/mcp as the setup handoff; never request credentials in conversation.

Start with `list_monitored_businesses` when the owned business ID is unknown. Select the business the user means; businesses shared by another owner are outside this connection. An empty account gets the returned setup link. Connecting does not start a trial, subscription or scan.

Use `get_visibility_report` for the latest saved capture, competitors, source links and bounded history. Preserve dates, provider failures and coverage. A saved capture does not query consumer AI applications now. Missing or failed captures are unknown, not absence. Compare only the returned complete baseline with matching model, prompt and capture recipe. Do not manufacture a change when comparable baseline fields are null, treat the oldest returned record as a first-ever baseline, or attribute a change to a particular website edit.

Present the main finding, supporting dated evidence and a useful unresolved next action. On a return visit, reread the report and `get_website_fixes` to recognize saved work and installation checks before recommending repeated work. Website drafts and installation verification are separate requested workflows. These reads do not publish a website, run paid scans or notify anyone.

For supplied observations without an owned account, the public evidence tools provide a separate workflow. Access can be revoked at https://mentioned-on.com/oauth/connections.
