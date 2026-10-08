# Forms — Parameter Reference

Parameter reference for every PDF4me **forms** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

> **Response note:** Both endpoints in this category return the resulting PDF as **raw binary data** (not a JSON-wrapped Base64 string). Save the response body directly as a `.pdf` file.

Docs index: https://docs.pdf4me.com/pdf4me-api/forms/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [AddFormField](#addformfield)
- [FillPdfForm](#fillpdfform)

---

## Quick index — pick the right endpoint

| User intent                                                                          | Action         |
| ------------------------------------------------------------------------------------ | -------------- |
| Add new interactive TextBox or CheckBox form fields to a PDF at specific coordinates | `AddFormField` |
| Populate existing form fields in a fillable PDF with data                            | `FillPdfForm`  |

---

## AddFormField

`POST /api/v2/AddFormField` — adds a single interactive form field (TextBox or CheckBox) to a PDF at a specified position on one or more pages.

**Docs:** https://docs.pdf4me.com/pdf4me-api/forms/add-form-fields-to-pdf.md

| JSON Key        | Type          | Required | Allowed values / notes                                                                                                            |
| --------------- | ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `docContent`    | base64 string | Yes      | Base64-encoded PDF content.                                                                                                       |
| `docName`       | string        | Yes      | Source PDF filename with `.pdf` extension, e.g. `output.pdf`.                                                                     |
| `fieldName`     | string        | Yes      | Name attribute for the form field, e.g. `"Input Field Name"`. Used for data collection and form processing.                       |
| `formFieldType` | string        | Yes      | Field type: `"TextBox"` for a text input field, `"CheckBox"` for a checkbox.                                                      |
| `positionX`     | integer       | Yes      | X coordinate (horizontal) of the field on the page in points.                                                                     |
| `positionY`     | integer       | Yes      | Y coordinate (vertical) of the field on the page in points.                                                                       |
| `Size`          | integer       | Yes      | Size (dimension) of the form field in points.                                                                                     |
| `initialValue`  | string        | Yes      | Default/initial value pre-filled into the field, e.g. `"input text"`. Use `""` for an empty field.                                |
| `pages`         | string        | Yes      | Pages to add the field to: `"1"` = page 1, `"1,3,5"` = specific pages, `"2-5"` = range, `"1,3,7-10"` = mixed, `"1-"` = all pages. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQKJeLjz9MK...",
  "docName": "output.pdf",
  "fieldName": "Input Field Name",
  "formFieldType": "TextBox",
  "positionX": 300,
  "positionY": 300,
  "Size": 4,
  "initialValue": "input text",
  "pages": "1"
}
```

---

## FillPdfForm

`POST /api/v2/FillPdfForm` — populates the existing form fields in a fillable PDF template with structured data, producing a filled PDF.

**Docs:** https://docs.pdf4me.com/pdf4me-api/forms/fill-a-pdf-form.md

| JSON Key             | Type             | Required | Allowed values / notes                                                                                                                                                                           |
| -------------------- | ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `templateDocContent` | base64 string    | Yes      | Base64-encoded content of the PDF form template (the fillable PDF).                                                                                                                              |
| `templateDocName`    | string           | Yes      | PDF form template filename with `.pdf` extension, e.g. `form.pdf`.                                                                                                                               |
| `InputFormData`      | array of objects | Yes      | Array of `{ "fieldName": "...", "fieldValue": "..." }` objects — one entry per form field to fill. `fieldName` must match the PDF form field name exactly.                                       |
| `dataArray`          | string           | Yes      | JSON-stringified representation of the key-value pairs to fill. Must mirror the same data as `InputFormData` in JSON string format, e.g. `"{\"firstname\": \"John\", \"lastname\": \"Adams\"}"`. |
| `outputType`         | string           | Yes      | Must be `"pdf"`.                                                                                                                                                                                 |
| `inputDataType`      | string           | Yes      | Must be `"json"`.                                                                                                                                                                                |
| `metaData`           | string           | No       | Additional metadata string. Pass `""` if unused.                                                                                                                                                 |
| `metaDataJson`       | string           | No       | Additional JSON metadata string. Pass `""` if unused.                                                                                                                                            |

**Example payload:**

```json
{
  "templateDocContent": "JVBERi0xLjQKJeLjz9MK...",
  "templateDocName": "form.pdf",
  "InputFormData": [
    { "fieldName": "firstname", "fieldValue": "John" },
    { "fieldName": "lastname", "fieldValue": "Adams" },
    { "fieldName": "gender", "fieldValue": "Male" }
  ],
  "dataArray": "{\"firstname\": \"John\", \"lastname\": \"Adams\", \"gender\": \"Male\"}",
  "outputType": "pdf",
  "inputDataType": "json",
  "metaData": "",
  "metaDataJson": ""
}
```
