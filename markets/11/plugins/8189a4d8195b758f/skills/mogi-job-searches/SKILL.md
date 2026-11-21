---
name: mogi-job-searches
description: Create, change, widen or remove the user's saved job searches (titles, places, work mode, pay, experience, companies to include or skip) and preview live results. Use for any request to change which jobs Mogi finds or to get more jobs.
metadata:
  short-description: Create, widen and tune searches
---

# Job searches

Each saved search runs every day and brings new matching jobs to the user's tracker. A user can
have up to 5, and always keeps at least one.

## Workflow

1. Call `list_searches` to see the current searches and how many jobs each found.
2. Translate the request into filters:
   - `keywords`: two to six full job titles ("Data Engineer", "Analytics Engineer"). Avoid
     single words like "Manager".
   - `exclude_titles`: words to skip ("Intern", "Director").
   - `locations` and `countries`; `modes` such as {"Remote": true, "Hybrid": false, "On-site": false}.
   - `experience` bands, `employment_types`, `salary_min` with `salary_only`.
   - `include_companies` / `exclude_companies`.
3. Change an existing search with `update_search` (only the fields you send change), or add a
   new one with `create_search`. Read the result back to the user.
4. Too few jobs? Offer `expand_searches`: it widens a search and adds related searches from
   the user's resume. Confirm first and read back what changed.
5. To check a search before saving, call `preview_new_jobs` once and show the sample. It is
   limited per day, so refine with the user between calls.
6. `add_jobs_from_search` saves the filters, adds the jobs the user picked from the preview
   and starts finding more.
7. Call `get_search_suggestions` when the user asks why they get the wrong jobs; apply or
   dismiss lines with `respond_to_search_suggestions`.

## Guardrails

- Confirm before `delete_search`. The last search cannot be deleted; change it instead.
- Never loop `preview_new_jobs`: each call buys live results.
