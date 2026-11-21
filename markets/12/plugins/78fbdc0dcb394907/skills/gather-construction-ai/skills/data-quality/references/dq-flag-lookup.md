# Flag Sentence Lookup Table (Steps 3–7)

One shared pattern for every flag sentence in Sections 2–5 and 9 of the report: state the metric,
then append the matching clause below when its trigger condition holds. Sentences are advisory
prose only — none of them compute a number; the numbers come from Steps 2–10 and (for
coverage-gap and duplicate arithmetic) from `scripts/shift_analytics.py` (see below Step 10).

| # | Step / Metric | Trigger | Clause to append |
|---|---|---|---|
| 1 | 3 / Shift coverage | Coverage < 90% | "⚠️ Shift coverage is [X]% — [Y] working days have no records. Missing dates: [list first 10]" |
| 2 | 3 / Supervisors active | Exactly 1 supervisor | "Only one supervisor is recording. If multiple supervisors operate on this project, records may be missing." |
| 3 | 4 / Narrative presence | <80% of records have a narrative | "⚠️ [X]% of shift records have no narrative. Narratives are critical for delay analysis, event identification, and claim evidence." |
| 4 | 4 / Narrative length | Average word count <30 | "⚠️ Narratives are very brief (avg [X] words). Short narratives reduce the effectiveness of $narrative-search and $events." |
| 5 | 4 / Boilerplate | Any near-identical narratives detected | "⚠️ [X] records appear to have identical or near-identical narratives — this may indicate copy-paste recording rather than contemporaneous diary entries." |
| 6 | 6 / Progress targets | No planned targets set | "Progress is recorded as actuals only — no planned targets are set. This limits the ability to assess variance and forecast completion." |
| 7 | 6 / Update frequency | Updates are sporadic | "Progress appears to be updated [frequency]. Regular updates (ideally daily) improve the accuracy of $progress and $cost-to-complete." |
| 8 | 7 / Access data | Zero access data recorded | "No access/possession data recorded. If this project requires access windows, this data gap should be addressed — access performance is critical for delay analysis and claims." |

For Step 5 (Resource Recording — Labour/Plant/Materials), each data type below 80% coverage
takes the type-specific clause: **Labour** → "Days without labour records make headcount
analysis unreliable and weaken measured mile calculations."; **Plant** → "Plant utilisation
analysis requires consistent daily recording — current gaps mean idle equipment may not be
identified."; **Materials** → "Material consumption tracking is incomplete — this limits the
ability to detect wastage or forecast requirements." If all three are ≥80%, use: "Resource
recording across labour, plant, and materials is at or above 80% — sufficient for reliable
analysis."
