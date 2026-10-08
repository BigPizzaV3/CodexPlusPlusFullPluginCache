---
name: ilovepdf-pdf-to-jpg
description: |
  Convert PDF pages to JPEG images, or extract embedded images from a PDF.
  Use this skill whenever the user wants to turn a PDF into images, screenshot PDF pages,
  or extract images that are embedded inside a PDF.
---

# iLovePDF — PDF to JPG

Converts a PDF to JPEG images. Can produce one image per page, or extract images
that are embedded within the PDF's content.

## When to Use

- "Convert this PDF to images"
- "Turn each page of this PDF into a JPG"
- "Extract the images from this PDF"
- "Convert PDF to JPG in high quality"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "pdf-to-jpg"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

`.pdf`

## Options

| Option        | Type   | Values              | Default      |
| ------------- | ------ | ------------------- | ------------ |
| `pdfjpg_mode` | string | `"pages"`, `"extract"` | `"pages"` |
| `quality`     | string | `"Normal"`, `"High"`   | iLovePDF default |

### Mode

- **`pages`** — Renders each PDF page as a separate JPEG image. Use for "convert to images".
- **`extract`** — Extracts images embedded within the PDF content. Use for "extract images from PDF".

### Quality

- **`Normal`** — 150 dpi output.
- **`High`** — 300 dpi output, larger files.

Only pass `quality` if the user explicitly mentioned quality or resolution.

## Example Calls

```json
// Convert each page to JPG (default)
{ "tool": "pdf-to-jpg", "options": { "pdfjpg_mode": "pages" } }

// High quality page conversion
{ "tool": "pdf-to-jpg", "options": { "pdfjpg_mode": "pages", "quality": "High" } }

// Extract embedded images
{ "tool": "pdf-to-jpg", "options": { "pdfjpg_mode": "extract" } }
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- `quality` only applies to `pdfjpg_mode: "pages"`. It has no effect in extract mode.
