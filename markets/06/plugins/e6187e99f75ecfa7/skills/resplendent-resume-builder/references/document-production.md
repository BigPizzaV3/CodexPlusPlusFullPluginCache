# Career-document production

Read this reference when creating or editing any downloadable paginated career document, including a resume, CV, cover letter, application response, reference sheet, or portfolio case study. It governs layout mechanics; use the relevant content reference and [quality controls](quality-controls.md) for final review. Apply ATS-specific rules to resumes/CVs and any artifact intended for machine parsing; apply the same render, text-order, privacy, and page-economy gates to every paginated artifact.

## Default layout for an ATS-safe resume

Use a simple, single-column, top-to-bottom document. Keep critical contact and career information in the document body, not in headers, footers, text boxes, tables, graphics, or images. Use standard section headings and selectable text.

Use the following as a calibrated default, not a one-size-fits-all aesthetic rule:

- **Body text:** an accessible 10–12 pt typeface; normally 10.5–11 pt for an experienced professional. Use single or near-single line spacing (1.0–1.08). Do not make body text 1.5-spaced by default.
- **Margins:** start at 0.75 in on all sides. Adjust within 0.5–1.0 in only when needed for the candidate's content and readability; never shrink type or margins simply to force a page count.
- **Within an entry:** keep the title, employer, dates, and its bullets visually compact. Use 0 pt before/after individual bullets and no empty paragraphs between them.
- **Between discrete entries:** use a modest 4–6 pt paragraph-after gap after the final bullet or line of an entry. This distinguishes roles/subsections without creating a blank-line rhythm.
- **Between sections:** place the separation before a new section heading: normally 8–10 pt before the heading and 3–4 pt after it. Do not add both blank paragraphs and paragraph spacing. Do not insert a blank line after every heading by default.
- **Name/contact block:** keep it compact and leave roughly 6–8 pt before the first section.

These values are a starting grid. Preserve visual hierarchy and legibility; change the grid only deliberately, consistently, and within the candidate's requested style. A creative, direct-viewing version may vary only after an ATS-safe companion is available.

## Reproducible visual systems

When the user does not supply a visual reference, choose one of the bundled original template specifications instead of improvising a new design:

- `assets/templates/ats-classic-resume.md`: the default for experienced professionals, managers, executives, and general business roles.
- `assets/templates/ats-compact-resume.md`: a denser alternative for technical candidates, extensive relevant experience, or a credible one-page fit.
- `assets/templates/matching-cover-letter.md`: a one-page letter using the same typography and alignment logic.

Treat these files as deterministic layout and content skeletons, not candidate-fact sources. Build the requested DOCX or PDF from the selected specification, replace every placeholder, and remove unused sections. Never invent facts to fill the layout.

If an asset cannot be used directly, reproduce its named style system:

| Token | Classic | Compact |
| --- | --- | --- |
| Typeface | Arial | Arial |
| Margins | 0.72 in | 0.65 in |
| Name | 18 pt bold, left aligned | 17 pt bold, left aligned |
| Headline/contact | 10.5/9.5 pt | 10/9 pt |
| Section heading | 10.5 pt bold, uppercase | 10 pt bold, uppercase |
| Role/body | 10.5 pt | 10 pt |
| Line spacing | 1.03 | 1.00 |
| Section spacing | 9 pt before, 3 pt after | 8 pt before, 2 pt after |
| Entry spacing | 5 pt after final bullet | 4 pt after final bullet |
| Bullet indent | 0.18 in hanging | 0.17 in hanging |

Use no more than four visible hierarchy levels: name, section heading, role header, and body/secondary text. Use bold for names, section headings, and employers; reserve italics for role titles. Keep all essential text black. Visual polish comes from hierarchy, alignment, and spacing, not decorative rules, icons, shaded panels, or graphics.

Use a consistent role header throughout the document. Default to employer in bold and location in regular text on the first line; use an italic role title and regular dates on the second, with dates aligned to a right tab stop. If a narrower layout causes collisions, move dates inline consistently rather than allowing detached or wrapped date fragments.

### Role-record integrity

For every experience entry selected for inclusion, reconcile the final document against the source record as a four-part tuple: **employer, title, location or work arrangement, and dates**. Preserve a supplied city/state, country, `Remote`, `Hybrid`, or other work-arrangement label; normalize punctuation or abbreviations only when meaning is unchanged. If the source does not establish the location, flag it for confirmation rather than inventing or silently dropping it. After generation, verify every included role tuple in the extracted final text and confirm that each location remains attached to the correct employer/title and dates.

## Page-count decision

Page count follows evidence, not a slogan.

1. Remove repetition, low-relevance detail, blank spacer paragraphs, excessive paragraph spacing, and unintended keep-together settings.
2. Test the Classic layout. If the content nearly fits one page, test Compact without going below its type and margin tokens.
3. Use one page only when all supported high-value evidence remains readable and the hierarchy still breathes. Do not silently remove meaningful content to reach one page.
4. Use two pages when relevant seniority, specialization, or evidence exceeds the readable one-page budget. Put the strongest, most recent case on page one and rebalance at a logical role or section boundary.
5. Treat a last page that is less than roughly half occupied as a review trigger, not an automatic failure. Recheck relevance, repetition, spacing, and section placement. Keep the shorter last page only when the remaining evidence is important and further compression would reduce clarity or truthfulness; explain that tradeoff to the user.

Do not claim that a universal occupancy percentage is an industry standard. The release question is whether the page space is justified by relevant evidence and whether the document looks intentional at normal viewing size.

## Whitespace and page economy

Whitespace should separate ideas, not compensate for missing layout rules.

- Use paragraph spacing, styles, and indents—never blank spacer paragraphs, repeated soft returns, or text color tricks—to control vertical space.
- Do not use manual page breaks to start routine sections or entries. Keep a heading with the first line that follows it, but do not keep an entire multi-bullet role together when that would create a large gap.
- Do not create a second page merely to satisfy a two-page target. A resume may be one or two pages when the evidence warrants it; an academic CV may be longer.
- If a page is blank or visibly half-empty because of forced breaks, spacer paragraphs, oversize styles, or keep-together settings, correct the layout and re-render. First remove layout waste and repetition; do not hide the problem by shrinking body text below 10 pt, crushing margins, inventing filler, or dropping supported content without telling the user.
- A genuinely short final section may remain short when its content is appropriate. Flag a constrained layout choice rather than fabricating content or pretending the page balance is ideal.

## Assigned-folder workspace

When the user assigns a folder for iterative document work, keep task-created artifacts in one job-specific workspace with these purposes:

```text
source/        untouched copies or references when a new source area is needed
working/       one canonical current editable draft per requested deliverable
qa/            current renders, extracted text, and validation notes
deliverables/  final editable/PDF pair for each requested deliverable only
```

Do not move, rename, overwrite, or delete pre-existing user files merely to impose this structure. If the assigned folder already contains source material, leave it in place and treat it as read-only input. Use stable filenames for each canonical draft and its QA outputs; create a new version only for a materially distinct target or user-requested milestone, not every edit. At completion, remove or consolidate only named QA or temporary outputs created during the current task. Treat user-edited files, requested milestones, and anything the user asked to retain as user-owned; never delete them as cleanup. Keep each final pair easy to identify.

## Editable file and PDF companion

When delivering an editable paginated career document such as DOCX or ODT, also create a PDF from that same final editable source unless the user explicitly opts out. Generate the PDF only after content and layout edits are complete so it cannot lag behind the editable file. Verify both final files for readable rendering, page count, required content, and logical text order. If conversion is unavailable or fails, deliver the verified editable file, explain the limitation plainly, and do not claim that a matching PDF was produced. A text-only or Markdown response does not trigger file creation.

## Required document release gate

For every downloadable paginated career document:

1. Create the document with named styles or an equivalent consistent style system.
2. For a resume/CV, reconcile every included employer/title/location-or-work-arrangement/date tuple against the source before judging layout.
3. Render the final editable document to page images using the applicable document workflow.
4. Inspect **every page**, not just the first, for blank/near-blank pages, large accidental gaps, orphaned headings, isolated bullets, clipped text, overlap, and inconsistent spacing.
5. Iterate and render again until the layout is clean.
6. When an editable file is being delivered, create its PDF companion from that final source unless the user opted out or conversion failed as described above; when a PDF exists, render or inspect it rather than assuming conversion preserved the layout.
7. Extract text from each final file and inspect the actual sequence rather than relying only on a mental check. For resumes/CVs, confirm, in order, the name, contact details, headline/profile, section headings, and every employer/title/location-or-work-arrangement/date tuple, followed by its bullets, skills, education, and credentials. For letters and other documents, confirm that sender, recipient, date, salutation, body, close, and any other required elements appear in logical reading order. Every date and location must remain associated with the correct item; essential text must not be missing, duplicated, or reordered; and hyperlinks must retain visible descriptive text.
8. Compare the extracted text with the rendered pages and, for paired files, compare the editable and PDF outputs with each other. A visually polished file that fails reading order or a stale/mismatched PDF is not releasable.
9. For an ATS-targeted resume, run a structured-field preflight: every included role has one unambiguous employer, canonical title, location/work arrangement, start date, and end date or current-role marker; Education states institution, field, credential/degree type when known, and completion/status; and the Skills section uses explicit, supported terms rather than relying on category labels. Flag compound-title and incomplete-education fields that may still require manual application-form review. A live parser check, when available and authorized, is evidence about that parser—not a universal ATS guarantee.

In the Resplendence Report Card, rate ATS & format integrity from the inspected output. A file that has not passed the visual gate cannot receive a 10.0 in that criterion.

## Visual inspection checklist

- Name is the strongest element; sections, roles, and body text have an unmistakable hierarchy.
- Employer/title/location-or-work-arrangement/date composition is consistent across entries, and every tuple matches the source.
- Compound titles or title progressions have been resolved into parser-safe supported records, or their truncation risk is disclosed.
- Education includes truthful credential/status detail, with unknown form-required fields explicitly flagged rather than guessed.
- Right-tabbed dates do not collide, wrap alone, or detach from their role.
- Bullet and hanging indents are consistent.
- No heading is orphaned; no bullet is stranded without clear role context.
- No clipped text, overlap, missing glyph, unexpected font substitution, blank page, or layout-generated gap remains.
- Page one presents the target and strongest evidence quickly.
- A second page, when used, contains substantive relevant evidence and looks intentional.
- No accomplishment or skill is repeated merely to fill visual space.
