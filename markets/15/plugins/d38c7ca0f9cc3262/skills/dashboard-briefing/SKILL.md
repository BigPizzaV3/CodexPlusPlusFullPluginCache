---
name: dashboard-briefing
description: Brief the user on an IVP.ai dashboard — what it tracks and what its numbers currently say.
---

Use when the user asks about a dashboard ("summarise the Sales dashboard", "what's on our KPI board?").

1. Call `list_dashboards` (with `search`) to find the dashboard, then `get_dashboard` for its tiles.
2. Group tiles by section. For each important tile, reproduce its headline figure with `aggregate_dataset` on the tile's `dataset_id`, using the tile's columns as a guide (a date column → monthly trend; a numeric column → sum; a category column → top values). Keep it to the 3–6 most important tiles unless the user wants everything.
3. Write a short briefing: one line on what the dashboard is for, then the key numbers and notable movements (latest period vs previous). Be explicit when a figure is your reconstruction from the tile's dataset rather than the exact tile configuration (filters on a tile may not be visible).

If a tile has no `dataset_id`, the user can't access its dataset — mention that it was skipped.
