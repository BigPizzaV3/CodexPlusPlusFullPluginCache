---
name: find-reduced-hours-jobs
description: "Find jobs and employers with a genuinely shorter working week (4-day weeks, 9-day fortnights, half-day Fridays) and explain what a working-hours schedule really means. Use when the user asks for 4-day-week or reduced-hours roles or employers, wants to compare schedules, or asks whether something like a compressed 4x10 counts as a 4-day week."
---

Use this skill when the user wants to find, compare or understand jobs or employers by their working-hours schedule.

## Steps

1. Work out what the user wants: the role or field, the country they can work in, remote, hybrid or onsite, seniority, and the schedule. If they ask for a "4-day week" and say nothing more, use `schedule_type` `4_day_week`. If the request has no role or field at all, ask one short question before searching.
2. For jobs, call `search_jobs` with those filters. For "which companies" questions, call `search_companies`.
3. When the user wants one result in detail, call `get_job` or `get_company` with the slug the search returned.
4. Call `explain_schedule_type` when the user's question turns on what a schedule means, or when you are about to describe a schedule you are not sure of.
5. For "how common is a 4-day week" questions, call `get_market_stats` and quote the as-of date.

## What to tell the user

- For each job: title, employer, where it is and whether it is remote, hybrid or onsite, the schedule in plain words, salary only if the result includes one, and the `url` on 4dayweek.io.
- Say how many listings matched (`total_matching`). If `has_more` is true, offer the next page.
- Applying happens on the listing's page on 4dayweek.io. `get_job` reports an `apply_method` that says whether that page hands off to the employer's own form or takes the application itself. These tools cannot apply or save anything for the user.

## Do not infer these

- Only `4_day_week` is reduced hours at full pay. `4_day_week_pro_rata` and `part_time` reduce hours at pro-rata pay. `compressed_week` is the same 40 hours packed into four days and is not a 4-day week, so never describe it as one.
- A job with no location restriction is worldwide-remote and matches any country filter. Read each result's `locations` and `work_arrangement` before saying where a job is based.
- Salary figures are in whole currency units for the stated period. Never estimate a salary the employer did not publish.
- Details such as the day off, vacation days or awards are present only where the employer published them. When one is missing, say it is not published.
- If a search returns nothing, or an employer is not tracked, say so. Do not invent a listing, a schedule or a day off.

The user's explicit instructions take priority over this skill.
