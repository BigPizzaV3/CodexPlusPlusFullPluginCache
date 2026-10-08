# Source registry — US federal

Verification labels below are original author notes, not results of the Codex compatibility
review. Recheck every endpoint and claim at run time. HTTP status alone does not verify
content. Runtime behavior is governed by `runtime-safety.md`.


Every URL here was fetched and confirmed live on **2026-09-09**. If a source fails at scan time,
report it as a named coverage gap; do not substitute recall. Re-verify anything that looks stale.

Tiers: `primary` = official publisher of the instrument · `regulator` = the regulator's own site ·
`secondary` = anything else (leads only, never findings).

---

## 1. Federal Register API — `primary`, the workhorse

**No API key required.** This provides searchable renditions of the daily publication for federal rules, proposed
rules, notices, and presidential documents. Prefer it over every agency website: it is structured,
date-filterable, gives stable identifiers, and carries the comment deadline.

FederalRegister.gov HTML is an informational rendition, not the official legal edition.
For reliance on an official edition, follow the document's govinfo.gov PDF link and
cross-check relevant provisions when accessible; disclose if that comparison was not done.

Base: `https://www.federalregister.gov/api/v1/documents.json`

### Parameters

| Parameter | Notes |
|---|---|
| `conditions[publication_date][gte]` | `YYYY-MM-DD`. **This is the delta boundary** — set to the profile's `last_scan_date`. |
| `conditions[publication_date][lte]` | Optional window end. |
| `conditions[type][]` | Repeatable. `RULE` (final), `PRORULE` (proposed), `NOTICE`, `PRESDOCU`. |
| `conditions[agencies][]` | Repeatable. Agency **slug** — see the table below. |
| `conditions[term]` | Full-text search. Use for `watch_keywords`. |
| `fields[]` | Repeatable. Always request: `document_number`, `title`, `publication_date`, `type`, `agencies`, `html_url`, `comments_close_on`, `effective_on`, `abstract`. |
| `per_page` | Max 1000. |
| `order` | `newest`, `oldest`, `relevance`. |

Response envelope: `count`, `total_pages`, `results[]`. Check `count` before paging — a broad query
over a long window returns thousands.

### Verified example

Proposed rules from the Labor Department since 2026-06-01:

```
https://www.federalregister.gov/api/v1/documents.json?conditions[agencies][]=labor-department&conditions[type][]=PRORULE&conditions[publication_date][gte]=2026-06-01&per_page=20&fields[]=title&fields[]=document_number&fields[]=publication_date&fields[]=comments_close_on&fields[]=effective_on&fields[]=html_url
```

Confirmed 2026-09-09: `count: 22`, first result document `2026-15717`.

### Provenance mapping

- `official_id` ← `document_number` (e.g. `2026-15717`)
- `source_url` ← `html_url` — already a deep link to the document. **Never cite the API query URL as
  the source**; cite `html_url`.
- `publisher` ← `"Federal Register"`, plus the agency name from `agencies[].name`
- Comment deadline ← `comments_close_on`; effective date ← `effective_on`
- `supporting_quote` ← fetch `html_url` and quote the document. The API's `abstract` is an editorial
  summary, **not** the instrument's own words — acceptable for triage, not as a `supporting_quote`
  for a date, threshold, or penalty.

### Traps

- **`effective_on` is `null` on proposed rules.** Verified: document `2026-15717` (PRORULE) returns
  `effective_on: null` with `comments_close_on: 2026-09-30`. Report the timeline as measured to the
  comment deadline and the effective date as `undated`. Never estimate one.
- **`significant` is unreliably populated** — verified `null` on a 2026 notice. Do not use it to
  filter or to justify an impact score.
- A `Notice` can carry real obligations (information collection, enforcement policy). Don't assume
  notices are low impact.

### Agency slugs (verified from `/api/v1/agencies`, 2026-09-09)

| Slug | Agency | Domain |
|---|---|---|
| `labor-department` | Labor Department | employment |
| `occupational-safety-and-health-administration` | OSHA | employment |
| `equal-employment-opportunity-commission` | EEOC | employment |
| `national-labor-relations-board` | NLRB | employment |
| `labor-management-standards-office` | Labor-Management Standards | employment |
| `federal-trade-commission` | FTC | consumer protection, privacy, AI |
| `consumer-financial-protection-bureau` | CFPB | consumer protection |
| `securities-and-exchange-commission` | SEC | ESG disclosure, governance |
| `industry-and-security-bureau` | BIS | export controls |
| `foreign-assets-control-office` | OFAC | sanctions |
| `u-s-customs-and-border-protection` | CBP | trade, forced-labour import bans |
| `environmental-protection-agency` | EPA | ESG, environmental |
| `health-and-human-services-department` | HHS | privacy (HIPAA) |
| `homeland-security-department` | DHS | employment eligibility, cyber |

Full list: `https://www.federalregister.gov/api/v1/agencies` (verified 200). Resolve a slug from
this endpoint rather than guessing — a wrong slug silently returns zero results, which reads exactly
like "nothing new," and that is a dangerous false negative.

---

## 2. eCFR API — `primary`, for codified text

**No key required. Use the API, not the website.**

- Title list: `https://www.ecfr.gov/api/versioner/v1/titles.json` (verified 200)
  Returns `meta` + `titles[]`, each with `number`, `name`, `latest_amended_on`, `latest_issue_date`,
  `up_to_date_as_of`.
- Title structure: `https://www.ecfr.gov/api/versioner/v1/structure/<YYYY-MM-DD>/title-<n>.json`
  Verified 2026-09-09 — confirms a part exists and returns its official label. Examples confirmed
  this way: title 45 part 164 "Security and Privacy", title 16 part 312 "Children's Online Privacy
  Protection Rule (Coppa Rule)", title 15 part 774 "The Commerce Control List", title 31 part 501
  "Reporting, Procedures and Penalties Regulations", title 29 part 1910 "Occupational Safety and
  Health Standards".
- Point-in-time full text is available under the same `versioner/v1` namespace.

### Two verification traps, both confirmed by control test on 2026-09-09

**The human-facing eCFR site is bot-gated and returns HTTP 200 for parts that do not exist.**
`https://www.ecfr.gov/current/title-99/part-9999` returned 200 with a "Request Access" interstitial —
identical to what real part URLs returned. **A 200 from `ecfr.gov/current/...` proves nothing.**
Verify part existence through the structure API above, where a fake part is correctly absent.

**`uscode.house.gov` is not usable programmatically.** It returned "Document not Found" for real
sections as well as fake ones. Do not cite it as a source you have verified. For US statutory text,
either cite the Federal Register document that amended it or state that you could not reach the
statute and log a coverage gap.

`up_to_date_as_of` matters: eCFR lags the Federal Register, so a very recent final rule may be in the
FR but not yet in eCFR. Cite the Federal Register for new changes and eCFR for the standing text, and
say which you are citing.

## 3. Regulations.gov v4 — `primary`, optional

`https://api.regulations.gov/v4/documents` — verified **403 without a key**. Requires a free
api.data.gov key. Treat as optional: use only if the user supplies a key, otherwise fall back to the
Federal Register, which covers the same rulemakings. Adds docket history and public comments.

## 4. Agency sources — `regulator`

Use for guidance, enforcement policy, and press announcements that never reach the Federal Register.
All verified 200 on 2026-09-09.

| Source | URL | Notes |
|---|---|---|
| FTC press releases | `https://www.ftc.gov/feeds/press-release.xml` | RSS. Enforcement and policy. |
| OFAC recent actions | `https://ofac.treasury.gov/recent-actions` | Sanctions designations, often effective immediately. |
| BIS Federal Register notices | `https://www.bis.doc.gov/index.php/federal-register-notices` | Export control rules. |
| SEC rulemaking activity | `https://www.sec.gov/rules-regulations/rulemaking-activity` | **Requires a descriptive User-Agent with contact details** — SEC returns 403 to generic agents. Verified 200 with a declared UA. |
| CFPB newsroom | `https://www.consumerfinance.gov/about-us/newsroom/` | |
| OSHA news releases | `https://www.osha.gov/news/newsreleases` | **Unreliable — User-Agent-gated.** Returned 200 to a browser-style UA and 403 to a declared tool UA in the same session on 2026-09-09. Treat a failure as a coverage gap, and prefer the `occupational-safety-and-health-administration` Federal Register slug, which is stable. |

Note the opposite UA requirements: SEC rejects generic agents and needs a declared one; OSHA did the
reverse. Neither is a reason to guess at content when a fetch fails — log the gap.

**Not included, deliberately:** `dol.gov/newsroom/releases` (403, bot-blocked) and
`eeoc.gov/newsroom/rss.xml` (404). Reach both agencies through the Federal Register API slugs above
instead — primary, structured, and filterable. Do not write these two URLs back in without
re-verifying them.

---

## 5. Optional US state research

This registry covers federal sources only. When `coverage.us_states` is nonempty, also
follow `sources-us-states.md` for those states. Otherwise disclose that state law was not
searched. Never infer state coverage from a federal result.
