# Convert — Parameter Reference

Parameter reference for every PDF4me **convert** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

The two universal keys (`docContent`, `docName`) are documented in `auth-and-conventions.md` and are listed in the per-endpoint tables below for completeness only when an endpoint uses them in the standard way. One endpoint — `ConvertJsonToExcel` — overloads `docName` to carry base64 content; that exception is called out in its section.

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/convert/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [To PDF from Office / images](#to-pdf-from-office--images)
  - [ConvertToPdf](#converttopdf)
  - [ConvertWordToPdfForm](#convertwordtopdfform)
- [From PDF to Office](#from-pdf-to-office)
  - [ConvertPdfToWord](#convertpdftoword)
  - [ConvertPdfToExcel](#convertpdftoexcel)
  - [ConvertPdfToPowerPoint](#convertpdftopowerpoint)
- [HTML / Markdown / URL → PDF](#html--markdown--url--pdf)
  - [ConvertHtmlToPdf](#converthtmltopdf)
  - [ConvertMdToPdf](#convertmdtopdf)
  - [ConvertUrlToPdf](#converturltopdf)
- [PDF post-processing](#pdf-post-processing)
  - [PdfA — create PDF/A](#pdfa--create-pdfa)
  - [FlattenPdf](#flattenpdf)
  - [LinearizePdf](#linearizepdf)
- [Specialty](#specialty)
  - [ConvertJsonToExcel](#convertjsontoexcel)
  - [ConvertVisio](#convertvisio)

---

## Quick index — pick the right endpoint

| User intent                                                    | Action                   |
| -------------------------------------------------------------- | ------------------------ |
| Convert Word, Excel, PowerPoint, or image to PDF               | `ConvertToPdf`           |
| Convert a Word doc with form controls into a fillable PDF form | `ConvertWordToPdfForm`   |
| Convert a PDF back to editable Word                            | `ConvertPdfToWord`       |
| Convert a PDF back to editable Excel                           | `ConvertPdfToExcel`      |
| Convert a PDF back to editable PowerPoint                      | `ConvertPdfToPowerPoint` |
| Render an HTML file (or HTML zip bundle) as a PDF              | `ConvertHtmlToPdf`       |
| Render a Markdown file (or md zip bundle) as a PDF             | `ConvertMdToPdf`         |
| Render a live web page (with optional auth) as a PDF           | `ConvertUrlToPdf`        |
| Convert PDF to PDF/A for archiving / compliance                | `PdfA`                   |
| Flatten form fields and annotations into static PDF content    | `FlattenPdf`             |
| Linearize / "fast web view" a PDF for streamed loading         | `LinearizePdf`           |
| Convert a JSON document into a formatted Excel sheet           | `ConvertJsonToExcel`     |
| Convert Visio (.vsd/.vsdx/.vsdm/.vstx/.vst) to PDF or image    | `ConvertVisio`           |

---

## To PDF from Office / images

### ConvertToPdf

`POST /api/v2/ConvertToPdf` — converts a Word, Excel, PowerPoint, or common image file into a PDF with formatting preserved.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/convert-to-pdf.md

**Supported inputs:** `.docx`, `.doc`, `.xlsx`, `.xls`, `.pptx`, `.ppt`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff` (50+ formats per the docs).

| JSON Key     | Type          | Required | Allowed values / notes                                                                                        |
| ------------ | ------------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the source file.                                                                                    |
| `docName`    | string        | Yes      | Source filename **with extension** (the extension drives format detection) — e.g. `report.docx`, `chart.png`. |

**Example payload:**

```json
{
  "docContent": "UEsDBBQABgAIAAAAIQ...",
  "docName": "report.docx"
}
```

---

### ConvertWordToPdfForm

`POST /api/v2/ConvertWordToPdfForm` — converts a Word document containing form controls into a fillable PDF form (preserves text fields, checkboxes, radio buttons, dropdowns).

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/convert-word-to-pdf-form.md

**Supported inputs:** `.docx`, `.doc`.

| JSON Key     | Type          | Required | Allowed values / notes                            |
| ------------ | ------------- | -------- | ------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the source Word document.               |
| `docName`    | string        | Yes      | Source filename with `.docx` or `.doc` extension. |

**Example payload:**

```json
{
  "docContent": "UEsDBBQABgAIAAAAIQ...",
  "docName": "intake-form.docx"
}
```

**Notes:** Use `ConvertToPdf` for plain Word→PDF; only reach for this endpoint when the source contains form controls that should remain interactive in the output.

---

## From PDF to Office

The three PDF→Office endpoints (`ConvertPdfToWord`, `ConvertPdfToExcel`, `ConvertPdfToPowerPoint`) share an identical parameter shape. The table and example below apply to all three; only the action name in the URL differs.

| JSON Key         | Type          | Required | Allowed values / notes                                                                                                                |
| ---------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`     | base64 string | Yes      | Base64 of the source PDF.                                                                                                             |
| `docName`        | string        | Yes      | Source PDF filename, e.g. `report.pdf`.                                                                                               |
| `qualityType`    | string        | Yes      | `Draft` (faster, looser layout) or `High` (slower, closer fidelity).                                                                  |
| `language`       | string        | Yes      | OCR/recognition language, e.g. `English`.                                                                                             |
| `mergeAllSheets` | boolean       | Yes      | `true` to merge multi-page output into a single sheet/section; `false` to keep per-page splits.                                       |
| `outputFormat`   | string        | Yes      | Per docs, send the literal string `"yes"` to enable formatted output (this is a flag the API parses as a string, not a content-type). |
| `ocrWhenNeeded`  | string        | Yes      | `"yes"` to run OCR automatically on scanned/image PDFs; `"no"` to skip.                                                               |

**Shared example payload (swap the action in the URL to target Word, Excel, or PowerPoint):**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "invoice.pdf",
  "qualityType": "High",
  "language": "English",
  "mergeAllSheets": true,
  "outputFormat": "yes",
  "ocrWhenNeeded": "yes"
}
```

### ConvertPdfToWord

`POST /api/v2/ConvertPdfToWord` — converts a PDF into an editable Word document (`.docx`).

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/pdf-to-word.md

### ConvertPdfToExcel

`POST /api/v2/ConvertPdfToExcel` — extracts tabular content from a PDF into an editable Excel workbook (`.xlsx`).

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/pdf-to-excel.md

### ConvertPdfToPowerPoint

`POST /api/v2/ConvertPdfToPowerPoint` — converts each PDF page into a PowerPoint slide (`.pptx`).

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/pdf-to-powerpoint.md

**Notes for the family:** `outputFormat` and `ocrWhenNeeded` are typed as strings in the docs, not booleans — send `"yes"`/`"no"`, not `true`/`false`. Set `ocrWhenNeeded` to `"yes"` for scanned/image PDFs; otherwise `"no"` is faster.

---

## HTML / Markdown / URL → PDF

### ConvertHtmlToPdf

`POST /api/v2/ConvertHtmlToPdf` — renders an HTML file (or a ZIP bundle of HTML + assets) into a PDF using a headless browser.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/html-to-pdf.md

**Supported inputs:** a single `.html` file or a `.zip` archive containing HTML, CSS, JS, and image assets.

| JSON Key              | Type          | Required | Allowed values / notes                                                                                                  |
| --------------------- | ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
| `docContent`          | base64 string | Yes      | Base64 of the HTML file or ZIP.                                                                                         |
| `docName`             | string        | Yes      | Filename, e.g. `page.html` or `site.zip`.                                                                               |
| `indexFilePath`       | string        | Yes      | Path to the entry HTML file within the ZIP, e.g. `index.html`. For a single HTML upload, set this to the same filename. |
| `layout`              | string        | Yes      | `Portrait` or `Landscape`.                                                                                              |
| `format`              | string        | Yes      | Page size: `A0`–`A8`, `Tabloid`, `Legal`, `Statement`, `Executive`.                                                     |
| `scale`               | number        | Yes      | Zoom factor 0–0.8 (e.g. `0.8`).                                                                                         |
| `topMargin`           | string        | Yes      | CSS-style length, e.g. `40px`.                                                                                          |
| `bottomMargin`        | string        | Yes      | CSS-style length, e.g. `40px`.                                                                                          |
| `leftMargin`          | string        | Yes      | CSS-style length, e.g. `40px`.                                                                                          |
| `rightMargin`         | string        | Yes      | CSS-style length, e.g. `40px`.                                                                                          |
| `printBackground`     | boolean       | Yes      | `true` to include CSS background colors / images in the PDF.                                                            |
| `displayHeaderFooter` | boolean       | Yes      | `true` to render browser-style header/footer with page numbers.                                                         |

**Example payload:**

```json
{
  "docContent": "PCFkb2N0eXBlIGh0bWw+...",
  "docName": "report.html",
  "indexFilePath": "report.html",
  "layout": "Portrait",
  "format": "A4",
  "scale": 0.8,
  "topMargin": "40px",
  "bottomMargin": "40px",
  "leftMargin": "40px",
  "rightMargin": "40px",
  "printBackground": true,
  "displayHeaderFooter": false
}
```

---

### ConvertMdToPdf

`POST /api/v2/ConvertMdToPdf` — renders a Markdown file (or a ZIP of Markdown + linked assets) into a PDF.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/markdown-to-pdf.md

**Supported inputs:** a single `.md` file or a `.zip` archive with multiple `.md` files plus referenced images/assets.

| JSON Key     | Type          | Required | Allowed values / notes                                                                                                                                  |
| ------------ | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the `.md` file or `.zip`.                                                                                                                     |
| `docName`    | string        | Yes      | Filename, e.g. `readme.md` or `docs.zip`.                                                                                                               |
| `mdFilePath` | string        | No       | **Required only when `docContent` is a ZIP.** Path to the entry Markdown inside the archive, e.g. `docs/readme.md`. Omit for single-file `.md` uploads. |

**Example payload (single file):**

```json
{
  "docContent": "IyBSZWFkbWUKCkhlbGxv...",
  "docName": "readme.md"
}
```

**Example payload (ZIP):**

```json
{
  "docContent": "UEsDBBQAAAAIAA...",
  "docName": "docs.zip",
  "mdFilePath": "docs/readme.md"
}
```

---

### ConvertUrlToPdf

`POST /api/v2/ConvertUrlToPdf` — fetches a live URL and renders it as a PDF, with optional auth for protected pages.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/url-to-pdf.md

**Supported inputs:** any HTTP/HTTPS URL — static pages, JS-driven SPAs, or auth-protected resources.

| JSON Key              | Type          | Required | Allowed values / notes                                                                                                  |
| --------------------- | ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
| `webUrl`              | string        | Yes      | Fully qualified URL, e.g. `https://example.com/report`.                                                                 |
| `authType`            | string        | Yes      | `NoAuth`, `Basic Auth`, `OAuth`, or `API Key`. Use `NoAuth` for public pages.                                           |
| `username`            | string        | Yes      | Username for `Basic Auth`. Send an empty string when `authType` is `NoAuth`.                                            |
| `password`            | string        | Yes      | Password / token for the chosen auth type. Send an empty string when `authType` is `NoAuth`.                            |
| `docContent`          | base64 string | Yes      | Per docs this is required even for URL conversion — pass an empty string or a placeholder if no local file is involved. |
| `docName`             | string        | Yes      | Output filename, e.g. `output.pdf`.                                                                                     |
| `layout`              | string        | Yes      | `landscape` or `portrait`.                                                                                              |
| `format`              | string        | Yes      | Page size: `A0`–`A8`, `Tabloid`, `Legal`, `Statement`, `Executive`.                                                     |
| `scale`               | number        | Yes      | Zoom factor 0.1–2.0 (e.g. `0.8` for 80%).                                                                               |
| `topMargin`           | string        | Yes      | CSS-style length — `px`, `in`, or `cm` units accepted (e.g. `40px`).                                                    |
| `bottomMargin`        | string        | Yes      | CSS-style length.                                                                                                       |
| `leftMargin`          | string        | Yes      | CSS-style length.                                                                                                       |
| `rightMargin`         | string        | Yes      | CSS-style length.                                                                                                       |
| `printBackground`     | boolean       | Yes      | `true` to include CSS backgrounds.                                                                                      |
| `displayHeaderFooter` | boolean       | Yes      | `true` to render browser-style header/footer.                                                                           |

**Example payload (public URL, no auth):**

```json
{
  "webUrl": "https://example.com/report",
  "authType": "NoAuth",
  "username": "",
  "password": "",
  "docContent": "",
  "docName": "example.pdf",
  "layout": "portrait",
  "format": "A4",
  "scale": 0.8,
  "topMargin": "40px",
  "bottomMargin": "40px",
  "leftMargin": "40px",
  "rightMargin": "40px",
  "printBackground": true,
  "displayHeaderFooter": false
}
```

---

## PDF post-processing

### PdfA — create PDF/A

`POST /api/v2/PdfA` — converts an existing PDF into a PDF/A-compliant archive document.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/create-pdfa.md

**Supported inputs:** any PDF.

| JSON Key         | Type          | Required | Allowed values / notes                                                                 |
| ---------------- | ------------- | -------- | -------------------------------------------------------------------------------------- |
| `docContent`     | base64 string | Yes      | Base64 of the source PDF.                                                              |
| `docName`        | string        | Yes      | Source PDF filename.                                                                   |
| `compliance`     | string        | Yes      | One of `PdfA1b`, `PdfA1a`, `PdfA2b`, `PdfA2u`, `PdfA2a`, `PdfA3b`, `PdfA3u`, `PdfA3a`. |
| `allowUpgrade`   | boolean       | Yes      | `true` to allow upgrading to a higher PDF/A level if the source qualifies.             |
| `allowDowngrade` | boolean       | Yes      | `true` to allow downgrading if strict compliance fails at the requested level.         |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "contract.pdf",
  "compliance": "PdfA2b",
  "allowUpgrade": true,
  "allowDowngrade": false
}
```

**Notes:** `PdfA2b` is the most common archival target. Set `allowDowngrade: true` if the request must succeed even when the source can't meet the requested level.

---

### FlattenPdf

`POST /api/v2/FlattenPdf` — flattens form fields, annotations, and interactive layers into static page content so the PDF can no longer be edited or filled.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/flatten-pdf.md

**Supported inputs:** any PDF.

| JSON Key     | Type          | Required | Allowed values / notes                |
| ------------ | ------------- | -------- | ------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the source PDF.             |
| `docName`    | string        | Yes      | Source PDF filename, e.g. `form.pdf`. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "filled-form.pdf"
}
```

---

### LinearizePdf

`POST /api/v2/LinearizePdf` — linearizes a PDF ("fast web view") so browsers can stream the first page before the whole file downloads. Also exposes optimization profiles for size/quality trade-offs.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/linearize-pdf.md

**Supported inputs:** any PDF.

| JSON Key          | Type          | Required | Allowed values / notes                                                                                 |
| ----------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `docContent`      | base64 string | Yes      | Base64 of the source PDF.                                                                              |
| `docName`         | string        | Yes      | Source PDF filename.                                                                                   |
| `optimizeProfile` | string        | Yes      | One of `web`, `Max`, `Print`, `Default`, `WebMax`, `PrintMax`, `PrintGray`, `Compress`, `CompressMax`. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJ...",
  "docName": "report.pdf",
  "optimizeProfile": "web"
}
```

**Notes:** `web` is the default fast-web-view profile. Use `Compress` / `CompressMax` to prioritize file size over fidelity, or `Print` / `PrintMax` for print-ready output.

---

## Specialty

### ConvertJsonToExcel

`POST /api/v2/ConvertJsonToExcel` — converts a JSON document into a formatted Excel worksheet with header styling, number/date formatting, and configurable starting cell.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/convert-json-to-excel.md

**Supported inputs:** a base64-encoded JSON document.

> **Naming gotcha:** unlike every other endpoint, `docName` here carries the **base64 JSON content**, not the filename. The output filename comes from `fileName` instead. Read the table carefully.

| JSON Key               | Type    | Required | Allowed values / notes                                                                                    |
| ---------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `fileName`             | string  | Yes      | Output Excel filename, e.g. `data_export.xlsx`.                                                           |
| `docName`              | string  | Yes      | **Base64-encoded JSON content** (overloaded — see note above).                                            |
| `worksheetName`        | string  | Yes      | Name of the sheet to create, e.g. `Sheet1`.                                                               |
| `isTitleWrapText`      | boolean | Yes      | Wrap text in title row.                                                                                   |
| `isTitleBold`          | boolean | Yes      | Bold the title row.                                                                                       |
| `convertNumberAndDate` | boolean | Yes      | Auto-detect and format numeric / date strings.                                                            |
| `numberFormat`         | string  | Yes      | Excel number format pattern, e.g. `"11"`.                                                                 |
| `dateFormat`           | string  | Yes      | Date format string, e.g. `"01/01/2025"`.                                                                  |
| `ignoreNullValues`     | string  | Yes      | `"true"` to skip null fields, `"false"` to render them as empty cells. (Sent as a string, not a boolean.) |
| `firstRow`             | integer | Yes      | 1-based starting row.                                                                                     |
| `firstColumn`          | integer | Yes      | 1-based starting column.                                                                                  |

**Example payload:**

```json
{
  "fileName": "orders.xlsx",
  "docName": "W3sib3JkZXJfaWQiOjEsImFtb3VudCI6OTl9XQ==",
  "worksheetName": "Orders",
  "isTitleWrapText": true,
  "isTitleBold": true,
  "convertNumberAndDate": true,
  "numberFormat": "11",
  "dateFormat": "01/01/2025",
  "ignoreNullValues": "true",
  "firstRow": 1,
  "firstColumn": 1
}
```

---

### ConvertVisio

`POST /api/v2/ConvertVisio?schemaVal=PDF` — converts Visio diagrams to PDF, PDF/A-1b, PNG, JPEG, SVG, or TIFF, with extensive control over rendering, image quality, and page selection.

**Docs:** https://docs.pdf4me.com/pdf4me-api/convert/convert-visio.md

**Supported inputs:** `.vsd`, `.vsdx`, `.vsdm`, `.vstx`, `.vst`.

> **Two casing gotchas:** (1) the action takes a `?schemaVal=PDF` query string, and (2) all parameter keys on this endpoint are **PascalCase** (`PageIndex`, not `pageIndex`). The two universal keys keep their lowercase form (`docContent`, `docName`).

| JSON Key             | Type          | Required | Allowed values / notes                                                    |
| -------------------- | ------------- | -------- | ------------------------------------------------------------------------- |
| `docContent`         | base64 string | Yes      | Base64 of the source Visio file.                                          |
| `docName`            | string        | Yes      | Source filename, e.g. `diagram.vsdx`.                                     |
| `OutputFormat`       | string        | Yes      | `PDF`, `PDF/A-1b`, `PNG`, `JPEG`, `SVG`, or `TIFF`.                       |
| `PageIndex`          | integer       | Yes      | 0-based index of the first page to render, e.g. `0`.                      |
| `PageCount`          | integer       | Yes      | Number of pages to render starting at `PageIndex`.                        |
| `DefaultFont`        | string        | Yes      | Fallback font when source font is missing, e.g. `Arial`.                  |
| `IncludeHiddenPages` | boolean       | Yes      | `true` to render hidden pages.                                            |
| `PageSize`           | string        | Yes      | Output page size, e.g. `A4`, `Letter`.                                    |
| `JpegQuality`        | integer       | Yes      | JPEG quality 1–100 (only meaningful when `OutputFormat: JPEG`).           |
| `SaveForegroundPage` | boolean       | Yes      | `true` to render only the foreground layer.                               |
| `IsPdfCompliant`     | boolean       | Yes      | `true` to enforce PDF/A compliance on PDF output.                         |
| `ImageBrightness`    | number        | Yes      | Brightness adjustment, typically `0.0`–`1.0`.                             |
| `ImageContrast`      | number        | Yes      | Contrast adjustment.                                                      |
| `ImageColorMode`     | string        | Yes      | Color space, e.g. `Default`, `Grayscale`.                                 |
| `CompositingQuality` | string        | Yes      | e.g. `Default`, `HighQuality`, `HighSpeed`.                               |
| `InterpolationMode`  | string        | Yes      | e.g. `Default`, `Bicubic`, `NearestNeighbor`.                             |
| `PixelOffsetMode`    | string        | Yes      | e.g. `Default`, `HighQuality`, `Half`.                                    |
| `Resolution`         | number        | Yes      | DPI, e.g. `150`.                                                          |
| `Scale`              | number        | Yes      | Output scale factor, e.g. `1.0`.                                          |
| `SmoothingMode`      | string        | Yes      | e.g. `Default`, `AntiAlias`, `None`.                                      |
| `TiffCompression`    | string        | Yes      | e.g. `LZW`, `CCITT4`, `None` (only meaningful when `OutputFormat: TIFF`). |
| `SaveToolBar`        | boolean       | Yes      | `true` to embed the Visio toolbar in the output.                          |
| `AutoFit`            | boolean       | Yes      | `true` to auto-fit content to the page.                                   |

**Example payload (render first 3 pages of a `.vsdx` to PDF):**

```json
{
  "docContent": "UEsDBBQAAAAIAA...",
  "docName": "network-diagram.vsdx",
  "OutputFormat": "PDF",
  "PageIndex": 0,
  "PageCount": 3,
  "DefaultFont": "Arial",
  "IncludeHiddenPages": false,
  "PageSize": "A4",
  "JpegQuality": 90,
  "SaveForegroundPage": false,
  "IsPdfCompliant": false,
  "ImageBrightness": 0.5,
  "ImageContrast": 0.5,
  "ImageColorMode": "Default",
  "CompositingQuality": "HighQuality",
  "InterpolationMode": "Bicubic",
  "PixelOffsetMode": "HighQuality",
  "Resolution": 150,
  "Scale": 1.0,
  "SmoothingMode": "AntiAlias",
  "TiffCompression": "LZW",
  "SaveToolBar": false,
  "AutoFit": true
}
```

**Notes:** Image-quality params (`JpegQuality`, `TiffCompression`, brightness/contrast, etc.) only affect their corresponding `OutputFormat` — for `PDF` output, sane defaults are fine. The docs list every parameter as required, so include them all even when their value is irrelevant to the chosen format.

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, response envelope, error codes.
- [`../examples/convert-to-pdf.py`](../examples/convert-to-pdf.py) — minimal sync call.
- Docs index: https://docs.pdf4me.com/pdf4me-api/convert/
