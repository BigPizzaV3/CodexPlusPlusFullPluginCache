---
name: weekly-household-reset
description: Use when the user wants to get their household's week in order in Woosh - what is on the agenda, which tasks are due, what to eat, and the shopping list that follows from it. Works on one of the user's private groups.
---

# Weekly household reset in Woosh

1. Find the household. Use `list_groups` and pick the private group the user means. Ask when there is more than one and the user has not said which.
2. Get the picture with `get_group_overview`, then read the week: `get_group_agenda` for appointments and work days, `list_tasks` for what is due and who does it, and `get_group_menu` for the meals already planned.
3. Sum the week up in a few lines: busy days, tasks due or overdue, and meals still missing.
4. Fill the gaps the user asks for:
   - Meals: put dishes on the menu with `plan_meals`. Suggest dishes the group already has before new ones.
   - Shopping: put the planned dishes' ingredients on the list with `menu_to_shopping`, and add anything else with `add_shopping_items`. Check the list with `get_shopping_list`.
   - Tasks: add one with `create_task`, or change one (its day, who does it) with `update_task`.
5. Say what you are about to add or change and wait for the user's go, unless your app already asks them to confirm each change: the group's members see it. Days in the menu and tasks are calendar dates; times in the agenda are UTC, so give them in the user's time zone.
6. If a tool is refused or not available, tell the user where to do it in the Woosh app (`woosh_guide` says where).
