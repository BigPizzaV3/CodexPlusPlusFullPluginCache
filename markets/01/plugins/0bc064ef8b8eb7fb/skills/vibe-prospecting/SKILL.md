---
name: vibe-prospecting
description: >-
  Find companies and contacts, build lead lists, enrich records with emails and
  phones, research firmographics and tech stacks, and surface buying intent or
  business events from Vibe Prospecting's B2B database (150M+ companies, 800M+
  professionals). Use for sales, GTM, and prospecting workflows — list building,
  account research, decision-maker search, contact enrichment, TAM/ICP sizing,
  lookalikes. Triggers on phrases like "find companies", "find
  prospects", "build a list", "who works at", "get emails", "enrich this
  company", "companies using Salesforce", "buying intent", or "export results".
---

# Vibe Prospecting

Connect this chat to live B2B company and contact intelligence — search, enrich, and export without leaving the conversation.

**Use only the Vibe Prospecting MCP tools in your tool list.** Follow each tool's live description and input schema — they are authoritative. Before the first real call for each distinct tool, read that schema and build arguments only from confirmed fields.

If tools are missing or return auth/401 errors: tell the user to connect/authorize **Vibe Prospecting** in their host’s plugin settings, then retry. Do not invent credentials or work around auth.

## Tools

| Tool | Use for |
|------|---------|
| `autocomplete` | Standardized filter values (required for controlled vocab) |
| `fetch-entities` | Search companies or people |
| `fetch-entities-statistics` | Aggregated breakdowns (only when filters fully match fetch) |
| `match-business` | Name/domain → `business_id` (max 50) |
| `match-prospects` | Email or name+company → `prospect_id` (max 40) |
| `enrich-business` | Firmographics, tech, funding, intent, etc. on a business table |
| `enrich-prospects` | Emails/phones (`enrich-prospects-contacts`) or profiles |
| `fetch-businesses-events` | Company event detail rows |
| `fetch-prospects-events` | People event detail rows |
| `show-sample` | Billable preview after exploration — required before you reply |
| `export-to-csv` | Credit-consuming full export (user must confirm first) |
| `get-dataset` | List or reload saved hub datasets |

Skip `match-*` if `fetch-entities` already returned IDs.

## Default workflow

1. Clarify only when required (see gates below).
2. `autocomplete` for every controlled-vocab filter you will use.
3. **One** comprehensive `fetch-entities` call (combine filters). Exception: linkedin→naics retry if results are too few or wrong type.
4. Optional `enrich-*` / `fetch-*-events` only when the user asked or answered a gate prompt with yes.
5. `show-sample` on each final `table_name` for this turn — then reply. Do not ask permission before `show-sample`.
6. Offer export only if there is more data than shown (or they asked for a file). Show cost → wait for explicit yes → `export-to-csv` on the **latest** `table_name`. **Never auto-export.**

## Hard rules

1. **`tool_reasoning`** — When the schema requires it, pass the user's request **verbatim** (≤2000 chars). Reuse that same string for the whole workflow. Do not invent a summary like "export".
2. **Chain with `session_id` + `table_name`.** Never invent either. Omit `session_id` on the first step; copy both from prior tool JSON afterward. After enrich/events, use the **new** `table_name` for every later step (especially export).
3. **`autocomplete` first** for: `linkedin_category`, `naics_category`, `company_tech_stack_tech`, `job_title`, `interests`, `skills`, `business_intent_topics`, `city_region` (USA cities). Use returned values only — never raw user wording.
4. **Never invent parameters.** Schema wins.
5. **One category type per fetch:** `linkedin_category` XOR `naics_category`. Prefer LinkedIn; fall back to NAICS only if LinkedIn is too broad / empty / wrong type.
6. **Location XOR:** `company_country_code` XOR `company_region_country_code` (same for prospect country/region).
7. **Quote `counts` correctly:** Tell the user `records_available` for delivered rows. `records_matching_filters` is headroom only — never claim you fetched all of it. Never do arithmetic on matching-filters for cost.

## Gates (ask before acting)

**Prospect location unclear** — If `entity_type: prospects` and location could mean person vs company HQ, ask which before fetching.

**Contact details** — Prospect fetch does **not** include email/phone values. `has_email` / `has_phone_number` only filter. If the user did not already ask for contacts, ask before fetching:

> Before I search, would you like to include contact details?
> - Emails only
> - Both emails and phone numbers
> - No thanks, prospects only

If they want emails/phones: after fetch, `enrich-prospects` with `enrich-prospects-contacts`, then `show-sample` the enriched table. Remember their choice for this session/dataset.

**Event details** — `filters.events` only selects matching companies/people; it does not add event columns. After presenting results, ask before `fetch-*-events` unless they already asked for event details.

**Export** — Explicit user confirmation after cost. Never export just because credits exist.

## `entity_type`

- Any people/roles/titles/contacts request → `prospects`
- Companies only, no people → `businesses`

Buying intent / "selling to" / "looking for customers" → use `business_intent_topics` (autocomplete required).

## Autocomplete vs direct

**Autocomplete required:** `linkedin_category`, `naics_category`, `company_tech_stack_tech`, `job_title`, `interests`, `skills`, `business_intent_topics`, `city_region` (USA).

**Use directly:** ISO `company_country_code` / `prospect_country_code` (Alpha-2), region codes (ISO 3166-2), fixed buckets (`company_size`, `company_revenue`, `company_age`, `job_level`, `job_department`), `website_keywords`, event type enums.

**Jobs:** Broad seniority/dept → `job_level` + `job_department` only. Specific title → `job_title` only (autocomplete). For executives, pair title search with `job_level` (often `c-suite`).

**Category strategy:** Autocomplete LinkedIn first. Include all applicable specific categories. If the best LinkedIn label is a parent industry that would pull in lots of wrong companies, switch to NAICS — never send both.

## Chaining patterns

- **People at prior companies:** `fetch-entities` with `entity_type: prospects`, same `session_id`, and `businesses_reference_table` = prior business table (prefer enriched table if you enriched).
- **Company details from a prospect table:** `enrich-business`, not another business fetch.
- **"More" / "another" results:** pass `exclude_key` `"business"` or `"prospects"` (or a prior `dataset_id` starting with `ds-`).
- **Saved lists:** `get-dataset` → use returned `session_id` + `table_name`. Upload lists in the hub: https://app.vibeprospecting.ai/lists

## `show-sample`

Required after each turn's fetch/enrich/events work, once per final `table_name`.

- `preview_table_columns`: 3–6 keys from that table's `preview.preview_data` — do not invent/rename keys; skip mostly-empty and id columns.
- `client_platform`: use `openai_chatgpt` for ChatGPT or `openai_codex` for Codex, as supported by the live tool schema.
- Render the returned final sample as a table in your reply; do not assume a widget or interactive UI displays it. Preserve returned row identities and associated company/contact fields. Use the final sample, not the masked exploration preview.
- Use the cost fields returned by `show-sample` for export confirmation. This OpenAI endpoint does not expose a separate cost-estimation tool.

## Enrich

- Max 3 enrichment types per call. Read schema for exact enum strings (`enrich-business-firmographics`, `enrich-prospects-contacts`, …).
- `financial-metrics` needs `parameters.date`. `website-keywords` needs `parameters.keywords`.
- Enrichment does not find people — use `fetch-entities` prospects (optionally with `businesses_reference_table`).

## Events

- Need `session_id`, `table_name`, `event_types` (and schema fields like `timestamp_from`).
- Sample/preview may show only a few events per entity; say so — full export has far more.
- Batching is capped server-side (~20 IDs).

## Filters

```json
{ "values": ["v1", "v2"], "negate": false }
{ "gte": 6, "lte": 24 }
true
```

`business_intent_topics` uses `{ "topics": ["Category:Topic"], "negate": false }` — topics from autocomplete only.

Business location filters match **HQ only**.

`max_per_company`: set only if the user gives a number.

Ambiguous industry/role words ("designers", "security", …): offer concrete subcategory options **and** "all relevant" — do not auto-pick the broadest term.

## Export & credits

- Export the latest enriched/events table when applicable.
- Insufficient credits: explain the server response and use only billing or upgrade instructions returned by the server. Do not call unavailable pricing tools.
- Export timeout: retry the **same** `export-to-csv` after a short wait — do not rebuild with `fetch-entities`.
- Partial export after top-up: same `session_id`/`table_name`, `exclude_key` = partial `dataset_id`, `limit` = remaining rows only.

## Support

https://www.vibeprospecting.ai/contact-us
