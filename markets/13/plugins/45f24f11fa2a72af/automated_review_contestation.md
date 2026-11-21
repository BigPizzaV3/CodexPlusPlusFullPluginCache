# Automated Review Contestation

## exec

exec is a document-editing API, not a general way to run code. It doesn't hide a separate set of operations. It runs short JavaScript against one Word, PowerPoint or Excel file, the same kind of thing as a code-interpreter tool.

- It can't be split into separate tools. The operations are the Office document model: about 5,100 methods and properties across 416 classes (paragraphs, runs, tables, cells, styles, shapes, charts, ranges, formulas). One real edit chains many of them, e.g. find a table, change a cell, restyle a row. Exposing each as its own tool would mean thousands of tools, or a small subset that can't do most edits.
- It's scoped and sandboxed:
  - It acts only on the file named by `fileId`, and only if the signed-in user can edit that file. Otherwise it's refused.
  - The code runs in an isolated sandbox with no network, no `fetch`, no `process`/`require`, and no host access.
  - Memory and time are capped, and calls are rate-limited per user.
  - `bash` and `fs` are an in-memory virtual shell over that file's own assets, not a real machine.
- The user sees and controls it. Every exec is shown live in the editor in the conversation. Each one has a short `intent` label naming the change. Every version is saved and can be restored.
- It's honestly annotated: readOnlyHint=false, destructiveHint=true, openWorldHint=false.

## read_guide

read_guide runs nothing. It returns fixed Markdown docs for exec (how it works, plus the API reference for the file type). It takes no file, reads no user data and has no side effects (readOnlyHint=true). I think it got flagged only because it documents exec.
