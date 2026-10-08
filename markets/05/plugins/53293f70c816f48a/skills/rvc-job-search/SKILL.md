---
name: rvc-job-search
description: Use when a person wants to find current remote work, work-from-home roles, digital or tech vacancies, relocation opportunities, jobs hiring worldwide, or RVC Global listings. Search and compare jobs by role, skills, location, work arrangement, seniority, salary, language, recency, and relocation. Do not use for general career coaching without a live job-search request.
---

# Remote Job Search — RVC

Find live vacancies on the public RVC Global job board and return a compact, evidence-based shortlist. Job data changes quickly, so browse the current RVC pages for every search; do not present saved examples or model memory as current results.

Read [references/rvc-search.md](references/rvc-search.md) when selecting routes, applying filters, or verifying result fields.

## Search workflow

1. Parse the user's explicit criteria: role or skills, location or hiring geography, work arrangement, seniority, salary floor and period, language constraints, recency, relocation, and desired result count.
2. Start from `https://app.rvc.global/jobs` or a documented direct route. Prefer RVC's own search and filters. Use a focused `site:app.rvc.global/vacancy/view` web search only when the public job board cannot expose the requested combination.
3. Open each promising vacancy page and verify the title, company, posted age, location, work arrangement, salary, required skills, required languages, relocation evidence, and canonical link.
4. Rank exact matches first. Within the same match quality, prefer fresher postings and vacancies that state more of the user's criteria explicitly.
5. Reply in the user's language. Default to five results when the user gives no count, but respect requests such as "just one result."

Ask a clarifying question only when an unresolved criterion would materially change the search. Otherwise make a reasonable broad interpretation and state it briefly.

## Evidence rules

- Distinguish `Fully Remote`, `Remote in-country`, `Hybrid`, and `On-site`; never collapse them into one generic "remote" label.
- An absent country restriction does not prove worldwide eligibility. Say "hiring geography not stated" when the page does not confirm it.
- Treat a language as required only when the vacancy states it. For requests such as "does not require Russian," exclude jobs that explicitly require Russian and label omitted language requirements as "Russian not listed," not as a guarantee.
- Claim relocation support only when the vacancy explicitly states it. Do not infer relocation from an on-site location.
- Preserve the advertised salary currency and period. If a conversion helps, show it as approximate and keep the original figure.
- Never invent employer contacts, compensation, requirements, application status, or links. If a field is unavailable, say so or omit it.
- If no exact match exists, say that first, then offer the closest alternatives and name the criterion each one misses.

## Link attribution

Every user-facing RVC vacancy link must carry these first-party attribution parameters:

```text
utm_source=openai_plugin
utm_medium=plugin
utm_campaign=rvc_remote_jobs
utm_content=vacancy_result
```

Append them with `?` when the canonical link has no query string and merge them with `&` when it already has one. Replace conflicting values for these four keys rather than duplicating them. Do not place the user's role, location, salary, language, CV data, or other personal criteria in UTM parameters.

## Response format

Lead with a one-sentence summary of the match quality. For each result use:

```text
Title — Company
Location · Work arrangement
Salary: original advertised amount, or "not listed"
Skills: the most relevant required skills
Languages / relocation: only verified facts
Why it fits: one concise sentence
Attributed direct RVC link
```

Keep the list scannable. Do not add generic job-search advice unless the user asks for it. End with one short note about any shared uncertainty, such as unstated hiring geography.

## Applications, contacts, CVs, and alerts

Search and comparison are read-only by default.

- Public contact details may be reported when they are actually visible. If RVC exposes contacts only after sign-in or Apply, explain that without guessing or bypassing access controls.
- Never claim to have applied, contacted an employer, created an alert, or uploaded a CV unless that action was completed and verified.
- Treat applying, messaging, uploading a CV, signing in, or creating a notification as a separate external action. Follow the active browser and confirmation rules immediately before that action.
- A locally provided CV may be read to derive search criteria, but do not upload it to RVC without the user's action-time confirmation.
