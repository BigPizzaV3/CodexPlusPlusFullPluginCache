# PDF — Parameter Reference

Parameter reference for every PDF4me **pdf** utility endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All PDF utility requests use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/pdf/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [GetPdfInformation](#getpdfinformation)
- [GetPdfMetadata](#getpdfmetadata)
- [RepairPdf](#repairpdf)

---

## Quick index — pick the right endpoint

| User intent                                                                    | Action              |
| ------------------------------------------------------------------------------ | ------------------- |
| Get raw document information or low-level PDF properties                       | `GetPdfInformation` |
| Get structured metadata such as title, author, page count, or encryption state | `GetPdfMetadata`    |
| Repair a corrupted or damaged PDF                                              | `RepairPdf`         |

---

## GetPdfInformation

`POST /api/v2/GetPdfInformation` — returns raw document information as a single metadata string.

**Docs:** https://docs.pdf4me.com/pdf4me-api/pdf/get-pdf-information.md

> **Key-casing note:** this endpoint uses title-case request keys, not the usual camelCase `docName` and `docContent`.

| JSON Key       | Type          | Required | Allowed values / notes                                      |
| -------------- | ------------- | -------- | ----------------------------------------------------------- |
| `File Name`    | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |
| `File Content` | base64 string | Yes      | Base64 of the source PDF.                                   |

**Example payload:**

```json
{
  "File Name": "document.pdf",
  "File Content": "Please put PDF base64 content"
}
```

**Response fields:**

| Field           | Type   | Description                                                                                          |
| --------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| `Metadata Info` | string | Raw document properties including author, title, subject, dates, security settings, and permissions. |

---

## GetPdfMetadata

`POST /api/v2/GetPdfMetadata` — returns structured metadata and document properties from a PDF.

**Docs:** https://docs.pdf4me.com/pdf4me-api/pdf/get-pdf-metadata.md

| JSON Key     | Type          | Required | Allowed values / notes                                      |
| ------------ | ------------- | -------- | ----------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the source PDF.                                   |
| `docName`    | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf"
}
```

**Response fields:**

| Field            | Type    | Description                                          |
| ---------------- | ------- | ---------------------------------------------------- |
| `Title`          | string  | Document title.                                      |
| `Subject`        | string  | Document subject or description.                     |
| `Author`         | string  | Document author.                                     |
| `Creator`        | string  | Application used to create the document.             |
| `Producer`       | string  | Software used to produce the PDF.                    |
| `Page Count`     | number  | Total number of pages.                               |
| `File Size`      | number  | File size in bytes.                                  |
| `PDF Version`    | string  | PDF specification version, e.g. `1.7`.               |
| `Creation Date`  | string  | Document creation timestamp.                         |
| `Modified Date`  | string  | Last modification timestamp.                         |
| `Is Encrypted`   | boolean | Whether the document is encrypted.                   |
| `Is Linearized`  | boolean | Whether the document is optimized for fast web view. |
| `PDF Compliance` | string  | PDF/A or related compliance level.                   |
| `Is Signed`      | boolean | Whether the document has a digital signature.        |

---

## RepairPdf

`POST /api/v2/RepairPdf` — repairs a corrupted or damaged PDF and returns a recovered file when possible.

**Docs:** https://docs.pdf4me.com/pdf4me-api/pdf/repair-pdf-document.md

| JSON Key     | Type          | Required | Allowed values / notes                                      |
| ------------ | ------------- | -------- | ----------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the corrupted PDF.                                |
| `docName`    | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf"
}
```

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/pdf/
