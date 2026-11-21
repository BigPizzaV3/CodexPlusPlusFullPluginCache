---
name: weekly-content-plan
description: Plan and schedule a week of posts in Adly. Use when the user asks for a content plan or calendar, several posts at once, or a week or month of content.
---

1. Select the brand (list_brands, select_brand) and read the connected networks with list_social_accounts.
2. Ask in one message: how many posts, which networks, which days and times, and the goal (sales, awareness, engagement). Use the user's answers; do not ask more than once.
3. Propose a short plan as a table: day, network, format (post, carousel, video), topic. Wait for the user to approve or edit it.
4. For each approved item, create it with the right create tool, poll with get_job, and show_job when ready. Keep going until each is ready. Tell the user how many are done as you go.
5. Show the final list with captions and times. After one explicit confirmation of the whole batch, call schedule_post for each item.
6. Finish with list_scheduled_posts so the user sees what is queued, and mention that any one can be cancelled with cancel_scheduled_post.

Each creation counts toward the user's Adly usage limit, so say how many items the plan will create before starting.
