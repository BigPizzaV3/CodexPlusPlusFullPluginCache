# Shared Patterns Index

One file per pattern — read only the ones a skill cites (`NN-slug.md`), never the whole directory. This index is for authors; skills cite specific files, never this README.

| # | File | Purpose | Typically needed by |
|---|---|---|---|
| 1 | `01-project-resolution.md` | Resolve which Gather project the user means | almost every skill |
| 2 | `02-date-range-parsing.md` | Normalise user date phrases to `from`/`to` | almost every skill |
| 3 | `03-empty-data-handling.md` | Answer, don't error, on no data | almost every skill |
| 4 | `04-pagination-rate-limits.md` | `getShiftRecords`/`getPeople` paging, rate limits, `modifiedSince`, quote-what-you-use | diary, photos, delay-analysis, narrative-search, weather-impact, people, delivery-notes |
| 5 | `05-contract-type-resolution.md` | Determine NEC/JCT/FIDIC before citing clauses | access, ce-builder, ce-quotation, events, commercial-report |
| 6 | `06-notification-compliance.md` | Time-bar windows per contract form | nec-deadlines, ce-builder, events |
| 7 | `07-event-to-clause-mapping.md` | Event category → clause table | access, commercial-report, ce-builder, events |
| 8 | `08-report-numbering.md` | Ref number prefixes and sequencing; cross-skill suggestions | every report-producing skill |
| 9 | `09-commercial-qa-gate.md` | QA checks before presenting priced totals | valuation, cvr, final-account, tender-pricing |
| 10 | `10-contractual-event-keywords.md` | Canonical event-detection keyword list | events, cost-to-complete, hooks.json (kept in sync) |
| 11 | `11-one-event-one-register.md` | Why DA/AC/WI registers must never be summed | delay-analysis, access, weather-impact |
| 12 | `12-schema-verification.md` | Verify a report field exists before computing on it; divide-by-zero convention | most `getCachedReport` skills |
| 13 | `13-contract-profile.md` | `contract-profile.md` file convention and consumer rules | contract-profile (producer), ce-builder, ce-quotation, nec-deadlines, weather-impact |
| 14 | `14-commercial-profile.md` | `commercial-profile.md` file convention and consumer rules | commercial-profile (producer), valuation, subcontractor-check, dayworks, plant-offhire, material-reconciliation, prelims-monitor |
| 15 | `15-programme-baseline.md` | Imported programme sidecar; STORED vs INDICATIVE doctrine | programme-import (producer), programme-impact, programme-compare, asbuilt-programme |
| 16 | `16-cost-ledger.md` | Imported cost ledger file convention | cost-import (producer), cvr |
| 17 | `17-correspondence-register.md` | Imported correspondence register | correspondence-import (producer), ce-builder, adjudication-pack |
| 18 | `18-tender-bill-boq.md` | BoQ/quote/pricing-build-up file conventions | boq-import, quote-levelling, tender-pricing |
| 19 | `19-interview-and-confirm.md` | Shared resolve→interview→confirm→write→next-steps skeleton | commercial-profile, contract-profile |
| 20 | `20-evidence-retrieval.md` | Shared getShiftRecords→getShiftRecord fallback discipline | subcontractor-check, valuation, narrative-search, delivery-notes |
| 21 | `21-fetch-once-cache.md` | `.gather-cache/` convention for one-fetch-per-run in agent chains | agents chaining multiple skills over one project/date range |
