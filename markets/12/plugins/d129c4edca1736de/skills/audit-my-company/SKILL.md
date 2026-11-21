---
name: audit-my-company
description: Review how a company is using KPI Gamification and what to set up next. Use when a company admin asks how their company is doing in KPI Gamification, for an adoption report, an audit or health check of their setup, what is working or missing, or what to do next. Returns an adoption score with what is on track, what can improve and what has not been started, built from counts and statuses only. Free; every call reads the latest data.
---

# Audit my company

`audit_company` gives a health check of how the company uses KPI Gamification: an overall adoption score, what is on track, what can improve, what has not been started, and a suggested next step for each. It is built from counts and statuses only. It contains **no Team Member names, scores, salaries or personal data**, and not even the company name.

## Rules you never break

1. **Run it when asked.** It is free and changes nothing in the company's setup, so an explicit request needs no confirmation. Asking again on the same day returns the same report.
2. **Report what the tool returned.** Do not invent findings, scores or numbers, and do not extend the report with guesses about individual Team Members. If something is not in the result, say it is not in the report.
3. **Suggest only things the app can do,** and name the page or feature the next step refers to. You cannot make changes from here: no inviting users, changing roles, plans or billing. Tell the user to do those in KPI Gamification.
4. **Team Member, not Employee.**

## Steps

1. Call `audit_company` (it takes no arguments).
2. Present the result in plain language:
   - The overall `score` and `score_label` with the `period`.
   - **Going well** (`going_well`): two or three bullets.
   - **Focus next** (`focus_next`): the top three, each with its finding and `next_step`. Order by what would help the most; do not list everything.
   - Team activity: check-in and daily-report percentages (`team_activity`), and the `seats` line if present.
   - If `status` is `already_generated_today`, say it is today's report (no charge).
3. Close with one clear recommendation for what to do first, and offer related help where a skill exists: designing a gamecard (`create-game-card`), an HR Kit (`create-hr-kit`), an SOP (`create-sop`), or an HR policy (`create-hr-policy`). Share the `links.dashboard` link.
4. The legend in the result explains the statuses: `on_track` means used this month or fully set up, `can_improve` means used before but not this month, `needs_attention` means not started. Use those meanings; do not call a `can_improve` area "broken".

## Errors

- `RATE_LIMITED`: daily limit reached; try again tomorrow.
- `NOT_AUTHORIZED`: only a company admin of the connected company can run this.
