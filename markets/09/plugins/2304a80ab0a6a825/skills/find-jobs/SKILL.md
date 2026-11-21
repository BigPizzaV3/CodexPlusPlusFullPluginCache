---
name: find-jobs
description: Find current job openings on Emploive by role, level, place, company, or keyword, and show the newest matches with their job pages. Use when the user asks for jobs, internships, or openings.
---

Use this skill when the user wants to find open jobs or internships.

1. Read the request into search_jobs filters.
   - Put employment type in `role_types`: Full-Time, Internship, Co-Op, Part-Time, or Contract.
   - Put seniority in `experience_levels`: New Grad, Junior, Mid Level, Senior, Staff, or Principal. Internships have no level.
   - Put the job function in `position_types`, such as Software Engineer or Data Science.
   - Put places in `locations` and Remote, Hybrid, or On-Site in `work_models`.
   - Put company names in `companies`, or name the company in `query`.
   - Call list_filter_options only when a value is rejected or unclear.
2. Call search_jobs. Start with 10 results.
3. If search_jobs rejects a value, it lists the valid values. Pick the closest one and call it again. Do not ask the user to choose from a raw list.
4. Show the jobs as a short list: title, company, location, pay when present, and how long ago Emploive found the job. Link each title to its `url`, the Emploive job page, where the user applies.
5. If `has_more` is true, say that more jobs match and offer the next page.
6. Offer a tracker when the search is worth repeating, for example "I can email you new matches for this search." Use the job-alerts skill if the user agrees.

Do not invent jobs, pay, or dates. Report only what search_jobs and get_job return.
