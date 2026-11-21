---
name: wejob
description: Search public WeJob job offers, training courses and company profiles in Switzerland. Use when the user asks for jobs, offres d'emploi, formations, companies or entreprises on WeJob.
---

# WeJob

WeJob is a Swiss job platform. This plugin gives read-only
access to its public catalog: active job offers, training courses and company
profiles. It never applies to a job, contacts a company or reads private data.

## Tool selection

- Job offers: `wejob_search_jobs`, then `wejob_get_job` for one offer.
- Training courses: `wejob_search_formations`, then `wejob_get_formation`.
- Companies: `wejob_search_companies`, then `wejob_get_company`.
- A broad search across all three: `search`; open a result with `fetch` and its
  `job:`, `formation:` or `company:` id.

## Search tips

- Put places in `location`: a city or a canton, in any language (Genève, Genf,
  Geneva, Vaud, Lausanne, Zurich). Several places can be comma-separated.
- Keep `query` short: one or two keywords such as `Java` or `data engineer`.
  Words are combined with OR, so long sentences dilute the results.
- Use the documented filter values listed in each tool, for example
  `employment_type` full_time or CDI, `work_mode` on_site, hybrid or remote,
  `experience_level` junior, intermediate, senior or expert. French terms such as
  temps plein or confirmé are accepted.
- Results include `pagination.total`: say how many results exist, not only how
  many are shown, and offer the next page when `has_more` is true.

## Answering

- Base every fact on tool results. If a field such as salary or work mode is
  missing, say it is not specified instead of guessing.
- When nothing matches, say so plainly and suggest a broader search (another
  canton, fewer filters).
- Give the public WeJob link of each result so the user can apply on WeJob.
