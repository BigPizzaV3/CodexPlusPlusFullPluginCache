---
name: mawsool-search-filters
description: Map a lead or company request onto Mawsool MCP search filters using the middleware accepted values for industry, country, seniority, job function, language, company size, revenue, founded year, and years of experience. Use before the Mawsool search tool, or when the user mentions filters, industry, country, city, seniority, headcount, revenue, or job title.
---

# Mawsool search filters

Call the Mawsool MCP `search` tool with these filters. Closed lists come from `middleware_service` on `apikeyshare` (`generate_filters_csv_v2.js` / `mawsool_api_allowed_filters.csv`). Copy closed values exactly. Never send a synonym for a closed field.

`search_type` is `people` or `companies`. `limit` is at most 25. `page` starts at 1.

## Build the filters object

1. Put the person's title in `job_title` (free text). Put level in `seniority` only when it matches the seniority list.
2. Put a city in `city`. Put the country in `location` using a string from [references/countries.md](references/countries.md).
3. Put industry in `industry` using a string from [references/industries.md](references/industries.md). Read that file before setting industry.
4. Copy seniority, function, language, company size, years, revenue, and founded year from the matching file in [references/filters.md](references/filters.md). Read that file before setting any closed filter.
5. One value is a string. Several values are an array. `{ "include": ["A", "B"] }` is also valid.
6. Drop any filter the user did not ask for.

## People

| Key | Value |
| --- | --- |
| `job_title` | Free text. `role` is an alias. Set `expand_job_titles` to `true` only when they want similar titles |
| `first_name`, `last_name` | Free text. Set `name_exact_match` to `true` for an exact name |
| `company_name` | Company name. `company` is an alias. Domain goes in `company_domain`. Numeric LinkedIn company id goes in `company_linkedin_id` |
| `seniority` | One of: `Owner / Founder`, `CXO`, `Partner`, `VP`, `Head`, `Director`, `Manager`, `Senior`, `Entry`, `Intern` |
| `function` | One of: `Operations`, `Business Development`, `Sales`, `Education`, `Engineering`, `Healthcare Services`, `Information Technology`, `Administrative`, `Arts and Design`, `Customer Success and Support`, `Finance`, `Community and Social Services`, `Media and Communication`, `Accounting`, `Marketing`, `Human Resources`, `Research`, `Program and Project Management`, `Legal`, `Military and Protective Services`, `Consulting`, `Entrepreneurship`, `Real Estate`, `Quality Assurance`, `Purchasing`, `Product Management`, `Leadership` |
| `industry` | Accepted industry string. `company_industry` is an alias |
| `location` | Accepted country. `country` is an alias |
| `company_location` | Accepted country for HQ. `headquarter` is an alias |
| `city` | Free text |
| `company_headcount` | `1-10`, `11-50`, `51-200`, `201-500`, `501-1000`, `1001-5000`, `5001-10000`, `10001+`. `company_size` is an alias |
| `language` | Lowercase name: `english`, `spanish`, `french`, `german`, `italian`, `portuguese`, `russian`, `chinese`, `japanese`, `korean`, `arabic`, `hindi`, `bengali`, `punjabi`, `javanese`, `telugu`, `vietnamese`, `marathi`, `turkish`, `dutch`, `polish`, `swedish`, `finnish`, `danish`, `norwegian`, `greek`, `hebrew`, `indonesian`, `malay`, `thai`. `languages` is an alias |
| `years_in_current_role` | `Less than 1 year`, `1 to 2 years`, `3 to 5 years`, `6 to 10 years`, `More than 10 years`. `experience_at_role` is an alias |
| `total_experience_years` | Same five strings. `experience` is an alias |
| `skills`, `education`, `keywords`, `behavioral_keywords` | Free text. `school` is an alias of `education` |
| `past_role`, `past_company` | `{ "include": ["..."] }` |

`revenue` and `founded_year` are company filters. Do not send them on a people search.

## Companies

Use `search_type: "companies"`.

| Key | Value |
| --- | --- |
| `company_name` | Name. `company` is an alias |
| `company_domain` | Domain only, such as `acme.com` |
| `industry`, `location`, `city`, `company_headcount` | Same accepted values as people |
| `keywords` | Free text |
| `revenue` | Id, not the dollar label: `0-1000000` ($0–$1M), `1000000-10000000` ($1M–$10M), `10000000-50000000` ($10M–$50M), `50000000-100000000` ($50M–$100M), `100000000-500000000` ($100M–$500M), `500000000-1000000000` ($500M–$1B), `1000000000+` ($1B+) |
| `founded_year` | `2020-2026`, `2010-2020`, `2000-2010`, `1990-2000`, `0-1990` (before 1990) |

## Phrase mapping

- Founder, owner, co-founder → seniority `Owner / Founder`. Keep their title in `job_title` when they named one.
- CEO, CTO, CFO, chief, C-level → seniority `CXO`.
- VP or vice president → seniority `VP`. Head → `Head`. Director → `Director`. Manager → `Manager`. Senior → `Senior`. Junior or entry → `Entry`. Intern → `Intern`.
- UAE or Emirates → `United Arab Emirates`. KSA or Saudi → `Saudi Arabia`. US, USA, or America → `United States`. UK or Britain → `United Kingdom`. Russia → `Russian Federation`. Vietnam → `Viet Nam`. South Korea → `Korea, Republic of`. Iran → `Iran, Islamic Republic of`. Syria → `Syrian Arab Republic`.
- Dubai, Riyadh, Doha, and other cities → `city`, plus `location` set to the accepted country.
- IT → function `Information Technology` and industry `Information Technology & Services` only when they mean the industry. Software or SaaS → industry `Computer Software`. Oil and gas → `Oil & Energy`. Healthcare or hospital → `Hospital & Health Care`.
- A headcount that crosses buckets becomes an array of the overlapping sizes. `50-200` is `51-200`.
- Exclude a current company with `company_name: { "exclude": ["Name"] }`. Exclude is not applied to seniority, industry, location, function, or headcount.

If an industry or country is not an exact list entry, read the reference file and pick the closest accepted string. Tell the user which value you used.

## Example

User: "VP Sales at software companies in Dubai, 50 to 200 people."

```json
{
  "search_type": "people",
  "page": 1,
  "limit": 10,
  "filters": {
    "job_title": "VP Sales",
    "seniority": "VP",
    "function": "Sales",
    "industry": "Computer Software",
    "location": "United Arab Emirates",
    "city": "Dubai",
    "company_headcount": "51-200"
  }
}
```
