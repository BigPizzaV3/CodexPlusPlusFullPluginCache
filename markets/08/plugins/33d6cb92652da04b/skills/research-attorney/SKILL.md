---
name: research-attorney
description: "Always call this first over raw `search_cases` or `search_documents` for any attorney-focused inquiry where the user provides the attorney's name and/or bar number."
metadata:
  displayName: "Research Attorney"
  seedlingSlug: "research_attorney"
---

### Jurisdiction

You need to know the state the user is interested in, or whether they're fine searching every state. If the request is ambiguous as to jurisdiction, ask before proceeding.

### Resolve the attorney's identity before you search

- **Capture the middle name if known** — you will search it three ways: omitted, as an initial, and fully spelled out.  

### Build the name-form SET (do not run a stop-at-first-hit ladder)

The same attorney is routinely indexed under several non-unified forms, and **each form returns a different, only-partially-overlapping subset.** Stopping at the first form that returns hits silently undercounts. So: assemble the applicable forms, run each as a **quoted phrase with the state filter**, then **combine the results and dedupe to case/docket id.**

Forms to include when applicable:

1. "First Last" (no middle)
2. "Last, First" (reversed)
3. "First Middle Last" (full middle spelled out)
4. "First M. Last" (middle initial)
5. reversed middle forms ("Last, First Middle", "Last, First M.")
6. legal/professional first-name swap (search *both*, e.g. Reagan **and** Richard)
7. punctuation-stripped variant for apostrophes / hyphens / accents (a quoted "O'Flaherty" returned 0 even though the firm is in the corpus)

Treat a large gap between forms as **expected**, not as evidence one form is wrong. When the surname is common, **lead with the full-middle form**. Only a pure "is this person in the data at all" check may treat the forms as alternatives; any counting/profiling question must union them.

### Run two retrieval lanes, then reconcile

Run the full-text name-form set **and** the entity filter (`entities=[{name, role: Attorney}]`, no middle initial so default slop absorbs the middle), and reconcile. **Never report one lane's number as "the" count without saying which lane produced it.** Treat an entity-lane **zero as non-dispositive** (it does *not* mean "no footprint"); treat an entity-lane **hit as still needing the counsel-of-record check below.**

Bar-number path (unchanged): `search_documents` with the bar number + quoted name; if empty, drop the bar number and run the name-form set across documents and cases.

### Match the tool to the question type

- **Analytical / aggregate** (practice areas, motion types, judges, win rates) → `search_documents` with `include_aggregations=true`; read the `practice_area`, `matter_type`, `judge`, `motion_type`, `outcome` facets.
- **Specific-case** (which cases, case vs. X) → `search_cases`, unioned with `search_documents` deduped by `case_name`. A firm filter `entities=[{name, role: Law Firm}]` is an *optional add, not a primary path* — coverage is sparse and it mis-resolves (a firm filter returned a plausible-but-wrong cluster for one common name and the wrong firm for another).
- When intent is unclear between analytical and specific-case, ask one clarifying question.

### Confirm one PERSON, not one NAME (disambiguation)

Namesakes are live and prolific, and aggregations blend them silently (two different "John Wayne Hogan"s; at least three "Mark Clark"s; two "Russell Hardin"s). Before reporting, **bucket the returned entity strings by firm + county + practice area.** Report only the bucket(s) matching your target. If two firms each look plausible, ask the user which.

### Counsel-of-record is a CHECK, not just a caveat

A full-text hit does not establish that the person was counsel:

- **Confirm the person appears in the document's structured Attorney list** before calling them counsel of record (one attorney's 12 full-text hits never tagged him as an attorney — pure noise).
- **Role mis-indexing:** an attorney can be indexed as a **Party** in his own case, so `role: Attorney` can miss filings and `role: Party` can capture counsel — don't trust the role tag alone.
- **Duplicate entity records:** the same name appeared twice in one document's attorney list — dedupe before counting.
- **OCR / spelling variants:** expect corrupted forms (e.g. "Mary W Clark" for "Mark W Clark") 

### How to read a ZERO

A zero across all forms means "not found in covered **state-court** records," not "no practice." Before concluding, escalate:

1. Run the **bare distinctive surname** (broadest contiguous net).
2. **Check whether the attorney's FIRM is in the data.** This is the most important step: Trellis often records counsel at the firm level (e.g. "COLLINS LAW FIRM"), not the individual. In one case every individual-name search returned 0 while the firm's matters — including a notable verdict — were in the data under the firm name. If so, pivot to `research_law_firm`.

### Reporting discipline

- **Report case-level counts in addition to raw document counts.** Aggregations count documents, and a single heavily-litigated matter skews everything. State results as "N documents across M cases."
- **State which lane/form produced each number**.
- **Don't quote the `practice_area` facet label verbatim**. Treat facets as directional and check the type strings.

### Anti-patterns

- Do not use unquoted multi-token free-text without a phrase quote and a state filter 

- When a free-text firm/name search returns a large count, verify the entity actually appears in the returned summaries before trusting the number.
