# Opportunity Checker Qualification Rules

## Qualified statuses

Only these two status values belong in the final LeadDeck Opportunity Checker CSV:

### EXPIRED_NOW_RENTAL

Use `EXPIRED_NOW_RENTAL` when all material conditions are supported by credible current evidence:

- The uploaded source identifies the property as an expired for-sale listing.
- No current Active, Coming Soon, Pending, or Under Contract for-sale listing is found.
- No credible sale after the source expiration date is found.
- Credible current evidence affirmatively indicates the property is currently available or actively marketed for rent as of the research date.

A rental page existing on the web is not enough. Historical or stale rental pages, rental history, rent estimates, cached/search-result snippets, "Check Back Soon for Upcoming Availability," "currently unavailable," or similar non-current availability signals do **not** qualify a property as `EXPIRED_NOW_RENTAL`.

If historical or subsequent rental evidence exists but current rental availability cannot be confirmed, preserve that evidence in `research_notes`. If the property otherwise satisfies the off-market rules, classify it as `EXPIRED_OFF_MARKET`.

`EXPIRED_NOW_RENTAL` is a strong opportunity signal because the observable sequence is For Sale → Expired → Currently Available for Rent. Do not speculate about why the owner chose to rent.

### EXPIRED_OFF_MARKET

Use `EXPIRED_OFF_MARKET` when:

- The uploaded source identifies the property as an expired for-sale listing.
- No current Active, Coming Soon, Pending, or Under Contract for-sale listing is found.
- No credible sale after the source expiration date is found.
- The evidence is sufficient to confidently match the researched property/unit to the source record.

## Do not qualify

Exclude a property from the final LeadDeck CSV when any of these apply:

- Current evidence shows Active or Coming Soon for sale.
- Current evidence shows Pending or Under Contract.
- Credible evidence shows a sale after the source expiration date.
- Sources materially conflict.
- The address or unit match is uncertain.
- Available evidence is insufficient to confidently assign one of the two qualified statuses.

**ACCURACY > QUANTITY.** Do not weaken the standard to reach any requested row count. Fewer verified rows is the correct result.


## Exact property identity rule

Before using any web evidence, verify that it belongs to the exact subject property. The evidence should match the source record's street number, street name, city, state, ZIP, and unit/address2 when applicable.

Never use a neighboring property, similar address, different street number, different unit, approximate search result, search-result snippet, or another property's listing history to qualify the subject property. If exact identity cannot be confidently established, exclude the property rather than guessing.

Validate **each source independently**. If one cited source matches the exact property and another cited source points to a different property/unit, discard the mismatched source completely. The valid source does not make the invalid source acceptable, and `research_notes` must never describe a mismatched source as evidence for the subject property.

## Ownership rule

No sale found does not prove that the seller from the expired listing still owns the property. Ownership verification is not required for opportunity qualification. Only make an ownership statement when credible evidence directly supports it.

## Research guidance

Use current credible public property/listing sources, including major real-estate portals, brokerage/listing sites, rental listings, and other relevant public sources. Cross-check sources when necessary. Compare all material listing/sale evidence to the expiration date from the uploaded source.

For rental evidence, distinguish between a page that exists and a property that is currently available. Read the current availability language on the source page whenever possible. Do not infer current availability from price text, rental history, a Rent Zestimate, an old listing page, or a search snippet alone.

For every property selected for the final CSV, record a concise evidence trail in `research_notes` that includes:

- the checked date;
- the material factual findings supporting the classification; and
- the complete `https://` URLs for the material sources used.

Write URLs in full so LeadDeck can preserve and render them as clickable evidence links. Every URL used as material evidence must be a **property-specific evidence page actually reviewed**. Do not cite a root domain, homepage, generic search page, category page, or a page for a different address/unit. Include useful historical or conflicting evidence only when it is exact-property evidence and helps explain the classification.

## Output order

Accuracy is the priority, not ranking optimization. After properties pass qualification and the mandatory evidence audit, assign unique integer `opportunity_rank` values beginning with 1 as a simple work/output order. When a Pocket Buyer or Target Buy Box is supplied, obvious Buy Box fit may inform the order, but do not spend research effort on subjective scoring and never let ranking considerations weaken verification.

## Mandatory final evidence audit

Before generating the CSV, audit **every selected row and every material URL**. A row may enter the final CSV only if it passes all applicable checks:

1. **Source-record check** — the uploaded file itself identifies the subject as an expired for-sale listing.
2. **Exact-property check** — every material source used in the classification matches the exact street number, street name, city, state, ZIP, and unit/address2 when applicable. Remove any source that refers to another property or unit.
3. **Specific-URL check** — every cited material URL is the actual property/listing evidence page reviewed. Root domains, homepages, generic search/category pages, and search-result pages fail this check.
4. **Current for-sale check** — no exact-property evidence shows Active, Coming Soon, Pending, or Under Contract. If it does, exclude the row.
5. **Post-expiration sale check** — no credible exact-property evidence shows a sale after the source expiration date. If it does, exclude the row.
6. **Rental check** — for `EXPIRED_NOW_RENTAL`, at least one exact-property, property-specific source must affirmatively show **current** rental availability/active rental marketing as of the research date. A displayed rent amount, historical rental record, stale page, cached snippet, `Check Back Soon`, `currently unavailable`, `off market`, or equivalent language fails this check. Negative/ambiguous availability language overrides the mere presence of a rental price.
7. **Conflict check** — if exact-property sources materially conflict and the conflict cannot be resolved with stronger current evidence, exclude the row.
8. **Notes check** — `research_notes` must accurately describe only evidence that passed the checks above and include the checked date plus full property-specific HTTPS URLs. Never claim a source says something its page does not support.

If a row fails an audit check, first correct it using valid exact-property evidence if available. If the evidence supports `EXPIRED_OFF_MARKET` but not `EXPIRED_NOW_RENTAL`, downgrade the status. If a qualified status still cannot be supported confidently, exclude the row. **Never substitute a nearby property, generic URL, assumption, or requested quantity for missing evidence.**

## Stopping rule

Continue researching until enough qualified candidates have been found to confidently select the number requested by the user, or until the entire uploaded file is exhausted. If no number is requested, default to 10. Once the requested set can reasonably be selected, stop unless the user explicitly requests research on every property.

## 0.1.4 deterministic verification protocol

The final evidence audit is a **hard pass/fail protocol**, not a general instruction. Complete it separately for each candidate before export. Do not rely on a search-engine result title, snippet, URL slug, AI summary, or prior conclusion as proof.

For each candidate, create an internal evidence ledger with the subject identity from the uploaded row and each source actually opened/reviewed. For every source, explicitly determine:

- `IDENTITY_MATCH`: PASS only when the opened source page itself identifies the same street number, street name, city/state and, when present, unit. If the page identifies another number or unit, FAIL and discard the source. ZIP differences require resolution; do not assume they are harmless.
- `DIRECT_PAGE`: PASS only for the actual property/listing detail page. Homepages, root domains, search pages, category pages, search snippets, and pages for nearby properties FAIL.
- `CURRENT_FOR_SALE`: YES / NO / UNKNOWN based only on exact-property evidence.
- `POST_EXPIRATION_SALE`: YES / NO / UNKNOWN based only on exact-property evidence and the source expiration date.
- `CURRENT_RENTAL`: YES / NO / UNKNOWN. YES requires explicit current availability or active rental marketing on the exact-property page. A price without current availability is UNKNOWN, not YES.
- `NEGATIVE_RENTAL_LANGUAGE`: YES when the exact-property page says or clearly indicates unavailable, off market, check back soon, no upcoming availability, or equivalent. If YES, that source cannot support `EXPIRED_NOW_RENTAL`.

### Qualification truth table

A candidate may be `EXPIRED_NOW_RENTAL` only when:
- source record = expired;
- no exact-property source establishes current for-sale/pending/under-contract status;
- no exact-property source establishes a post-expiration sale;
- at least one source has `IDENTITY_MATCH=PASS`, `DIRECT_PAGE=PASS`, `CURRENT_RENTAL=YES`, and `NEGATIVE_RENTAL_LANGUAGE=NO`;
- no stronger/current exact-property source materially contradicts current rental availability.

A candidate may be `EXPIRED_OFF_MARKET` only when:
- source record = expired;
- exact-property direct-page evidence is sufficient to support current off-market/not-currently-for-sale status;
- no exact-property source establishes current for-sale/pending/under-contract status;
- no exact-property source establishes a post-expiration sale;
- unresolved material conflicts are absent.

If a required fact remains UNKNOWN, do not silently convert UNKNOWN to NO. Exclude the candidate unless the remaining exact-property evidence independently satisfies the relevant qualified status.

### Citation integrity test

Immediately before writing each CSV row, re-open/re-check the evidence represented by every URL that will appear in `research_notes` and ask:
1. Does this page itself identify the exact subject property/unit?
2. Does this page itself support the factual sentence I am about to write?
3. Is this the direct page I actually used?

If any answer is NO or UNKNOWN, remove that URL and any claim that depends on it. Re-evaluate qualification after removal. If the row no longer qualifies, exclude it.

**Never write phrases such as “exact-address evidence,” “exact property,” “currently available,” “off market,” or “no post-expiration sale found” unless the retained evidence ledger supports that precise claim.**

### Search versus evidence

Search results may be used to discover candidate pages, but search results are not evidence. Open the result and validate the destination page. If the destination cannot be reviewed, do not cite it and do not use its snippet as a qualifying fact.

### Minimum evidence behavior

Prefer fewer rows with auditable direct evidence over more rows with weak evidence. The requested count is a maximum target, never a quota. Do not replace a rejected property with a less-verifiable property merely to preserve the requested count.
