---
name: next-actions
description: Tell a brand what to do next to improve its AI visibility, from the plan in 3RD and the recommended tasks not yet in it. Use when the user asks what to do next, what to prioritize, or what is in their plan.
---

Use this skill to answer "what should we do?" from the brand's own plan.

1. Call `list_brands` and take the `brandId`. Ask which brand if there are several and the user named none.
2. Call `get_playbook` with the `brandId`. These are the tasks already in the plan, with a full brief and checklist each.
3. Call `list_suggested_tasks` with the `brandId`. These are recommended tasks that are not in the plan yet.
4. Optionally call `get_opportunity_radar` to show which of the five drivers (content coverage, content quality, crawlability, authority, outreach) is weakest. A driver with `dataAvailable: false` is not measured; never call it a weakness.
5. Answer in two clearly separate parts:
   - **In your plan:** the open tasks, most relevant first, each with its link (`url`).
   - **Suggested next:** the recommended tasks, presented as suggestions the team can add, not as planned work.

`expectedLift` is a model estimate, not a measured effect; say so. When it is null, the effect is unknown, not zero. Do not add tasks or change a task's status unless the user asks; `update_task_status` changes the plan for the whole team.
