---
name: get-started
description: Connect a Leafpad site, see which pages are losing traffic, and review one refresh before anything goes live.
---

Help the user start with Leafpad. Do this in order.

1. Call `leafpad_list_organizations`. If there is one site, use its slug. If there are several, ask which site to use. Never guess a site the user does not belong to.
2. Call `find_pages_needing_attention` for that slug. Summarize the pages losing traffic and any refresh waiting for a decision. Use the page title and the reason. Do not invent click counts.
3. If a proposal is waiting, call `get_refresh_proposal` for one of them and describe the current page and the proposed change. Stop there. Do not call `approve_refresh` or `reject_refresh` unless the user explicitly chooses one.

If Search Console is not connected, say so and still show the approval queue when the planner returns one. If the site is not on the refresh planner, say there is no approval queue.
