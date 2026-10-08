# Extract — Parameter Reference

Parameter reference for every PDF4me **extract** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/extract/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [ClassifyDocument](#classifydocument)
- [ExtractAttachmentFromPdf](#extractattachmentfrompdf)
- [ExtractPdfFormData](#extractpdfformdata)
- [ExtractResources](#extractresources)
- [ExtractTableFromPdf](#extracttablefrompdf)
- [ExtractTextByExpression](#extracttextbyexpression)
- [ExtractTextFromWord](#extracttextfromword)
- [ParseDocument](#parsedocument)

---

## Quick index — pick the right endpoint

| User intent                                                             | Action                     |
| ----------------------------------------------------------------------- | -------------------------- |
| Identify the type/category of a PDF (invoice, contract, report…)        | `ClassifyDocument`         |
| Extract embedded file attachments from a PDF                            | `ExtractAttachmentFromPdf` |
| Extract all form field names, values, and types from a fillable PDF     | `ExtractPdfFormData`       |
| Extract text content and/or images from a PDF                           | `ExtractResources`         |
| Extract table structures and cell data from a PDF                       | `ExtractTableFromPdf`      |
| Extract text matching a regex pattern from a PDF                        | `ExtractTextByExpression`  |
| Extract text from a Word document with page range and filtering options | `ExtractTextFromWord`      |
| Parse a PDF with a custom template to extract structured field data     | `ParseDocument`            |

---

## ClassifyDocument

`POST /api/v2/ClassifyDocument` — analyzes a PDF's content, structure, and metadata to identify its document type (e.g. invoice, contract, report) and return a confidence-scored classification.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/classify-document.md

| JSON Key     | Type          | Required | Allowed values / notes                                          |
| ------------ | ------------- | -------- | --------------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64-encoded PDF content.                                     |
| `docName`    | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `document.pdf`. |

**Response shape:**

```json
{
  "documentType": "invoice",
  "category": "financial",
  "confidence": 0.95,
  "metadata": {
    "pageCount": 1,
    "createdDate": "2024-01-15T10:30:00Z"
  }
}
```

- **`documentType`**: Identified type (e.g. `"invoice"`, `"contract"`, `"report"`).
- **`category`**: Broad grouping (e.g. `"financial"`, `"legal"`, `"business"`).
- **`confidence`**: Classification confidence score, 0.0–1.0.
- **`metadata`**: Additional document info (page count, creation date, etc.).

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "document.pdf"
}
```

---

## ExtractAttachmentFromPdf

`POST /api/v2/ExtractAttachmentFromPdf` — extracts all files embedded as attachments inside a PDF document, returning each file's name and Base64-encoded content.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/extract-attachment-from-pdf.md

| JSON Key     | Type          | Required | Allowed values / notes                                        |
| ------------ | ------------- | -------- | ------------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64-encoded PDF content.                                   |
| `docName`    | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`. |

**Response shape:**

```json
{
  "outputDocuments": [
    {
      "fileName": "attachment1.txt",
      "streamFile": "base64-encoded-content..."
    },
    { "fileName": "attachment2.pdf", "streamFile": "base64-encoded-content..." }
  ]
}
```

- **`outputDocuments`**: Array of extracted attachment objects.
  - **`fileName`**: Original name of the embedded file.
  - **`streamFile`**: Base64-encoded content of the extracted file. Decode to get the binary.

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf"
}
```

---

## ExtractPdfFormData

`POST /api/v2/ExtractPdfFormData` — extracts all form field data (names, values, and types) from a fillable PDF form. Supports text fields, checkboxes, radio buttons, dropdowns, and signature fields.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/extract-form-data-from-pdf.md

| JSON Key     | Type          | Required | Allowed values / notes                                        |
| ------------ | ------------- | -------- | ------------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64-encoded PDF content.                                   |
| `docName`    | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`. |

**Response shape:**

```json
{
  "formFields": [
    { "fieldName": "Name", "fieldValue": "John Doe", "fieldType": "text" },
    {
      "fieldName": "Email",
      "fieldValue": "john@example.com",
      "fieldType": "text"
    },
    { "fieldName": "Date", "fieldValue": "2024-01-15", "fieldType": "date" }
  ]
}
```

- **`formFields`**: Array of form field objects.
  - **`fieldName`**: Name attribute of the form field.
  - **`fieldValue`**: Current value entered in the field.
  - **`fieldType`**: Field type — `text`, `checkbox`, `radio`, `date`, `number`, `dropdown`, `signature`.

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf"
}
```

---

## ExtractResources

`POST /api/v2/ExtractResources` — extracts text content and/or embedded images from a PDF. Use `extractText` and `extractImages` flags to control what is returned.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/extract-resources.md

| JSON Key        | Type          | Required | Allowed values / notes                                               |
| --------------- | ------------- | -------- | -------------------------------------------------------------------- |
| `docContent`    | base64 string | Yes      | Base64-encoded PDF content.                                          |
| `docName`       | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `sample.pdf`.        |
| `extractText`   | boolean       | Yes      | `true` to extract all text content; `false` to skip text extraction. |
| `extractImages` | boolean       | Yes      | `true` to extract embedded images; `false` to skip image extraction. |

**Response shape:**

```json
{
  "textList": ["extracted text content...", "more text..."],
  "imageList": [
    { "fileName": "image1.png", "imageContent": "base64-encoded-image..." },
    { "fileName": "image2.jpg", "imageContent": "base64-encoded-image..." }
  ]
}
```

- **`textList`**: Array of extracted text strings (present when `extractText` is `true`).
- **`imageList`**: Array of image objects (present when `extractImages` is `true`).
  - **`fileName`**: Extracted image filename (includes format extension).
  - **`imageContent`**: Base64-encoded image content. Decode to get the binary image.

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "sample.pdf",
  "extractText": true,
  "extractImages": true
}
```

---

## ExtractTableFromPdf

`POST /api/v2/ExtractTableFromPdf` — detects and extracts table structures from a PDF, returning each table's rows and cell data as a structured JSON array.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/extract-table-from-pdf.md

| JSON Key     | Type          | Required | Allowed values / notes                                        |
| ------------ | ------------- | -------- | ------------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64-encoded PDF content.                                   |
| `docName`    | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`. |

**Response shape:**

```json
{
  "tables": [
    {
      "rows": [
        ["Header 1", "Header 2", "Header 3"],
        ["Data 1", "Data 2", "Data 3"],
        ["Data 4", "Data 5", "Data 6"]
      ],
      "columns": 3
    }
  ]
}
```

- **`tables`**: Array of table objects, one per table found in the document.
  - **`rows`**: Two-dimensional array — outer array is rows, inner arrays are cell values. The first row typically contains column headers.
  - **`columns`**: Number of columns in the table.

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf"
}
```

---

## ExtractTextByExpression

`POST /api/v2/ExtractTextByExpression` — searches a PDF for all text matches against a regular expression pattern across a specified page range, returning all matches as an array.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/extract-text-by-expression.md

| JSON Key       | Type          | Required | Allowed values / notes                                                                                                                                      |
| -------------- | ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`   | base64 string | Yes      | Base64-encoded PDF content.                                                                                                                                 |
| `docName`      | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`.                                                                                               |
| `expression`   | string        | Yes      | Regular expression pattern. Supports standard regex syntax including groups, quantifiers, and anchors — e.g. `"\\d+"`, `"[A-Za-z]+"`, `"https?://[^\\s]+"`. |
| `pageSequence` | string        | Yes      | Pages to process: `"1-"` = all pages, `"1-3"` = range, `"1,2,3"` = specific pages.                                                                          |

**Response shape:**

```json
{
  "textList": ["extracted text 1", "extracted text 2", "extracted text 3"]
}
```

- **`textList`**: Array of strings, each being a text substring from the PDF that matched `expression`.

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf",
  "expression": "\\d+",
  "pageSequence": "1-"
}
```

---

## ExtractTextFromWord

`POST /api/v2/ExtractTextFromWord` — extracts plain text from a Word document (`.docx`/`.doc`) with control over page range, comment removal, header/footer stripping, and tracked-change acceptance.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/extract-text-from-word.md

| JSON Key             | Type          | Required | Allowed values / notes                                                                               |
| -------------------- | ------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| `docContent`         | base64 string | Yes      | Base64-encoded Word document content.                                                                |
| `docName`            | string        | Yes      | Source Word filename (without extension or with `.docx`/`.doc`), e.g. `"output"` or `"report.docx"`. |
| `StartPageNumber`    | integer       | Yes      | 1-based starting page number for extraction.                                                         |
| `EndPageNumber`      | integer       | Yes      | 1-based ending page number for extraction.                                                           |
| `RemoveComments`     | boolean       | Yes      | `true` = strip comments from output; `false` = include comments.                                     |
| `RemoveHeaderFooter` | boolean       | Yes      | `true` = strip headers and footers from output; `false` = include them.                              |
| `AcceptChanges`      | boolean       | Yes      | `true` = accept all tracked changes before extraction; `false` = reject changes.                     |

**Response shape:**

```json
{
  "extractedText": "Extracted text content from Word document pages 1 to 3...",
  "fileName": "output.txt"
}
```

- **`extractedText`**: Plain text content from the specified page range, filtered per the request flags.
- **`fileName`**: Output filename for the text content.

**Example payload:**

```json
{
  "docContent": "UEsDBBQABgAIAAAAIQ...",
  "docName": "output",
  "StartPageNumber": 1,
  "EndPageNumber": 3,
  "RemoveComments": true,
  "RemoveHeaderFooter": true,
  "AcceptChanges": true
}
```

---

## ParseDocument

`POST /api/v2/ParseDocument` — parses a PDF using a pre-configured template from the PDF4me dashboard, extracting structured field data (e.g. invoice fields, form values) based on the template's capture areas.

**Docs:** https://docs.pdf4me.com/pdf4me-api/extract/parse-document.md

> **Pre-requisite:** You must first create a parse template in the [PDF4me dashboard](https://dev.pdf4me.com/dashboard/) and obtain its `TemplateId` (GUID). `ParseId` is a unique GUID you generate per-operation (any GUID generator works).

| JSON Key       | Type          | Required | Allowed values / notes                                                                                                                                     |
| -------------- | ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docName`      | string        | Yes      | Name of the PDF file to parse, e.g. `"document.pdf"`.                                                                                                      |
| `TemplateId`   | string (GUID) | Yes\*    | GUID of the parse template from the PDF4me dashboard, e.g. `"12345678-1234-1234-1234-123456789abc"`. \*Required unless `TemplateName` is provided instead. |
| `ParseId`      | string (GUID) | Yes      | Unique GUID identifying this parsing operation. Generate client-side.                                                                                      |
| `docContent`   | base64 string | No       | Base64-encoded PDF content. If omitted, the API fetches the document by `docName`.                                                                         |
| `TemplateName` | string        | No       | Template name as an alternative to `TemplateId`, e.g. `"invoice_template"`.                                                                                |

**Response shape:**

```json
{
  "parsedData": {
    "field1": "value1",
    "field2": "value2"
  },
  "documentType": "invoice",
  "pageCount": 1,
  "confidence": 0.95
}
```

- **`parsedData`**: Object whose keys and values are the fields extracted by the template.
- **`documentType`**: Identified document type.
- **`pageCount`**: Number of pages in the document.
- **`confidence`**: Parsing confidence score, 0.0–1.0.

**Example payload (using TemplateId):**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "document.pdf",
  "TemplateId": "12345678-1234-1234-1234-123456789abc",
  "ParseId": "87654321-4321-4321-4321-cba987654321"
}
```

**Example payload (using TemplateName):**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "document.pdf",
  "TemplateName": "invoice_template",
  "ParseId": "87654321-4321-4321-4321-cba987654321"
}
```
