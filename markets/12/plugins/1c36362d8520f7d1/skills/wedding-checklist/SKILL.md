---
name: wedding-checklist
description: 체크리스트, 할 일, 일정, D-day, 진행률, 템플릿으로 할 일을 만들 때 사용한다. Use when viewing, searching, summarizing, or creating WeddingFlow todos, checklist progress, daily or monthly counts, categories, or applying a checklist template. Do not use for budgets, magazines, or rental.
---

# WeddingFlow checklist

Answer in Korean. Saved checklist items come only from the connected WeddingFlow MCP server.

## Tools

Call only tools the server actually exposes. Arguments use `path_params`, `query`, and `body`, and only the sections that tool declares. The signed-in user and wedding come from the token. Never send another user's id.

| Intent | Tool |
| --- | --- |
| List tasks | `get_api_v1_todo` |
| One task | `get_api_v1_todo_by_todo_id` |
| Categories | `get_api_v1_todo_category` |
| Completion rate | `get_api_v1_todo_rate` |
| Daily counts | `get_api_v1_todo_aggregate_daily` |
| Monthly counts | `get_api_v1_todo_aggregate_monthly` |
| Template list | `get_api_v1_template` |
| Tasks inside a template | `get_api_v1_template_by_template_id_tasks` |
| Create one task | `post_api_v1_todo` |
| Apply or switch a template | `post_api_v1_todo_template` |

Keep `page_size` and `limit` at 20 or below. List filters go in `query`: `category`, `completed`, `is_ai`, `is_template`, `is_pinned`, `exclude_no_schedule`, `step`, `search`, `due_date_start`, `due_date_end`, and `ordering`. Default ordering is pinned first, then due date.

## Create

Confirm the title, due date, and category before calling a POST tool. Do not retry a failed POST.

If `post_api_v1_todo` returns `already_exists: true`, nothing new was saved. Tell the user the title and `due_date` already exist, and ask whether they want to change that schedule. Do not call `post_api_v1_todo` again for the same title. This connection cannot edit the saved task. If they want a different date, say the change has to be made in the WeddingFlow app.

`post_api_v1_todo` body:

- `title`: required, at most 100 characters. A duplicate title in the same wedding returns `already_exists: true` with the existing `due_date`.
- `memo`: optional.
- `due_date`: optional ISO date (`YYYY-MM-DD`).
- `category` or `category_name`: optional. Look up categories first when the user names one.
- `step`, `is_pinned`: optional.

Do not send `user` or `wedding`.

`post_api_v1_todo_template` body is `template_id`. Show the template name and warn that applying a template can change the saved checklist before calling it.

## Limits

This connection cannot complete, edit, delete, or reorder an existing task. If the user asks for that, say it has to be done in the WeddingFlow app and still show the current list.

If OAuth is required, use the host authorization flow. Never ask for tokens or passwords. If a tool is missing or returns an error, say what failed and do not claim the task was saved.
