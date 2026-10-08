---
name: ilovepdf-merge-pdf
description: |
  Combine multiple PDF files into a single PDF.
  Use this skill whenever the user wants to join, merge, combine, or concatenate
  two or more PDF files into one document.
---

# iLovePDF — Merge PDF

Combines multiple PDF files into a single document, preserving the order in which
files are provided.

## When to Use

- "Merge these PDFs"
- "Combine these two files into one"
- "Join my PDF attachments"
- "Concatenate these PDFs in order"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "merge-pdf"`.

Use `ilovepdf_attach` when the user has attached files to the chat message.
Use `ilovepdf` when the user provides file URLs.

**Requires at least 2 PDF files.** If only one file is provided, ask the user for the
additional file(s) before calling the tool.

## Accepted File Types

`.pdf` (all files must be PDFs)

## Options

No configurable options. Files are merged in the order they are provided.

## Example Calls

```json
// User attaches two PDFs and asks to merge them
{
  "tool": "merge-pdf",
  "options": {}
}
```

## Notes

- Preserve the attachment order when passing files — the user's stated order is respected.
- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- Do not ask the user for merge settings before calling the tool; there are no options
  to configure.
