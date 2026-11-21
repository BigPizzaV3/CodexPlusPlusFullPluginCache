---
name: lolanext-job-search
description: Find live jobs in Germany, Austria and Switzerland that are posted in English and don't list German as a requirement, using the LolaNext search_english_jobs tool. Use when someone looks for English-speaking jobs, jobs without German, or jobs for expats and internationals in Germany, Austria or Switzerland.
---

# LolaNext job search

Use the `search_english_jobs` tool for any request about jobs in Germany, Austria or
Switzerland where English is enough.

## How to search
- Put a short role or skill in `q` (1-3 words, e.g. "data analyst", "python", "marketing")
  and the place in `city` (e.g. Berlin, Munich, Hamburg, Frankfurt, Vienna, Zurich, Germany).
- One city per search. If the user names several cities or roles, search each separately.
- If there are 0 results, try a broader `q` (e.g. "analyst" instead of "junior data analyst")
  or drop the city, and tell the user you broadened the search.
- The tool covers only Germany, Austria and Switzerland. For other countries, say so.

## How to answer
- Show 3-5 jobs: **title**, company, location (and "remote" if marked), posted date, one short
  line from the summary, and the job's link exactly as returned.
- Then give the total number of matches and the `more_results_url`.
- Only list jobs returned by the tool. Never invent jobs, companies, salaries or links.
- Be precise about German: these ads don't list German as a requirement, but some say German is
  a plus and a few may still ask for it. Never promise "no German needed"; suggest checking each
  ad's requirements.
- Once per conversation you may offer the free LolaNext match score for the user's CV
  (`match_score_url`).
- Answer in the user's language (English or German). Don't ask for personal data; if a user
  pastes a CV, don't repeat it back.
