---
name: find-remote-jobs
description: Search Himalayas for remote jobs that fit the user, by role, country, seniority, employment type, salary, category, benefits or company, and shortlist them with the details that matter. Use when the user asks to find, browse or compare remote jobs, asks what jobs fit their profile or a location, or wants new matches since they last checked.
---

# Find remote jobs

Follow [himalayas-basics](../himalayas-basics/SKILL.md) for the shared rules.
Search works without signing in. New matches and the tracker need an account.

## 1. Pin down the search

Ask only for what the user has not said and the search needs:

- **Role or keywords**, such as "product designer" or "Rust".
- **Where they can work from.** Remote jobs are open to listed countries or
  worldwide. Resolve the country with `get_correct_country_name` when it is
  abbreviated or misspelt.
- Optional: seniority (`experience`), employment `type`, a salary floor
  (`salary_min` with `currency`), `salary_required`, `markets` (categories),
  `benefits` or `companies`.

If the user is signed in and asks for jobs that fit them, read
`get_my_profile` first and take the role, location, work permits and salary
expectations from it. Say which profile facts you used.

## 2. Search

- `search_jobs` with a keyword and filters. `sort: recent` for the newest,
  `salaryDesc` to lead with pay.
- `worldwide: true` returns only jobs open to every country.
  `exclude_worldwide: true` with a country returns only jobs specific to it.
- `get_jobs` browses the latest jobs with no keyword.
- Results are paged. Fetch the next `page` only when the first page is not
  enough.

For a signed-in user who wants what is new, call `get_new_matches`. It returns
jobs matching their profile posted since an agent last checked.

- **Plus plan:** the reply lists the jobs and moves the check-in point, so
  the next call returns only newer ones.
- **Free:** the reply gives the number of new matches; listing them needs a
  Himalayas Plus plan. Say so once (see himalayas-basics), then do the free
  version: run `search_jobs` for the user's primary role and location with
  `sort: recent`.
- **Profile incomplete:** the reply lists what is missing. Offer
  [build-candidate-profile](../build-candidate-profile/SKILL.md), and search in
  the meantime.

## 3. Shortlist

For the three to five most promising jobs, call `get_job_details` with the
`company_slug` and `job_slug` from the results. Present each with:

- title, company and the Himalayas link;
- where it is open to, and whether that fits the user;
- salary, if listed;
- seniority and employment type;
- one line on why it fits, and anything that rules it out, such as a time zone
  or a visa requirement.

Use `get_related_jobs` when the user likes a job and wants more like it.

## 4. Next steps

Offer to save jobs to the tracker (see
[track-applications](../track-applications/SKILL.md)) or to start applying
(see [apply-to-jobs](../apply-to-jobs/SKILL.md)). When the user passes on a
match, `skip_job` with the reason keeps it out of future matches; confirm
first. Use the `job_closed` reason only when the listing really is closed: it
reports the job as expired for everyone.
