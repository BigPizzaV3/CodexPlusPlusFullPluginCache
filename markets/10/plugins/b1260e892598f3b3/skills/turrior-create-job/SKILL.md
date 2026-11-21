---
name: turrior-create-job
description: Create and optionally publish a Turrior job post when the user asks to create, post, or publish a vacancy.
---

Use this skill when the user wants to create a new Turrior job post.

1. Gather the missing job details in one concise message. Always determine the recruiting location before calling `create-new-job`.
2. Location rules:
   - Maximum 5 countries.
   - A city may be used only with exactly one country.
   - `onsite` requires both country and city.
   - "Worldwide" or "no restriction" means no `countryIds`.
3. Never guess dictionary IDs:
   - category → `search-categories`
   - country → `search-countries`
   - city → `find-city`, using the country's lowercase ISO2 `countryCode`
4. If a city search is ambiguous, ask the user to choose.
5. Call `create-new-job` only when the user has asked to create the job. Include all information already available rather than creating an unnecessarily incomplete draft.
6. If the user wants the job published, call `publish-job`. If required fields are missing, explain what must be completed.
7. After creation, offer to create and attach a video quiz with at least one introductory question about the candidate and their relevant experience. Explain that it can provide additional information for candidate scoring.
8. After successful publication, retrieve the job if necessary and return its public application URL:
   `https://turrior.com/apply/{slug}`
