# Companies, teaming and socioeconomic status

Resolve identity before you combine evidence. Preserve the legal name, doing-business-as name, UEI and corporate family distinctions. A company is the user's only when calibration returned it or the user named it as theirs. A corporate family is not one award recipient. A shared NAICS code, a similar name or a graph neighbor does not prove a teaming relationship. State what supports a suggested partner and what remains unknown.

The people directory is not available yet. Use the people and contact details named in returned source documents. Cite the source. Do not infer private contact details.

### `g2x_search_companies`

Search the company directory by name or 12-character SAM UEI. Each UEI stays a separate row so you can choose the intended entity.

- Inputs: `query` (required, company name or UEI; a five-character CAGE code is not a search term here, and the tool says so when the query looks like one); `limit` (1 to 8, default 5); `cursor` (continuation from the previous company search).
- Output: matching companies with UEI, location, award history and a link to the G2X profile. When several legal entities fit, keep them distinct and ask which one the user means when it matters.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"query": "Leidos"}`

### `g2x_rank_companies`

Rank companies by federal contract awards, by obligated dollars or by award count. Use it to find the biggest performers in a market. Use the company search to find one company by name.

- Inputs: at least one of `naics` (6-digit codes), `psc` (4-character codes), `agencies` (code or exact name) or `fiscal_years` is required; `min_award_value`, `min_obligated`, `min_award_count` (floors); `sort` (`obligated` by default, or `award_count`); `limit` (1 to 50, default 25); `cursor` (next page of the same search).
- Output: ranked company rows with the total and a cursor for the next page.
- Plan: all plans, when the connection offers it. Each search counts toward the account's daily GovCon Directory searches (free accounts get 10 a day). Read only. On the research endpoint: no.
- Example: `{"naics": ["541519"], "fiscal_years": [2024, 2025], "sort": "obligated", "limit": 10}`

### `g2x_get_graph_neighborhood`

Return one company's one-hop public contracting relationships: awards it won and companies it subcontracted with. It never returns multi-hop paths or account-private relationships.

- Inputs: `uei` (required, the company's 12-character SAM UEI); `limit_per_relation` (1 to 5, default 4).
- Output: linked public records, each with how it is related and a G2X link. The answer says when relationships were left out; never report a partial answer as the full neighborhood.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"uei": "<12-character UEI from company search>"}`

### `g2x_company_contract_history`

Return one company's federal contracting portfolio by UEI.

- Inputs: `uei` (required); `fiscal_year_start`, `fiscal_year_end`; `naics_code`; `set_aside`; `expiring_within_days` (1 to 1825; also return the awards ending inside this many days); `limit` (1 to 50, default 25).
- Output: prime award counts, IDV awards the company holds, associated contract vehicles and, when asked, the awards ending soonest.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"uei": "<12-character UEI>", "expiring_within_days": 180}`

### `g2x_teaming_partners`

Find potential teaming partners in one NAICS code, ranked by awards.

- Inputs: `naics_code` (required, the opportunity's 6-digit NAICS code, as text or number); `excluded_ueis` (up to 10 UEIs to leave out, such as your own company or direct competitors); `min_past_performance` (minimum awards in this NAICS, default 3); `fiscal_year_start`, `fiscal_year_end` (default window: the current fiscal year and two before it); `limit` (1 to 25, default 10); `cursor` (next page; keep the same NAICS, fiscal years and exclusions).
- Output: partner rows with obligated dollars and certification check results, plus a cursor for more partners.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"naics_code": "541611", "excluded_ueis": ["<your company UEI from calibration>"]}`

### `g2x_socioeconomic_status`

Return one company's SAM socioeconomic certifications by UEI, such as 8(a), SDVOSB, HUBZone and WOSB, plus its registration purpose. Do not invent certifications from a company name or website.

- Inputs: `uei` (required).
- Output: one answer with the company's certifications and registration purpose.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"uei": "<12-character UEI>"}`

### `g2x_company_evidence`

Assemble cited proof for a due diligence question from procurement records and opportunity documents.

- Inputs: `query` (required, the claim to find evidence for); `limit` (passages per section, 1 to 15, default 8).
- Output: cited passages. Every passage keeps the record it came from, and coverage that could not be checked is said plainly. Keep those citations in anything you draft from it.
- Plan: all plans, when the connection offers it. Read only. On the research endpoint: yes.
- Example: `{"query": "companies with past performance running cloud migrations for VA"}`

### `g2x_company_signals`

Find recent public web and news signals about a company. Signals are context, not confirmed facts. Check any award or contract claim against the G2X record, and cite the original source and its date.

- Inputs: `company` (required, company or organization name); `topics` (up to 3 angles, such as teaming or acquisition); `limit` (1 to 8, default 5).
- Output: signal rows with a link to each source. Distinguish company statements from independent reporting.
- Plan: Starter and up. Each call spends one metered external lookup from the account allowance. It changes nothing in the account, but it is not on the research endpoint because it spends.
- Example: `{"company": "Leidos", "topics": ["teaming"]}`

### `g2x_company_web_profile`

Read a company's own public page and its most recent public posts. Posts are the company's own statements, not confirmed facts.

- Inputs: `company` (required); `domain` (the company's website domain, the surest way to find its page); `username` (the page username, if known); `posts` (recent posts to include, 1 to 5, default 3).
- Output: one answer with page facts and recent posts, each linked. Distinguish current employment from historical employment, and inference from fact.
- Plan: Starter and up. Each call spends one metered external lookup from the account allowance. It changes nothing in the account, but it is not on the research endpoint because it spends.
- Example: `{"company": "Leidos", "domain": "leidos.com"}`
