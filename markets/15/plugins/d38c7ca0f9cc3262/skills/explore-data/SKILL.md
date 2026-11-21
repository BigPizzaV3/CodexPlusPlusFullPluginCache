---
name: explore-data
description: Answer a business question from the user's IVP.ai datasets — find the right dataset, check its columns, aggregate, and explain the result.
---

Use the IVP tools to answer questions about the user's data ("what were sales by region last quarter?", "who are our top customers?").

0. **Use agreed metrics when they exist.** If the question is about a data room, or `describe_dataset` shows the dataset is in one, call `get_semantic_layer` for that data room. When the metric the user asks about is defined there, answer with `query_metrics` (metrics, dimensions with a time `grain`, filters, `order_by`) instead of `aggregate_dataset`, and say the figure uses the data room's agreed definition. Otherwise continue below.
1. **Find the dataset.** Call `list_datasets` (use `search` with a key noun from the question). If several look plausible, pick the best match by name and mention which one you used; ask the user only if it is genuinely ambiguous.
2. **Check the columns.** Call `describe_dataset` before querying. Map the user's words to real columns (match on display names). Note which columns are `number` (needed for sum/avg) and `timestamp` (needed for date bucketing).
3. **Compute, don't page.** Use `aggregate_dataset` for totals, counts, averages, trends and rankings:
   - Trends: `group_by` the timestamp column with a `granularity` (month by default) and sort ascending by it.
   - Rankings: `group_by` the entity, add the metric, `sort` by the metric descending, `limit` to the top N.
   - Time windows: use a `last_n_days` filter or `gte`/`lt` on the timestamp column.
   Use `preview_dataset` only when the user wants to see example rows.
4. **Answer.** Lead with the direct answer, then a compact table of the key rows. State the dataset, filters and any assumptions (e.g. "month = calendar month of Created"). If `truncated` is true, say the result was capped.

Never invent numbers — only report values returned by the tools. If a column the question needs doesn't exist, say so and suggest the closest available one.
