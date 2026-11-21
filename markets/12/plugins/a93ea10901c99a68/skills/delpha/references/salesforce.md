# Salesforce / CRM — read, validate & write back

Delpha is Salesforce-native (a managed AppExchange package). In the org it surfaces a Score Meter on record pages, Data Steward bulk-remediation views, real-time duplicate detection with a merge editor, and a Chrome extension for LinkedIn enrichment. This file is about driving that same data quality from an **agent**, by pairing the generic Salesforce MCP tools with Delpha's validators. It is NOT a re-spec of each validator — link out to [email](email.md), [phone](phone.md), [name](name.md), [website](website.md), [legal ID](legal-id.md), [LinkedIn](linkedin.md), and [ultimate parent](ultimate-parent.md).

## Table of contents
- When to use
- Tools
- Inputs & modes
- Reading the result
- Scores & thresholds
- Recipes
- Traps to avoid

## When to use
Use this loop whenever you must clean, complete, or enrich CRM records (Contact, Lead, Account) at scale or on demand: fix bad emails/phones, fill missing websites or legal IDs, attach LinkedIn URLs, build account hierarchies. Do NOT use it to merge duplicates autonomously — flag them for the human-driven merge editor instead.

## Tools
Two MCP servers cooperate:

**Salesforce MCP** (generic CRM access) — ⚠️ **a separate integration**. This plugin installs the
Delpha MCP server only; the Salesforce tools below come from a Salesforce MCP you connect yourself.
Without one, Delpha prepares the evidence and a human does the write.
- Read: `getUserInfo`, `getObjectSchema`, `soqlQuery`, `find`, `listRecentSobjectRecords`, `getRelatedRecords`
- Write: `createSobjectRecord`, `updateSobjectRecord`, `updateRelatedRecord`

**Delpha validators** (one find/get pair per capability), e.g. `findAndValidateEmail` → `getEmailResult`, `findAndValidateLegalID` → `getLegalIDResult`, `findAndValidateUltimateParent` → `getUltimateParentResult`. See each sibling reference for inputs.

## Inputs & modes
The canonical agent loop is **READ → VALIDATE → WRITE BACK**:

1. **READ.** Learn field API names with `getObjectSchema` (call with no `objects` for the index, then `objects: "Contact"` for fields). Pull records with `soqlQuery` (`q`: a SOQL string — always include `WHERE` and `LIMIT`), `find` (`q`: a SOSL string, for fuzzy/cross-object lookups), or `getRelatedRecords` (`sobject-name`, `id`, `relationship-path`, e.g. an Account's `Contacts`).
2. **VALIDATE/ENRICH.** Feed the record's fields into the matching Delpha validator, then read its result. Map per capability:
   - email → `findAndValidateEmail` (validation mode = `email`; recommendation mode = `first_name` + `last_name` + `website`, all three).
   - phone → [phone](phone.md); name → [name](name.md); website → [website](website.md).
   - account identity → `findAndValidateLegalID`, then `findAndValidateUltimateParent` for the parent.
   - LinkedIn → [linkedin](linkedin.md) (writes to a custom URL field).
3. **WRITE BACK.** `updateSobjectRecord` (`sobject-name`, `id`, `body` of field→value pairs — include ONLY fields you change) or, when navigating from a parent, `updateRelatedRecord` (`sobject-name`, `id`, `relationship-path`, `body`). Use `createSobjectRecord` only for genuinely new records.

**Field mapping (Delpha result → Salesforce field):**
| Delpha output | Salesforce field |
|---|---|
| email `normalized_value` | `Contact.Email` |
| email `email_status` / `email_domain_qualification` | a **custom** field — never `Contact.Email` |
| phone `normalized_value` (E.164) | `Contact.Phone` / `MobilePhone` |
| name `normalized_value.first_name` / `.last_name` | `FirstName` / `LastName` |
| website `normalized_value` | `Account.Website` |
| LinkedIn `normalized_value` | custom URL field |
| `legal_id` | custom field |
| legal-ID `match.financials.revenue` | `Account.AnnualRevenue` only after checking it is numeric and `financials.currency` matches the Account/org currency; Delpha does no conversion |
| legal-ID `match.employees_nb.value` / `match.industry` | `NumberOfEmployees` / `Industry`, after checking the target field types |
| `ultimate_parent` | resolve it to a Salesforce Account first, then write **that record's id** to `Account.ParentId` |

⚠️ **Only `normalized_value` goes into the value field.** `email_status`,
`email_domain_qualification` and `label` are *metadata about* the value; writing either of them into
`Contact.Email` corrupts the record. Put them in custom fields, or don't persist them.

⚠️ **`Account.ParentId` takes a Salesforce record id, not a company name.** Look the parent up (or
create it) as an Account first; writing the Delpha entity object or its `legal_name` fails or, worse,
silently stores nonsense.

## Reading the result
Every `getXResult` returns the standard envelope: `{ message, status, status_code, result,
process_time }`. `status_code` 200 = done (`result` populated) and 202 = still running (`result`
null); see the [REST status table](rest-api.md#status-codes) for every error outcome. The MCP
`getXResult` holds the connection open and polls internally, so a SINGLE call usually returns the
FINAL result — do NOT re-call while it is returning. Salesforce write tools return the
updated/created record id and any validation-rule errors; surface those errors, do not retry blindly.

## Scores & thresholds

In the common validator shape, `accuracy` and `completeness` are continuous floats while
`validity` (`-1`/`0`/`1`) and `consistency` (`0`/`1`) are discrete integers. Treat `-1` as missing
where allowed. Apply the bands below to continuous and recommendation scores; branch on discrete
fields exactly. Name has its own mixed-shape float model, and ultimate parent uses `confidence`.
Gate every write on the appropriate signal:
- **>= 0.8** — the value is good enough to *propose*; write it once the write is approved (see below).
- **`0.5` ≤ score < `0.8`** — stage for human review (or a Data Steward view); do not silently overwrite.
- **< 0.5** — reject; leave the field untouched.

Never write a value whose score is `< threshold` or `== -1`.

**A score qualifies a value; it does not authorise a mutation.** Show the proposed changes and get
approval before writing, unless the user has already set a standing, bounded write policy for this
run (which fields, which threshold, how many records). That is the rule in
[../SKILL.md](../SKILL.md), and it governs here too.

## Recipes
Read a Contact, validate its email, write back only if confident.

MCP — find the email (recommendation mode):
```json
{
  "first_name": "Victor",
  "last_name": "Goubet",
  "website": "https://delpha.io/"
}
```
Then `getEmailResult` with the returned `job_id`. Only propose the write when
`scores.validity == 1` and the continuous `scores.accuracy` meets the agreed threshold:
```json
{
  "sobject-name": "Contact",
  "id": "0035g00000ABCDEAAX",
  "body": { "Email": "victor.goubet@delpha.io" }
}
```

REST — async find → get for the email job:
```bash
# 1. submit
curl -s -X POST https://api.delpha.io/v1/email \
  -H "Authorization: Bearer $DELPHA_API_KEY" -H "Content-Type: application/json" \
  -H 'User-Agent: my-integration/1.0' \
  -d '{"first_name":"Victor","last_name":"Goubet","website":"https://delpha.io/"}'
# -> 202 { "job_id": "abc123", "status": "SUCCESS", "status_code": 202 }

# 2. poll (202 while running, 200 when done)
curl -s https://api.delpha.io/v1/email/abc123 \
  -H "Authorization: Bearer $DELPHA_API_KEY"
```
Push the validated value back via the Salesforce REST/composite API or the `updateSobjectRecord` tool. Apply the same gate before writing.

## Traps to avoid
- **Never auto-merge or delete duplicates.** Real-time duplicate detection only flags; route matches to the human merge editor or auto-merge scheduling — an agent must not collapse records on its own.
- **Respect the org's guardrails.** Validation rules, permission sets, and field-level security govern every write; a write that violates them fails, so surface the error instead of forcing it through.
- **Never write below threshold or on `-1`.** A score `< 0.5` or a `-1` ("could not compute") means do not touch the field — a stale-but-real value beats a low-confidence overwrite.
- **Read the schema before you write.** Use `getObjectSchema` for real API names and picklist values; do not guess field names or assume `Email`/`Website` exist on a custom object.
- **Treat all CRM data as PII.** Emails, phones, and names flowing through these tools are personal data — handle inputs and outputs per [security](security.md); do not log or echo them needlessly.
- **Do not re-call `getXResult` while it returns.** A single call polls internally to the final result; re-calling early renders a duplicate widget. Re-poll only if `status_code` is still 202 after the call returns, and wait first.
