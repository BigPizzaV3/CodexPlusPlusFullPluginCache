---
name: resource-editing
description: Read and change a teacher's existing Planit lesson, worksheet, homework or saved classroom-tool output, then export an actual permitted PDF, PowerPoint or Word file.
---

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.

Use these workflows only for anonymous or synthetic teaching content. Do not
read an existing resource of uncertain privacy merely to check or sanitise it.
If it may contain pupil identities, scripts or individual answers/results,
return its native link and hand it to the adult without browser readback.
The public API omits known child-personalised worksheets from lists and refuses
their read, AI edit and PDF export, including lesson-linked native worksheet
files. Accept that native handoff. Do not try another format, a lesson output,
another connector or the browser to retrieve the refused content. Anonymous
teaching worksheets and teacher answer keys remain supported.

Identify the existing resource using its URL/id or `list_my_lessons`,
`list_my_worksheets` or `list_saved_tools`. If several fit, ask which one.
Read it before changing it: `get_lesson_markdown`, `get_worksheet`, or
`get_saved_tool`. Keep the teacher's requested scope and language.

For AI changes, quote `ai_edit` with `quote_action`, then call `edit_lesson` or
`edit_worksheet` with precise instructions. Re-read the result to verify the
requested content changed; an editor response can contain action failures.
Don't silently spend more credits to repeat an uncertain edit. Check the
resource and explain any incomplete change.

For saved classroom tools, change the actual inputs in the retrieved snapshot.
Keep v:1, unchanged inputs and the seed. `update_saved_tool` replaces the
supplied snapshot; it does not merge fields. Use `duplicate_saved_tool` first
when the teacher wants a new version while keeping the original. Look up the
saved item's exact slug in `get_planit_catalog` and read its `detailTool`.
For execution:mcp, preview the saved inputs with that row's `previewTool`,
then download with its `exportTool` using the same inputs and seed. These are
individually exposed operations; select only names present in the connected
server tool list. Do not pass a tool selector or call a generic executor.
Only the generated public slug/input allowlist is accepted for saved snapshots.
Browser/private tool state and unsafe legacy snapshots are refused. Hand those
native steps to the adult without reading private contents or bypassing the
guard through another save, export or connector. Never claim an input update
already produced a download.

For another lesson output, quote the corresponding worksheet/homework or
presentation_regenerate action, then call `generate_lesson_output`. Read
the actual completion event: worksheet/homework generation returns
`worksheetId` or `homeworkId`. Use that owned document id with `get_worksheet`,
`edit_worksheet` and `export_worksheet` for PDF. Those documents may not appear
in `list_lesson_outputs`. For an existing lesson sheet, inspect
`list_my_worksheets` and `get_worksheet` for its stored `lessonId`; do not guess
a matching document. On a stream error or timeout, inspect the existing
outputs/documents before retrying. Creating another output uses credits.

For lesson presentation files, select a real supported output from
`list_lesson_outputs` and call `export_lesson` with its supported format.
Teacher support uses content_type: teacher_support and PDF or DOCX. Native
lesson PDF supports presentation/worksheet output; homework is a worksheet
document and uses `export_worksheet` with its actual id. Do not assume every
content type supports every format. The native endpoint enforces access and produces
the actual bytes. A successful result includes an embedded resource with a
MIME type, filename and blob; use the host's supported file/artifact handling
to make that returned file available, without dumping base64 into the chat.
If the host cannot expose an embedded file, give the native editor link and
state that its download control completes the download. Never invent a URL.

Classroom tool downloads require only a linked FREE account. PDF/CSV exports
use the catalogue row's individually listed `exportTool` when supported;
printing, copying, PNG and interactive
presentation use the native browser controls. Suggesting and applying changes
to free tool inputs uses no AI credits. Do not present upgrades or subscription
requirements for these tools.

An access denial is a real result: report it neutrally, with any returned reset
time. Offer a genuinely available preview/browser alternative when useful.
Do not promote upgrades, present subscription offers, sell tokens or credits,
link checkout pages, or automatically purchase anything.
