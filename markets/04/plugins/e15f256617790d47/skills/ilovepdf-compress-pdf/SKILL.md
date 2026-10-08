---
name: ilovepdf-compress-pdf
description: |
  Compress PDF files to reduce their size while preserving quality.
  Use this skill whenever the user wants to make a PDF smaller, reduce file size,
  or optimize a PDF for sharing or uploading.
---

# iLovePDF — Compress PDF

Reduces PDF file size while preserving visual quality. Ideal for sharing via email,
uploading to platforms with size limits, or general storage optimization.

## When to Use

- "Compress this PDF"
- "Make this PDF smaller"
- "Reduce the file size of this PDF"
- "Optimize this PDF for email"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "compress-pdf"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

`.pdf`

## Options

| Option              | Type   | Values                              | Default         |
| ------------------- | ------ | ----------------------------------- | --------------- |
| `compression_level` | string | `"recommended"`, `"extreme"`, `"low"` | `"recommended"` |

- **recommended** — Best balance of size reduction and quality.
- **extreme** — Maximum compression; may reduce visual quality noticeably.
- **low** — Minimal compression; preserves quality with modest size reduction.

Only pass `compression_level` if the user explicitly stated a preference.
Default to `"recommended"` otherwise.

## Example Calls

```json
// User attaches a PDF and asks to compress it
{
  "tool": "compress-pdf",
  "options": { "compression_level": "recommended" }
}

// User asks for maximum compression
{
  "tool": "compress-pdf",
  "options": { "compression_level": "extreme" }
}
```

## Notes

- The widget handles the upload, processing, and download — do not attempt to
  process the file yourself or claim the operation is done before the widget confirms.
- Do not ask the user for compression options before calling the tool unless they
  volunteered a preference. The widget provides a fallback UI for those who want to adjust.
