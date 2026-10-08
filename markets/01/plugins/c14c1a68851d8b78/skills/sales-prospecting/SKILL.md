---
name: sales-prospecting
description: Build qualified prospect lists with DataForB2B. Define an ICP, find matching companies and decision makers, layer buying signals (funding, hiring, growth, intent posts), and enrich work emails for outreach. Use when the user says "find prospects", "build a lead list", "find companies that...", "who should I sell to", "decision makers at...", "companies that just raised", "lead gen", or describes a product and asks who to target.
---

# Sales Prospecting with DataForB2B

You are helping a seller build a pipeline. DataForB2B gives you structured search over companies and professional profiles, live job postings (hiring signals), and social posts (intent signals). Your job is to turn a product pitch into an ICP, the ICP into precise filters tested against real samples, and the filters into a signal-prioritized list of decision makers with verified contact info.

Tools used: `search_company`, `search_people` (core), `typeahead`, `enrich_profiles`, `enrich_company`, `search_jobs`, `search_posts`.

## Workflow

### 1. Define the ICP (before any search)

DEFAULT TO ASKING. A one-line brief ("find me leads for my SaaS") is never fully specified: ask up to 4 short questions, each with 2-4 concrete suggestions drawn from your domain knowledge, and only skip the ones the brief already answers. The goal is to land on filterable values: `current_company_category` values and `current_company_keyword` phrase variants for the companies, a title OR-group for the person.

1. **What does the user SELL, concretely?** Capability, channel, use case, and who feels the pain ("an email verification API" is not enough: sold to cold-email senders? to signup-form owners fighting fake accounts?). This decides WHO buys and WHY, i.e. the persona titles and the buying signals worth layering.
2. **The target companies' domain, concretely: what do they DO?** This is what becomes the filters, so push past the label. "Fintech" can mean payment processors, neobanks, credit/lending, accounting SaaS, or crypto: each maps to different category values and different keyword phrases. Offer concrete sub-domain choices in the question.
3. **Value-chain position, the number one source of off-target lists.** Companies that BUILD/SELL that product, agencies/integrators that DEPLOY it for clients, or companies that USE it internally? Builders get product categories and term variants plus agency exclusions (`not_in`); deployers get the agency/consulting categories; users get the buyer-side industries.
4. **Firmographics and persona**: size range, geography, funding stage if relevant, which titles sign and which champion.

Then translate the answers, not the original label, into filters: the domain answer goes through `typeahead` type=category (use every niche category that matches) OR-ed with 3 to 6 `current_company_keyword` `=` phrase variants built from how those companies describe themselves. Example: the user sells an email verification API to cold-email senders → `{"op":"or","conditions":[{"column":"current_company_category","type":"=","value":"lead generation"},{"column":"current_company_category","type":"=","value":"sales automation"},{"column":"current_company_keyword","type":"=","value":"cold email"},{"column":"current_company_keyword","type":"=","value":"email outreach"},{"column":"current_company_keyword","type":"=","value":"email deliverability"}]}` AND-ed with size/geo and the persona titles.

Explicit answers are **hard constraints**. When results are thin, widen how the target is EXPRESSED (more term variants, more categories, more title spellings), never by silently relaxing size, geography, or the persona. If the honest pool is 60 companies, deliver 60 and say so. Ask once: if the user already answered, use the answers, and treat a skipped question as no preference.

### 2. Resolve uncertain values with `typeahead`

Filter values must match what is stored. Resolve any value you are not sure of BEFORE committing to it (each returned suggestion costs a small amount of credits, empty results are free):

| Column | typeahead `type` |
|---|---|
| company `name` / people `current_company` | `company` (also returns the `org_xxx` id) |
| company `category` / people `current_company_category` | `category` |
| company `industry` | `company_industry` |
| people `current_company_industry` | `company_industry` |
| `city` / `region` / people `profile_location` | `city` / `region` / `location` |
| `investor` / `current_company_investor` | `investor` |
| `current_title` | `title` |

If typeahead returns 0 matches, don't re-resolve the same way: switch type (category vs industry), try a shorter term, or use the term directly in a `like`/`=` filter. Never loop resolving the same value.

### 3. Test 2 or 3 approaches, keep the best

Design 2 or 3 distinct filter sets that qualify the target differently, for example: (A) category (plus industry), (B) description/keyword TERM VARIANTS OR-ed together, (C) a stricter or looser variant (different categories, add or drop a size/funding condition). Run each with `count` 10, compare `total` and READ the sample records ("are these actually what the user wants?"), then scale the winner. One page of 10 results tells you more than any amount of filter theorizing.

**One-step vs company-first, for people targets:** search people directly whenever the ICP describes the companies by their attributes; everything maps to `current_company_*` columns: category, industry, size, funding stage, has_funding, investor, and `current_company_keyword` for what the company DOES when no category fits ("payment orchestration"). One call, no ids to copy. Company-first (`search_company` → `org_xxx` ids → `search_people` with `current_company_id in [ids]`) is for when the user hands you a LIST of specific companies (domains, names, page URLs) and wants their decision makers: resolve the whole list in one `search_company` call (`domain in ["stripe.com","adyen.com",...]`; names via typeahead type=company). The other residual cases are company-only signal columns (live job postings via `job_title`, growth, `last_funding_date`) and hand-vetting the account list before outreach.

Volume calibration: aim for at least ~100 matches before ranking. Under ~100, add term variants and OR more category/industry values (never drop a hard constraint). `total` is capped at 10,000; capped means too broad, tighten.

### 4. Layer buying signals

A list ranked by signal converts far better than a flat ICP dump:

- **Fresh funding**: `last_funding_date >= "YYYY-MM-DD"` and/or `funding_stage_normalized in [...]`. Budget just landed.
- **Hiring**: on `search_company`, `job_title` / `job_location` filter companies by their LIVE job postings (`job_title like "SDR"` finds companies hiring SDRs right now, a strong signal for anyone selling sales tooling). "Is hiring" exists nowhere as a stored people column; it always goes through the company side. For digging into the postings themselves, `search_jobs` (keyword, location, freshness, `company_ids` to check one account).
- **Headcount growth**: `employee_growth_6m > 10` (percent). Growing companies buy; shrinking ones churn.
- **Intent posts**: `search_posts` with a pain-point or competitor keyword (platform "linkedin", "twitter" or "reddit", `date_posted "past_month"`), with `include: ["comments","reactions"]`. The author is in-market and every engager is a warm lead with profile attached. A single interesting post URL can be expanded via `post_url` + `include`.

Use signals as filters when the user asked for them, as ranking keys otherwise (a plain ICP request gets exactly the filters asked, nothing extra).

### 5. Enrich (only on request) and deliver

Enrichment bills extra credits, so it is opt-in: run it only when the user asked for emails/contact info, or after proposing it and getting a yes. Otherwise deliver the list without contacts and offer enrichment as the next step.

When approved, `enrich_profiles` in bulk (up to 100 per call, concurrent server-side) with `enrich_work_email` true: sales outreach uses the work email. Failed profiles return an `error` and cost nothing. Enrich the qualified list, not the raw dump. `enrich_company` fills full account data (funding history, offices, growth, `signals.actively_hiring`) for accounts going into sequences or CRM.

Show the user, in this order:

1. **Search recap** (1-2 sentences): the ICP as you interpreted it (including the BUILD/DEPLOY/USE choice), the filters in plain words, and the pool size. Example: "1,008 founders/CEOs of seed to Series A fintechs in the US and UK. Here are the top 15, ranked by funding recency." No raw filter JSON in the answer (share it only if the user asks).
2. **The prospect table**, up to 25 rows, sorted hot (signal < 30 days) before warm before cold:

| Company | Size | Signal | Contact | Title | Work email | Why now |
|---|---|---|---|---|---|---|
| [Acme Pay](company website) | 51-200 | Series A, 2026-06-12 | [Jane Smith](linkedin profile url) | CEO | jane@acmepay.com | Raised 6 weeks ago and hiring 3 SDRs, building the sales team your tool equips |

These two links are ALWAYS present: Company links to the company's website (fall back to its company page URL if no website is known), Contact links to the person's LinkedIn profile URL. Signal names the trigger with its date (funding round, live job postings, growth %), Work email shows the enriched address or "not enriched yet", "Why now" ties the signal to the user's product in one short line, not generic praise.

3. **Next steps** (one line): what you can do from here, e.g. show more of the pool, enrich the remaining contacts, layer another signal, or draft the outreach.

Above 25 rows, write a CSV with the same columns (company website and LinkedIn profile URL as their own columns), and keep only the top 10 in the chat table.

## Column reference

Use the EXACT value formats shown. Only these columns exist. If the user asks for a criterion with no column, do not invent one or proxy it; say plainly it is not filterable and run the rest.

### `search_company`

- **Basic**: `name`, `tagline`, `description`, `domain`, `universal_name`; `keyword` (full-text across name/tagline/description)
- `industry`: broad lowercase taxonomy ("software development", "financial services", "advertising services"). Niche terms (fintech, saas, AI) are NOT industries
- `category`: lowercase, holds BROAD values (software, consulting, e-commerce) AND NICHE ones (saas ~34k companies, fintech ~25k, artificial intelligence ~29k, marketplace, edtech). The precision lever for niche targeting; resolve with typeahead type=category first, and only fall back to a broad industry if no niche category matches
- **Size**: `employee_count`, integer with comparison operators, or range strings "1-10","11-50","51-200","201-500","501-1000","1001-5000","5001-10000","10001+" with `=`/`in`
- **Headquarters**: `country_iso_code` (ISO-2 UPPERCASE: US, FR, GB not UK; no "Europe" value, use `in` with the country list), `city`, `region`
- **Offices**: `office_country`, `office_city`, `office_region` (any office, not just HQ)
- **Growth**: `employee_growth_1m` / `_6m` / `_12m` (percent, numeric operators), `recent_hires_count`
- **Metadata**: `founded_year`; `company_type` UPPERCASE snake_case ("PRIVATELY_HELD","PUBLIC_COMPANY","NON_PROFIT","PARTNERSHIP","SELF_OWNED","EDUCATIONAL","SELF_EMPLOYED","GOVERNMENT_AGENCY"); `follower_count`; `page_verified` (true/false)
- **Funding**: `has_funding` (true/false, use for "funded"); `funding_stage_normalized` snake_case (seed_round, series_a ... series_h, series_unknown, pre_seed_round, angel_round, grant, private_equity_round, debt_financing, convertible_note, corporate_round, equity_crowdfunding, post_ipo_equity, post_ipo_debt, undisclosed); `last_funding_amount_usd`; `last_funding_date` ("YYYY-MM-DD")
- `investor`: backer/accelerator/fund. THE column for "YC companies", "a16z portfolio". Expand abbreviations (YC becomes "Y Combinator", a16z becomes "Andreessen Horowitz") and resolve with typeahead type=investor. Keyword/description matching misses most of them: a company's description rarely names its investors (keyword "Y Combinator" finds ~30 companies, investor = "y combinator" finds ~2800)
- **Live job postings**: `job_title`, `job_location`. Filter companies by what they are hiring for RIGHT NOW

### `search_people` (the columns that qualify the ACCOUNT on a person row)

`current_company_category` and `current_company_industry` (note: Capitalized broad taxonomy here, "Computer Software"), `current_company_size` (ranges "2-10" ... "10001+"), `current_company_id` (org_xxx), `current_company_has_funding`, `current_company_funding_stage` (snake_case, legacy forms without _round also exist: use `in` with BOTH, e.g. `["seed_round","seed"]`), `current_company_investor`, and `current_company_keyword`: full-text on the EMPLOYER's name/tagline/description (`=` exact phrase, `like` all-words; OR several `=` phrase variants for recall). It is resolved server-side to the matching companies (capped at the 10,000 best matches), so it replaces the whole search_company + copy-the-org-ids flow in one call.

Person-side: `current_title`, `profile_country` (ISO-2), `profile_location` / `current_job_location` (free text; OR the two for city-level recall), `keyword` (the person's HEADLINE), `years_of_experience`, `years_in_current_position`, `has_email`, plus past_* mirrors of the company columns. `profile_industry` is the person's self-declared label: sector targeting goes through `current_company_category` / `current_company_industry` instead.

**`keyword` on people searches the person's headline.** It qualifies the PERSON ("plaid integration", "RevOps"), never the company: "marketing automation" in a people keyword returns marketers, not people AT marketing-automation companies. Company traits go on the current_company_* columns or through the account-based flow.

## Operator craft

A condition is `{"column": ..., "type": <operator>, "value": ..., "value2": <only for between>}`. Groups are `{"op": "and"|"or", "conditions": [...]}` and can be nested.

- **`like` matches ALL the words ANYWHERE** in the field (any order, not adjacent). Fine for single distinctive words ("SDR"); noisy for multi-word terms made of common words: keyword like "AI sales agent" matches ANY company whose description contains "AI", "sales" and "agent" scattered across sentences (roughly 14x more matches, mostly off-target).
- **`=` on text columns is an EXACT PHRASE** (words adjacent, in order). Prefer it for multi-word terms, OR-ing several `=` phrase variants to keep recall: "AI sales agent" becomes an `or` group of "AI SDR" / "AI sales agent" / "autonomous SDR" / "AI outreach automation" / "AI prospecting". More precise variants = more recall WITHOUT losing precision.
- **`regex` adds word boundaries**, REQUIRED for short title acronyms (3 letters or fewer: CEO, CTO, COO, CFO, CMO, CRO, VP, PM, SDR, AE...): `like` substring-matches unrelated words (COO matches "Coordinator", VP matches "VPS"). The `value` stays RAW TEXT: `{"type":"regex","value":"CEO"}`, never `\bCEO\b` or `^CEO$` (the backend adds boundaries itself; injected syntax breaks the query and returns 0). Regex still matches the acronym ANYWHERE in the title ("CEO" also matches a "Data Analyst, CEO's Office"), and some acronyms are ambiguous (CRO is also conversion rate optimization): the sample-check catches these, refine with `not_like` exclusions.
- **`in` / `not_in` take a JSON ARRAY** (`["FR","DE"]`), never a comma-separated string. Each element matches like `like`, NOT as a phrase: a list of multi-word phrases needs an `or` group of `=` conditions.
- **Same-column alternatives go in ONE `or` group**, AND-ed with the rest. AND-ing two categories or two titles returns nothing.
- Numeric columns take `>`, `>=`, `<`, `<=`, `between` (value + value2). Booleans take `=` true/false.

**Categories are self-tagged**, so a category broader than the qualified ICP catches companies that merely touch the theme (a GovTech bidding platform self-tags "sales automation"). When the ICP is a specific product subtype, a generic category must not qualify a company alone: AND it with description evidence (`category = "sales automation"` AND `description = "AI SDR"` variants), or use only categories as specific as the ICP itself. A category-only filter is fine when the ICP is genuinely that broad ("sales tech companies").

Defaults: keep `enrich_live` false (cached, 0.75 credits/result, fast). Live enrichment (1.5 credits) is opt-in when freshness genuinely matters.

## Recipes

**Decision makers at funded fintechs (one-step):**
```json
{"op":"and","conditions":[
  {"op":"or","conditions":[
    {"column":"current_title","type":"regex","value":"CEO"},
    {"column":"current_title","type":"like","value":"Founder"},
    {"column":"current_title","type":"like","value":"Co-Founder"}
  ]},
  {"column":"current_company_category","type":"=","value":"fintech"},
  {"column":"current_company_funding_stage","type":"in","value":["seed_round","series_a","seed"]},
  {"column":"profile_country","type":"in","value":["US","GB"]}
]}
```

**Niche company qualification without a category (`current_company_keyword`):** when no category fits what the target companies DO, put the phrase variants directly in the people search, e.g. `{"op":"or","conditions":[{"column":"current_company_keyword","type":"=","value":"payment orchestration"},{"column":"current_company_keyword","type":"=","value":"payment routing"}]}` AND-ed with titles and geography. One call, no company search, no ids to copy.

**Decision makers at a user-given company list (the main company-first case):** one `search_company` call resolves the whole list to ids: `{"column":"domain","type":"in","value":["stripe.com","adyen.com","checkout.com"]}` (for names, resolve each with typeahead type=company). Then `search_people` with `current_company_id in [org_xxx ids]` + the persona title OR-group, and enrich work emails in bulk.

**Company-first on signal columns (or hand-vetted accounts):** `search_company` with the signal columns (`job_title`, `last_funding_date`, growth) plus firmographics, vet the accounts, then `search_people` with `current_company_id in [org_xxx ids]` + persona titles. Put EVERY company-level criterion in the `search_company` call itself, keep only person-level filters on the people side: a loose company search wastes the id list on companies you would discard anyway.

**Companies that raised recently:** `search_company` with `last_funding_date >= <6 months ago>`, `funding_stage_normalized in ["series_a","series_b"]`, `country_iso_code in [...]`, `employee_count between`. Then decision makers at the chosen ids.

**Hiring-signal prospecting (selling dev tooling):** `search_company` with `job_title like "platform engineer"` plus ICP firmographics: only companies with live postings for that role match. The job spend is the budget proof.

**Intent-based warm leads:** `search_posts` keyword "<pain point or competitor>", `date_posted "past_month"`, `include ["comments","reactions"]`. Qualify authors and engagers against the ICP (title, company), then `enrich_profiles` the matches.

**Lookalike expansion:** `enrich_company` on the user's 2 or 3 best customers, read their category/size/geo/funding profile, then `search_company` mirroring those attributes, excluding existing customers by id (`not_in`).

**Consumer app / B2C targeting (a known trap):** the app categories ("mobile apps", "consumer apps") are heavily polluted by dev AGENCIES and missing on many real consumer apps. Build both parts: (a) EXCLUDE agencies: never use a category containing "development"/"consulting"/"design" as a positive filter, and add `category not_in ["mobile app development","app development","web development","it consulting","consulting","web design","digital marketing","advertising","staffing", ...]`; (b) ADD RECALL: OR the niche consumer industries (`industry in ["social networking platforms","internet marketplace platforms","computer games"]`) and OR `description = "App Store"` / `"Google Play"` / `"download the app"` (one `=` phrase condition each): a company distributing on the app stores is consumer-facing by definition.

## Guardrails

- Apply exactly the filters the user asked for; suggest extra signals as options rather than silently adding them.
- Work emails go through verification during enrichment; still honor opt-outs and applicable law (GDPR, CAN-SPAM) in any outreach drafted afterward.
- State data freshness honestly: cached data can lag reality; say when results are cached vs live-enriched.

## Common mistakes

1. Skipping the BUILD/DEPLOY/USE question and delivering agencies when the user sells to product companies.
2. AND-ing two titles or two categories (returns nothing): same-column alternatives go in one `or` group.
3. Putting a company trait in the people `keyword`: use `current_company_category` or the company-first flow.
4. Going company-first when `current_company_*` columns already express the ICP (including `current_company_keyword` for description terms): copying ids is slow and bounds the pool; company-first is for company-only signal columns (live job postings, growth, funding dates) or hand-vetted account lists.
5. `like` with multi-word common-word terms: use OR-ed `=` phrase variants.
6. `like` with short acronyms (VP matches "VPS"): use `regex`, raw value only, no `\b` or `^`.
7. Passing `in` a comma-separated string instead of a JSON array.
8. Searching investors in keyword/description instead of the `investor` column.
9. Trusting a broad self-tagged category alone for a specific ICP instead of AND-ing description evidence.
10. Relaxing hard ICP constraints to hit a volume target instead of widening term variants.
11. Scaling without reading a 10-result sample, enriching the raw dump instead of the qualified list, or enriching at all without the user asking or approving it.
