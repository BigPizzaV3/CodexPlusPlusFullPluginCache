---
name: wedding-budget
description: 예산, 비용, 지출, 스드메, 예물, 혼수, 허니문 예산, 플라워 내역을 보거나 저장할 때 사용한다. Use when reading or saving the WeddingFlow budget, expense items, or flower records. Do not use for dress-rental quotes or honeymoon destination surveys.
---

# WeddingFlow budget

Answer in Korean. Account totals and saved expenses come from the WeddingFlow MCP server. Label general budget advice separately from retrieved numbers.

## Tools

Use `path_params`, `query`, and `body` only as each tool declares. Identity comes from the token.

| Intent | Tool |
| --- | --- |
| Read the budget | `get_api_v1_budget` |
| Save the budget | `post_api_v1_budget` |
| List expenses | `get_api_v1_cost` |
| One expense | `get_api_v1_cost_by_cost_id` |
| Add an expense | `post_api_v1_cost` |
| Flower records | `get_api_v1_flower` |

Keep `page_size` and `limit` at 20 or below. Filter expenses with `query.category`.

## Budget fields

`post_api_v1_budget` creates or updates the one active budget. All fields are optional; send only values the user confirmed. Amounts are won, integers.

- `wedding_date`, `wedding_place`, `total`
- Category allocations: `place` (장소), `studio_dress_makeup` (스드메), `gifts` (예물예단), `preparations` (혼수), `honeymoon` (허니문), `etc` (기타), `remain` (예비)

Read the current budget first. Show the previous value and the new value, then wait for confirmation. Do not retry a failed POST.

## Expense fields

`post_api_v1_cost` only creates an item. This connection cannot edit or delete an expense.

- `category`: `place`, `studio_dress_makeup`, `gifts`, `preparations`, `honeymoon`, `etc`
- `title` (at most 100 characters), `memo` (at most 500)
- `amount`
- `is_executed`
- `scheduled_date`, `executed_date` as `YYYY-MM-DD`
- `payment_method`: `card`, `cash`, `transfer`, `other`

Confirm category, title, and amount before saving. Do not invent a price that the server did not return.

If a tool is missing or authorization fails, explain the limit and offer to draft the numbers in chat without claiming they were saved.
