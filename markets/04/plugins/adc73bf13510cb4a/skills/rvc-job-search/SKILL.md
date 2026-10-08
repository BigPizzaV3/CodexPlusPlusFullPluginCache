---
name: rvc-job-search
description: Use when a user asks to search current RVC Global vacancies by role and geography. Do not use for general career advice, resume editing, or explanations about remote work.
---

# RVC Job Search

Call `search_current_job_vacancies` once for each current-vacancy search.

- Put a short role or specialty phrase in `role_text`.
- Put target job countries in `target_country_codes`.
- If the role or geography is missing, pass `null` or an empty list; show the localized clarification returned by the tool.
- Include seniority, salary, language, and work arrangement only when the user states them.
- For Worldwide Remote, use `target_country_codes: []` and `work_arrangements: ["FULLY_REMOTE"]`.

Present the returned Markdown once without rewriting vacancy titles or links.
