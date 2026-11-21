---
name: reducto-office
description: Edit Word (.docx), PowerPoint (.pptx) and Excel (.xlsx) files in Reducto Office, a live editor the user watches and types into. Use when the user wants to write, revise, redline or format a document, build or change a slide deck, or fill or format a spreadsheet, or opens or attaches one of these files.
---

# Reducto Office

Reducto Office shows a live Word document, PowerPoint deck or Excel workbook in the conversation. Your edits appear while the user watches, and the user can type in the same file.

## Start

- A file the user opens with Open in → Reducto Office arrives through `open_document`. The editor shares its `fileId` once it loads; use that, and do not call `open_editor` for it.
- A .docx, .doc, .pdf, .pptx or .xlsx the user attached in ChatGPT: call `open_editor` with `file` set to the attachment. A .doc or .pdf becomes a Word document; check a converted PDF's layout before you edit.
- For a new file, call `open_editor` with `kind`: `docx` (the default), `pptx` or `xlsx`. It shows a blank file. A blank deck has no slides yet.
- To show a file from a link (`…/d/<id>`) or `list_files`, call `open_editor` with `fileId`.
- Show each file once. The editor shows every `exec` live, and each `open_editor` call opens another copy of it. Do not open the file's links in a browser.
- To show the user their files or the Reducto Office home, call `open_home`. Never open office.reducto.ai in a browser: the user is not signed in there.
- `list_files` lists the user's files for you.
- A local file (Codex CLI): call `create_file`, upload the file with `curl -sfT <path> '<uploadUrl>'`, then call `open_editor` with its `fileId`.

## Save to disk

With a shell: the open result has a download link. Run its `curl` command to write the current file over the local one. The link expires in 15 minutes; `open` with `fileId` returns a new one without another editor. Never look for tokens or credentials.

Without a shell (ChatGPT, Claude): tell the user to use Export in the editor.

## Edit

1. Call `read_guide` with the file's `kind` once before the first `exec`. It has the API and recipes for that kind.
2. Call `exec` with `fileId`, `agent` (your name, for example "chatgpt"), `intent` (a few words the user sees) and `code` (JavaScript against the live file).
3. `code` gets `doc` for Word, `presentation` for PowerPoint and `workbook` for Excel. They follow the Office.js object model without `run`, `sync` or `load`.
4. Read before you write: `readPage()` or `text()` in Word, `renderPage(n)` for a slide, `renderRange(sheet, range)` for cells.
5. Make small edits in each call. The user sees each change as it lands.

## Rules

- If a result starts with "Note:", someone else changed the file. Read it again before you edit content you saw earlier.
- Use tracked changes when the user asks for a redline or review of a Word document.
- Do not paste the file back into the conversation. The user sees it in the editor.
- The editor tells you where the user is: in Word, the caret's line or the selected text; in a deck, the slide and the selected shape ids; in a workbook, the sheet, range and active cell, with the cell values. "This", "here" and "these cells" mean that place. Use the ids and addresses it gives you in exec.
