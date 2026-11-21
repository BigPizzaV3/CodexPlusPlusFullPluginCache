---
name: manage-goals-and-funnels
description: List, create and delete OpenRevenue goals, and create, change or delete funnels. Use when the user asks which goals exist, wants to set up a conversion goal, track an event or page as a goal, build or edit a funnel, or remove a goal or funnel. Do not use for funnel conversion reports (use funnel-health), traffic totals, referrers, visitors, or performance.
---

# Manage goals and funnels

Use this skill to view goals and to change the goals and funnels configured on a site. Changes write to the user's account and need an owner or admin on the project.

1. Resolve `domain` (ask, or call `list_projects` if needed).
2. Call `list_goals` or `list_funnels` first. If the user only asked what exists, answer from that and stop. Do not create a duplicate of something already there.
3. Before any change, tell the user exactly what you will create, change or delete, and wait for them to agree. Do this every time.
4. Create a goal with `create_goal`: `domain`, `name` and `type` (`event`, `page`, `pageviews`, `visitors`, `visits`, `bounce_rate`, `visit_duration`, `views_per_visit` or `revenue`). `event` needs `value` set to the event name; `page` needs `value` set to the page path. Add `target` when the user gives one.
5. Create a funnel with `create_funnel`: `domain`, `name` and 2 to 8 ordered `steps`, each with a `type` (`pageview`, `event`, `outbound` or `exit`) and a `value`.
6. Change a funnel with `update_funnel`. It replaces all steps, so send the complete new list.
7. Delete with `delete_goal` or `delete_funnel` and `confirm: true` only after the user approved that specific deletion in this conversation. Deleting cannot be undone.
8. If you are unsure which event name or page path the user means, ask. Do not guess.
9. After a change, report what happened using the tool's response only.

If a tool reports missing permission, say that an owner or admin has to do it, and stop. If a tool errors or access is denied, say so and stop.
