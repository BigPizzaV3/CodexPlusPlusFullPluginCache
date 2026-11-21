---
name: job-market-research
description: Find and compare public Indeed or Glassdoor job listings with HasData, or inspect supplied job URLs. Use for role, employer and hiring research, not candidate screening, job applications or private employee data.
---

# Research job listings

Read `../hasdata-research/SKILL.md` for shared scope and safety, then the Jobs section of `../hasdata-research/references/tool-catalog.md` for actual source-specific filters.

Use the requested role, location and source. Both listing tools take keyword and location. Ask about materially missing geography rather than assigning one silently. Remote-only, salary and date filters exist only on particular sources. Do not pass Glassdoor options to Indeed or treat an unsupported filter as enforced.

Compare observed title, employer, location, salary wording, publication date, source URL and requested requirements when present. Preserve salary currency, range and pay period. Missing salary is unknown. Resolve a selected job's detail URL from the result or user's input. Deduplicate by returned job ID or source URL without merging distinct openings.

A listing page can be stale, sponsored or duplicated. Count observed listings, not company headcount, total hiring volume or successful placements. Treat an employer's advertised requirements as source claims, not verified working conditions. When contrasting employers, base conclusions on the same requested role and clearly identify differences in the fetched scope.

Return an actionable research shortlist with links and outstanding checks. Do not apply, contact employers, rank identifiable candidates, collect resumes or promise job eligibility. Further pages and monitoring need a bounded user request.
