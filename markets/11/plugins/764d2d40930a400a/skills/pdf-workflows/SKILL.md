---
name: pdf-workflows
description: Plan and guide PDF editing, splitting, and merging workflows in the Private PDF browser app by Dayfiles, including page ranges, file order, scanned-text limitations, and output review.
---

# Private PDF workflows

Help the user turn their requested PDF change into a precise plan and carry it out in Private PDF at https://dayfiles.com/. This package includes three MCP entry tools: `open_edit_workspace`, `open_split_workspace`, and `open_merge_workspace`. Invoke the matching tool when the user wants to perform that task. The tool opens a browser-local workspace; it does not process documents on the server or accept chat attachments. Never put filenames, file IDs, page ranges, document text, or passwords in tool arguments; all three tools take an empty object. The user selects files and enters processing settings directly inside the workspace. If the host cannot render the workspace or save a download, use the browser fallback URL from the tool result. If browser control is available and authorized, assist through its normal interface. A tool result only establishes that the workspace opened, never that a PDF operation succeeded.

Normal PDF processing in the web app happens on the user's device. Prefer selecting files directly in the app; do not request a chat attachment just to explain a workflow. Chat attachments, text, and screenshots shared with the assistant are subject to the host's data practices; do not promise that assistant access remains local. Do not send document data to analytics, support forms, or external processing services. Keep document data out of link query strings. Do not change consent preferences as part of a PDF operation.

## Split PDF

Use https://dayfiles.com/split-pdf/. Work with one PDF and explicit inclusive page ranges, using page positions starting at 1 rather than printed page labels. Ask for missing page boundaries when they affect the result. When the total is known, reject zero, negative, descending, or out-of-bounds ranges. Flag overlaps or omitted pages and let the user decide whether they are intentional.

Provide the range plan, expected file count, and page count per output. For a 12-page input split into 1-4, 5-8, 9-12, expect three four-page PDFs. In the app, select the PDF, configure the planned ranges, review the preview, run the operation, and download the result. Multiple outputs may be offered in a ZIP. Do not suggest split-by-file-size as an available operation.

## Merge PDF

Use https://dayfiles.com/merge-pdf/. Establish the input order; use labels such as A, B, C when filenames are unnecessary. Do not infer alphabetical or chronological order unless requested. The tool requires at least two PDFs. If the user wants selected pages only, first prepare those page selections using the split workflow, then merge the resulting files.

Provide an ordered input list and, when counts are known, the expected total pages. Select the PDFs in the app, review and adjust the file queue, run Merge, and download the new document. Preserve the originals. Verify the output's page count and the transitions between input documents before claiming success.

## Edit PDF

Use https://dayfiles.com/edit-pdf/. Distinguish changing existing text, adding text, and changing scanned text. Existing text can be edited in the dedicated workspace. Pages without usable text require local OCR recognition and manual correction. Recognition supports printed English; handwriting, poor scans, and other languages have no accuracy guarantee. Do not promise exact font or layout preservation. When the app reports font substitution or another limitation, relay it before export.

Select the PDF directly in the browser, locate the target page, make the requested edits, inspect the preview, and export a new PDF. A saved draft is not an exported document. Treat whiteout as visual covering, not verified redaction. Do not claim visual signatures are cryptographic signatures. For sensitive-content removal, clarify that the editing workflow alone does not establish removal of underlying data.

## Completion and failures

State whether you delivered a plan, guided an operation, or verified an exported result. A tool link or a successful click does not establish success. When available, reopen the downloaded PDF and verify expected page count/order plus the edited areas. Without access to the output, say validation remains with the user. On malformed or encrypted input, cancellation, browser failure, or unsupported editing, retain the original and explain the specific next step. Never bypass a document password or overwrite the original as a recovery tactic.
