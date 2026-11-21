---
name: enrich-contacts
description: "Research company data, custom buying signals and business contact details in Compelling lists; find decision-makers when needed. Use for technologies, certifications, hiring activity, work emails or LinkedIn profiles, for companies in the user’s chosen markets (Firmenrecherche, Ansprechpartner, Datenanreicherung). Reading saved values alone does not require new research."
---

# Research companies and contacts in Compelling

The single most important rule: **contact discovery and enrichment are separate steps.**
`compelling_find_contacts` returns only name + job title. Emails, phone numbers, LinkedIn
URLs, and every other data point are **insights** — columns you define once and then research.

## Workflow

1. **Confirm the workspace** (`compelling_get_workspace`) and locate the list (`compelling_list_lists`).
2. **Choose the requested work.** For company-only research, skip contact discovery and work
   with `record_type='accounts'`. Read saved values without new research when that is all the
   user asks for. **Find contacts only when requested or necessary to identify the requested
   decision-makers**, using `compelling_find_contacts`:
   - Pass `roles` (title + optional persona + `per_title_limit`) to define who to look for, or omit to use the list's configured roles.
   - Cap spend with `limit` (accounts processed). Costs 2 credits per contact — offer `compelling_estimate_credits(action='find_contacts')` first.
   - It is asynchronous: pass `wait_seconds`, or long-poll `compelling_contacts_run_status`.
3. **Define the enrichment column** with `compelling_add_insight` (free — defining a column researches nothing):
   - Contacts: `email`, `personalLinkedin` (NOT `linkedinUrl` — that is the account-level value), `salutation`, `phoneNumber`, `premiumPhoneNumber`.
   - Accounts: `revenue`, `industry`, `employees`, `linkedinUrl`, `hqPhone`, …
   - Anything else is a custom type (`boolean`, `singleChoice`, `multipleChoice`, `integer`, `entity`, `url`, `date`, `jobtitle`, …) and needs a `question` + `header_name`; for accounts include `{company_name}` and `{domain}` in the question.
   - Custom company questions can cover SAP usage, ISO 13485 certification or current hiring.
     Preserve any time window the user specifies; do not present historical evidence as current.
   - Reuse existing columns — check `compelling_list_insights` before adding duplicates.
4. **Research the values** with `compelling_run_insight`. It requires an **explicit scope**: pass `account_ids`/`contact_ids` or a `limit` — there is no "run on everything" default. Credit-spending; offer an estimate first.
5. **Poll** `compelling_insight_status` (with `wait_seconds`), then **read values** via `compelling_read_list` — ground truth.

## Bringing your own data

If the user already has accounts/contacts (CRM export, CSV), write them directly with
`compelling_ingest_records` — no research, zero credits. Identify accounts by `domain`
(resolve-or-create) or `account_id` (attach existing). Known values go in as final insight
answers via existing `question_id`s.

Ingest can overwrite existing insight answers. Before replacing values, explain the affected
records and columns and obtain authorization for those replacements. Use authorization the
user has already given; do not ask again for the same scope.

## Credit authorization

An estimate-only request does not authorize starting a paid run. If the user asks for a cost
preview or explicitly withholds approval, return the estimate (or ask for missing scope)
without starting contact discovery or enrichment. When the user has already authorized the
paid action and its scope, proceed without asking for the same authorization again.

## Pitfalls

- There is no single "find contacts with email" call — find contacts first, then run the email insight on them.
- `record_type='accounts'` takes `account_ids`; `contacts` takes `contact_ids` — never mix.
- Counters are eventually consistent; trust `compelling_read_list`, not run counters.

## Evidence and language

Answer in the user's language and retain official company names and job titles. Report missing
or inconclusive research honestly. When evidence is requested, surface available sources and
reasons from Compelling (use `compelling_get_account_knowledge` for a company brief when
appropriate); never invent a source or imply that every researched answer has a citation.
