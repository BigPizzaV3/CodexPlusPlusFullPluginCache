---
name: clean-data
description: "Tidy a pasted list of companies or contacts before matching or enrichment: normalize company names, domains, countries and emails, flag invalid rows with a reason, match each row to AgentSource records, and remove duplicates that resolve to the same company or person. Use for 'clean this list', 'match these companies to domains', 'dedupe these contacts', 'which of these emails are valid', 'prep this list for enrichment'. Works on lists pasted in chat, up to roughly 100 rows. Not for building a new list (use list-builder)."
---

# Clean Data

Standardize and check a pasted list, then match it so duplicates collapse onto real company or person records. Nothing is deleted: every row stays, with a status and reason.

## Connector rules

Use only the AgentSource tools in your tool list. Each tool's live description and input schema are authoritative; if this skill disagrees with a tool, follow the tool.

- **`tool_reasoning`** is required on every call: the user's original request in their exact words (up to 2000 characters), reused unchanged across chained calls for the same task. Never replace it with a per-step rationale or add personal data the user did not write.
- **Sessions:** reuse `session_id` from the previous response while continuing the same request; omit it to start a new request. Never invent one.
- **Chaining by ID:** pass `business_id` and `prospect_id` values from `match-business`, `match-prospects` or `fetch-entities` results. Do not re-match entities that a fetch already returned.
- **`autocomplete` first**, one concept per call, for `linkedin_category`, `naics_category`, `company_tech_stack_tech`, `job_title`, `interests`, `skills`, `business_intent_topics`, and US `city_region`. Use the returned values as-is. Use ISO codes directly for countries (`US`) and regions (`US-CA`).
- **What you see:** every tool returns full results inline. `fetch-entities` returns up to `page_size` rows per call (at most 500) and a `next_cursor` for the next page; `fetch-entities-statistics` returns aggregates over every match.
- **Credits:** every data call uses credits on the user's AgentSource account. Request only the rows and enrichments the task needs, count with `fetch-entities-statistics` before a large pull, and confirm with the user before fetching more than 100 rows or enriching contact details for more than 50 people.
- **Limits per call:** `match-business` 50 companies, `match-prospects` 40 people, `enrich-business` and `enrich-prospects` 50 IDs, `fetch-businesses-events` 20 companies. Name several enrichment types in one `enrichments` list rather than one call each.
- **Presenting:** show returned records in a table with the fields that matter for the task. Never mention session IDs or internal table names.
- **Event details:** if a fetch used the `events` filter and the user did not already ask for event details, ask before calling `fetch-businesses-events` or `fetch-prospects-events`.
- **Lists:** work from lists pasted in chat or text from attached files, in batches that respect the limits above.

## Input

A list of companies or contacts pasted in chat, or the text of an attached file. Roughly 100 rows is the practical limit in one conversation; for more, work in batches. Note which column is the company name, domain, email, LinkedIn URL, phone or country; ask only if it is unclear. For a very large file, suggest the user clean it in a spreadsheet first.

## Workflow

1. **Profile the input.** Report row count, fill rate for each field, and obvious problems: placeholder text ("N/A", "none", "-"), pasted addresses in the name field, many spellings of one country, free-email providers, and role addresses.
2. **Standardize,** keeping the raw value beside the normalized one:
   - *Company name:* trim, collapse spaces, remove stray punctuation, and drop a trailing legal suffix (Inc, LLC, Ltd, GmbH, S.A.) for matching only.
   - *Domain:* strip the protocol and `www`, keep the registrable domain, lowercase. Flag free-email domains separately.
   - *Country:* convert to ISO two-letter codes (`United States` → `US`, `UK` → `GB`, `Deutschland` → `DE`).
   - *Email:* trim and lowercase.
   - *LinkedIn:* keep the full profile URL.
3. **Validate** each field and tag the row; never delete one:
   - *Email:* syntax, role addresses (`info@`, `sales@`, `noreply@`, `support@`), well-known free or disposable providers. You cannot check deliverability or mail servers, so say that valid means well-formed.
   - *Domain:* looks like a real domain, no IP address or spaces.
   - *Country:* resolves to a code.
   Give each problem a short reason code (`role_address`, `free_provider`, `invalid_syntax`, `placeholder`).
4. **Match the valid rows.**
   - Companies with a name and/or domain: `match-business`, up to 50 per call.
   - People: `match-prospects`, up to 40 per call, by email, LinkedIn URL or phone number, or full name plus company name (add the company's `business_id` when you have it). Skip rows tagged as role addresses or disposable domains so you do not spend matching on them.
   Match results are complete, so read them directly. Check a resolved company for the shell-entity pattern (a big brand with 1-50 employees under "Corporate Managing Offices") and retry with the other domain. An email miss stays a miss; never retry it as a name search.
5. **Deduplicate on the IDs.** Rows that resolve to the same business ID or prospect ID are duplicates; keep the first, mark the others with the ID of the survivor. Different IDs are different entities even if the names look alike, and subsidiaries or brands under one parent (for example a parent and its product domains) are separate companies; `enrich-business` with `company-hierarchies` shows the tree.
6. **Report** and offer next steps.

## Reply

- **Profile:** a short before-and-after summary of fill rates and the issues found.
- **Standardization:** three to five example changes (`"  ACME, Inc. "` → `acme`, `"WWW.Acme.COM"` → `acme.com`).
- **Validation:** counts of valid and invalid rows and a frequency list of reason codes.
- **Result table:** the input row, normalized value, status (matched, unmatched, invalid, duplicate of row N), reason, and the matched name and domain. Show the first rows in chat and offer the rest in batches.
- **Next steps:** enrich the matched rows with `enrich-company` or `enrich-contact`, or score them with `score-leads`. If the match rate is low, suggest adding LinkedIn URLs, company domains or work emails.

## Limitations

- Validation checks format only: no deliverability or mail-server check, and no phone verification.
- Person-name parsing is simple; non-Western name orders and compound surnames may need the user's confirmation.
- Free-email addresses cannot be tied to a company by themselves; pair them with a name and company for a prospect match.
- Matching returns an ID or nothing, with no confidence score.
- Works in chat, so very large files need to be split.
