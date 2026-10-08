# Excel — Parameter Reference

Parameter reference for every PDF4me **Excel** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All Excel endpoints use `POST https://api.pdf4me.com/office/ApiV2Excel/<Action>`.

**Common request structure:** Most Excel endpoints share three root-level keys — `document` (object with `Name` — the Excel filename with extension), `docContent` (base64 string of the file), and an action object specific to the operation. All responses return `{ "document": "<base64>", "fileName": "...", "success": true, "errorMessage": null }`.

Docs index: https://docs.pdf4me.com/pdf4me-api/excel/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [ExcelAddImageHeaderFooter](#exceladdimageheaderfooter)
- [ExcelAddTextHeaderFooter](#exceladdtextheaderfooter)
- [ExcelAddWatermark](#exceladdwatermark)
- [ExcelAddRows](#exceladdrows)
- [ExcelDeleteRows](#exceldeleterows)
- [ExcelUpdateRows](#excelupdaterows)
- [ExcelDeleteWorksheet](#exceldeleteworksheet)
- [ExcelExtractRows](#excelextractrows)
- [ExcelExtractWorksheet](#excelextractworksheet)
- [ExcelMergeFiles](#excelmergefiles)
- [ExcelMergeRows](#excelmergerows)
- [ExcelParseCsv](#excelparsecsv)
- [ExcelRemoveHeaderFooter](#excelremoveheaderfooter)
- [ExcelDeleteWatermark](#exceldeletewatermark)
- [ExcelFindAndReplaceTextInExcel](#excelfindandreplacetextinexcel)
- [ExcelSecure](#excelsecure)
- [ExcelUnlock](#excelunlock)

---

## Quick index — pick the right endpoint

| User intent                                           | Action                           |
| ----------------------------------------------------- | -------------------------------- |
| Add an image (logo) to Excel header or footer         | `ExcelAddImageHeaderFooter`      |
| Add a text header or footer to an Excel document      | `ExcelAddTextHeaderFooter`       |
| Add a text watermark to an Excel document             | `ExcelAddWatermark`              |
| Insert new rows from JSON data into an Excel sheet    | `ExcelAddRows`                   |
| Delete rows by index range from an Excel sheet        | `ExcelDeleteRows`                |
| Update existing rows in an Excel sheet with JSON data | `ExcelUpdateRows`                |
| Remove one or more worksheets from a workbook         | `ExcelDeleteWorksheet`           |
| Read and extract row data from an Excel sheet         | `ExcelExtractRows`               |
| Extract specific worksheets into a new workbook       | `ExcelExtractWorksheet`          |
| Merge multiple Excel workbooks into one               | `ExcelMergeFiles`                |
| Merge JSON row data into an Excel table or range      | `ExcelMergeRows`                 |
| Convert a CSV file into an Excel workbook             | `ExcelParseCsv`                  |
| Remove headers and footers from an Excel document     | `ExcelRemoveHeaderFooter`        |
| Remove watermarks from an Excel document              | `ExcelDeleteWatermark`           |
| Find and replace text across all worksheets           | `ExcelFindAndReplaceTextInExcel` |
| Password-protect an Excel document                    | `ExcelSecure`                    |
| Remove password protection from an Excel document     | `ExcelUnlock`                    |

---

## ExcelAddImageHeaderFooter

`POST /office/ApiV2Excel/ExcelAddImageHeaderFooter` — adds an image (PNG, JPG, JPEG, or GIF) to the header or footer of an Excel document with position and margin control.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/add-image-header-footer.md

**Root-level parameters:**

| JSON Key                            | Type          | Required | Allowed values / notes                                                                                          |
| ----------------------------------- | ------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `document`                          | object        | Yes      | Must contain `Name` (string) — Excel filename with `.xlsx` or `.xls` extension, e.g. `{ "Name": "data.xlsx" }`. |
| `docContent`                        | base64 string | Yes      | Base64-encoded Excel file content.                                                                              |
| `imageContent`                      | base64 string | Yes      | Base64-encoded image file. Supports PNG, JPG, JPEG, GIF.                                                        |
| `addImageHeaderFooterToExcelAction` | object        | Yes      | Action configuration — see optional parameters below. Pass `{}` to use all defaults.                            |

**Parameters inside `addImageHeaderFooterToExcelAction`:**

| JSON Key           | Type     | Default    | Notes                                                                                                             |
| ------------------ | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------- |
| `isHeader`         | boolean  | `true`     | `true` = header, `false` = footer.                                                                                |
| `position`         | string   | `"Center"` | Horizontal alignment: `"Left"`, `"Center"`, or `"Right"`. Case-insensitive.                                       |
| `worksheetNames`   | string[] | all sheets | Names of worksheets to apply image to. If both `worksheetNames` and `worksheetIndexes` are empty, applies to all. |
| `worksheetIndexes` | int[]    | all sheets | 1-based worksheet indexes.                                                                                        |
| `topMargin`        | number   | `1.9`      | Top page margin in centimeters.                                                                                   |
| `bottomMargin`     | number   | `1.9`      | Bottom page margin in centimeters.                                                                                |
| `leftMargin`       | number   | `1.9`      | Left page margin in centimeters.                                                                                  |
| `rightMargin`      | number   | `1.9`      | Right page margin in centimeters.                                                                                 |
| `cultureName`      | string   | —          | Culture code for processing, e.g. `"en-US"`.                                                                      |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "imageContent": "iVBORw0KGgoAAAANS...",
  "addImageHeaderFooterToExcelAction": {
    "isHeader": true,
    "position": "Center",
    "worksheetNames": ["Sheet1", "Report"],
    "topMargin": 1.9,
    "bottomMargin": 1.9
  }
}
```

---

## ExcelAddTextHeaderFooter

`POST /office/ApiV2Excel/ExcelAddTextHeaderFooter` — adds a custom text string to the header or footer of an Excel document with font styling, transparency, and orientation options.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/add-text-header-footer.md

**Root-level parameters:**

| JSON Key                           | Type          | Required | Allowed values / notes                 |
| ---------------------------------- | ------------- | -------- | -------------------------------------- |
| `document`                         | object        | Yes      | `{ "Name": "data.xlsx" }`              |
| `docContent`                       | base64 string | Yes      | Base64-encoded Excel file content.     |
| `addTextHeaderFooterToExcelAction` | object        | Yes      | Must contain `watermarkText` (string). |

**Parameters inside `addTextHeaderFooterToExcelAction`:**

| JSON Key          | Type    | Default      | Notes                                                                                                                |
| ----------------- | ------- | ------------ | -------------------------------------------------------------------------------------------------------------------- |
| `watermarkText`   | string  | **required** | Text to display in the header or footer.                                                                             |
| `fontFamily`      | string  | `"Arial"`    | Font family name, e.g. `"Times New Roman"`.                                                                          |
| `fontSize`        | number  | `72`         | Font size in points (8–72).                                                                                          |
| `fontColor`       | string  | `"black"`    | Hex color code or color name, e.g. `"#0000FF"`.                                                                      |
| `semiTransparent` | boolean | `false`      | `true` = 50% opacity, `false` = 100% opaque.                                                                         |
| `rotation`        | number  | `0`          | Rotation angle in degrees (0–360).                                                                                   |
| `fontName`        | string  | —            | Specific font name; overrides `fontFamily`.                                                                          |
| `orientation`     | string  | —            | Preset orientation — `"Horizontal"`, `"Vertical"`, `"Diagonal"`, or `"Upside-Down"`. Takes priority over `rotation`. |
| `cultureName`     | string  | —            | Culture code, e.g. `"en-US"`.                                                                                        |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "addTextHeaderFooterToExcelAction": {
    "watermarkText": "Confidential Report 2024",
    "fontFamily": "Arial",
    "fontSize": 12,
    "fontColor": "#0000FF",
    "orientation": "Horizontal"
  }
}
```

---

## ExcelAddWatermark

`POST /office/ApiV2Excel/ExcelAddWatermark` — adds a text watermark (e.g. "DRAFT", "Confidential") to Excel worksheets with font styling and transparency control.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/add-text-watermark.md

**Root-level parameters:**

| JSON Key                    | Type          | Required | Allowed values / notes                 |
| --------------------------- | ------------- | -------- | -------------------------------------- |
| `document`                  | object        | Yes      | `{ "Name": "data.xlsx" }`              |
| `docContent`                | base64 string | Yes      | Base64-encoded Excel file content.     |
| `addWatermarkToExcelAction` | object        | Yes      | Must contain `watermarkText` (string). |

**Parameters inside `addWatermarkToExcelAction`:**

| JSON Key          | Type    | Default      | Notes                                                |
| ----------------- | ------- | ------------ | ---------------------------------------------------- |
| `watermarkText`   | string  | **required** | Text to display as watermark, e.g. `"Confidential"`. |
| `fontFamily`      | string  | `"Arial"`    | Font family name.                                    |
| `fontSize`        | number  | `72`         | Font size in points.                                 |
| `fontColor`       | string  | `"black"`    | Hex color or color name, e.g. `"#808080"`.           |
| `semiTransparent` | boolean | `false`      | `true` = 50% opacity.                                |
| `cultureName`     | string  | —            | Culture code, e.g. `"en-US"`.                        |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "addWatermarkToExcelAction": {
    "watermarkText": "Confidential",
    "fontColor": "#808080",
    "semiTransparent": true
  }
}
```

---

## ExcelAddRows

`POST /office/ApiV2Excel/ExcelAddRows` — inserts rows from JSON data into an Excel sheet using table-based (header matching) or coordinate-based (row/column position) insertion.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/add-rows.md

**Root-level parameters:**

| JSON Key               | Type          | Required | Allowed values / notes             |
| ---------------------- | ------------- | -------- | ---------------------------------- |
| `document`             | object        | Yes      | `{ "Name": "data.xlsx" }`          |
| `docContent`           | base64 string | Yes      | Base64-encoded Excel file content. |
| `addRowsToExcelAction` | object        | Yes      | Must contain `jsonInput` (string). |

**Parameters inside `addRowsToExcelAction`:**

| JSON Key                | Type    | Default        | Notes                                                                                            |
| ----------------------- | ------- | -------------- | ------------------------------------------------------------------------------------------------ |
| `jsonInput`             | string  | **required**   | JSON-encoded array of row objects or a single object, e.g. `"[{\"Name\":\"John\",\"Age\":30}]"`. |
| `worksheetName`         | string  | `"Sheet1"`     | Target worksheet name.                                                                           |
| `tableName`             | string  | —              | Excel table name for table-based mode. Leave empty for coordinate-based mode.                    |
| `excelRowNumber`        | int     | —              | 1-based row position within the table (table mode only).                                         |
| `insertFromRow`         | int     | —              | 1-based start row for coordinate mode.                                                           |
| `insertFromColumn`      | int     | —              | 1-based start column for coordinate mode.                                                        |
| `convertNumericAndDate` | boolean | `true`         | Automatically convert JSON strings to Excel numbers and dates.                                   |
| `dateFormat`            | string  | `"yyyy-MM-dd"` | Excel date format pattern.                                                                       |
| `numericFormat`         | string  | `"N2"`         | Excel numeric format pattern.                                                                    |
| `ignoreNullValues`      | boolean | `false`        | Skip null values instead of inserting empty cells.                                               |
| `ignoreAttributeTitles` | boolean | `false`        | Case-insensitive header matching.                                                                |
| `cultureName`           | string  | `"en-US"`      | Culture for date/number parsing.                                                                 |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "addRowsToExcelAction": {
    "jsonInput": "[{\"Name\":\"John\",\"Age\":30},{\"Name\":\"Jane\",\"Age\":28}]",
    "worksheetName": "Sheet1"
  }
}
```

---

## ExcelDeleteRows

`POST /office/ApiV2Excel/ExcelDeleteRows` — removes rows from an Excel worksheet by specifying a row index range.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/delete-rows.md

**Root-level parameters:**

| JSON Key                  | Type          | Required | Allowed values / notes                                       |
| ------------------------- | ------------- | -------- | ------------------------------------------------------------ |
| `document`                | object        | Yes      | `{ "Name": "data.xlsx" }`                                    |
| `docContent`              | base64 string | Yes      | Base64-encoded Excel file content.                           |
| `deleteRowsToExcelAction` | object        | Yes      | Action configuration — see below. Pass `{}` to use defaults. |

**Parameters inside `deleteRowsToExcelAction`:**

| JSON Key         | Type   | Default | Notes                                          |
| ---------------- | ------ | ------- | ---------------------------------------------- |
| `worksheetName`  | string | —       | Target worksheet name.                         |
| `worksheetIndex` | int    | —       | Target worksheet index (0-based).              |
| `fromRow`        | int    | —       | 1-based start row index of the deletion range. |
| `toRow`          | int    | —       | 1-based end row index of the deletion range.   |
| `cultureName`    | string | —       | Culture code for processing.                   |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "deleteRowsToExcelAction": {
    "worksheetName": "Sheet1",
    "fromRow": 5,
    "toRow": 10
  }
}
```

---

## ExcelUpdateRows

`POST /office/ApiV2Excel/ExcelUpdateRows` — updates existing rows in an Excel worksheet with JSON data using table-based or coordinate-based targeting.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/update-rows.md

**Root-level parameters:**

| JSON Key                  | Type          | Required | Allowed values / notes             |
| ------------------------- | ------------- | -------- | ---------------------------------- |
| `document`                | object        | Yes      | `{ "Name": "data.xlsx" }`          |
| `docContent`              | base64 string | Yes      | Base64-encoded Excel file content. |
| `updateRowsToExcelAction` | object        | Yes      | Must contain `jsonInput` (string). |

**Parameters inside `updateRowsToExcelAction`:**

| JSON Key                | Type    | Default      | Notes                                                                    |
| ----------------------- | ------- | ------------ | ------------------------------------------------------------------------ |
| `jsonInput`             | string  | **required** | JSON-encoded array of row objects with updated values.                   |
| `worksheetName`         | string  | —            | Target worksheet name.                                                   |
| `tableName`             | string  | —            | Excel table name for table-based mode. Leave empty for coordinate-based. |
| `excelRowNumber`        | int     | —            | 1-based row position in table mode.                                      |
| `insertFromRow`         | int     | —            | 1-based start row for coordinate mode.                                   |
| `insertFromColumn`      | int     | —            | 1-based start column for coordinate mode.                                |
| `convertNumericAndDate` | boolean | `true`       | Automatic type conversion for numbers and dates.                         |
| `cultureName`           | string  | —            | Culture for date/number parsing.                                         |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "updateRowsToExcelAction": {
    "jsonInput": "[{\"Name\":\"John\",\"Age\":31}]",
    "worksheetName": "Sheet1",
    "insertFromRow": 2
  }
}
```

---

## ExcelDeleteWorksheet

`POST /office/ApiV2Excel/ExcelDeleteWorksheet` — removes one or more worksheets from an Excel workbook by name or index.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/delete-worksheets.md

**Root-level parameters:**

| JSON Key                       | Type          | Required | Allowed values / notes                                        |
| ------------------------------ | ------------- | -------- | ------------------------------------------------------------- |
| `document`                     | object        | Yes      | `{ "Name": "data.xlsx" }`                                     |
| `docContent`                   | base64 string | Yes      | Base64-encoded Excel file content.                            |
| `deleteWorksheetToExcelAction` | object        | Yes      | Must specify at least `worksheetNames` or `worksheetIndexes`. |

**Parameters inside `deleteWorksheetToExcelAction`:**

| JSON Key           | Type     | Default | Notes                                                       |
| ------------------ | -------- | ------- | ----------------------------------------------------------- |
| `worksheetNames`   | string[] | —       | Names of worksheets to delete, e.g. `["Sheet2", "Sheet3"]`. |
| `worksheetIndexes` | int[]    | —       | Indexes of worksheets to delete (0-based), e.g. `[1, 2]`.   |
| `cultureName`      | string   | —       | Culture code for processing.                                |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "deleteWorksheetToExcelAction": {
    "worksheetNames": ["Sheet2", "Sheet3"]
  }
}
```

---

## ExcelExtractRows

`POST /office/ApiV2Excel/ExcelExtractRows` — reads and returns row data from an Excel worksheet as a structured JSON array. **Note:** the response `document` and `fileName` fields will be `null`; the data is in the `rowData` array.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/extract-rows.md

**Root-level parameters:**

| JSON Key                   | Type          | Required | Allowed values / notes                                                                  |
| -------------------------- | ------------- | -------- | --------------------------------------------------------------------------------------- |
| `document`                 | object        | Yes      | `{ "Name": "data.xlsx" }`                                                               |
| `docContent`               | base64 string | Yes      | Base64-encoded Excel file content.                                                      |
| `extractRowsToExcelAction` | object        | Yes      | Action configuration — see below. Pass `{}` to extract all rows from the default sheet. |

**Parameters inside `extractRowsToExcelAction`:**

| JSON Key         | Type   | Default | Notes                             |
| ---------------- | ------ | ------- | --------------------------------- |
| `worksheetName`  | string | —       | Target worksheet name.            |
| `worksheetIndex` | int    | —       | Target worksheet index (0-based). |
| `fromRow`        | int    | —       | 1-based start row index.          |
| `toRow`          | int    | —       | 1-based end row index.            |
| `cultureName`    | string | —       | Culture code for processing.      |

**Response shape (differs from other endpoints):**

```json
{
  "document": null,
  "fileName": null,
  "success": true,
  "errorMessage": null,
  "rowData": [
    { "ColumnA": "value1", "ColumnB": "value2" },
    { "ColumnA": "value3", "ColumnB": "value4" }
  ]
}
```

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "extractRowsToExcelAction": {
    "worksheetName": "Sheet1",
    "fromRow": 1,
    "toRow": 50,
    "cultureName": "en-US"
  }
}
```

---

## ExcelExtractWorksheet

`POST /office/ApiV2Excel/ExcelExtractWorksheet` — extracts one or more worksheets from an Excel workbook into a new workbook containing only the selected sheets.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/extract-worksheets.md

**Root-level parameters:**

| JSON Key                        | Type          | Required | Allowed values / notes                                        |
| ------------------------------- | ------------- | -------- | ------------------------------------------------------------- |
| `document`                      | object        | Yes      | `{ "Name": "data.xlsx" }`                                     |
| `docContent`                    | base64 string | Yes      | Base64-encoded Excel file content.                            |
| `extractWorksheetToExcelAction` | object        | Yes      | Must specify at least `worksheetNames` or `worksheetIndexes`. |

**Parameters inside `extractWorksheetToExcelAction`:**

| JSON Key           | Type     | Default | Notes                                                         |
| ------------------ | -------- | ------- | ------------------------------------------------------------- |
| `worksheetNames`   | string[] | —       | Names of worksheets to extract, e.g. `["Sheet1", "Summary"]`. |
| `worksheetIndexes` | int[]    | —       | Indexes of worksheets to extract (0-based), e.g. `[0, 2]`.    |
| `cultureName`      | string   | —       | Culture code for processing.                                  |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "extractWorksheetToExcelAction": {
    "worksheetNames": ["Sheet1", "Summary"]
  }
}
```

---

## ExcelMergeFiles

`POST /office/ApiV2Excel/ExcelMergeFiles` — merges two or more Excel workbooks into a single workbook. All files and options are provided inside the action object; there are no separate top-level `document` / `docContent` keys for this endpoint.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/merge-files.md

**Root-level parameters:**

| JSON Key                  | Type   | Required | Allowed values / notes            |
| ------------------------- | ------ | -------- | --------------------------------- |
| `mergeFilesToExcelAction` | object | Yes      | Must contain `documents` (array). |

**Parameters inside `mergeFilesToExcelAction`:**

| JSON Key         | Type   | Default      | Notes                                                                                                                                         |
| ---------------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `documents`      | array  | **required** | Array of file objects, each with `filename` (string, e.g. `"file1.xlsx"`) and `fileContent` (base64 string). Files are merged in array order. |
| `outputFileName` | string | —            | Output workbook filename, e.g. `"merged.xlsx"`.                                                                                               |
| `cultureName`    | string | —            | Culture code for processing.                                                                                                                  |

**Example payload:**

```json
{
  "mergeFilesToExcelAction": {
    "documents": [
      { "filename": "file1.xlsx", "fileContent": "UEsDBBQABgAIAAAA..." },
      { "filename": "file2.xlsx", "fileContent": "UEsDBBQABgAIAAAA..." }
    ],
    "outputFileName": "merged.xlsx"
  }
}
```

---

## ExcelMergeRows

`POST /office/ApiV2Excel/ExcelMergeRows` — merges row data from JSON into an Excel table or range, combining existing sheet data with new rows.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/merge-rows.md

**Root-level parameters:**

| JSON Key                 | Type          | Required | Allowed values / notes             |
| ------------------------ | ------------- | -------- | ---------------------------------- |
| `document`               | object        | Yes      | `{ "Name": "data.xlsx" }`          |
| `docContent`             | base64 string | Yes      | Base64-encoded Excel file content. |
| `mergeRowsToExcelAction` | object        | Yes      | Must contain `jsonInput` (string). |

**Parameters inside `mergeRowsToExcelAction`:**

| JSON Key                | Type    | Default      | Notes                                            |
| ----------------------- | ------- | ------------ | ------------------------------------------------ |
| `jsonInput`             | string  | **required** | JSON-encoded array of row objects to merge.      |
| `worksheetName`         | string  | —            | Target worksheet name.                           |
| `tableName`             | string  | —            | Excel table name for table-based merge.          |
| `convertNumericAndDate` | boolean | `true`       | Automatic type conversion for numbers and dates. |
| `cultureName`           | string  | —            | Culture for date/number parsing.                 |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "mergeRowsToExcelAction": {
    "jsonInput": "[{\"Name\":\"John\",\"Age\":30}]",
    "worksheetName": "Sheet1",
    "tableName": "SalesTable"
  }
}
```

---

## ExcelParseCsv

`POST /office/ApiV2Excel/ExcelParseCsv` — converts CSV content into an Excel workbook with configurable delimiter and character encoding.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/parse-csv.md

**Root-level parameters:**

| JSON Key                | Type          | Required | Allowed values / notes                                             |
| ----------------------- | ------------- | -------- | ------------------------------------------------------------------ |
| `document`              | object        | Yes      | `{ "Name": "output.xlsx" }` — used as output filename placeholder. |
| `docContent`            | base64 string | Yes      | Base64-encoded CSV file content.                                   |
| `csvParseToExcelAction` | object        | Yes      | Action configuration — see below.                                  |

**Parameters inside `csvParseToExcelAction`:**

| JSON Key         | Type   | Default | Notes                                                 |
| ---------------- | ------ | ------- | ----------------------------------------------------- |
| `outputFileName` | string | —       | Output Excel filename, e.g. `"output.xlsx"`.          |
| `delimiter`      | string | `","`   | Field delimiter character, e.g. `","`, `";"`, `"\t"`. |
| `encoding`       | string | —       | Character encoding, e.g. `"UTF-8"`, `"ISO-8859-1"`.   |
| `cultureName`    | string | —       | Culture code for number/date parsing.                 |

**Example payload:**

```json
{
  "document": { "Name": "output.xlsx" },
  "docContent": "TmFtZSxBZ2UKSm9obiwzMApKYW5lLDI4",
  "csvParseToExcelAction": {
    "outputFileName": "output.xlsx",
    "delimiter": ",",
    "encoding": "UTF-8"
  }
}
```

---

## ExcelRemoveHeaderFooter

`POST /office/ApiV2Excel/ExcelRemoveHeaderFooter` — clears all text and image headers and footers from an Excel document, optionally targeting specific worksheets.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/remove-header-footer.md

**Root-level parameters:**

| JSON Key                          | Type          | Required | Allowed values / notes                                                     |
| --------------------------------- | ------------- | -------- | -------------------------------------------------------------------------- |
| `document`                        | object        | Yes      | `{ "Name": "data.xlsx" }`                                                  |
| `docContent`                      | base64 string | Yes      | Base64-encoded Excel file content.                                         |
| `removeHeaderFooterToExcelAction` | object        | Yes      | Action configuration — see below. Pass `{}` to remove from all worksheets. |

**Parameters inside `removeHeaderFooterToExcelAction`:**

| JSON Key           | Type     | Default    | Notes                                                         |
| ------------------ | -------- | ---------- | ------------------------------------------------------------- |
| `worksheetNames`   | string[] | all sheets | Worksheet names to clear. Empty = apply to all worksheets.    |
| `worksheetIndexes` | int[]    | all sheets | Worksheet indexes (0-based). Empty = apply to all worksheets. |
| `cultureName`      | string   | —          | Culture code for processing.                                  |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "removeHeaderFooterToExcelAction": {
    "worksheetNames": ["Sheet1", "Report"]
  }
}
```

---

## ExcelDeleteWatermark

`POST /office/ApiV2Excel/ExcelDeleteWatermark` — removes text and image watermarks from an Excel document, optionally targeting specific worksheets.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/remove-watermark.md

**Root-level parameters:**

| JSON Key                       | Type          | Required | Allowed values / notes                                                     |
| ------------------------------ | ------------- | -------- | -------------------------------------------------------------------------- |
| `document`                     | object        | Yes      | `{ "Name": "data.xlsx" }`                                                  |
| `docContent`                   | base64 string | Yes      | Base64-encoded Excel file content.                                         |
| `deleteWatermarkToExcelAction` | object        | Yes      | Action configuration — see below. Pass `{}` to remove from all worksheets. |

**Parameters inside `deleteWatermarkToExcelAction`:**

| JSON Key           | Type     | Default    | Notes                                                             |
| ------------------ | -------- | ---------- | ----------------------------------------------------------------- |
| `worksheetNames`   | string[] | all sheets | Worksheet names to clear watermarks from. Empty = all worksheets. |
| `worksheetIndexes` | int[]    | all sheets | Worksheet indexes (0-based). Empty = all worksheets.              |
| `cultureName`      | string   | —          | Culture code for processing.                                      |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "deleteWatermarkToExcelAction": {
    "worksheetNames": ["Sheet1"]
  }
}
```

---

## ExcelFindAndReplaceTextInExcel

`POST /office/ApiV2Excel/ExcelFindAndReplaceTextInExcel` — finds and replaces text across all worksheets in an Excel workbook with support for literal or regex matching, case sensitivity, whole-cell matching, and optional formatting changes.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/replace-text.md

**Root-level parameters:**

| JSON Key                   | Type          | Required | Allowed values / notes             |
| -------------------------- | ------------- | -------- | ---------------------------------- |
| `document`                 | object        | Yes      | `{ "Name": "data.xlsx" }`          |
| `docContent`               | base64 string | Yes      | Base64-encoded Excel file content. |
| `replaceTextToExcelAction` | object        | Yes      | Must contain `phrases` (array).    |

**Parameters inside `replaceTextToExcelAction`:**

| JSON Key      | Type   | Default      | Notes                                                                                                                                                                                                                                                                                                                    |
| ------------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `phrases`     | array  | **required** | Array of replacement objects. Each object: `searchText` (string), `replacementText` (string — set to `""` to delete), `isExpression` (bool, default `false` — treat `searchText` as regex), `caseSensitive` (bool, default `false`), `matchEntireCell` (bool, default `false`). Optional `formatting` object per phrase. |
| `cultureName` | string | —            | Culture code for processing.                                                                                                                                                                                                                                                                                             |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "replaceTextToExcelAction": {
    "phrases": [
      {
        "searchText": "OldCompanyName",
        "replacementText": "NewCompanyName",
        "caseSensitive": false,
        "matchEntireCell": false
      },
      {
        "searchText": "DRAFT",
        "replacementText": "",
        "matchEntireCell": true
      }
    ]
  }
}
```

---

## ExcelSecure

`POST /office/ApiV2Excel/ExcelSecure` — applies password protection to an Excel document at up to three independent levels: file encryption, workbook structure, and worksheet content.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/secure-document.md

**Root-level parameters:**

| JSON Key            | Type          | Required | Allowed values / notes                        |
| ------------------- | ------------- | -------- | --------------------------------------------- |
| `document`          | object        | Yes      | `{ "Name": "data.xlsx" }`                     |
| `docContent`        | base64 string | Yes      | Base64-encoded Excel file content.            |
| `secureExcelAction` | object        | Yes      | At least one protection option should be set. |

**Parameters inside `secureExcelAction`:**

| JSON Key                      | Type    | Default | Notes                                                                                                                                                 |
| ----------------------------- | ------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `password`                    | string  | —       | File encryption password (Level 1 — password to open). Also used as fallback for workbook/worksheet protection if their specific passwords are empty. |
| `protectWorkbook`             | boolean | `false` | Enable workbook structure protection (Level 2 — prevents adding/deleting/renaming sheets).                                                            |
| `protectWorkbookPassword`     | string  | —       | Password for workbook protection. Falls back to `password` if empty.                                                                                  |
| `protectWorksheets`           | boolean | `false` | Enable worksheet content protection (Level 3 — prevents cell edits).                                                                                  |
| `worksheetProtectionType`     | string  | `"All"` | Protection type: `"Contents"`, `"Objects"`, `"Scenarios"`, or `"All"`.                                                                                |
| `worksheetProtectionPassword` | string  | —       | Password for worksheet protection. Falls back to `password` if empty.                                                                                 |
| `worksheetNames`              | string  | —       | Comma-separated worksheet names to protect; empty = all.                                                                                              |
| `worksheetIndexes`            | string  | —       | Comma-separated worksheet indexes (0-based) to protect; empty = all.                                                                                  |
| `cultureName`                 | string  | —       | Culture code for processing.                                                                                                                          |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "secureExcelAction": {
    "password": "MyPassword123",
    "protectWorkbook": true,
    "protectWorksheets": true,
    "worksheetProtectionType": "All"
  }
}
```

---

## ExcelUnlock

`POST /office/ApiV2Excel/ExcelUnlock` — removes password protection (file encryption, workbook structure, and worksheet protection) from an Excel document.

**Docs:** https://docs.pdf4me.com/pdf4me-api/excel/unlock-document.md

**Root-level parameters:**

| JSON Key            | Type          | Required | Allowed values / notes                                |
| ------------------- | ------------- | -------- | ----------------------------------------------------- |
| `document`          | object        | Yes      | `{ "Name": "data.xlsx" }`                             |
| `docContent`        | base64 string | Yes      | Base64-encoded password-protected Excel file content. |
| `unlockExcelAction` | object        | Yes      | Must contain `password` (string).                     |

**Parameters inside `unlockExcelAction`:**

| JSON Key      | Type   | Default      | Notes                              |
| ------------- | ------ | ------------ | ---------------------------------- |
| `password`    | string | **required** | Password used to protect the file. |
| `cultureName` | string | —            | Culture code for processing.       |

**Example payload:**

```json
{
  "document": { "Name": "data.xlsx" },
  "docContent": "UEsDBBQABgAIAAAA...",
  "unlockExcelAction": {
    "password": "MyPassword123"
  }
}
```
