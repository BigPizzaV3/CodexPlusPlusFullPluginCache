# Edit — Parameter Reference

Parameter reference for every PDF4me **edit** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/edit/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [AddAttachmentToPdf](#addattachmenttopdf)
- [AddHtmlHeaderFooter](#addhtmlheaderfooter)
- [AddMargin](#addmargin)
- [AddPageNumber](#addpagenumber)
- [ImageStamp](#imagestamp)
- [SignPdf](#signpdf)
- [Stamp — text watermark](#stamp--text-watermark)

---

## Quick index — pick the right endpoint

| User intent                                         | Action                |
| --------------------------------------------------- | --------------------- |
| Embed one or more files inside a PDF as attachments | `AddAttachmentToPdf`  |
| Add an HTML header, footer, or both to every page   | `AddHtmlHeaderFooter` |
| Add whitespace margins around page content          | `AddMargin`           |
| Stamp page numbers onto a PDF                       | `AddPageNumber`       |
| Overlay an image (logo, watermark) on PDF pages     | `ImageStamp`          |
| Add a signature image to a PDF                      | `SignPdf`             |
| Overlay a text watermark or stamp on PDF pages      | `Stamp`               |

---

## AddAttachmentToPdf

`POST /api/v2/AddAttachmentToPdf` — embeds one or more files as attachments inside a PDF, creating a document package with linked embedded resources.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/add-attachment-to-pdf.md

| JSON Key      | Type             | Required | Allowed values / notes                                                                                                                                                                                                 |
| ------------- | ---------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`  | base64 string    | Yes      | Base64 of the source PDF.                                                                                                                                                                                              |
| `docName`     | string           | Yes      | Output PDF filename, e.g. `output.pdf`.                                                                                                                                                                                |
| `attachments` | array of objects | Yes      | Each object must contain `docName` (string — attachment filename with extension, e.g. `file.txt`) and `docContent` (base64 string — content of the attachment). Multiple attachments can be provided in a single call. |

**Example payload (single attachment):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "attachments": [
    {
      "docName": "notes.txt",
      "docContent": "RXhhbXBsZSBvZiBhdHRhY2htZW50IGZpbGUuIA=="
    }
  ]
}
```

**Example payload (multiple attachments):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "attachments": [
    {
      "docName": "file1.txt",
      "docContent": "RXhhbXBsZSBvZiBhdHRhY2htZW50IGZpbGUuIA=="
    },
    {
      "docName": "file2.pdf",
      "docContent": "JVBERi0xLjQKJ..."
    }
  ]
}
```

---

## AddHtmlHeaderFooter

`POST /api/v2/AddHtmlHeaderFooter` — renders an HTML string as a header, footer, or both on PDF pages, with full inline CSS support.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/add-header-footer-to-pdf.md

> **Important:** `htmlContent` must be a **plain HTML string**, not base64 encoded. Inline CSS within the HTML tags is fully supported.

| JSON Key        | Type          | Required | Allowed values / notes                                                                                                                                                     |
| --------------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`    | base64 string | Yes      | Base64 of the source PDF.                                                                                                                                                  |
| `docName`       | string        | Yes      | Output PDF filename, e.g. `output.pdf`.                                                                                                                                    |
| `htmlContent`   | string        | Yes      | Plain HTML string (not base64). May include inline CSS. E.g. `<div style="text-align:center;">Header</div>`.                                                               |
| `location`      | string        | Yes      | `Header`, `Footer`, or `Both`.                                                                                                                                             |
| `pages`         | string        | No       | Page targeting: `""` for all pages, `"1"` for a single page, `"1,3,5"` for specific pages, `"2-5"` for a range, `"1,3,7-10"` for a mix, `"2-"` for from page 2 to the end. |
| `skipFirstPage` | boolean       | No       | `true` to exclude the first page; `false` (default) to include it.                                                                                                         |
| `marginLeft`    | number        | No       | Left margin in pixels, e.g. `20.0`.                                                                                                                                        |
| `marginRight`   | number        | No       | Right margin in pixels, e.g. `20.0`.                                                                                                                                       |
| `marginTop`     | number        | No       | Top margin in pixels, e.g. `50.0`.                                                                                                                                         |
| `marginBottom`  | number        | No       | Bottom margin in pixels, e.g. `50.0`.                                                                                                                                      |

**Example payload (minimal):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "htmlContent": "<div style='text-align: center; font-family: Arial; font-size: 12px;'>Company Confidential</div>",
  "location": "Footer"
}
```

**Example payload (all options):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "htmlContent": "<div style='text-align: center; font-family: Arial; font-size: 12px; color: #FF0000;'>Document Header PDF4me</div>",
  "location": "Header",
  "pages": "",
  "skipFirstPage": false,
  "marginLeft": 20.0,
  "marginRight": 20.0,
  "marginTop": 50.0,
  "marginBottom": 50.0
}
```

---

## AddMargin

`POST /api/v2/AddMargin` — adds whitespace margins (in millimeters) to any side of a PDF; the page dimensions expand to accommodate the added space, preserving all original content.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/add-margin-to-pdf.md

| JSON Key       | Type          | Required | Allowed values / notes                                     |
| -------------- | ------------- | -------- | ---------------------------------------------------------- |
| `docContent`   | base64 string | Yes      | Base64 of the source PDF.                                  |
| `docName`      | string        | Yes      | Output PDF filename, e.g. `output.pdf`.                    |
| `marginLeft`   | integer       | No       | Left margin in mm (0–100). Omit to add no left margin.     |
| `marginRight`  | integer       | No       | Right margin in mm (0–100). Omit to add no right margin.   |
| `marginTop`    | integer       | No       | Top margin in mm (0–100). Omit to add no top margin.       |
| `marginBottom` | integer       | No       | Bottom margin in mm (0–100). Omit to add no bottom margin. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "marginLeft": 20,
  "marginRight": 20,
  "marginTop": 25,
  "marginBottom": 25
}
```

**Notes:** Page size grows to absorb the added margins — content is not cropped. You can specify margins for any subset of sides; omitted sides are left unchanged.

---

## AddPageNumber

`POST /api/v2/AddPageNumber` — stamps customizable page numbers onto a PDF with control over format, position, font, and whether to skip the first page.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/add-page-number-to-pdf.md

**Format placeholders:** `#` = current page number; `{1}` = total page count. Examples: `"# of {1}"` → "1 of 10", `"Page #"` → "Page 1", `"#"` → "1".

| JSON Key           | Type          | Required | Allowed values / notes                                             |
| ------------------ | ------------- | -------- | ------------------------------------------------------------------ |
| `docContent`       | base64 string | Yes      | Base64 of the source PDF.                                          |
| `docName`          | string        | Yes      | Output PDF filename, e.g. `output.pdf`.                            |
| `pageNumberFormat` | string        | Yes      | Format string using `#` and `{1}` placeholders, e.g. `"# of {1}"`. |
| `alignX`           | string        | Yes      | Horizontal alignment: `left`, `center`, or `right`.                |
| `alignY`           | string        | Yes      | Vertical alignment: `top`, `middle`, or `bottom`.                  |
| `marginXinMM`      | integer       | No       | Horizontal margin from edge in mm (0–100), e.g. `2`.               |
| `marginYinMM`      | integer       | No       | Vertical margin from edge in mm (0–100), e.g. `2`.                 |
| `fontSize`         | integer       | No       | Font size (8–72), e.g. `12`.                                       |
| `isBold`           | boolean       | No       | `true` for bold page numbers.                                      |
| `isItalic`         | boolean       | No       | `true` for italic page numbers.                                    |
| `skipFirstPage`    | boolean       | No       | `true` to omit page number from page 1.                            |

**Example payload (minimal):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "pageNumberFormat": "# of {1}",
  "alignX": "right",
  "alignY": "bottom"
}
```

**Example payload (styled, skip cover page):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "pageNumberFormat": "# of {1}",
  "alignX": "right",
  "alignY": "bottom",
  "marginXinMM": 2,
  "marginYinMM": 2,
  "fontSize": 12,
  "isBold": true,
  "isItalic": false,
  "skipFirstPage": true
}
```

---

## ImageStamp

`POST /api/v2/ImageStamp` — overlays a logo, watermark image, or any image file onto PDF pages with control over position, size, opacity, and layering.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/image-stamp.md

**Supported image formats:** JPG, PNG, GIF, and other common formats.

| JSON Key          | Type          | Required | Allowed values / notes                                                                                                                             |
| ----------------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`      | base64 string | Yes      | Base64 of the source PDF.                                                                                                                          |
| `docName`         | string        | Yes      | Output PDF filename, e.g. `output.pdf`.                                                                                                            |
| `imageFile`       | base64 string | Yes      | Base64 of the stamp image.                                                                                                                         |
| `imageName`       | string        | Yes      | Stamp image filename with extension, e.g. `logo.png`.                                                                                              |
| `alignX`          | string        | Yes      | Horizontal alignment: `Left`, `Center`, or `Right`.                                                                                                |
| `alignY`          | string        | Yes      | Vertical alignment: `Top`, `Middle`, or `Bottom`.                                                                                                  |
| `pages`           | string        | No       | Page targeting: `""` for all pages, `"1"` for a single page, `"1,3,5"` for specific pages, `"2-5"` for a range, `"2-"` for from page 2 to the end. |
| `heightInMM`      | string        | No       | Stamp height in mm (10–200).                                                                                                                       |
| `widthInMM`       | string        | No       | Stamp width in mm (10–200).                                                                                                                        |
| `heightInPx`      | string        | No       | Stamp height in pixels (20–600).                                                                                                                   |
| `widthInPx`       | string        | No       | Stamp width in pixels (20–600).                                                                                                                    |
| `marginXInMM`     | string        | No       | Horizontal margin in mm (0–100).                                                                                                                   |
| `marginYInMM`     | string        | No       | Vertical margin in mm (0–100).                                                                                                                     |
| `marginXInPx`     | string        | No       | Horizontal margin in pixels (0–300).                                                                                                               |
| `marginYInPx`     | string        | No       | Vertical margin in pixels (0–300).                                                                                                                 |
| `opacity`         | integer       | No       | Transparency 0–100: `0` = invisible, `100` = fully opaque.                                                                                         |
| `isBackground`    | boolean       | No       | `true` to render stamp behind page content; `false` (default) for foreground.                                                                      |
| `showOnlyInPrint` | boolean       | No       | `true` to make stamp visible only when printing; `false` to show on screen too.                                                                    |

**Example payload (minimal):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "imageFile": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJ...",
  "imageName": "logo.png",
  "alignX": "Center",
  "alignY": "Middle"
}
```

**Example payload (semi-transparent background watermark on all pages):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "imageFile": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJ...",
  "imageName": "watermark.png",
  "alignX": "Center",
  "alignY": "Middle",
  "pages": "",
  "widthInMM": "80",
  "heightInMM": "40",
  "opacity": 30,
  "isBackground": true,
  "showOnlyInPrint": false
}
```

**Notes:** Size can be specified in either mm or px — both can be set simultaneously. If the stamp should appear behind text and graphics, set `isBackground: true`. `opacity: 30` is a good starting point for a translucent watermark.

---

## SignPdf

`POST /api/v2/SignPdf` — places a signature image onto a PDF with full control over position, size, opacity, and layering. Functionally identical to `ImageStamp` but semantically distinct for signature use cases.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/sign-pdf.md

**Supported image formats:** JPG, PNG, and other common formats.

| JSON Key          | Type          | Required | Allowed values / notes                                                                                                                              |
| ----------------- | ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`      | base64 string | Yes      | Base64 of the source PDF.                                                                                                                           |
| `docName`         | string        | Yes      | Output PDF filename, e.g. `output.pdf`.                                                                                                             |
| `imageFile`       | base64 string | Yes      | Base64 of the signature image.                                                                                                                      |
| `imageName`       | string        | Yes      | Signature image filename with extension, e.g. `signature.png`.                                                                                      |
| `alignX`          | string        | Yes      | Horizontal alignment: `Left`, `Center`, or `Right`.                                                                                                 |
| `alignY`          | string        | Yes      | Vertical alignment: `Top`, `Middle`, or `Bottom`.                                                                                                   |
| `pages`           | string        | No       | Page targeting: `"1"` for page 1, `"1,3,5"` for specific pages, `"2-5"` for a range, `"2-"` for from page 2 to the end. Omit to apply to all pages. |
| `widthInMM`       | string        | No       | Signature width in mm (10–200).                                                                                                                     |
| `heightInMM`      | string        | No       | Signature height in mm (10–200).                                                                                                                    |
| `widthInPx`       | string        | No       | Signature width in pixels (20–600).                                                                                                                 |
| `heightInPx`      | string        | No       | Signature height in pixels (20–600).                                                                                                                |
| `marginXInMM`     | string        | No       | Horizontal margin in mm (0–100).                                                                                                                    |
| `marginYInMM`     | string        | No       | Vertical margin in mm (0–100).                                                                                                                      |
| `marginXInPx`     | string        | No       | Horizontal margin in pixels (0–300).                                                                                                                |
| `marginYInPx`     | string        | No       | Vertical margin in pixels (0–300).                                                                                                                  |
| `opacity`         | string        | No       | Transparency 0–100 (sent as a **string**, e.g. `"100"`): `"0"` = invisible, `"100"` = fully opaque.                                                 |
| `isBackground`    | boolean       | No       | `true` to render signature behind page content; `false` (default) for foreground.                                                                   |
| `showOnlyInPrint` | boolean       | No       | `true` to make signature visible only when printing; `false` to show on screen too.                                                                 |

**Example payload (minimal — sign last page, bottom-right):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "imageFile": "iVBORw0KGgoAAAANSUhEUgAA...",
  "imageName": "signature.png",
  "alignX": "Right",
  "alignY": "Bottom"
}
```

**Example payload (sign last page only, sized, with margin):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "imageFile": "iVBORw0KGgoAAAANSUhEUgAA...",
  "imageName": "signature.png",
  "pages": "3",
  "alignX": "Right",
  "alignY": "Bottom",
  "widthInMM": "50",
  "heightInMM": "25",
  "marginXInMM": "20",
  "marginYInMM": "20",
  "opacity": "100",
  "isBackground": false
}
```

**Notes:** `opacity` is sent as a **string** (e.g. `"100"`), unlike `ImageStamp` where it is an integer. To sign only the final page of an n-page document you must know n in advance and pass it explicitly (e.g. `"pages": "5"` for a 5-page doc). Use `isBackground: false` so the signature renders on top of existing content.

---

## Stamp — text watermark

`POST /api/v2/Stamp` — overlays a customizable text watermark or stamp on PDF pages with control over font, color, rotation, opacity, and layering.

**Docs:** https://docs.pdf4me.com/pdf4me-api/edit/text-stamp.md

**Supported fonts:** `Arial`, `Times New Roman`, `Helvetica`, `Courier New`.

**Rotation values:** `0` (horizontal), `45` (diagonal), `90` (vertical), `-45` (reverse diagonal).

| JSON Key          | Type          | Required | Allowed values / notes                                                                                                                         |
| ----------------- | ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`      | base64 string | Yes      | Base64 of the source PDF.                                                                                                                      |
| `docName`         | string        | Yes      | Output PDF filename, e.g. `output.pdf`.                                                                                                        |
| `pages`           | string        | Yes      | Page targeting: `"all"` for all pages, `"1"` for page 1, `"1,3,5"` for specific pages, `"2-5"` for a range, `"2-"` for from page 2 to the end. |
| `text`            | string        | Yes      | Text to stamp, e.g. `"CONFIDENTIAL"`.                                                                                                          |
| `alignX`          | string        | Yes      | Horizontal alignment: `left`, `center`, or `right`.                                                                                            |
| `alignY`          | string        | Yes      | Vertical alignment: `top`, `middle`, or `bottom`.                                                                                              |
| `marginXInMM`     | string        | No       | Horizontal margin from left edge in mm.                                                                                                        |
| `marginYInMM`     | string        | No       | Vertical margin from top edge in mm.                                                                                                           |
| `marginXInPx`     | string        | No       | Horizontal margin in pixels.                                                                                                                   |
| `marginYInPx`     | string        | No       | Vertical margin in pixels.                                                                                                                     |
| `opacity`         | string        | No       | Transparency 0–100 (as a string): `"0"` = invisible, `"100"` = fully opaque. `"30"` works well for a subtle watermark.                         |
| `fontName`        | string        | No       | Font: `Arial`, `Times New Roman`, `Helvetica`, or `Courier New`.                                                                               |
| `fontSize`        | integer       | No       | Font size (8–72).                                                                                                                              |
| `fontColor`       | string        | No       | Hex color string, e.g. `"#FF0000"` for red.                                                                                                    |
| `isBold`          | boolean       | No       | `true` for bold text.                                                                                                                          |
| `isItalics`       | boolean       | No       | `true` for italic text.                                                                                                                        |
| `underline`       | boolean       | No       | `true` to underline the text.                                                                                                                  |
| `rotate`          | integer       | No       | Rotation angle: `0`, `45`, `90`, or `-45`.                                                                                                     |
| `isBackground`    | boolean       | No       | `true` to render stamp behind page content; `false` for foreground.                                                                            |
| `showOnlyInPrint` | boolean       | No       | `true` to show only when printing; `false` to show on screen too.                                                                              |
| `transverse`      | boolean       | No       | `true` for transverse (perpendicular) positioning mode.                                                                                        |
| `fitTextOverPage` | boolean       | No       | `true` to auto-scale the text to fill the page; `false` to use `fontSize`.                                                                     |

**Example payload (minimal — diagonal "CONFIDENTIAL" watermark):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "pages": "all",
  "text": "CONFIDENTIAL",
  "alignX": "center",
  "alignY": "middle"
}
```

**Example payload (styled semi-transparent diagonal watermark):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "output.pdf",
  "pages": "all",
  "text": "DRAFT",
  "alignX": "center",
  "alignY": "middle",
  "opacity": "30",
  "fontName": "Arial",
  "fontSize": 48,
  "fontColor": "#FF0000",
  "isBold": true,
  "isItalics": false,
  "underline": false,
  "rotate": 45,
  "isBackground": true,
  "showOnlyInPrint": false
}
```

**Notes:** `opacity`, `marginXInMM`, `marginYInMM`, `marginXInPx`, and `marginYInPx` are all sent as **strings** even though they represent numbers. `pages` accepts `"all"` as a convenience alias (unlike `AddHtmlHeaderFooter` and `ImageStamp` which use an empty string `""` for all pages). When `fitTextOverPage: true`, `fontSize` is ignored and the text is auto-scaled to span the page.

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/edit/
