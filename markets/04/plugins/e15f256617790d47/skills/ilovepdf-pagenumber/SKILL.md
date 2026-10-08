---
name: ilovepdf-pagenumber
description: |
  Add page numbers to a PDF document.
  Use this skill whenever the user wants to number the pages of a PDF, add a footer
  or header with page numbers, or customize how page numbers appear.
---

# iLovePDF — Add Page Numbers

Adds page numbers to a PDF. Supports full control over position, format, font,
color, and whether to skip the cover page.

## When to Use

- "Add page numbers to this PDF"
- "Number the pages starting from 2"
- "Add a footer with page numbers, skip the first page"
- "Put page numbers at the top right"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "pagenumber"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

`.pdf`

## Options

| Option                | Type    | Values / Format                             | Default          |
| --------------------- | ------- | ------------------------------------------- | ---------------- |
| `pages`               | string  | `"all"`, `"1-5"`, `"3-end"`, etc.          | `"all"`          |
| `starting_number`     | number  | First displayed number                      | `1`              |
| `text`                | string  | Format string — `{n}` = current, `{p}` = total | `"{n}"`      |
| `first_cover`         | boolean | `true` to skip numbering page 1             | `false`          |
| `vertical_position`   | string  | `"top"`, `"bottom"` only                    | `"bottom"`       |
| `horizontal_position` | string  | `"left"`, `"center"`, `"right"`             | `"center"`       |
| `font_family`         | string  | See list below                              | `"Arial Unicode MS"` |
| `font_size`           | number  | Point size                                  | `12`             |
| `font_color`          | string  | Hex color e.g. `"#000000"`                  | `"#000000"`      |
| `facing_pages`        | boolean | Book-style: odd right, even left            | `false`          |

### Format String Examples

| `text` value      | Output on page 3 of 10 |
| ----------------- | ---------------------- |
| `"{n}"`           | `3`                    |
| `"Page {n}"`      | `Page 3`               |
| `"{n} of {p}"`    | `3 of 10`              |
| `"- {n} -"`       | `- 3 -`                |

### Supported Font Families

`Arial`, `Arial Unicode MS`, `Verdana`, `Courier`, `Times New Roman`,
`Comic Sans MS`, `WenQuanYi Zen Hei`, `Lohit Marathi`

Similar font names are auto-matched (e.g. "Times" → "Times New Roman").

> ⚠️ `vertical_position` supports `"top"` and `"bottom"` only — `"middle"` is not
> supported by the iLovePDF API and will be substituted with `"bottom"`.

## Example Calls

```json
// Default page numbers at the bottom center
{ "tool": "pagenumber", "options": {} }

// Page numbers at top right, skip cover, format "Page N of P"
{
  "tool": "pagenumber",
  "options": {
    "vertical_position": "top",
    "horizontal_position": "right",
    "first_cover": true,
    "text": "Page {n} of {p}"
  }
}
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- Excluding only the last page in `pages` is not supported by the iLovePDF API.
- Only pass options the user explicitly stated; the widget collects remaining settings in-card.
