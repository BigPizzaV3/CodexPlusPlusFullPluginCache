# Pattern 20: Evidence Retrieval Fallback (getShiftRecords → getShiftRecord)

Several skills (`subcontractor-check`, `valuation`, `narrative-search`, `delivery-notes`, and
any future evidence-seeking skill) fall back to mining raw shift records when a dashboard report
doesn't carry the field they need. Follow this shared shape rather than re-deriving it per skill.

1. **Prefer the report first.** Only fall back to shift records when the relevant
   `getCachedReport` output lacks the field (delivery data, narrative detail, attribution) —
   check the report before mining records.
2. **Bounded window.** Fall back only within the already-resolved project and date range — never
   widen the window to "find more evidence" without telling the user and asking.
3. **Cap the pull.** Follow Pattern 4 (pagination and rate limits) exactly: `getShiftRecords`
   first to identify candidate records, then `getShiftRecord` per record. Warn the user before
   fetching more than ~25 individual records ("this will take roughly Nx0.5 seconds and N API
   calls — proceed, or narrow the range?").
4. **Quote what you use.** Per Pattern 4, quote only the fields the output actually needs from
   each `getShiftRecord` result (narrative excerpt, tag, timestamp, attached asset reference) —
   never the whole JSON object into the transcript.
5. **Cite the record.** Every fact sourced this way is cited by its shift-record UUID and date
   (e.g. "per shift record `[uuid]`, [date]") so a reader can trace it back — never presented as
   if it came from the aggregated report.
6. **NO RECORDS is a finding, not silence.** If neither the report nor the record search
   surfaces the fact, say so explicitly and flag it as a data gap or query for the user — never
   fill the gap with an inference from adjacent records.
