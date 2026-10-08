# Find & Search — Parameter Reference

Parameter reference for every PDF4me **find & search** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/find-search/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [FindAndReplace](#findandreplace)
- [ConvertOcrPdf](#convertocrpdf)

---

## Quick index — pick the right endpoint

| User intent                                                               | Action           |
| ------------------------------------------------------------------------- | ---------------- |
| Find specific text in a PDF and replace it with new text                  | `FindAndReplace` |
| Convert a scanned/image-based PDF to a searchable, editable PDF using OCR | `ConvertOcrPdf`  |

---

## FindAndReplace

`POST /api/v2/FindAndReplace` — searches a PDF for an exact text string and replaces every match with new text, targeting specific pages or the entire document.

**Docs:** https://docs.pdf4me.com/pdf4me-api/find-search/find-and-replace-text.md

> **Response note:** Responses return the modified PDF as **raw binary data** (not a JSON-wrapped Base64 string). Save the response body directly as a `.pdf` file.

| JSON Key       | Type          | Required | Allowed values / notes                                                                                                                    |
| -------------- | ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`   | base64 string | Yes      | Base64-encoded PDF content.                                                                                                               |
| `docName`      | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`.                                                                             |
| `oldText`      | string        | Yes      | Exact text to search for. Case-sensitive.                                                                                                 |
| `newText`      | string        | Yes      | Replacement text to insert wherever `oldText` is found.                                                                                   |
| `pageSequence` | string        | Yes      | Pages to process: `"1"` = page 1 only, `"1,3,5"` = specific pages, `"2-5"` = range, `"1,3,7-10"` = mixed, `"1-"` = all pages from page 1. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf",
  "oldText": "input_old_text",
  "newText": "output_new_text",
  "pageSequence": "1-"
}
```

---

## ConvertOcrPdf

`POST /api/v2/ConvertOcrPdf` — runs OCR on a scanned or image-based PDF to produce a fully searchable and editable PDF. Supports two quality tiers, intelligent skip-if-already-searchable processing, and optional language hints for improved accuracy.

**Docs:** https://docs.pdf4me.com/pdf4me-api/find-search/convert-pdf-to-editable-pdf-using-ocr.md

| JSON Key         | Type          | Required | Allowed values / notes                                                                                                                         |
| ---------------- | ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`     | base64 string | Yes      | Base64-encoded PDF content.                                                                                                                    |
| `docName`        | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`.                                                                                  |
| `qualityType`    | string        | Yes      | OCR quality tier: `"Draft"` = 1 API call per file (fast, normal PDFs); `"High"` = 2 API calls per page (best accuracy, for scanned documents). |
| `ocrWhenNeeded`  | string        | Yes      | `"true"` to skip OCR when the PDF already contains searchable text; `"false"` to always run OCR regardless.                                    |
| `outputFormat`   | string        | Yes      | Must be `"true"` for standard PDF output.                                                                                                      |
| `language`       | string        | No       | Language of the source document, e.g. `"English"`, `"Spanish"`, `"French"`, `"German"`. Only specify if recognition output is poor without it. |
| `mergeAllSheets` | boolean       | No       | Merge all sheets if applicable.                                                                                                                |

**Response shape (synchronous):**

```json
{
  "docName": "output.pdf",
  "docContent": "JVBERi0xLjQKJeLjz9MK..."
}
```

- **`docName`**: Output PDF filename.
- **`docContent`**: Base64-encoded OCR-processed PDF. Decode to get the binary file.

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf",
  "qualityType": "Draft",
  "ocrWhenNeeded": "true",
  "outputFormat": "true",
  "language": "English"
}
```
