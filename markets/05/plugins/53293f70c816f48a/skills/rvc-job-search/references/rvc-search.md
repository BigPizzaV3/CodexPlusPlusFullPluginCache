# RVC search surface

Use this reference for live searches on the public RVC Global site. Routes and labels were verified against the public interface on 2026-08-26; when a route no longer works, return to `https://app.rvc.global/jobs` and use the visible search controls instead of guessing URL variants.

## Main routes

- All jobs: `https://app.rvc.global/jobs`
- Role examples: `/jobs/python`, `/jobs/java`, `/jobs/react`, `/jobs/typescript`, `/jobs/nodejs`, `/jobs/golang`, `/jobs/rust`, `/jobs/devops`, `/jobs/data-science`, `/jobs/product-management`, `/jobs/design`
- Work arrangement: `/jobs/fully-remote`, `/jobs/remote-in-country`, `/jobs/hybrid`
- Seniority: `/jobs/senior`, `/jobs/middle`, `/jobs/junior`
- Country examples: `/jobs/usa`, `/jobs/uk`, `/jobs/canada`, `/jobs/germany`, `/jobs/poland`, `/jobs/spain`, `/jobs/netherlands`, `/jobs/portugal`
- Remote-by-country examples: `/jobs/remote-jobs-usa`, `/jobs/remote-jobs-uk`, `/jobs/remote-jobs-canada`, `/jobs/remote-jobs-germany`, `/jobs/remote-jobs-poland`
- Known combinations include `/jobs/python-remote`, `/jobs/fully-remote-golang`, `/jobs/fully-remote-java`, `/jobs/fully-remote-react`, `/jobs/fully-remote-typescript`, `/jobs/fully-remote-devops`, `/jobs/fully-remote-nodejs`, `/jobs/senior-python`, and `/jobs/junior-python`.

Use one known direct route for the strongest criterion, then refine with visible filters. Do not generate arbitrary combination slugs; use the all-jobs page when a combination is not listed here.

## Search controls

The public job board exposes a text search with scopes `All`, `Company`, `Title`, and `Skill`, plus filters for:

- Job Function
- Key Competency
- Seniority
- Work arrangement
- Location
- Language
- Salary
- Relocation
- Extra criteria

Use the smallest set of filters that expresses the user's must-haves. When a control returns no results, relax only one lower-priority criterion at a time and label the resulting alternatives.

## Vacancy verification

Open the canonical `/vacancy/view/...` page for every reported result. Capture only fields that are visibly supported:

- title and company
- posting age or date
- location and work arrangement
- employment type
- original salary range, currency, and period
- required skills
- required languages
- explicit relocation support
- direct vacancy URL

The page may also offer `Apply Now`, `Notify On Similar`, or `Match by CV`. These are state-changing or data-transmitting workflows, not part of a read-only search. Do not activate them without the user's specific request and any action-time confirmation required by the active browser rules.

## Fallback search

If RVC's public filters cannot express a request, use one focused search query such as:

```text
site:app.rvc.global/vacancy/view "Senior Python" "Fully Remote"
```

Open and verify each result on RVC. Search snippets alone are not sufficient evidence because vacancies can expire or change.
