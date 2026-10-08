# Word — Parameter Reference

Parameter reference for every PDF4me **word** endpoint covered by this skill. This file documents the per-endpoint payload shapes — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, error handling, and general request conventions, see [`auth-and-conventions.md`](auth-and-conventions.md) where applicable.

Most Word operations use the Office base path `POST https://api.pdf4me.com/office/ApiV2Word/<Action>`. The main exception in this file is `DisableTrackingChangesInWord`, which uses the standard `https://api.pdf4me.com/api/v2/<Action>` path.

Most Word endpoints return the Office-style response envelope:

```json
{
  "document": "<base64 .docx>",
  "fileName": "output.docx",
  "success": true,
  "errorMessage": null
}
```

The `document` field is base64-encoded Word content — not raw binary and not the usual `File Content` envelope used by many non-Office endpoints.

Docs index: https://docs.pdf4me.com/pdf4me-api/word/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [ExtractMetadata](#extractmetadata)
- [AddWatermark](#addwatermark)
- [DeletePages](#deletepages)
- [AddTextWatermark](#addtextwatermark)
- [CompareDocuments](#comparedocuments)
- [MergeDocuments](#mergedocuments)
- [OptimizeDocument](#optimizedocument)
- [ReplaceText](#replacetext)
- [UpdateTableOfContents](#updatetableofcontents)
- [ReplaceTextWithImage](#replacetextwithimage)
- [ApplySecurity](#applysecurity)
- [SplitDocument](#splitdocument)
- [UpdateHeadersAndFooters](#updateheadersandfooters)
- [DisableTrackingChangesInWord](#disabletrackingchangesinword)

---

## Quick index — pick the right endpoint

| User intent                                              | Action                         |
| -------------------------------------------------------- | ------------------------------ |
| Extract metadata or document properties from a Word file | `ExtractMetadata`              |
| Add an image watermark to a Word document                | `AddWatermark`                 |
| Delete pages from a Word document                        | `DeletePages`                  |
| Add a text watermark to a Word document                  | `AddTextWatermark`             |
| Compare two Word documents and track changes             | `CompareDocuments`             |
| Merge multiple Word documents into one                   | `MergeDocuments`               |
| Compress or reduce the file size of a Word document      | `OptimizeDocument`             |
| Find and replace text in a Word document                 | `ReplaceText`                  |
| Update or generate a table of contents                   | `UpdateTableOfContents`        |
| Replace a text placeholder with an image                 | `ReplaceTextWithImage`         |
| Password-protect or restrict editing of a Word document  | `ApplySecurity`                |
| Split a Word document into multiple parts                | `SplitDocument`                |
| Add or update headers and footers in a Word document     | `UpdateHeadersAndFooters`      |
| Disable change tracking in a Word document               | `DisableTrackingChangesInWord` |

---

## ExtractMetadata

Extract comprehensive metadata and document statistics from a Word file — title, author, page count, word count, custom properties, and more.

> **Note:** Returns a `metadata` object — not a `document` field. The `document` and `fileName` fields in the response are `null`.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/ExtractMetadata`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/extract-metadata.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                                                                                   |
| ------------ | ------ | -------- | ------------------------------------------------------------------------------------------------------- |
| `document`   | Object | ✅       | Must contain `Name` (string) — Word filename with `.docx` extension, e.g. `{ "Name": "document.docx" }` |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content                                                                    |

### Optional Parameters

| JSON Key      | Type   | Default          | Notes                                                            |
| ------------- | ------ | ---------------- | ---------------------------------------------------------------- |
| `cultureName` | String | InvariantCulture | Culture code for date/time formatting, e.g. `"en-US"`, `"de-DE"` |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "cultureName": "en-US"
}
```

### Response

```json
{
  "document": null,
  "fileName": null,
  "success": true,
  "errorMessage": null,
  "metadata": {
    "Author": "John Doe",
    "Title": "Project Proposal",
    "Subject": "Q1 2024 Planning",
    "Keywords": "planning, budget, strategy",
    "Comments": "Draft version for review",
    "Category": "Business",
    "Company": "Acme Corporation",
    "Manager": "Jane Smith",
    "Created": "1/15/2024 10:30:00 AM",
    "LastModified": "1/20/2024 2:45:00 PM",
    "LastPrinted": "1/18/2024 9:15:00 AM",
    "RevisionNumber": 3,
    "TotalEditingTime": 120,
    "Pages": 8,
    "Words": 2150,
    "Characters": 12800,
    "Paragraphs": 45,
    "Custom_Department": "Marketing"
  }
}
```

Custom document properties are prefixed with `Custom_` in the response.

---

## AddWatermark

Add an image watermark (PNG, JPG, JPEG, BMP, or GIF) to all pages of a Word document, positioned behind the text.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/AddWatermark`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/add-watermark.md>

### Required Parameters

| JSON Key               | Type   | Required | Notes                                                                                  |
| ---------------------- | ------ | -------- | -------------------------------------------------------------------------------------- |
| `document`             | Object | ✅       | `{ "Name": "document.docx" }`                                                          |
| `docContent`           | Base64 | ✅       | Base64-encoded Word document content                                                   |
| `watermarkFileName`    | String | ✅       | Watermark image filename with extension, e.g. `"watermark.png"`                        |
| `watermarkFileContent` | Base64 | ✅       | Base64-encoded watermark image (PNG, JPG, JPEG, BMP, GIF). Transparent PNG recommended |

### Optional Parameters

| JSON Key          | Type            | Default | Notes                                                                 |
| ----------------- | --------------- | ------- | --------------------------------------------------------------------- |
| `scale`           | Number (float)  | `1.0`   | Scaling factor (0.1–10.0). Overridden by `width`/`height` if provided |
| `semiTransparent` | Boolean         | `false` | `true` = 50% opacity, `false` = 100% opaque                           |
| `width`           | Number (double) | —       | Watermark width in points. Overrides `scale`                          |
| `height`          | Number (double) | —       | Watermark height in points. Overrides `scale`                         |
| `alignImage`      | Boolean         | `true`  | `true` = center on page, `false` = top-left within margins            |
| `cultureName`     | String          | `null`  | Culture code, e.g. `"en-US"`                                          |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "watermarkFileName": "watermark.png",
  "watermarkFileContent": "<base64 image>",
  "scale": 1.5,
  "semiTransparent": true,
  "alignImage": true
}
```

### Response

```json
{
  "document": "<base64 .docx with watermark>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## DeletePages

Remove specific pages or page ranges from a Word document.

> At least one of `startPage`, `endPage`, or `pageNumbers` must be provided.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/DeletePages`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/delete-pages.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                |
| ------------ | ------ | -------- | ------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`        |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content |

### Optional Parameters (at least one required for deletion)

| JSON Key      | Type    | Default | Notes                                                                   |
| ------------- | ------- | ------- | ----------------------------------------------------------------------- |
| `startPage`   | Integer | —       | 1-based start page. If only this is provided, deletes from here to end  |
| `endPage`     | Integer | —       | 1-based end page. Range is inclusive                                    |
| `pageNumbers` | String  | —       | Comma-separated page numbers or ranges, e.g. `"2,4,6"` or `"1-3,5,7-9"` |
| `cultureName` | String  | `null`  | Culture code, e.g. `"en-US"`                                            |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "startPage": 2,
  "endPage": 4,
  "pageNumbers": "7,9"
}
```

### Response

```json
{
  "document": "<base64 .docx with pages deleted>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## AddTextWatermark

Add a customisable text watermark (e.g. "CONFIDENTIAL", "DRAFT") to all pages of a Word document.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/AddTextWatermark`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/add-text-watermark.md>

### Required Parameters

| JSON Key        | Type   | Required | Notes                                                      |
| --------------- | ------ | -------- | ---------------------------------------------------------- |
| `document`      | Object | ✅       | `{ "Name": "document.docx" }`                              |
| `docContent`    | Base64 | ✅       | Base64-encoded Word document content                       |
| `watermarkText` | String | ✅       | Text to display. Cannot be null, empty, or whitespace-only |

### Optional Parameters

| JSON Key          | Type            | Default     | Notes                                                                                                                     |
| ----------------- | --------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| `fontFamily`      | String          | `"Arial"`   | Font family, e.g. `"Calibri"`, `"Times New Roman"`                                                                        |
| `fontName`        | String          | —           | Font name (similar to `fontFamily`)                                                                                       |
| `fontSize`        | Number (double) | `72`        | Font size in points (1–1000)                                                                                              |
| `fontColor`       | String          | `"#808080"` | Named (`"Red"`), hex (`"#FF0000"` or `"FF0000"`), or RGB (`"RGB(255,0,0)"`)                                               |
| `semiTransparent` | Boolean         | `false`     | `true` = 50% opacity                                                                                                      |
| `orientation`     | String          | —           | Predefined orientation: `Horizontal` (0°), `Vertical` (90°), `Diagonal` (45°), `Upside-Down` (180°). Overrides `rotation` |
| `rotation`        | Number (double) | `0`         | Custom rotation angle (0–360°). Used if `orientation` not provided                                                        |
| `cultureName`     | String          | `null`      | Culture code, e.g. `"en-US"`                                                                                              |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "watermarkText": "CONFIDENTIAL",
  "orientation": "Diagonal",
  "fontFamily": "Arial",
  "fontSize": 72,
  "fontColor": "#FF0000",
  "semiTransparent": true
}
```

### Response

```json
{
  "document": "<base64 .docx with text watermark>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## CompareDocuments

Compare two Word documents and produce a document with tracked changes showing all differences.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/CompareDocuments`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/compare-documents.md>

### Required Parameters

| JSON Key           | Type   | Required | Notes                                                        |
| ------------------ | ------ | -------- | ------------------------------------------------------------ |
| `firstDocument`    | Object | ✅       | Base document reference: `{ "Name": "original.docx" }`       |
| `firstDocContent`  | Base64 | ✅       | Base64-encoded content of the first (base) document          |
| `secondDocument`   | Object | ✅       | Comparison document reference: `{ "Name": "modified.docx" }` |
| `secondDocContent` | Base64 | ✅       | Base64-encoded content of the second document                |

### Optional Parameters

| JSON Key            | Type   | Default | Notes                        |
| ------------------- | ------ | ------- | ---------------------------- |
| `comparisonOptions` | Object | —       | See comparison options below |

**`comparisonOptions` fields:**

| Field                     | Type    | Notes                                     |
| ------------------------- | ------- | ----------------------------------------- |
| `ignoreFormatting`        | Boolean | Focus on text, ignore styling changes     |
| `ignoreCaseChanges`       | Boolean | Case-insensitive comparison               |
| `ignoreComments`          | Boolean | Exclude comment changes                   |
| `ignoreTables`            | Boolean | Exclude table structure/content changes   |
| `ignoreFields`            | Boolean | Exclude field updates                     |
| `ignoreFootnotes`         | Boolean | Exclude footnote changes                  |
| `ignoreTextboxes`         | Boolean | Exclude textbox changes                   |
| `ignoreHeadersAndFooters` | Boolean | Exclude header/footer changes             |
| `author`                  | String  | Author name attributed to tracked changes |

### Example Payload

```json
{
  "firstDocument": { "Name": "original.docx" },
  "firstDocContent": "<base64>",
  "secondDocument": { "Name": "modified.docx" },
  "secondDocContent": "<base64>",
  "comparisonOptions": {
    "ignoreFormatting": false,
    "ignoreComments": true,
    "author": "Legal Review System"
  }
}
```

### Response

```json
{
  "document": "<base64 .docx with tracked changes>",
  "fileName": "comparison-result.docx",
  "success": true,
  "errorMessage": null
}
```

---

## MergeDocuments

Combine multiple Word documents into one. Documents are merged in array order; the first document is the base.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/MergeDocuments`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/merge-documents.md>

### Required Parameters

| JSON Key    | Type  | Required | Notes                                                                                                                                                       |
| ----------- | ----- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `documents` | Array | ✅       | Array of document objects. Each must have `filename` (string) and `docContent` (Base64). Optional per-item: `sortPosition` (integer), `formatMode` (string) |

### Optional Parameters

| JSON Key       | Type   | Default | Notes                                        |
| -------------- | ------ | ------- | -------------------------------------------- |
| `mergeOptions` | Object | —       | Merge options (formatting, compliance, etc.) |

### Example Payload

```json
{
  "documents": [
    { "filename": "doc1.docx", "docContent": "<base64>" },
    { "filename": "doc2.docx", "docContent": "<base64>" },
    { "filename": "doc3.docx", "docContent": "<base64>" }
  ],
  "mergeOptions": {}
}
```

### Response

```json
{
  "document": "<base64 merged .docx>",
  "fileName": "merged-document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## OptimizeDocument

Reduce the file size of a Word document by compressing images, cleaning up content, removing unused styles, and normalising formatting.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/OptimizeDocument`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/optimize-document.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                |
| ------------ | ------ | -------- | ------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`        |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content |

### Optional Parameters

| JSON Key            | Type   | Default | Notes                                                                                                                                                                 |
| ------------------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `optimizationLevel` | String | —       | `"Low"`, `"Medium"`, or `"Max"`. `Max` achieves ~80–90% file size reduction and removes comments, revisions, personal info, macros, hidden content, and unused styles |
| `wordVersion`       | String | `null`  | Target Word version for compatibility                                                                                                                                 |
| `cultureName`       | String | `null`  | Culture code, e.g. `"en-US"`                                                                                                                                          |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "optimizationLevel": "Max"
}
```

### Response

```json
{
  "document": "<base64 optimised .docx>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## ReplaceText

Find and replace one or more text strings in a Word document. Multiple replacements are processed sequentially in the order specified.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/ReplaceText`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/replace-text.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                                                          |
| ------------ | ------ | -------- | ------------------------------------------------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`                                                  |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content                                           |
| `phrases`    | Array  | ✅       | Array of replacement objects (see structure below). At least one item required |

**Each `phrases` item:**

| Field            | Type    | Notes                                                                 |
| ---------------- | ------- | --------------------------------------------------------------------- |
| `findText`       | String  | Text to search for. Cannot be null or empty                           |
| `replaceText`    | String  | Replacement text. Empty string removes the found text (default: `""`) |
| `matchCase`      | Boolean | `true` = case-sensitive, `false` = case-insensitive (default)         |
| `matchWholeWord` | Boolean | `true` = whole word only, `false` = partial match allowed (default)   |

### Optional Parameters

| JSON Key      | Type   | Default | Notes                        |
| ------------- | ------ | ------- | ---------------------------- |
| `cultureName` | String | `null`  | Culture code, e.g. `"en-US"` |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "phrases": [
    {
      "findText": "[COMPANY_NAME]",
      "replaceText": "Acme Corporation",
      "matchCase": false,
      "matchWholeWord": false
    },
    {
      "findText": "[DATE]",
      "replaceText": "2024-01-15",
      "matchCase": false,
      "matchWholeWord": false
    }
  ],
  "cultureName": "en-US"
}
```

### Response

```json
{
  "document": "<base64 .docx with replacements>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## UpdateTableOfContents

Update an existing Table of Contents or create a new one at the start of the document, based on the document's heading styles.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/UpdateTableOfContents`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/update-table-of-contents.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                |
| ------------ | ------ | -------- | ------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`        |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content |

### Optional Parameters

| JSON Key        | Type    | Default | Notes                                                                           |
| --------------- | ------- | ------- | ------------------------------------------------------------------------------- |
| `headingLevels` | String  | `"1-3"` | Heading levels to include. Range: `"1-3"`, single: `"1"`, combined: `"1-2,4-6"` |
| `useHyperlinks` | Boolean | `true`  | `true` = TOC entries are clickable links                                        |
| `hideTabLeader` | Boolean | `true`  | `true` = no dots between text and page numbers                                  |
| `useUppercase`  | Boolean | `true`  | `true` = TOC entries in uppercase                                               |
| `cultureName`   | String  | `null`  | Culture code, e.g. `"en-US"`                                                    |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "headingLevels": "1-4",
  "useHyperlinks": true,
  "hideTabLeader": false,
  "useUppercase": false,
  "cultureName": "en-US"
}
```

### Response

```json
{
  "document": "<base64 .docx with updated TOC>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## ReplaceTextWithImage

Replace all occurrences of a specified text string with an image throughout a Word document.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/ReplaceTextWithImage`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/replace-text-with-image.md>

### Required Parameters

| JSON Key       | Type   | Required | Notes                                                                                   |
| -------------- | ------ | -------- | --------------------------------------------------------------------------------------- |
| `document`     | Object | ✅       | `{ "Name": "document.docx" }`                                                           |
| `docContent`   | Base64 | ✅       | Base64-encoded Word document content                                                    |
| `findText`     | String | ✅       | Case-sensitive text to replace. Cannot be null or empty, e.g. `"[LOGO]"`, `"SIGN_HERE"` |
| `imageContent` | Base64 | ✅       | Base64-encoded replacement image (PNG, JPG, JPEG, BMP, GIF)                             |

### Optional Parameters

| JSON Key              | Type            | Default | Notes                                                                                |
| --------------------- | --------------- | ------- | ------------------------------------------------------------------------------------ |
| `width`               | Number (double) | —       | Image width in points                                                                |
| `height`              | Number (double) | —       | Image height in points                                                               |
| `maintainAspectRatio` | Boolean         | `true`  | Maintain image proportions when resizing                                             |
| `skipFirstPage`       | Boolean         | `false` | `true` = skip replacement on first page                                              |
| `applyTo`             | String          | —       | Target scope for replacement                                                         |
| `pageNumbers`         | String          | —       | Specific pages or ranges to target, e.g. `"1,2,3"` or `"1,3,5-7"`. Empty = all pages |
| `ignorePageNumbers`   | String          | —       | Page numbers to exclude from replacement                                             |
| `cultureName`         | String          | `null`  | Culture code, e.g. `"en-US"`                                                         |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "findText": "[LOGO]",
  "imageContent": "<base64 image>",
  "width": 200,
  "height": 100,
  "maintainAspectRatio": true,
  "skipFirstPage": false
}
```

### Response

```json
{
  "document": "<base64 .docx with images inserted>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## ApplySecurity

Apply password protection and/or editing restrictions to a Word document.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/ApplySecurity`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/secure-document.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                |
| ------------ | ------ | -------- | ------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`        |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content |

### Optional Parameters

| JSON Key               | Type   | Default | Notes                                                                                             |
| ---------------------- | ------ | ------- | ------------------------------------------------------------------------------------------------- |
| `secureOnOpen`         | String | `"no"`  | `"yes"` = require password to open; requires `secureOnOpenPassword`                               |
| `secureOnOpenPassword` | String | —       | Password to open the document. Required when `secureOnOpen` is `"yes"`. Recommended 8+ characters |
| `securityOptions`      | Object | —       | Editing restriction settings (see below)                                                          |

**`securityOptions` fields:**

| Field                | Type   | Notes                                                                                            |
| -------------------- | ------ | ------------------------------------------------------------------------------------------------ |
| `protectionType`     | String | `NoProtection`, `ReadOnly`, `AllowComments`, `AllowFormFields`, `AllowRevisions`                 |
| `protectionPassword` | String | Password to remove the editing restriction. Required when `protectionType` is not `NoProtection` |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "secureOnOpen": "yes",
  "secureOnOpenPassword": "SecurePass123!",
  "securityOptions": {
    "protectionType": "ReadOnly",
    "protectionPassword": "EditPass456!"
  }
}
```

### Response

```json
{
  "document": "<base64 .docx with security applied>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## SplitDocument

Split a Word document into multiple parts by pages, sections, headings, or custom page ranges.

> **Note:** The response returns only the **first split document**. The filename is a GUID-based string, e.g. `"a1b2c3d4-e5f6-7890-abcd-ef1234567890.docx"`.

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/SplitDocument`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/split-document.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                |
| ------------ | ------ | -------- | ------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`        |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content |

### Optional Parameters

| JSON Key      | Type   | Default      | Notes                                                                         |
| ------------- | ------ | ------------ | ----------------------------------------------------------------------------- |
| `splitType`   | String | `"allpages"` | `allpages`, `array`, `numberofpages`, `section`, `headings`                   |
| `splitConfig` | String | —            | Required for `array`, `numberofpages`, and `headings` split types (see below) |
| `cultureName` | String | `"en-US"`    | Culture code, e.g. `"en-US"`                                                  |

**`splitType` values and `splitConfig` requirements:**

| `splitType`     | `splitConfig` required? | `splitConfig` format                   | Example                               |
| --------------- | ----------------------- | -------------------------------------- | ------------------------------------- |
| `allpages`      | No                      | —                                      | Split each page into its own document |
| `array`         | Yes                     | Comma-separated page numbers or ranges | `"1-3,4,5-7"` → 3 docs                |
| `numberofpages` | Yes                     | Positive integer (N)                   | `"3"` → split after every 3 pages     |
| `section`       | No                      | —                                      | One document per Word section break   |
| `headings`      | Yes                     | Heading style name (case-insensitive)  | `"Heading 1"`                         |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "splitType": "headings",
  "splitConfig": "Heading 1",
  "cultureName": "en-US"
}
```

### Response

```json
{
  "document": "<base64 first split .docx>",
  "fileName": "a1b2c3d4-e5f6-7890-abcd-ef1234567890.docx",
  "success": true,
  "errorMessage": null
}
```

---

## UpdateHeadersAndFooters

Add or update headers and footers in a Word document. Supports HTML content, page number fields, and different layouts for first page, even/odd pages, and all pages.

> **Supported page number fields in content:** `PAGE`, `NUMPAGES`, `SECTION`, `SECTIONPAGES`

**Endpoint:** `POST https://api.pdf4me.com/office/ApiV2Word/UpdateHeadersAndFooters`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/update-headers-footers.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                |
| ------------ | ------ | -------- | ------------------------------------ |
| `document`   | Object | ✅       | `{ "Name": "document.docx" }`        |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content |

### Optional Parameters — Simple (plain text / uniform HTML)

| JSON Key        | Type    | Default | Notes                                |
| --------------- | ------- | ------- | ------------------------------------ |
| `headerContent` | String  | —       | Simple header text for all pages     |
| `footerContent` | String  | —       | Simple footer text for all pages     |
| `isHtml`        | Boolean | —       | Whether content is HTML              |
| `isHtmlMode`    | Boolean | —       | Use HTML mode for content processing |

### Optional Parameters — Per-page HTML

| JSON Key              | Type   | Notes                               |
| --------------------- | ------ | ----------------------------------- |
| `allPagesHeaderHtml`  | String | Header HTML applied to all pages    |
| `firstPageHeaderHtml` | String | Header HTML for first page only     |
| `evenPagesHeaderHtml` | String | Header HTML for even-numbered pages |
| `oddPagesHeaderHtml`  | String | Header HTML for odd-numbered pages  |
| `allPagesFooterHtml`  | String | Footer HTML applied to all pages    |
| `firstPageFooterHtml` | String | Footer HTML for first page only     |
| `evenPagesFooterHtml` | String | Footer HTML for even-numbered pages |
| `oddPagesFooterHtml`  | String | Footer HTML for odd-numbered pages  |

### Optional Parameters — General

| JSON Key      | Type   | Default | Notes                        |
| ------------- | ------ | ------- | ---------------------------- |
| `cultureName` | String | `null`  | Culture code, e.g. `"en-US"` |

### Example Payload

```json
{
  "document": { "Name": "document.docx" },
  "docContent": "<base64>",
  "allPagesHeaderHtml": "<div style='text-align: center; font-size: 12px; border-bottom: 1px solid #ccc;'>Company Name | Department</div>",
  "allPagesFooterHtml": "<div style='text-align: center; font-size: 9px;'>Page PAGE of NUMPAGES | © 2024 Company Name</div>",
  "cultureName": "en-US"
}
```

### Response

```json
{
  "document": "<base64 .docx with updated headers/footers>",
  "fileName": "document.docx",
  "success": true,
  "errorMessage": null
}
```

---

## DisableTrackingChangesInWord

Disable change tracking and revision mode in a Word document, removing the tracked-changes state so the document appears as final with no pending revisions.

> **Base URL for this endpoint is the standard PDF4me path, not `office/ApiV2Word/`.**  
> **Request uses `docName` + `docContent` (not a `document` object).**  
> **Response uses `"File Content"` (not `document`/`fileName`/`success`).**

**Endpoint:** `POST https://api.pdf4me.com/api/v2/DisableTrackingChangesInWord`  
**Docs:** <https://docs.pdf4me.com/pdf4me-api/word/disable-tracking-changes-in-word.md>

### Required Parameters

| JSON Key     | Type   | Required | Notes                                                                 |
| ------------ | ------ | -------- | --------------------------------------------------------------------- |
| `docName`    | String | ✅       | Word document filename with `.docx` extension, e.g. `"document.docx"` |
| `docContent` | Base64 | ✅       | Base64-encoded Word document content                                  |

### Example Payload

```json
{
  "docName": "document.docx",
  "docContent": "<base64>"
}
```

### Response

```json
{
  "File Content": "<base64 .docx with tracking disabled>"
}
```
