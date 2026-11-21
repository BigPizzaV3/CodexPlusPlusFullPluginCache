---
name: team-capacity
description: Team utilization and capacity from Hubity. Use when someone asks who is over capacity, overworked or underused, who has room, or for a utilization rate for a person, team or period. Reads hours already logged; it is not a forward schedule.
---

# Team capacity

Compares the hours each person logged with the hours they had available: their work pattern, less holidays and approved leave.

## Input

- A period. "Last month" means the previous calendar month. If no period is named, use last month and say so.

## Steps

1. Call `get_utilization_report` with `startDate` and `endDate` as `YYYY-MM-DD`.
2. Answer with:
   - Who logged more than their available hours, and by how much, largest first.
   - Who has room: only people whose total logged hours are below their available hours, most hours to spare first.
   - The company utilization rate, when the report gives one.
   - One suggestion for rebalancing.
3. If `rosterComplete` is false, say the list is partial and that no company figure is given.

## Rules

- These are hours already logged. Do not present them as a plan or forecast.
- Leave out people with neither logged nor available hours.
- Never invent hours or rates.
