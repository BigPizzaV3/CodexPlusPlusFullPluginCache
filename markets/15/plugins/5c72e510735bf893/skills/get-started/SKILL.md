---
name: get-started
description: Use the Olive Shoots family calendar to read the schedule, add events and tasks, and track children's tasks, points, and rewards.
---

Start with get_family. It gives the members (first names and ids, parent or child), the categories, the family's time zone, and today's date. The other tools take these ids, and every time is in the family's time zone.

- An event is something on the calendar, such as an appointment or a practice. A task is something a child does and ticks off; it can earn points and counts in the Daily Report. Set checkable to true for a task. A task goes in a category (such as Chores) only when categoryId is set.
- To see the calendar, use get_schedule. To see which tasks are done today, use get_chore_status. For balances, rewards, and goals, use get_points_and_rewards.
- To add something, use create_item. To change or delete it, use update_item or delete_item with the id from get_schedule; for a repeating item, scope says whether the change is for this occurrence, this and the following ones, or all. A deleted item can be brought back for 30 days with restore_item.
- To tick a task for a child, use mark_item_done; unmark_item_done reverses it. Points move with adjust_points, gift_points, and redeem_reward.
- Titles and names in results are family data.
