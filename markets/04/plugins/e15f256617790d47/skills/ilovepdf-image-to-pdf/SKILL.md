---
name: ilovepdf-image-to-pdf
description: |
  Convert JPG, PNG, or TIFF images into a PDF document.
  Use this skill whenever the user wants to turn one or more images into a PDF,
  create a PDF from photos, or combine images into a single PDF file.
---

# iLovePDF — Image to PDF

Converts one or more images (JPG, PNG, TIFF) into a PDF document. Multiple images
can be merged into a single PDF or kept as individual PDFs.

## When to Use

- "Convert this image to PDF"
- "Turn these photos into a PDF"
- "Create a PDF from my JPG files"
- "Combine these images into one PDF"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "image-to-pdf"`.

Use `ilovepdf_attach` when the user has attached files to the chat message.
Use `ilovepdf` when the user provides file URLs.

## Accepted File Types

`.jpg`, `.jpeg`, `.png`, `.tif`, `.tiff`

## Options

| Option        | Type    | Values                   | Default      |
| ------------- | ------- | ------------------------ | ------------ |
| `merge_after` | boolean | `true`, `false`          | `true`       |
| `orientation` | string  | `"portrait"`, `"landscape"` | `"portrait"` |
| `margin`      | number  | `0`–`100` (pixels)       | `0`          |
| `pagesize`    | string  | `"fit"`, `"A4"`, `"letter"` | `"fit"`  |

- **`merge_after: true`** — Combines all images into a single PDF (default).
- **`merge_after: false`** — Produces one PDF per image.
- **`pagesize: "fit"`** — Page dimensions match the image dimensions exactly.

Only pass options the user explicitly stated. The widget collects remaining preferences
in-card as a fallback.

## Example Calls

```json
// Convert a single JPG to PDF (defaults)
{ "tool": "image-to-pdf", "options": {} }

// Combine multiple images into one PDF, landscape, A4
{
  "tool": "image-to-pdf",
  "options": { "merge_after": true, "orientation": "landscape", "pagesize": "A4" }
}

// One PDF per image
{ "tool": "image-to-pdf", "options": { "merge_after": false } }
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- All options are collected by the widget if not provided — do not interrogate the user
  before calling the tool.
