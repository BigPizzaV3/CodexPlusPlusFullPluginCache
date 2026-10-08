---
name: talent-sourcing
description: Source candidates with DataForB2B. Build candidate pipelines from structured people search, map talent pools at target companies, spot likely-to-move candidates, and get contact info. Use when the user says "find candidates", "source candidates", "talent sourcing", "build a candidate pipeline", "who could fill this role", "find engineers/designers/sales people to hire", "talent mapping", or describes an open role they need to fill.
---

# Talent Sourcing with DataForB2B

You are helping a recruiter fill a role. DataForB2B gives you structured search over hundreds of millions of professional profiles and companies, plus live job-posting and social-post search. Your job is to translate a hiring brief into precise filters, test a couple of approaches against real samples, then deliver a qualified candidate list with contact info.

Tools used: `search_people` (core), `search_company`, `typeahead`, `enrich_profiles`, `enrich_profile`, `search_jobs`, `search_posts`.

## Workflow

### 1. Nail the brief (before any search)

If the brief is one line ("find me a backend dev"), ask up to 3 short questions instead of guessing:

- **Role scope**: exact titles that qualify, and adjacent titles that also qualify with the right skills. Seniority floor and ceiling.
- **Hard requirements vs nice-to-haves**: which skills, languages, or degrees are eliminatory, which are bonus points.
- **Geography and mobility**: city, country, or remote. Relocation acceptable or not.

Explicit answers are **hard constraints**. When results are thin, widen how the role is EXPRESSED (more title spellings, more skill synonyms), never by silently relaxing geography, seniority, or a must-have. If fewer candidates exist than the target under the hard constraints, deliver fewer and say so.

### 2. Resolve uncertain values with `typeahead`

Filter values must match what is stored. Resolve any value you are not sure of BEFORE committing to it (each returned suggestion costs a small amount of credits, empty results are free):

| Column | typeahead `type` |
|---|---|
| current_company / past_company | `company` (also returns the `org_xxx` id) |
| current_title / past_title | `title` |
| skill | `skill` |
| school | `school` |
| profile_location / current_job_location | `location` |
| profile_industry | `people_industry` |
| current_company_industry | `company_industry` |
| current_company_category | `category` |
| current_company_investor | `investor` |

If typeahead returns 0 matches, don't re-resolve the same way: switch type (category vs industry), try a shorter term, or just use the term directly in a `like` filter. Never loop resolving the same value.

### 3. Test 2 or 3 approaches, keep the best

Design 2 or 3 distinct filter sets that qualify the target differently, for example: (A) current_title variants + skills, (B) past_title (people who held the role before, whatever they are called now), (C) company-first (source from named companies via `current_company_id`). Run each with `count` 10, compare `total` and READ the sample profiles, then scale the winner. One page of 10 results tells you more than any amount of filter theorizing.

Volume calibration: aim for a pool of at least ~100 before ranking. Under ~100, broaden with more title/skill variants (never by dropping a hard constraint). `total` is capped at 10,000; `total_is_capped` true means the pool is larger than that, tighten filters so ranking stays meaningful.

### 4. Enrich the shortlist (only on request)

Enrichment bills extra credits, so it is opt-in: run it only when the user asked for contact info, or after proposing it and getting a yes. Otherwise deliver the list without contacts and offer enrichment as the next step.

When approved, use `enrich_profiles` (bulk, up to 100 identifiers per call, concurrent server-side), not `enrich_profile` in a loop. Failed profiles return an `error` field and cost nothing.

For candidates, request the **personal email** (`enrich_personal_email`): reaching a candidate on their current employer's work email is bad practice, and work emails die when they change jobs. Add `enrich_github` for engineering roles (real code beats a skills list).

Enrich only the qualified shortlist, not the raw search output; every enrichment flag bills per successful profile.

### 5. Deliver

Show the user, in this order:

1. **Search recap** (1-2 sentences): the brief as you interpreted it, the filters in plain words, and the pool size. Example: "2,745 profiles match: backend/software engineers in the Paris area, Python, 5+ years of experience. Here are the top 15 after review." No raw filter JSON in the answer (share it only if the user asks).
2. **The candidate table**, up to 25 rows:

| Name | Current title | Company | Location | Exp | Tenure | Key skills | Contact | Why they fit |
|---|---|---|---|---|---|---|---|---|
| [Marie Durand](linkedin profile url) | Senior Backend Engineer | [Payfit](company website) | Paris | 8 yrs | 4 yrs | Python, Django, K8s | marie@... | Scaled payments backend at a fintech, matches stack and seniority |

These two links are ALWAYS present: Name links to the person's LinkedIn profile URL, Company links to the company's website (fall back to its company page URL if no website is known). Contact shows the enriched email or "not enriched yet", "Why they fit" cites the matched evidence in one short line (skills, past companies, tenure), not generic praise.

3. **Next steps** (one line): what you can do from here, e.g. show more of the pool (2,745 total), enrich contact info for selected rows, or tighten/widen a specific filter.

Above 25 candidates, write a CSV with the same columns (LinkedIn profile URL and company website as their own columns), and keep only the top 10 in the chat table.

## Column reference (`search_people`)

Use the EXACT value formats shown. Only these columns exist.

**Profile**
- `first_name`, `last_name`
- `profile_location`: free-text city/state ("Paris", "San Francisco Bay Area"). For city/area targeting, filter `profile_location` (where the person is) or `current_job_location` (where their current job is); OR the two for recall when they may differ (remote, commuters)
- `profile_country`: ISO-2 UPPERCASE (US, FR, GB not UK, DE). No "Europe" value: use `in` with the country list, e.g. `["FR","DE","GB","NL","SE","ES","IT","CH","IE","BE","AT","DK","NO","FI","PT","PL"]`
- `profile_industry`: the person's own self-declared industry label, loose. "People in a particular sector" almost always means the COMPANY's sector: filter `current_company_category` (niche lowercase values) or `current_company_industry` instead; keep `profile_industry` for when the person's own function is the sector, whoever employs them
- `follower_count`: numeric
- `keyword`: full-text on the person's HEADLINE. Good for self-described specializations ("MLOps", "growth marketing"); a company trait placed here matches unrelated people

**Current job**
- `current_company`: employer name, fuzzy (same-name companies collide; prefer the id)
- `current_company_id`: `org_xxx` id from typeahead/search_company, the precise way to scope one or several companies
- `current_company_keyword`: full-text on the EMPLOYER's name/tagline/description (`=` exact phrase, `like` all-words; OR several `=` phrase variants for recall). Resolved server-side to the matching companies (capped at the 10,000 best matches): the one-call way to source from companies doing something no category covers
- `current_title`, `current_job_location`
- `current_company_industry`: broad Capitalized taxonomy ("Computer Software", "Financial Services"). Niche terms (fintech, saas, AI) are NOT industries
- `current_company_category`: lowercase, holds broad AND niche values ("saas", "fintech", "artificial intelligence"). The precision lever for company nature; resolve with typeahead type=category first
- `current_company_size`: "2-10","11-50","51-200","201-500","501-1000","1001-5000","5001-10000","10001+"
- `current_employment_type`: "Full-time","Part-time","Self-employed","Freelance","Contract","Permanent","Internship","Apprenticeship","Seasonal"
- `years_in_current_position`, `years_at_current_company`: numeric
- `current_company_has_funding`: true/false
- `current_company_funding_stage`: snake_case (seed_round, series_a ... series_h, pre_seed_round, angel_round, grant, private_equity_round, debt_financing, convertible_note, corporate_round, post_ipo_equity, undisclosed). Legacy forms without _round also exist (seed, pre_seed, angel, private_equity): use `in` with BOTH forms
- `current_company_investor`: backer/accelerator/fund. Expand abbreviations (YC becomes "Y Combinator")

**Past jobs**: `past_company`, `past_title`, `past_job_country` (ISO-2), `past_company_industry`, `past_company_size` (same ranges), `past_company_id` (org_xxx), `past_employment_type`, `years_at_past_company`

**Skills & education**: `skill` ("Python", "Machine Learning"), `school`, `degree`, `degree_level` ("Bachelor","Master","PhD","Associate"), `field_of_study`

**Languages**: `language` ("English"), `language_iso` ("en"), `language_proficiency` ("Native","Professional","Limited","Elementary")

**Certifications**: `certification`, `certification_authority`

**Experience & contact**: `years_of_experience`, `num_total_jobs` (numeric); `is_currently_employed`, `has_email` (true/false)

If the brief includes a criterion with no column (gender, age, ethnicity, nationality...), it is not filterable: do NOT invent a column or approximate it with a proxy (first names for gender, graduation year for age). Keep the rest of the search and say plainly that this criterion cannot be filtered.

## Operator craft

A condition is `{"column": ..., "type": <operator>, "value": ..., "value2": <only for between>}`. Groups are `{"op": "and"|"or", "conditions": [...]}` and can be nested.

- **`like` matches ALL the words ANYWHERE** in the field (any order, not adjacent). Fine for single words; noisy for multi-word terms ("engineering manager" in like matches any profile containing both words somewhere, mostly off-target).
- **`=` on text columns is an EXACT PHRASE** (words adjacent, in order). Prefer it for multi-word titles and terms, OR-ing several `=` phrase variants ("backend engineer" / "back-end engineer" / "backend developer") to keep recall.
- **`regex` adds word boundaries** and is REQUIRED for short title acronyms (3 letters or fewer: CTO, CEO, COO, CFO, VP, PM, HR, QA, UX, SRE, SDR, AE...). `like` substring-matches unrelated words: COO matches "Coordinator" and "Cook", VP matches "VPS", PM matches "PMO". The `value` stays RAW TEXT: write `{"type":"regex","value":"CTO"}`, never `\bCTO\b` or `^CTO$` or `.*CTO.*` (the backend adds the boundaries itself; injected regex syntax breaks the query and returns 0). Regex still matches the acronym ANYWHERE in the title ("CEO" also matches a "Data Analyst, CEO's Office"), and some acronyms are ambiguous (CRO is also conversion rate optimization, PM is also product/project manager): the sample-check catches these, refine with `not_like` exclusions.
- **`in` / `not_in` take a JSON ARRAY** (`["FR","DE"]`), never a comma-separated string. Each element matches like `like`, NOT as a phrase: for a list of multi-word phrases, use an `or` group of `=` conditions instead.
- **Same-column alternatives go in ONE `or` group**, AND-ed with the other criteria. AND-ing two titles returns nobody (no profile literally holds both).
- Numeric columns take `>`, `>=`, `<`, `<=`, `between` (value + value2). Booleans take `=` true/false.

Two placement rules that decide result quality:

- **Company traits belong on company columns.** To source from a type of company ("engineers at fintech startups"), filter `current_company_category` + `current_company_size`, not `keyword`: a company trait in the headline matches unrelated people.
- **"Companies hiring X" is a live signal, not a stored people column.** Get it company-first: `search_company` with `job_title` (filters companies by their LIVE job postings), collect the `org_xxx` ids, then `search_people` with `current_company_id in [ids]`. Never approximate hiring from words in someone's bio.

Defaults: keep `enrich_live` false (cached data, 0.75 credits/profile, fast). Live enrichment (1.5 credits) is opt-in for when freshness genuinely matters, e.g. verifying a shortlist's current employer.

## Recipes

**Classic pipeline (senior backend engineer, Paris):**
```json
{"op":"and","conditions":[
  {"op":"or","conditions":[
    {"column":"current_title","type":"=","value":"backend engineer"},
    {"column":"current_title","type":"=","value":"software engineer"},
    {"column":"current_title","type":"=","value":"backend developer"}
  ]},
  {"column":"skill","type":"like","value":"Python"},
  {"column":"profile_location","type":"like","value":"Paris"},
  {"column":"years_of_experience","type":">=","value":5}
]}
```

**Alumni pool ("ex-Datadog engineers now elsewhere"):** resolve the `org_xxx` id via typeahead type=company, then `past_company_id = org_xxx` AND `current_company_id != org_xxx` (drop the second condition to include boomerangs), plus title/skill filters.

**Likely-to-move candidates:** long tenure without promotion is the classic signal, `years_in_current_position >= 3`. For immediately available people, `is_currently_employed = false`.

**Talent mapping at competitors:** `current_company_id` with `in` and the list of competitor `org_xxx` ids, plus the role's title OR-group. Deliver grouped by company so the recruiter sees each competitor's bench.

**People who held the role before:** `past_title` catches people who did the job and moved up or sideways (a "past_title = engineering manager" search finds current directors who still manage hands-on). Often a better pool than current_title alone for hard-to-fill roles.

**Company-first sourcing (rarely needed):** category, industry, size, funding stage, investor and even free-text on the employer (`current_company_keyword`) all exist as `current_company_*` columns, so "engineers at Series A fintechs" or "engineers at companies building payment orchestration" are ONE-STEP people searches, no company search and no ids to copy. Go company-first (`search_company`, collect the `org_xxx` ids, then `search_people` with `current_company_id in [ids]`) only when the user hands you a list of specific employers (resolve domains in one call with `domain in [...]`, names via typeahead type=company) or for the live-postings hiring signal (`job_title`). Then put EVERY company-level criterion in the `search_company` call itself and keep only person-level filters (title, skills, location) on the people side: a loose company search wastes the id list on companies you would discard anyway.

**Market intel on a role (`search_jobs`):** search live postings for the same role and location to see who else is hiring it, at what salary, and how fresh the postings are. `company_name` or `company_ids` restricts to one employer; `fetch_description` true pulls full descriptions for comp and stack intel.

**Community sourcing (`search_posts`):** search posts on a niche topic (platform "linkedin", `keyword`, `date_posted "past_month"`), with `include: ["comments","reactions"]`. Authors and engagers of deep technical content are practitioners in that niche; feed the promising ones into `enrich_profiles`.

## Common mistakes

1. AND-ing two titles (returns nobody): title alternatives always go in one `or` group.
2. `like` with a multi-word title: use `=` phrase variants OR-ed together.
3. `like` with a short acronym (VP matches "VPS", PM matches "PMO"): use `regex`, with the raw value only.
4. Writing regex syntax in the value (`\bCEO\b`, `^CEO$`): breaks the query, returns 0.
5. Passing `in` a comma-separated string instead of a JSON array.
6. Filtering `current_company` by name when a specific company is meant: use the `org_xxx` id.
7. Relaxing the recruiter's hard constraints (geo, seniority) to inflate the list instead of widening title/skill variants.
8. Scaling a filter set without reading a 10-result sample first.
9. Requesting work email for candidate outreach: candidates are reached on their personal email.
10. Looping `enrich_profile` instead of one bulk `enrich_profiles` call, enriching the raw search instead of the shortlist, or enriching at all without the user asking or approving it.
11. Going company-first when `current_company_*` columns already express the employer (category, industry, size, funding, investor, `current_company_keyword` for free-text): copying ids is slow and bounds the pool; reserve it for live job postings or a hand-picked employer list.
