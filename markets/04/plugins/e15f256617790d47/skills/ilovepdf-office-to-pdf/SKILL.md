---
name: ilovepdf-office-to-pdf
description: |
  Convert Microsoft Office documents (Word, Excel, PowerPoint) to PDF.
  Use this skill whenever the user wants to turn a .doc, .docx, .xls, .xlsx,
  .ppt, or .pptx file into a PDF.
---

# iLovePDF — Office to PDF

Converts Microsoft Office documents to PDF format. Supports Word, Excel, and
PowerPoint files.

## When to Use

- "Convert this Word document to PDF"
- "Turn this Excel spreadsheet into a PDF"
- "Export this PowerPoint as PDF"
- "Convert my .docx to PDF"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "office-to-pdf"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

| Format      | Extensions           |
| ----------- | -------------------- |
| Word        | `.doc`, `.docx`      |
| Excel       | `.xls`, `.xlsx`      |
| PowerPoint  | `.ppt`, `.pptx`      |

## Options

No configurable options. The conversion uses iLovePDF defaults.

## Example Calls

```json
// Convert an attached Word document to PDF
{ "tool": "office-to-pdf", "options": {} }
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- If the user provides a file type that is not in the accepted list (e.g., `.odt`),
  inform them that only the formats listed above are supported.
