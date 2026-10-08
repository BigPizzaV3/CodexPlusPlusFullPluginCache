# Interactive experience and artifact design

Use these patterns to make the assessment feel guided and action-oriented without requiring custom UI.

## Turn structure

Apply the opening-notice and practice-page closing rules in `../SKILL.md` before this turn structure. The first response begins with both full notices, once. Do not repeat them at the end or on later turns in the same interaction unless the user explicitly requests the notice text. Each result, interim-findings, artifact-delivery, or closing response ends with the practice-page line, after any artifact links and useful next-step prompts. A one-response assessment begins with the notices and ends with the practice-page line, not another notice display.

Display the responsible-law-firm identification at the position required by `../SKILL.md`, while keeping the practice-page line last when required.

For assessment content after any required opening notices and opening identification, use this order:

1. `Step X of 7 — <short step name>`.
2. A one-sentence explanation of why the step matters.
3. No more than three questions or requests.
4. A compact `Recorded so far` summary when the user has already supplied information.
5. `Still to answer` listing unanswered items from the current or earlier batches.
6. `Choose a next step` with two to four tailored prompt options.

Keep the options short, specific, and phrased as messages the user can send verbatim. Prefer choices that advance the workflow, correct the record, inspect evidence, or create a useful interim output.

When the host exposes native follow-up suggestions or action controls, use those affordances. Otherwise show a numbered list. Do not describe ordinary Markdown text as clickable.

### Typical prompts during the assessment

Choose only those relevant to the current state:

- `Continue to the next step`
- `Let me upload documents for this section`
- `Show the gaps identified so far`
- `Change one of my earlier answers`
- `Mark this item as unknown and continue`

Do not repeat the same four choices mechanically on every turn. Tailor labels to the subject, such as `Review my cap table` or `Build the IP coverage matrix`.

If the user answers only part of a multi-question batch, mark answered items and carry every omitted item forward as Pending. Do not infer that silence means Unknown, Not applicable, or no. If the user expressly skips an item, mark it Explicitly skipped and keep it in `Still to answer` until resolved or the assessment ends.

## Standard final dashboard

Once an outcome can be calculated, automatically create one compact visual summary. When the `visualize` capability or an equivalent in-conversation visualization tool is available, use it. Otherwise use the fallback below.

The dashboard must contain:

1. Title: `<Company name> financing readiness`.
2. Three headline metrics: readiness score out of 100, assessment completeness, and evidence coverage.
3. The outcome label directly beside or beneath the readiness score.
4. Seven horizontal category bars using each category's earned points and maximum points.
5. A concise explanation for the lowest-scoring or user-selected category.
6. A `Priority sequence` arranged as Now, Next, and Later, using no more than ten total actions.

Use the same category order as the scoring framework. Keep labels visible, pair color with text, and use one restrained status color rather than a different decorative color for every category. Make the first render useful without interaction and ensure the information remains understandable without color.

Render the title exactly once. If the visual contains `<Company name> financing readiness`, do not repeat the same heading immediately before or after it in narrative text. If no visual is used, provide one narrative heading only.

If local interaction is available, let the user select a category bar to update the category explanation. Do not add filters, tabs, decorative charts, or controls that do not change a decision.

### Nonvisual fallback

Show the three metrics first, followed by a category table with `Category`, `Earned`, `Maximum`, `Status`, and `Key driver`, then the Now/Next/Later action list. Preserve the same numbers and labels used in the narrative result.

## Artifact menu

After the standard dashboard and concise findings, present two to four relevant creation prompts. Use these as defaults and tailor them when a stronger next step is apparent:

- `Create my editable readiness workbook`
- `Generate a concise readiness report`
- `Build my data-room index and action plan`
- `Prepare my questions for counsel`

If the user selects an artifact, create it in the best editable format supported by the current surface. Do not create every artifact automatically unless requested.

Include both required notices from `../SKILL.md` verbatim once in each standalone report, workbook, or data-room index/action plan: place them at the beginning of a narrative report, or in a clearly labeled, fully readable `Notices` sheet or section for a workbook or index. Do not duplicate them at the end. A standalone artifact's notices do not replace the first conversation response's opening display. End a narrative report or text action plan with the practice-page line from `../SKILL.md`; include that link in the Summary or main index sheet for a workbook. The artifact-delivery response ends with the same practice-page line, not repeated notices. Use that URL for any Pillsbury contact link, not an email address.

Include the exact responsible-law-firm statement from `../SKILL.md` as visible text in every standalone report, workbook, or data-room index/action plan. In a narrative report, place it immediately after the opening notices. In a workbook or index, include it in the main Summary/index sheet and in the Notices sheet or section. Keep it readable in the document body, not only in file properties, comments, or a hidden sheet. Do not reproduce privileged communications or attorney work product in generated artifacts.

### Readiness workbook

Prefer `.xlsx`; use `.csv` files only as a fallback. Include these sheets when the data exists:

1. `Summary` — outcome, score, completeness, evidence coverage, seven category scores, and a category chart.
2. `Checklist` — every weighted item, status, score contribution, evidence source, observation, owner, and priority.
3. `Document Register` — the fields from the document-review protocol.
4. `Inconsistencies` — sources compared, mismatch, owner, and specialist review.
5. `Action Plan` — Now/Next/Later, action, owner, target date, and status.
6. `Data Room Index` — the columns defined in the data-room reference.

Use formulas for summaries when the environment supports reliable spreadsheet recalculation. Keep Unknown distinct from Missing and keep counsel-review items visibly separate from ordinary administrative actions.

### Readiness report

Prefer `.docx`; use Markdown or PDF only when requested or when editable documents are unavailable. Include:

- Company, sector, and operating-footprint context.
- Outcome and the three headline metrics.
- Category findings and key evidence.
- Priority sequence.
- Questions for counsel.
- Methodology and the legal-information boundary.

Keep the report concise enough for a founder or company executive to act on quickly.

### Data-room package

Prefer an editable `.xlsx` index and action plan. If the user explicitly requests a folder structure, also create a clearly named folder tree or ZIP containing empty folders and an index; never copy confidential source documents into it unless the user expressly asks and the environment permits it.

## Final next-step prompts

After any artifact is created, suggest two to four logical continuations before the final practice-page line, unless the user has asked to stop. For example:

- `Update the assessment using the new documents`
- `Explain my three highest-priority gaps`
- `Create a 30-day preparation plan`
- `Show what changed since the last assessment`

Never send a message, contact Pillsbury, or create an external data room merely because the user selects a prompt.
