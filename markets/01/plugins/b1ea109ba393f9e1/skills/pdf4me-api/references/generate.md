# Generate — Parameter Reference

Parameter reference for every PDF4me **generate** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/generate/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [EnableTrackingChangesInWord](#enabletrackingchangesinword)
- [GenerateDocument](#generatedocument)
- [GenerateDocuments](#generatedocuments)
- [GetTrackingChangesInWord](#gettrackingchangesinword)
- [ReplaceTextWithImageInWord](#replacetextwithimageinword)

---

## Quick index — pick the right endpoint

| User intent                                                                                  | Action                        |
| -------------------------------------------------------------------------------------------- | ----------------------------- |
| Turn on change tracking in a Word document                                                   | `EnableTrackingChangesInWord` |
| Generate a single document from a Word/HTML/PDF template with JSON or XML data               | `GenerateDocument`            |
| Generate multiple documents in bulk from a template with a data file (Excel, CSV, JSON, XML) | `GenerateDocuments`           |
| Extract/read the tracked changes from a Word document                                        | `GetTrackingChangesInWord`    |
| Replace a specific text string in a Word document with an image                              | `ReplaceTextWithImageInWord`  |

---

## EnableTrackingChangesInWord

`POST /api/v2/EnableTrackingChangesInWord` — activates the change-tracking feature on a Word document so that future edits are recorded as tracked changes.

**Docs:** https://docs.pdf4me.com/pdf4me-api/generate/enable-tracking-changes-in-word.md

**Response:** Returns `{ "File Content": "<base64>" }` — the processed `.docx` with tracking enabled. Decode `File Content` to get the binary Word file.

| JSON Key     | Type          | Required | Allowed values / notes                                           |
| ------------ | ------------- | -------- | ---------------------------------------------------------------- |
| `docName`    | string        | Yes      | Source Word filename with `.docx` extension, e.g. `output.docx`. |
| `docContent` | base64 string | Yes      | Base64-encoded Word document content.                            |

**Example payload:**

```json
{
  "docName": "output.docx",
  "docContent": "UEsDBBQABgAIAAAAIQ..."
}
```

---

## GenerateDocument

`POST /api/v2/GenerateDocument` — generates a **single** output document by merging a template (Word, HTML, or PDF with mustache syntax or merge fields) with data from a JSON or XML source.

**Docs:** https://docs.pdf4me.com/pdf4me-api/generate/generate-document-single.md

**Response:** Returns `{ "File Content": "<base64>" }` — the generated document in the requested `outputType`. Decode `File Content` to get the binary file.

| JSON Key           | Type          | Required | Allowed values / notes                                                                                         |
| ------------------ | ------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| `templateFileType` | string (enum) | Yes      | Template format: `"DOCX"` for Word, `"HTML"` for HTML, `"PDF"` for PDF.                                        |
| `templateFileName` | string        | Yes      | Template filename with proper extension, e.g. `template.docx`.                                                 |
| `templateFileData` | base64 string | Yes      | Base64-encoded template file content.                                                                          |
| `documentDataType` | string (enum) | Yes      | Data file format: `"JSON"` or `"XML"`.                                                                         |
| `documentDataFile` | base64 string | Yes      | Base64-encoded data file content (JSON or XML).                                                                |
| `outputType`       | string (enum) | Yes      | Output format: `"PDF"`, `"DOCX"` (Word), `"XLSX"` (Excel), or `"HTML"`.                                        |
| `metaDataJson`     | string        | Yes      | JSON metadata string for the operation, e.g. `"{\"version\":\"1.0\"}"`. Pass `"{}"` if unused.                 |
| `documentDataText` | string        | No       | Alternative to `documentDataFile` — provide data inline as a JSON or XML string, e.g. `"{\"name\":\"John\"}"`. |
| `fileMetaData`     | string        | No       | Additional supplementary metadata JSON string.                                                                 |

**Example payload:**

```json
{
  "templateFileType": "DOCX",
  "templateFileName": "template.docx",
  "templateFileData": "UEsDBBQABgAIAAAAIQ...",
  "documentDataType": "JSON",
  "documentDataFile": "eyJuYW1lIjoiSm9obiJ9",
  "outputType": "PDF",
  "metaDataJson": "{\"version\":\"1.0\",\"author\":\"PDF4me\"}",
  "documentDataText": "{\"name\":\"John\",\"email\":\"john@example.com\"}"
}
```

---

## GenerateDocuments

`POST /api/v2/GenerateDocuments` — generates **multiple** output documents in a batch by merging a single template with a multi-record data source (Excel, CSV, JSON, or XML). Produces one output document per data record.

**Docs:** https://docs.pdf4me.com/pdf4me-api/generate/generate-documents-multiple.md

**Response:** Returns `{ "Output Documents": [ ... ] }` — an array of generated document objects, one per data record.

| JSON Key           | Type          | Required | Allowed values / notes                                                               |
| ------------------ | ------------- | -------- | ------------------------------------------------------------------------------------ |
| `templateFileType` | string (enum) | Yes      | Template format: `"Docx"` for Word, `"HTML"` for HTML, `"PDF"` for PDF.              |
| `templateFileName` | string        | Yes      | Template filename with proper extension, e.g. `template.docx`.                       |
| `templateFileData` | base64 string | Yes      | Base64-encoded template file content.                                                |
| `documentDataType` | string (enum) | Yes      | Data file format: `"Json"`, `"Xml"`, `"Excel"`, or `"Csv"`.                          |
| `documentDataFile` | base64 string | Yes      | Base64-encoded data file content (Excel, CSV, JSON, or XML with multiple records).   |
| `outputType`       | string (enum) | Yes      | Output format per document: `"Docx"` (Word), `"PDF"`, `"Xlsx"` (Excel), or `"HTML"`. |
| `metaDataJson`     | string        | No       | JSON metadata string for the operation.                                              |
| `documentDataText` | string        | No       | Alternative to `documentDataFile` — provide data inline as a JSON or XML string.     |
| `fileMetaData`     | string        | No       | Additional supplementary metadata JSON string.                                       |

**Example payload:**

```json
{
  "templateFileType": "Docx",
  "templateFileName": "template.docx",
  "templateFileData": "UEsDBBQABgAIAAAAIQ...",
  "documentDataType": "Json",
  "documentDataFile": "W3sibmFtZSI6IkpvaG4ifV0=",
  "outputType": "Docx",
  "metaDataJson": "{\"version\":\"1.0\",\"author\":\"PDF4me\"}",
  "documentDataText": "{\"name\":\"John\",\"email\":\"john@example.com\"}"
}
```

---

## GetTrackingChangesInWord

`POST /api/v2/GetTrackingChangesInWord` — extracts and returns the tracked changes (revision history, modifications, author attribution) from a Word document.

**Docs:** https://docs.pdf4me.com/pdf4me-api/generate/get-tracking-changes-in-word.md

**Response:** Returns `{ "File Content": "<base64>" }` — the Word document with extracted change tracking information. Decode `File Content` to get the binary Word file.

| JSON Key     | Type          | Required | Allowed values / notes                                           |
| ------------ | ------------- | -------- | ---------------------------------------------------------------- |
| `docName`    | string        | Yes      | Source Word filename with `.docx` extension, e.g. `output.docx`. |
| `docContent` | base64 string | Yes      | Base64-encoded Word document content.                            |

**Example payload:**

```json
{
  "docName": "output.docx",
  "docContent": "UEsDBBQABgAIAAAAIQ..."
}
```

---

## ReplaceTextWithImageInWord

`POST /api/v2/ReplaceTextWithImageInWord` — searches a Word document for a specific text string and replaces every occurrence with an image (stamp, logo, graphic, etc.).

**Docs:** https://docs.pdf4me.com/pdf4me-api/generate/replace-text-with-image-in-word.md

**Response:** Returns `{ "File Content": "<base64>" }` — the processed `.docx` with text replaced by the image. Decode `File Content` to get the binary Word file.

| JSON Key           | Type          | Required | Allowed values / notes                                                                                                                                  |
| ------------------ | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docName`          | string        | Yes      | Source Word filename with `.docx` extension, e.g. `output.docx`.                                                                                        |
| `docContent`       | base64 string | Yes      | Base64-encoded Word document content.                                                                                                                   |
| `SearchText`       | string        | Yes      | Exact text string to search for and replace. Case-sensitive matching. All occurrences will be replaced.                                                 |
| `ImageFileName`    | string        | Yes      | Replacement image filename with extension, e.g. `stamp.png`. Supported formats: JPG, PNG, BMP, TIFF, and more.                                          |
| `ImageFileContent` | base64 string | Yes      | Base64-encoded image file content.                                                                                                                      |
| `IsFirstPageSkip`  | boolean       | No       | `true` to skip the first page (leave it unchanged); `false` (default) to include all pages.                                                             |
| `PageNumbers`      | string        | No       | Target specific pages: `"1"` = page 1, `"1, 3, 5"` = specific pages, `"1-5"` = range, `"1, 3-7, 10"` = mixed. Leave empty or omit to process all pages. |

**Example payload:**

```json
{
  "docName": "output.docx",
  "docContent": "UEsDBBQABgAIAAAAIQ...",
  "SearchText": "Djokovic",
  "ImageFileName": "stamp.png",
  "ImageFileContent": "iVBORw0KGgoAAAANSUhEUgAA...",
  "IsFirstPageSkip": false,
  "PageNumbers": "1"
}
```
