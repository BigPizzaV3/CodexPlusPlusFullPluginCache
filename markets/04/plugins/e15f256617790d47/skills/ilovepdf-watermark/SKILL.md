---
name: ilovepdf-watermark
description: |
  Add a text or image watermark to a PDF.
  Use this skill whenever the user wants to stamp, brand, or overlay text (e.g. "DRAFT",
  "CONFIDENTIAL") or an image onto a PDF document.
---

# iLovePDF — Add Watermark

Adds a text or image watermark to every page (or selected pages) of a PDF.
Supports full control over font, color, position, transparency, rotation, and tiling.

## When to Use

- "Add a DRAFT watermark to this PDF"
- "Stamp CONFIDENTIAL on every page"
- "Add our logo as a watermark"
- "Put a 50% transparent watermark centered on this PDF"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "watermark"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

`.pdf` (target document)  
For image watermarks: also provide a `.jpg` or `.png` as the watermark overlay.

## ⚠️ Important: Collect Watermark Text Before Calling

For **text mode**, always ask the user for the watermark text in chat **before** calling
the tool. Do not call the tool without it.

## Options

| Option                | Type    | Values / Format                           | Default      |
| --------------------- | ------- | ----------------------------------------- | ------------ |
| `mode`                | string  | `"text"` *(required)*,  `"image"`         | `"text"`     |
| `text`                | string  | Watermark text — **collect in chat first**| —            |
| `font_family`         | string  | See list below                            | —            |
| `font_size`           | number  | Point size                                | `14`         |
| `font_color`          | string  | Hex color e.g. `"#FF0000"`                | —            |
| `font_style`          | string  | `"Bold"`, `"Italic"`, or `null` (Regular) | `null`       |
| `transparency`        | number  | `0`–`100`                                 | `100`        |
| `rotation`            | number  | Degrees                                   | `0`          |
| `layer`               | string  | `"above"`, `"below"`                      | `"above"`    |
| `mosaic`              | boolean | Tile watermark across full page           | `false`      |
| `vertical_position`   | string  | `"top"`, `"middle"`, `"bottom"`           | `"middle"`   |
| `horizontal_position` | string  | `"left"`, `"center"`, `"right"`           | `"center"`   |
| `pages`               | string  | `"all"`, `"1-5"`, `"3-end"`, etc.        | `"all"`      |

### Supported Font Families

`Arial`, `Arial Unicode MS`, `Verdana`, `Courier`, `Times New Roman`,
`Comic Sans MS`, `WenQuanYi Zen Hei`, `Lohit Marathi`

Similar font names are auto-matched (e.g. "Times" → "Times New Roman").

## Example Calls

```json
// Text watermark: DRAFT, centered, 50% transparent
{
  "tool": "watermark",
  "options": {
    "mode": "text",
    "text": "DRAFT",
    "transparency": 50,
    "vertical_position": "middle",
    "horizontal_position": "center"
  }
}

// Diagonal CONFIDENTIAL stamp, red, rotated 45°
{
  "tool": "watermark",
  "options": {
    "mode": "text",
    "text": "CONFIDENTIAL",
    "font_color": "#FF0000",
    "rotation": 45,
    "transparency": 40
  }
}
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- Excluding only the last page in `pages` is not supported by the iLovePDF API.
- For image watermarks, the user must provide the PDF and the watermark image in the same request.
