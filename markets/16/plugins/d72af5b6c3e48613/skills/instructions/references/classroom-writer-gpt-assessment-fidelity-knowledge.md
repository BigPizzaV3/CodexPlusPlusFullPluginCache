Current owner correction (11 October 2026): Classroom Writer has GeoGebra, not a separate Functions App. Do not offer the legacy functions specialist tool, functionSetup or explore-function action. Prepare interactive function investigations in GeoGebra using geoGebraCommands or a teacher-approved geoGebraResource. This correction supersedes older catalogues and prior conversation claims.

# Classroom Writer source-assessment fidelity policy

## Purpose and authority

Use this policy whenever a teacher uploads a PDF, Word document, answer key, rubric, worksheet, examination paper, or related source and asks for a Classroom Writer resource.

This file supplements the plugin's main instructions. The main Instructions still control tone, approval, security, and use of the official `create_classroom_writer_assessment_file` MCP tool. This policy controls source analysis, fidelity, tables, visuals, answer keys, graph and labelling tasks, compression, and quality checks.

The governing rule is:

> Preserve everything students need to understand and answer the original task. Never silently omit, flatten, invent, or claim support for an essential element.

## Current platform capability boundary

Before planning, call get_classroom_writer_capabilities and use its live catalogue together with the current create_classroom_writer_assessment_file schema. Older unsupported-feature statements in this resource are historical, not a reason to downgrade currently supported fields.

The catalogue read on 2026-10-11 supports questions, native tables, graph, diagram, drawing and labelling responses, permitted public raster image URLs, specialist tools and controlled parameter simulations through supported fields. Use only the actual tool schema; the catalogue does not authorise invented fields. Uploaded assets without a supported transport, page layout and arbitrary executable content must not be assumed supported.

Music Studio, Portfolio Hub and Javalab/Simulation Bank require teacher setup. Describe exact manual steps before approval; do not invent blocks or claim they are configured. Keep expectedAnswer, markingNotes and answerGraph private. Preserve safe supported LaTeX.

If an essential element cannot be represented faithfully by the current supported fields, document an exact manual placeholder or a teacher-approved adaptation. Preserve every source-fidelity check below.

### Absolute prohibition: no text-art replacements

Never recreate an uploaded image, diagram, table, chart, graph, map, labelled figure, or response surface as:

- ASCII art or Unicode box-drawing characters;
- a Markdown code fence;
- pipes, underscores, brackets, repeated letters, or spacing intended to look like a picture;
- a written list positioned to imitate labels, arrows, axes, cells, or anatomical structures;
- a "simplified diagram" invented from the assistant's memory.

Text art is not a visual asset and is not a faithful or accessible substitute. It may change relationships, remove labels, corrupt formatting, and become unusable on different screen sizes.

If the original visual cannot be inserted through an official supported field, stop and show this status before approval:

> **Manual visual required:** The original [name of visual] from [file and page] must be added in Classroom Writer. The current MCP tool cannot embed it. It has not been replaced or recreated.

The final MCP tool blueprint may contain the surrounding question wording, but it must not contain a fake diagram or claim that the visual is present.

If the MCP tool later exposes a supported image, table, graph, canvas, annotation, or layout field, use that official field and the fidelity rules below. Never invent fields or submit unsupported properties.

## Mandatory source-analysis workflow

### 1. Assign each upload a role

Identify each file as one of:

- student assessment or worksheet;
- teacher answer key or worked solution;
- rubric, criteria, or mark scheme;
- source booklet, data sheet, formula sheet, or supplementary material;
- duplicate or alternate version.

Never place teacher answers from an answer key into student-visible content.

### 2. Inspect the complete files, not only extracted text

For every page, inspect both the text and the rendered page. Text extraction alone does not reliably preserve tables, merged cells, blank response areas, labels, diagrams, graph axes, colour coding, page order, or the relationship between a question and its visual.

When both student and answer-key versions are supplied, compare them page by page and question by question.

### 3. Build an internal source inventory

Before drafting, record:

- file role, page count, title, subject, grade/age, language, assessment type, duration, and total marks;
- all sections, questions, subquestions, original numbering, marks, criteria, and command terms;
- every table, image, diagram, chart, map, graph, equation, formula, data set, label area, and source extract;
- which cells, labels, axes, regions, or diagram parts are already completed and which are student response spaces;
- expected response mode: text, choice, table entry, calculation, graph, drawing, annotation, upload, or mixed;
- the matching answer, worked solution, marking guidance, rubric strand, and marks for every marked item;
- any discrepancy between the student paper and answer key.

Use stable internal references such as `Student PDF p3, Table 1` and `Answer key p3, Q1` while comparing. Do not expose unnecessary technical notes to the teacher.

### 4. Classify every visual element

Classify each visual or table as:

- **answer-essential**: students cannot answer correctly without it;
- **response-essential**: it is the place where students must enter, draw, plot, shade, or label an answer;
- **supporting**: useful evidence or context but not the response surface;
- **decorative**: safe to omit without changing meaning.

Answer-essential and response-essential elements must never disappear. Decorative elements may be omitted to reduce size. Supporting elements may be simplified only with teacher approval.

### 5. Prepare a fidelity plan before building

Show the teacher a compact plan containing:

- source files and their roles;
- page, section, question, and total-mark counts;
- a list of tables and visuals, with the proposed handling of each;
- every unsupported or uncertain element;
- the proposed answer-space type and size for each question;
- what will be included in the teacher answer key;
- any approved change from the original.

Ask only about genuine choices. If an essential table or image is clearly required, recommend including it; do not ask whether it may be silently omitted.

## Fidelity rules

### Wording, order, numbering, marks, and criteria

- Preserve the original section and question order unless the teacher asks for restructuring.
- Preserve question and subquestion numbering exactly where practical.
- Preserve command terms, mathematical symbols, units, data values, marks, criteria, and referenced source labels.
- Do not paraphrase assessable wording merely to make it shorter.
- Correct an obvious typo only after identifying it to the teacher when the change could affect meaning or an answer.
- Recalculate question-mark totals and compare them with the stated total.

### Native text and equations

- Use native text for readable source text. Do not turn whole pages into screenshots.
- Use native mathematical notation or supported equation fields for formulas and symbols.
- Preserve superscripts, subscripts, fractions, roots, inequalities, vectors, units, and significant notation.
- Use an image only when a visual arrangement cannot be represented faithfully by supported native components.

### Tables

When an official native table field is available:

- recreate data-entry and response tables as native editable tables;
- preserve row and column order, headers, merged-header meaning, units, given values, blank response cells, and row/column labels;
- distinguish locked display cells from student response cells;
- retain colour only when it encodes meaning; otherwise use accessible borders and headings;
- split an extremely wide table only when the relationship remains clear and the teacher approves.

Do not convert a meaningful table into prose. Do not use one large text box when students are expected to answer specific cells.

If the current MCP schema cannot faithfully represent a particular source table, For a table-dependent task, choose one of these outcomes and state it explicitly:

1. prepare the surrounding questions and mark the table for manual addition in Classroom Writer;
2. use a teacher-approved text-response substitute when the table is not central to the assessed skill;
3. postpone final file creation until the supported table component is available.

### Images, diagrams, maps, charts, and source figures

When an official supported visual field is available:

- use the exact supplied visual or a clean crop from the original source;
- crop surrounding page whitespace, headers, footers, and unrelated content;
- preserve every label, legend, scale, axis, arrow, symbol, colour key, and data value needed to answer;
- do not redraw, beautify, or replace an answer-essential visual unless the teacher explicitly approves the change;
- place the visual next to the question or source text that references it;
- add concise alternative text that describes the informational content without revealing the answer;
- never include answer-key annotations in the student version.

If an exact source visual cannot be supplied through a permitted supported image field, Describe the exact missing visual and where the teacher must add it manually. Never pretend it was embedded, and never replace it with ASCII art, a code block, boxes, arrows, repeated letters, or an invented simplified figure.

### Graphing, drawing, and labelling tasks

If a question asks students to plot, sketch, shade, draw, annotate, label, connect, or identify a region, keep that response mode. A long-text box is not an equivalent replacement unless the teacher approves a changed assessment objective.

When official supported tools exist:

- use a graph or function canvas for plotting and graph construction;
- preserve axis names, units, scale, origin, range, interval, grid, supplied points, curves, and restrictions;
- use a science/drawing canvas for diagrams and sketches;
- use the supplied image as a locked background for labelling or annotation, leaving student labels or marks editable;
- reproduce the completed teacher graph, diagram, or labels only in the answer key.

If the current schema cannot preserve a required graphing, drawing or labelling response, Flag them as manual-completion requirements or obtain explicit approval for a substitute. Do not automatically turn them into prose questions or text-art diagrams.

### Answer key and marking guidance

- Create exactly one answer-key entry for every marked question or subquestion.
- Keep expected answers and marking notes outside student-visible content.
- Preserve acceptable alternatives, required working, units, accuracy, method marks, follow-through rules, criteria, and partial-credit guidance when supplied.
- For a table answer, preserve the completed table structure in the teacher version when supported.
- For a graph, drawing, or labelling answer, preserve the completed visual in the teacher version when supported.
- If the source answer key appears wrong or contradicts the student paper, identify the conflict; do not silently choose or invent an answer.

## Visual resizing and file-size control

Apply these rules only through an official supported asset field or through a manual asset prepared for the teacher. They do not authorise unsupported asset transports or fields.

### Preparation order

1. Crop first: remove page margins and unrelated content.
2. Remove duplicates and decorative images.
3. Resize while preserving aspect ratio.
4. Choose the format by content type.
5. Compress adaptively and inspect legibility.

### Recommended limits

- Maximum long edge: **1400 pixels**. This matches Classroom Writer's current student-image resizing limit.
- Photographs or continuous-tone artwork: JPEG at approximately **74% quality**, or an officially supported equivalent.
- Line art, graphs, tables, diagrams, screenshots, and text-heavy visuals: PNG or lossless WebP when available; reduce dimensions before applying lossy compression.
- Prefer one tightly cropped asset over a full-page raster image.
- Aim for the smallest file that keeps all text, labels, thin lines, decimal points, mathematical symbols, and colour distinctions readable at normal assessment zoom.
- Inspect the final resized asset visually. If a label or cell value is difficult to read, increase resolution or split the visual into logically labelled parts.

Do not enlarge a small original. Do not repeatedly recompress the same asset. Do not duplicate one image in multiple places if an official reusable reference is supported.

Importer limits and asset support must be checked against the current catalogue and MCP schema; do not treat historical importer restrictions as current MCP restrictions. Never bypass these limits with base64, HTML, external links, invented fields, or renamed files.

## Build decision

Assign one status before seeking final approval:

- **Faithful and supported**: every essential element and response mode is supported.
- **Faithful after manual completion**: text, questions, answers, marks, and settings can be built, but listed visuals/tables/tools must be added by the teacher in Classroom Writer.
- **Teacher-approved adaptation**: the teacher explicitly approved identified substitutions that change presentation but not the assessed objective.
- **Not faithfully convertible yet**: an unsupported element is central to the assessed objective and no acceptable substitute was approved.

Only describe the result as a faithful conversion when the status is **Faithful and supported** or when all named manual-completion steps have actually been completed outside the MCP tool.

## Final pre-compilation review

Before asking for approval, verify and show:

- source page count and source roles;
- section, question, subquestion, and total-mark counts;
- original-to-Classroom-Writer question mapping;
- table and visual inventory with a status for every item;
- all graph, drawing, labelling, calculation, and table-entry response modes;
- answer-key coverage for every marked item;
- settings, tools, calculator rule, timing, word count, and student supports;
- all deviations, omissions, substitutions, and manual-completion steps.

The teacher's approval must cover material substitutions and omissions. General approval does not erase a previously undisclosed loss of essential content.

## Post-build quality statement

After the MCP tool returns a downloadable file, state only what is known from the approved blueprint and the MCP tool result. Because the protected `.cwriter` package must not be decoded or inspected, do not claim that unsupported elements were embedded or that the protected output was visually compared with the original.

Recommend that the teacher import the file into Classroom Writer and complete this final check:

- every question and mark is present;
- every required table and visual is present and readable;
- student and answer-key content are separated;
- graph, drawing, labelling, and table response areas work as intended;
- PDF preview has acceptable page breaks and answer-space sizes;
- saving, refreshing, submission, teacher review, and downloads work.

## Example: a table-heavy mathematical investigation

For an assessment such as a locker investigation containing factor-entry tables, a 10-by-10 locker-status matrix, a hallway image, rubric descriptors, and a completed 18-by-18 answer matrix:

- identify each table and matrix individually rather than calling them generic "source material";
- keep factor-entry cells as structured student responses when supported;
- preserve supplied cells and leave only intended student cells editable;
- keep the hallway image if the teacher wants the original context, but mark it decorative if it is not required to solve the task;
- do not place completed red answer values in student content;
- preserve the completed matrices and mathematical justification in the teacher answer key;
- if a particular table, matrix or image is unsupported, mark that element for manual addition instead of silently replacing them with text boxes;
- do not call that protected MCP tool output a true visual copy until those elements have been added and checked in Classroom Writer.

## Compact response pattern for teachers

Use this structure rather than a long technical explanation:

**Source check** — files, roles, pages, questions, marks.

**Tables and visuals** — each item, whether essential, and proposed handling.

**Classroom Writer build** — sections, response types, answer spaces, settings, and answer key.

**Manual steps or adaptations** — unsupported items and exact substitute, if any.

**Approval** — ask the teacher to approve the complete reviewed plan before calling the MCP tool.
