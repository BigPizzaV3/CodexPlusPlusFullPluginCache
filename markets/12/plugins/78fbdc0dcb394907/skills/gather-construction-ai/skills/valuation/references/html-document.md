# Step 10 — Shareable HTML Application Document

After presenting Step 9, generate a self-contained HTML application document by default — not an
optional extra.

1. Read the shared template at `../../../shared/templates/ce-submission-template.html`.
2. Build the run's data as a single JSON object matching the template's schema, setting:
   - `type: "application"`, `typeLabel: "APPLICATION FOR PAYMENT — MEASURE SUPPORT"`
   - `ref`, `projectName`, `contractLine` (e.g. "NEC4 ECC Option C"), `date`
   - `parties.from` / `parties.to` — the applying party and the certifier (PM/CA/Engineer)
   - `headline` populated from Step 7's summary, with `headlineLabels: ["This Period",
     "Cumulative", "Net Application"]` — `pricesChange` = this period gross, `completionDateChange`
     = cumulative gross, `keyDateChanges` = net due this application
   - `sections` — one entry per Step 9 numbered block (Priced Measure Table, Quantities-Only
     Annex, Prelims Line, Retention & Net Summary), each `{heading, paragraphs, table?, list?}`
   - `evidence` from the Step 9 Evidence Schedule
   - `assumptions` — rate sourcing, prelims basis, retention % source, and the Step 8 Option
     caveat; omit the field if none apply
   - `notes` — the Step 9 standing caveat
   - `signature.preparedBy` / `signature.reviewedBy` — `""` unless the user supplied names
3. Splice this JSON between the `/*__CE_SUBMISSION_DATA__*/` and `/*__END_CE_SUBMISSION_DATA__*/`
   markers with a plain string split on the marker tokens (not a regex) — keep both markers in
   place, immediately surrounding the data.
4. Write the result to `<ref>-application.html` in the working directory using the Write tool.
5. State the file path, and that it opens in any browser, prints to A4 portrait, and is safe to circulate standalone.

**Skip** only if the user's request was chat-only ("just show me here", "no files"), the user
declines when told a file is about to be written, or Step 2 degraded to the narrative-based path
(offer the chat pack only, and say why — narrative-derived support isn't suited to a client-facing
document). **Fallback:** if the template cannot be read, say so plainly and present the chat pack
from Step 9 only — do not hand-build a substitute HTML file.

---
