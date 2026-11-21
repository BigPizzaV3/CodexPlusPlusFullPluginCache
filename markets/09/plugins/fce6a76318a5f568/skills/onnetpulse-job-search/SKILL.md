---
name: onnetpulse-job-search
description: Help users discover active public jobs, hiring companies, categories, countries, and locations on OnNetPulse, with canonical links back to OnNetPulse for details and applications.
---

# OnNetPulse job search

Use the OnNetPulse MCP tools for public job discovery. Do not invent job, company, location, salary, or availability information.

## Choose the tool

- Use `onnetpulse.search_jobs` for job searches and supported filters.
- Use `onnetpulse.get_job` when the user wants the full public details for a specific result.
- Use `onnetpulse.search_companies` to find companies with active public jobs.
- Use `onnetpulse.get_company` for a company profile and its active jobs.
- Use `onnetpulse.browse_categories` when the user wants categories or needs to refine a broad search.
- Use `onnetpulse.browse_countries` for country-level discovery.
- Use `onnetpulse.browse_locations` for cities, counties, and other supported locations.

## Search behavior

1. Translate the user's stated intent into the narrowest supported filters.
2. Preserve explicit constraints such as country, location, workplace, employment type, experience level, salary, freshness, and sorting.
3. Use `page` and `limit` when the user asks for more results; keep result sets focused.
4. If there are no results, explain that clearly and suggest one concrete broader refinement.
5. If a tool reports an invalid or unavailable record, do not retry with an invented identifier.

## Responses and links

- Clearly distinguish facts returned by OnNetPulse from suggestions or follow-up questions.
- Include the job or company name, relevant location and workplace details, and salary only when returned by the tool.
- Use the returned canonical OnNetPulse URL for job and company links.
- When the user wants to inspect or apply for a job, direct them to the OnNetPulse page. Never return an external employer application URL.
- Do not expose internal identifiers, database details, stack traces, credentials, or unrelated personal data.
- Do not claim that a job is still available unless the tool returned it as active.
