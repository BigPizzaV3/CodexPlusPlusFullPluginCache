---
name: ken-search
description: Create and validate people-search filters for the 280M+ contact database and persist them as a saved search bound to the campaign.
---

# Lead Search Skill

Build people-search filters for the Kenso contact database (280M+ people), check that the lead count fits the campaign, and save the filters as a saved search.

## Inputs

- Broad ICP, segments, and the lead target from the plan in the conversation. Ask the user for any that is missing.
- Workspace research for targeting details and any named target accounts.

## Core Principles

- **Breadth over perfection** - Capture the full addressable market. AI qualification handles edge cases.
- **Size to the target** - When the user or the calling agent sets a lead target and a count range, tune to that range. Otherwise aim for 3x-10x the desired contacts: about 5x covers enrichment (~30% email found), verification (~70% valid), and qualification (~60% pass).
- **Function + seniority over long title lists** for broad roles. Use `isDecisionMaker: true` instead of listing VP/CLevel/Director.
- **No keywords** - They shrink the search for no gain. Let qualification judge.
- **Only 6 supported countries** - United Kingdom, United States, Canada, Ireland, New Zealand, Australia. Never author `countries` or `companyHeadquarters` outside them. If the ICP is elsewhere, tell the user instead of building an empty search.
- **Full-phrase title matching** - A title matches the whole phrase, not single words. Expand every role into 8-15 real variants (`"VP Marketing"`, `"VP of Marketing"`, `"Vice President Marketing"`, `"Head of Marketing"`, `"Director of Marketing"`); unexpanded lists silently miss people.
- **Trust normalization** - Pass `"United States"`, `"California"`, `"Berlin"` as written; full names, ISO codes, and abbreviations all work, and industry `&`/`and`/`+` variants match. For a fuzzy value, pass the most common natural-language label; resolve a company name with `search_companies(body={"name": "..."})`.
- **Skip the catalog** - Don't call `get_search_filters()`: it returns the whole dropdown catalog (20-50k+ tokens). The values below and in the reference cover nearly every search.

## Filter Keys

`search_people()`, `get_people_search_facets()` and the saved searches (`create_saved_search()`) take one filter object with these exact camelCase keys. A snake_case or unknown key is rejected with 400 `unknown_filter_fields`, and the message names it (with the key it most likely meant, such as `companyHeadcount` for `companyHeadcountMin`). (They are API keys, not app form names such as `titles`, `geos`, or `headcount`.)

| Key | Value |
|-----|-------|
| `currentTitles`, `excludeTitles`, `pastTitles` | string[] of full-phrase titles |
| `seniorityLevels`, `excludeSeniorityLevels` | `Training`, `Entry`, `Individual`, `Senior`, `Manager`, `Director`, `VP`, `CLevel`, `Owner`, `Partner` |
| `functions`, `excludeFunctions` | LinkedIn job functions: `Engineering`, `Sales`, `Marketing`, `Finance`, `Operations`, `Human Resources`, ... |
| `isDecisionMaker` | `true` (VP+ shortcut) |
| `industries`, `excludeIndustries` | lowercase LinkedIn industries: `"software development"`, `"financial services"` |
| `companyHeadcount` | `{"min": 51, "max": 500}` |
| `companyTypes` | `"Privately Held"`, `"Public Company"`, `"Non Profit"`, ... |
| `companyHeadquarters`, `excludeCompanyHeadquarters` | HQ locations (6 countries only) |
| `currentCompanies`, `excludeCompanies`, `pastCompanies` | company names |
| `currentCompanyIds` | numeric index ids from `search_companies()`, never invented |
| `countries`, `states`, `cities`, `excludeCountries` | person location |
| `companyFundingAmount`, `companyFundedWithinDays` | `{"min", "max"}` whole USD; days 1-3650 |
| `yearsOfExperience`, `yearsInCurrentRole`, `yearsInCurrentCompany` | `{"min", "max"}` |
| `skills`, `excludeSkills`, `schools`, `degrees`, `languages` | string[] |
| `page`, `pageSize` | integers (`pageSize` max 100) |

More keys (names, job-change signals, education, sort), the full function and industry lists, and account (company) search keys: `references/ken-search-filters.md`.

## Validate Before Every Count

1. Every key is in the table or the reference, camelCase. Drop anything else.
2. Lists are string arrays; ranges are `{"min", "max"}` objects with min <= max; booleans are `true` or omitted; ids are numbers.
3. Locations stay inside the 6 supported countries.
4. Don't combine `currentTitles` AND `seniorityLevels` AND `functions` unless the ICP truly needs all three.
5. Omit empty arrays and nulls.

## Workflow

1. **Target** - segments x contacts per segment = desired contacts (default ~1,000-2,000 per segment unless the plan or caller sets a target). The campaign's contact limit wins when present.
2. **People-first or account-first** - Default is people-first (role + company attributes). Account-first when research names target accounts or the plan says ABM: resolve names with `search_companies(body={"name": "..."})`, then `search_people_at_companies(account_ids=[...], current_titles=[...])` (flat arguments).
3. **Expand** - `expand_search_terms(kind="titles", titles=[...])` and `expand_search_terms(kind="industries", industries=[...])`; merge the variants. If expand errors, keep the values you have.
4. **Build and validate** the filter object.
5. **Facets** - `get_people_search_facets(body=<filters>)`. If one bucket holds over 60% of results, the other dimensions are probably too narrow: loosen them.
6. **Count** - `search_people(body={<filters>, "page": 1, "pageSize": 1})` and read `totalResults`. Too few: broaden titles, add industries, widen geography, drop a seniority constraint. Too many: narrow titles or geography, add seniority or company size. Up to 3 retunes, then go with the best and note the gap.
7. **Sanity check (optional)** - `lookup_person_by_linkedin_url(linked_in_url=...)` on 1-2 example prospects from the research.

## Save the Search

Every search built for a campaign gets saved: the saved search is the source of truth and lets the user open the filters in People Search.

`create_saved_search(name="{campaign name} - filters", search_type="people", filters_json=<filter object>, is_shared=true)`

- Pass the object itself (not double-encoded) and `is_shared=true`. Add `workspace_id` when the user can see more than one workspace.
- Re-runs: `list_saved_searches()` first; update a same-named search with `update_saved_search(search_id=..., filters_json=...)`. Never leave two for one campaign.
- Account-first: also save the account filter set with `search_type="account"`, named `"{campaign name} - accounts"`.
- Multi-list: one saved search per list, named `"{campaign name} - {list name}"`.

Then put the saved search id, filter summary, result count and desired contacts in the conversation as a `## Search Filters` summary. Qualification and segmentation read it to avoid restating filters. Report every saved search id, the count-to-target ratio, and any save that failed with its error.

## Multi-list Campaigns

When the plan mixes distinct ICPs (e.g. SaaS founders + agency founders), build, validate, and save one filter set per list instead of one OR'd mega-search. Each list is imported on its own with its own import limit, split half/half by default or by the user's weights; the import is the campaign build's step, not this skill's. A campaign list that still has contacts cannot be deleted, so get the split right first; fix a bad combined import with manual segments.

## Recruiting campaigns

For a campaign with `kind` `recruiting`, search for people who could take the role. Take the title, the must-haves, the location and the remote policy from the user or the role description in the conversation.

- Titles: `currentTitles` with the role's title and its close variants; add `pastTitles` for people who did the job before and moved up or sideways.
- Experience: `yearsOfExperience` from the must-haves (`{"min": 5}` for "5+ years"). `yearsInCurrentRole` or `tenureRipe` favours people ready to move. `promoted` and `changedJobRecently` usually mean someone just settled in, so use them only when the role asks for it.
- Skills and education: `skills` for the must-have tools and languages; `schools`, `degrees` and `fieldsOfStudy` only when the role requires them.
- Place: a place the user names ("in the US"), else the role's location, as person location (`cities`, `states` or `countries`), never `companyHeadquarters`. A remote role uses `countries` only. Search covers 6 countries, so say so when the role is based elsewhere. Never narrow a place the user named to fit a candidate count: that count is the campaign's contact limit, which already caps what is sourced.
- Employer: an industry the user names goes in `industries`. LinkedIn industries have no AI or developer-tools industry, so for "AI startups" or "developer-tool companies" keep the closest industry (`software development`) and put the words in `keywords` (`"AI devtools"`). This is the one case for `keywords` here: they match the headline, summary and title, so they find people who sell or build that kind of product. "Startup" is a headcount (`companyHeadcount` `{"max": 200}`). Say once that the employer type is matched on profile words, not a company label.
- Exclude the hiring company (`excludeCompanies`), so the campaign never reaches its own staff. `pastCompanies` finds alumni of companies whose people fit.
- Never filter on age, gender, race, religion, disability, family status or nationality, or on a stand-in for one (a graduation year for age).

Validate and count as for any search. A candidate audience is smaller than a buyer one: a few hundred to 2,000 people for one role is normal.

## Errors

If a step errors, continue when possible and note it. On `plan_limit` or `billing`, surface `error.message` and `error.recovery.summary`; never retry blindly.
