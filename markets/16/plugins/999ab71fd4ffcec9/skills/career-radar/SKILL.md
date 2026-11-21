---
name: career-radar
description: Use when a user wants recurring or on-demand job discovery, especially remote roles, evaluated against their resume, experience, preferences, or target roles. Search for new opportunities, validate their status, avoid repeats when history is available, and produce a concise evidence-based report.
---

# Career Radar

Career Radar helps each user discover and prioritize job opportunities using an independent profile. It is designed to run as an on-demand request or as a scheduled ChatGPT task. The host performs web research; this skill defines the onboarding flow, search protocol, evaluation method, and report format.

## Operating principles

- Never apply to a job, contact a recruiter, or submit personal information.
- Use the user's resume and stated preferences as the source of truth for their profile.
- Never assume, reuse, or expose another user's profile, resume, preferences, or search history.
- Prefer primary sources: the employer's career page or the original application page.
- Do not invent a salary, requirement, date, location, technology, or hiring status.
- Mark uncertain facts as `Não verificado` and explain why.
- Prefer fresh listings that are still accepting applications.
- Do not repeat a previously reported opportunity unless there is a meaningful update.
- Treat a job as a distinct opportunity by its canonical application URL, then by employer plus normalized title.

## First-run onboarding

At the first use, or whenever the current profile is incomplete, collect a profile before searching. Ask for the fields below in one concise onboarding message. Do not require a specific resume format.

1. Resume or a structured career summary.
2. Target roles and seniority.
3. Preferred and required technologies, industries, and exclusions.
4. Work model, geography, time zone, and work authorization constraints.
5. Languages, salary expectations, and other filters, if relevant.
6. Desired search frequency and report window, when setting up a task.

Confirm the interpreted profile before the first search. If the user declines to provide a resume, continue with the structured summary and explicitly reduce confidence in technical-fit conclusions. Do not require the user to provide individual job links. The purpose of this skill is to discover them.

Keep the profile scoped to the user's ChatGPT conversation, task, or agent context. The skill does not create a permanent profile store.

See `docs/user-profile.md` for the neutral profile contract.

## Search protocol

For each run:

1. Translate the target roles and profile into several focused search queries.
2. Search for listings published or updated since the previous report. If no previous date is available, use the last 7 days and clearly state that assumption.
3. Include searches in Portuguese and English when relevant to the user's market.
4. Search employer career pages and reputable job boards. Avoid relying on snippets alone.
5. Collect more candidates than needed, then normalize title, employer, location, work model, date, URL, and source.
6. Remove obvious duplicates before evaluation.
7. Check the original listing for an active application flow. A search result alone is not proof that a vacancy remains open.
8. Evaluate the strongest candidates first and stop when the report has enough high-quality results.

When the user requests Brazil, interpret `100% remoto no Brasil` as remote work that can be performed from Brazil. Do not silently treat `remote` as worldwide eligibility.

## Evaluation

Score each validated opportunity from 0 to 100 using the rubric in `docs/scoring-rubric.md`. Explain every score with evidence from both the resume and the listing.

Use these outcome bands:

- `85-100`: forte prioridade
- `70-84`: boa aderência
- `55-69`: aderência parcial
- `0-54`: baixa prioridade

Separate hard blockers from learnable gaps. A missing preferred tool should not outweigh a mismatch in work authorization, seniority, or core responsibilities.

## Deduplication and history

Use task or conversation history when available. Compare canonical URLs, employer, normalized title, location, and listing date. Report only new jobs or meaningful changes such as a reopened listing, changed requirements, or a material status update.

If reliable history is unavailable, say so briefly and avoid claiming that the result is globally deduplicated. Persistent deduplication, source-specific history, and alert state require the optional MCP phase described in `docs/future-mcp.md`.

## Report format

Start with a short run summary:

- search date and freshness window;
- number of listings reviewed;
- number of active opportunities reported;
- limitations, including unavailable history or unverified details.

Then use the template in `docs/report-template.md`. Include, for every opportunity:

- role, employer, location, and work model;
- compatibility score and priority band;
- original application link;
- evidence-based strengths;
- material gaps or risks;
- application status and verification date;
- a direct recommendation: `Priorizar`, `Avaliar` or `Não priorizar`.

End with a compact comparison table and one suggested next action. Never present a fabricated certainty score as a fact about hiring likelihood.

## Scheduled task setup

When the user asks for a recurring search, collect or confirm the cadence, preferred execution time, time zone, freshness window, minimum compatibility score, maximum results, target roles, and delivery format. Daily and weekly searches are both valid. Help the user configure the host's scheduling feature; the plugin itself does not create or modify schedules.

The task instruction should contain the user's own profile and preferences, or refer to profile information that the host explicitly makes available to that task:

```text
Use Career Radar to search for new opportunities matching my saved resume and preferences. Search recent listings, validate that applications are open, do not repeat previously reported jobs unless there is a meaningful change, and return the standard Career Radar report. Do not apply to any job.
```

If the user requests a daily or weekly schedule without specifying a time zone, ask for it instead of guessing. If the host cannot persist the profile or history for scheduled runs, explain the limitation and include the necessary profile fields in the task instructions.
