---
name: plan-a-conference
description: Find the right conferences for someone, save one to their Prompt Prospect workspace and start its research. Use when the user asks which events to attend, wants a conference near a place or in an industry, or names an event to add.
---

Use the Prompt Prospect tools in this order. Every tool answers with plain data; report it in the user's terms.

1. **Find candidates.** Call `find_events` with what the user gave: `near` (a US city or metro), `category` (fintech, saas, martech, hrtech, healthtech, security, and so on) or `q` (a keyword). Ask for a place or a topic only if the user gave neither. Show up to five results with date, city and organizer, and say which are already in the workspace (`in_workspace_event_id` is set).
2. **Confirm before adding.** `add_event` saves the event and starts research, which reads the event's pages and posts. Research is included, but it runs for 5 to 20 minutes and it is the user's workspace, so name the event and ask once before calling it. Pass `catalog_slug` for a catalog event or `url` for any other event website. If the answer carries `code: "event_limit_reached"`, the workspace has used the events its plan includes: say so, with the limit and when the count starts over (both are in the answer); do not retry.
3. **Tell them what happens next.** Research runs on Prompt Prospect's side. The user is emailed when it finishes, and `event_overview` shows progress (`research.status`, people found so far) whenever they ask. Do not poll on your own. Once research finishes, Prompt Prospect checks everyone against the workspace's target customer by itself; `event_overview`'s `next_step` says when that is still pending.
4. **Already researched?** If `list_my_events` or `find_events` shows the event with people found, skip to the `find-people-at-an-event` skill instead of adding it again.

Boundaries: never invent an event, date or venue; if `find_events` returns nothing, say so and offer to add the event by its website URL.
