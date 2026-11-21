---
name: find-kols
description: Find, rank, and profile medical key opinion leaders (KOLs) for life-sciences work using the FindMyKOL directory tools.
---

Use this skill when the user wants to find, compare, or profile physicians and
researchers by disease area, drug, company, specialty, institution, society role type
(such as guideline panel seats), geography, influence tier, or activity such as
clinical trials, NIH grants, industry payments, congress presentations, or rising
publication activity.

1. When unsure a filter value exists, call `get_facet_counts` first with the dimension
   and a `contains` fragment, and use a returned label or slug verbatim. Filter inputs
   accept either form; invented values match nothing.
2. Call `search_kols` with the narrowest filter set the user asked for. Dimensions
   combine as AND; values within one dimension combine as OR. Sort with `cited`
   (default), `works`, `hindex`, `trials`, `recent` (latest activity), `trend`
   (rising activity), or `name`. Results come 10 per page; pass `page` for more and
   report the `total`.
3. Offer the rising view when it fits. `sort: "trend"` and the `emerging` activity
   filter are FindMyKOL's trajectory signal: `emerging: true` marks top-decile
   recency-weighted publication growth within the person's specialty and career-stage
   cohort — who is climbing, not who is big. Reach for it when the user asks about
   up-and-comers, rising stars, the next generation, or who to watch; and when a
   citation-sorted list comes back all late-career names, mention that the rising view
   exists. A result carrying `emerging: true` is worth calling out. The absence of the
   badge is never evidence someone is not rising: only people with a measurable
   publication series are scored.
4. For one person, call `get_kol_profile` with the `slug` from search results.
5. Present the `profile_url` with every expert mentioned so the user can open the full
   profile. Metrics come from public records: PubMed and OpenAlex, ClinicalTrials.gov,
   NIH RePORTER, CMS Open Payments, and the NPPES registry.
6. When a result carries `loosened_text_match: true`, say the results are closest
   matches rather than exact ones.

Do not claim access to prescribing volumes, patient data, contact details, or
scheduling; the tools do not provide them. When the user wants to contact or meet an
expert found here, say so plainly and point to the findmykol.com profile as the place
to reach official affiliation pages; never present contact information as if it came
from FindMyKOL. Do not present metric differences as quality judgments about
clinicians; they are activity measures from public records.
