---
name: research-companies-and-salaries
description: Research remote companies and pay on Himalayas, covering company profiles, tech stacks, benefits and open jobs, salary benchmarks by role, seniority and country, and which skills, categories, countries and industries have the most remote jobs. Use when the user asks about a company, wants companies that hire remotely in a field or country, asks what a role pays, or wants remote job market trends.
---

# Research companies and salaries

Follow [himalayas-basics](../himalayas-basics/SKILL.md) for the shared rules.
Every tool here works without signing in.

## Companies

- `search_companies` finds companies by keyword, country, benefits or
  `tech_stack`. `sort: jobs` leads with the companies hiring most.
- `get_companies` browses remote-friendly companies.
- `get_company_details` with the company slug returns the profile: about,
  size, founding year, tech stack, benefits, open jobs and social links.

For a company deep dive, report what the company does, size and age, where it
hires, benefits, tech stack, and its open jobs that fit the user. Add salary
benchmarks for those roles from the next section.

## Salaries

`get_salary_data` takes a job title, with optional `seniority` and `country`,
and returns the minimum, median and maximum in US dollars. Titles are matched
loosely. When comparing countries or seniority levels, call it once per
combination and show the results in one table. Say which country and level
each row is, and that figures are in USD a year.

## Market trends

`get_remote_work_statistics` returns the top entries by job or company count
(`record`) for `skills`, `categories`, `countries` or `industries` (`type`),
optionally in one country. Use it to answer which skills are in demand or
where remote hiring is busiest.
