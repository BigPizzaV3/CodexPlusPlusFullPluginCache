---
name: opportunity-checker
description: Research an uploaded file of aged expired real estate listings, identify and rank the requested number of qualified expired-listing opportunities for a Pocket Buyer or Target Buy Box, and create a LeadDeck-ready seller CSV.
---

# 10 Leads to 10K — Opportunity Checker

Use this skill when the user wants to research an uploaded aged-expired real-estate listing file and identify properties worth working in LeadDeck.

The job is: **FILTER → VERIFY → QUALIFY → FORMAT**.

## Governing principle

**ACCURACY > QUANTITY.** Never fill the requested count by weakening the evidence standard. Returning fewer verified properties is the correct result when additional properties cannot be supported confidently.

## Workflow

1. Read the uploaded source file. Preserve legitimate source information; never invent missing fields.
2. If the user supplied a Pocket Buyer or Target Buy Box, use it when selecting and ranking opportunities. If none is supplied, continue using the properties in the uploaded file and rank on opportunity signal and evidence quality; do not invent a Buy Box.
3. Research candidate properties using current public web sources. Compare current evidence with the source expiration date.
4. Apply the qualification rules in `references/qualification-rules.md`.
5. Continue through the file until there are enough qualified candidates to select the number the user requested, or until the file is exhausted. If the user does not specify a number, default to 10. Do not assume a fixed number of source rows will yield 10 opportunities.
6. Run the mandatory final evidence audit **and the 0.1.4 deterministic verification protocol** defined in `references/qualification-rules.md` on every candidate before it may enter the CSV. Treat every evidence check as pass/fail/unknown; never convert unknown into a favorable assumption. Any candidate that fails the audit must be corrected using valid evidence or excluded. Never keep a row merely to reach the requested count.
7. Assign unique integer `opportunity_rank` values beginning with 1 only as a simple output order. Do not spend research effort optimizing rank; verification accuracy is the priority.
8. Create a CSV using exactly the contract in `references/leaddeck-csv-contract.md`. Include only qualified properties. Do not add ambiguous, listed, pending, or sold properties merely to reach the requested count.
9. Give a concise summary before the file: properties researched, qualified properties selected, count of `EXPIRED_NOW_RENTAL`, and count of `EXPIRED_OFF_MARKET`.
10. Tell the user the next step is: **LeadDeck → Import Sellers → Import + Skip Trace**.

## Important boundaries

- This skill qualifies property opportunities; it is not a skip-tracing workflow.
- Do not research contact information merely to populate owner, phone, or email fields. Preserve legitimate contact information already present in the uploaded source; otherwise leave it blank for LeadDeck/BatchData enrichment.
- No sale found does not prove the expired seller still owns the property. Never state continuing ownership without direct credible evidence.
- Do not infer seller motivation. Describe observed listing/rental/sale evidence only.
- Uncertainty must never be converted into `EXPIRED_OFF_MARKET`.
- Search results are discovery only, never qualifying evidence. Open and review the direct property page. Evidence must match the exact subject property. Never use a neighboring address, similar street number, different unit, approximate search result, search snippet, or generic domain page as evidence for the subject property. A valid source for one fact does not rescue an invalid source for another fact; discard every mismatched source completely.
- A rental page or rental history by itself does not prove current rental availability. Only use `EXPIRED_NOW_RENTAL` when credible current evidence affirmatively shows the property is currently available or actively marketed for rent.
- For every selected property, preserve an audit trail in `research_notes`: checked date, concise factual findings, and the complete property-specific HTTPS URLs of the material sources actually used for classification. Root domains, homepages, generic search/category pages, and URLs for other properties are prohibited.
- If the entire file is exhausted before the requested number of properties qualify, return only the qualified properties actually found and tell the user additional aged-expired candidates are needed.
- Explicit user instructions take priority over this workflow when they do not conflict with safety or truthfulness requirements.
