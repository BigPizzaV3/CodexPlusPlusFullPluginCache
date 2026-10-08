---
name: dayze-notable-people
description: >-
  Look up public notable people in Dayze by life-in-days (who, age-in-days,
  day_number milestones, birthday peers). Use for celebrities, historical
  figures, "how old in days", Nobel/career day numbers, or comparing two lives —
  not for the signed-in user's private calendar or CRM.
---

# Dayze notable people

Public biographical / temporal lane. No API key required for free-tier `notable_*` (x402 may apply after limits).

## Workflow

1. Resolve the person: `notable_search` → pick best slug.
2. Fetch `notable_pack` (or `notable_pack_premium` when richer pack is needed).
3. Answer with day_number facts (days lived at milestones), birthday peers, and concise bio — do not invent milestones missing from the pack.
4. Compare two people with `compare_lives` when asked.

## Rules

- Prefer pack fields over model memory for dates and day numbers.
- This is not a universal identity registry — only Dayze notable catalog coverage.
- Private life questions belong to **dayze-life-context** / `get_context_pack`.

## Output

2–3 sentence summary, then 3–5 day_number highlights, then peers if relevant.
