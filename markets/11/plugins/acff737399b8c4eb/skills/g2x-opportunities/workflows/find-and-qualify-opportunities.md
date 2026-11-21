# Find and qualify opportunities for my NAICS

Goal: a shortlist of open opportunities that fit the user's company, with the evidence behind each one and the next question to answer.

## Steps

1. Calibrate. Call `g2x_calibrate_session` with `{}`. Confirm the company, NAICS codes, agencies and certifications in one sentence. If there is no profile, ask the setup questions in [Account](../references/account.md) and work from the answers.
2. Search open notices. Call `g2x_search_opportunities` with words from the user's goal as `query` and the profile NAICS codes as `naics_codes`. Example: `{"query": "cybersecurity", "naics_codes": ["541512"], "status": "open"}`. When the user wants notices they can read now, add `"with_readable_documents": true`.
3. Widen inside documents when titles are thin. Call `g2x_search_supplementary` with requirement language, for example `{"query": "zero trust architecture"}`. Keep the passages and page citations.
4. Open the best fits. For each, call `g2x_get_record` with its id. Check agency, notice type, set-aside, NAICS and the response deadline with its time zone when given.
5. Check eligibility, then fit. Separate mandatory eligibility (set-aside, NAICS size context, deadline) from softer signals (agency history, place, contract size). Do not invent certifications or past performance.
6. Save only on request. If the user asked to keep matches, add them with `g2x_watch_records` or `g2x_add_to_pipeline` under [Pipelines](../references/pipelines.md). Research alone does not authorize that write.

## What to tell the user

For each recommendation: agency, title, solicitation number when present, response deadline, why it might fit, what could rule the company out, what to check next, and the G2X link. Say which profile values drove the search and any one-query override you applied. Say plainly when results are provisional or when a search was not matched to the company.

Stop and ask when the goal needs a detail that changes the search: which company, which market or which deadline window.
