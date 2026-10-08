# Document Copy/Edit/QA Checklist

## Before writing

- Resolve every unique source once; ignore duplicate URLs.
- Keep title, ID/path, parent folder, modified time, and revision only when each field is necessary for the current operation; retain them only in transient task state.
- Confirm that the source is readable and that a copy can be created.
- Inspect all tabs or sections and count pages/slides/sheets, tables, lists, and other repeated structures.
- Note protected controls, comments, suggestions, hidden content, formulas, links, and embedded media.
- Create the working copy in the same logical folder unless the user specifies another location.
- Confirm the copy's title and a user-usable reference before editing; do not echo raw private IDs, signed parameters, or unnecessary user-directory segments.

## Minimal-change checks

- Modify only the named property or content.
- Preserve text when changing formatting.
- Preserve formatting when changing text unless reflow is unavoidable.
- Preserve formulas, data validation, merged cells, dimensions, filters, frozen panes, and charts in spreadsheets.
- Preserve masters, layouts, speaker notes, animation intent, and object order in presentations.
- Preserve sections, headers, footers, footnotes, citations, tables, and list nesting in documents.
- Preserve Korean Unicode text exactly; do not normalize or re-encode without a demonstrated need.

## Verification

- Re-fetch the saved artifact after the write.
- Compare source and copy structure counts.
- Search for Unicode replacement characters (`U+FFFD`), private-use glyph leakage, or unexpected missing text.
- Export to PDF or another stable preview format.
- Render and inspect every page or slide at readable resolution.
- Check clipping, overflow, overlaps, orphan headings, blank trailing pages, changed line breaks, and table splits.
- For spreadsheets, inspect formulas and representative cells directly in addition to any PDF preview.
- Repeat export/render after every corrective edit.

## Handoff

- Provide an authorized, user-usable reference or descriptive label for the untouched original.
- Provide an authorized, user-usable reference or descriptive label for the edited copy.
- State the exact requested change.
- State the checks that passed.
- Call out any format limitation or item that could not be proven.
