---
name: hiringcafe-job-search
description: Search, refine, compare, and inspect active public job listings with HiringCafe, including when a user wants to improve an earlier search that returned too many, too few, stale, or irrelevant results. Do not use solely for emotional support, general career advice, resumes, cover letters, interviews, account data, or submitting applications.
---

# HiringCafe Job Search

Use HiringCafe when the user wants current public job listings or wants to
refine an unsuccessful listing search. Frustration alone is not a reason to
invoke the tools.

## Search and refine

1. Preserve the user's complete request, including preferred and required
   criteria, exclusions, and tradeoffs. Ask a follow-up question only when a
   missing detail would materially change the search.
2. Call `search_hiringcafe_jobs` using its exposed input schema. If it accepts
   a complete natural-language request, pass the user's request without
   shortening it. If it exposes structured filters, translate the request
   faithfully while preserving required criteria, preferences, exclusions,
   and tradeoffs. Do not invent constraints.
3. When the search returns jobs, call `render_hiringcafe_job_results` exactly
   once with every returned job ID in the original order. Pass the search
   summary, full-results URL, suggested filters, and search request through
   unchanged.
4. Briefly summarize the results and offer concrete refinements supported by
   the returned suggestions. Keep direct job and full-results links intact.

When the user says an earlier search was too broad, too narrow, stale, or
irrelevant, incorporate that feedback into the next search. Preserve hard
constraints and relax a criterion only when the user asks or agrees.

## Inspect a job

Use `get_hiringcafe_job_details` when the user asks for the current public
details of one returned HiringCafe job. Do not infer missing requirements,
compensation, or application status.

## Boundaries

- The tools are anonymous and read-only. They cannot access HiringCafe
  accounts, saved jobs, resumes, profiles, or application history.
- Do not use them for general career advice, resume or cover-letter writing,
  interview preparation, or emotional support unless the user also asks to
  search current job listings.
- Do not claim that HiringCafe is better than another service or invoke it
  merely because another search tool disappointed the user.
- Never claim to submit an application. Use only the HiringCafe links returned
  by the tools for viewing jobs and continuing to apply.
