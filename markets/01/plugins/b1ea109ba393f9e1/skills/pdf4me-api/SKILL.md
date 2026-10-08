---
name: pdf4me-api
description: >
  Use PDF4me to process PDF, Word, Excel, and image files or integrate the PDF4me REST API.
  Trigger for PDF4me requests involving conversion, editing, merging, splitting, compression, OCR,
  extraction, barcodes or QR codes, forms, security, image processing, and Office automation.
  Do not trigger for generic document questions that do not require PDF4me.
---

# PDF4me REST API Skill

PDF4me is a comprehensive enterprise-grade cloud document processing platform that delivers advanced capabilities — conversion, merging, splitting, OCR, data extraction, editing, barcode generation, Excel automation, image processing, form handling, security, and more — all through a single, consistent REST API. Built with enhanced performance, GDPR compliance, and professional-grade output backed by guaranteed uptime and global availability.

Most PDF4me document endpoints follow a common pattern: POST a JSON payload to an action endpoint, usually with base64-encoded file content, and receive either a JSON result with base64-encoded output or structured extraction data. Excel and most Word operations use separate Office base paths, and a few endpoints return raw binary responses or use non-standard key casing.

**Base URL:** `https://api.pdf4me.com`  
**Common endpoint pattern:** `POST https://api.pdf4me.com/api/v2/<ActionName>`  
**Other endpoint families:** Excel uses `/office/ApiV2Excel/<ActionName>` and most Word operations use `/office/ApiV2Word/<ActionName>`  
**Get an API key:** `https://dev.pdf4me.com/dashboard/#/api-keys/`

---

## Authentication & Conventions

Every request uses `Authorization: Basic <your_api_key>` with `Content-Type: application/json`. Many endpoints use the familiar `docContent` and `docName` payload shape, but that is not universal across the full platform. Some endpoints use Office-style request bodies, title-case or PascalCase keys, or raw binary responses instead of the standard `"File Content"` / `"File Name"` envelope.

For full details — auth examples, encoding snippets, error codes, and rate limit retry — see [`references/auth-and-conventions.md`](references/auth-and-conventions.md).

---

## Workflow

1. Identify the requested document operation and input/output formats.
2. Read `references/auth-and-conventions.md`, then read only the category reference that matches the task.
3. Confirm required inputs that are missing. Never ask the user to paste an API key into chat; use the `PDF4ME_API_KEY` environment variable or the configured PDF4me tool connection.
4. Build the request using the exact endpoint, field names, and response type in the selected reference. Preserve the source files unless the user explicitly asks to replace them.
5. Execute the request through the configured PDF4me tool or an HTTP client. For a direct Python example, adapt `scripts/convert-to-pdf.py`.
6. Verify that the expected output was returned, save it with a clear filename, and report the output path or structured result. If the API fails, report the status and safe diagnostic details without exposing credentials or document contents.

---

## API Categories & Reference Files

| Goal                                                                    | Reference                   |
| ----------------------------------------------------------------------- | --------------------------- |
| Convert Word, Excel, PPT, images, HTML, Markdown, URL, or Visio to PDF  | `references/convert.md`     |
| Convert PDF to Word, Excel, or PowerPoint                               | `references/convert.md`     |
| Convert JSON to Excel                                                   | `references/convert.md`     |
| Create PDF/A, flatten, or linearize a PDF                               | `references/convert.md`     |
| Convert a Word form to a fillable PDF                                   | `references/convert.md`     |
| Add a barcode or QR code to a PDF                                       | `references/barcode.md`     |
| Generate a standalone barcode image                                     | `references/barcode.md`     |
| Read / detect barcodes in a PDF                                         | `references/barcode.md`     |
| Create or read a Swiss QR payment bill                                  | `references/barcode.md`     |
| Embed file attachments inside a PDF                                     | `references/edit.md`        |
| Add an HTML header or footer to PDF pages                               | `references/edit.md`        |
| Add whitespace margins to a PDF                                         | `references/edit.md`        |
| Stamp page numbers onto a PDF                                           | `references/edit.md`        |
| Overlay an image watermark or logo on PDF pages                         | `references/edit.md`        |
| Add a signature image to a PDF                                          | `references/edit.md`        |
| Overlay a text watermark or stamp on PDF pages                          | `references/edit.md`        |
| Add an image or text header/footer to an Excel document                 | `references/excel.md`       |
| Add a text watermark to an Excel document                               | `references/excel.md`       |
| Add, delete, update, extract, or merge rows in Excel                    | `references/excel.md`       |
| Delete or extract worksheets from an Excel workbook                     | `references/excel.md`       |
| Merge multiple Excel workbooks into one                                 | `references/excel.md`       |
| Convert a CSV file to Excel                                             | `references/excel.md`       |
| Remove headers, footers, or watermarks from Excel                       | `references/excel.md`       |
| Find and replace text in an Excel document                              | `references/excel.md`       |
| Password-protect or unlock an Excel document                            | `references/excel.md`       |
| Classify/identify the type and category of a document                   | `references/extract.md`     |
| Extract file attachments embedded in a PDF                              | `references/extract.md`     |
| Extract form field names, values, and types from a fillable PDF         | `references/extract.md`     |
| Extract text content and/or images from a PDF                           | `references/extract.md`     |
| Extract table structures and cell data from a PDF                       | `references/extract.md`     |
| Extract text from a PDF matching a regex pattern                        | `references/extract.md`     |
| Extract text from a Word document with page range and filter options    | `references/extract.md`     |
| Parse a PDF with a template to extract structured field data            | `references/extract.md`     |
| Find text in a PDF and replace it with new text                         | `references/find-search.md` |
| Convert a scanned or image-based PDF to a searchable/editable PDF       | `references/find-search.md` |
| Add interactive TextBox or CheckBox form fields to a PDF                | `references/forms.md`       |
| Fill existing form fields in a PDF with data                            | `references/forms.md`       |
| Enable change tracking in a Word document                               | `references/generate.md`    |
| Generate a single document from a template with JSON or XML data        | `references/generate.md`    |
| Generate multiple documents in bulk from a template with a data file    | `references/generate.md`    |
| Extract tracked changes / revision history from a Word document         | `references/generate.md`    |
| Replace a text string in a Word document with an image                  | `references/generate.md`    |
| Add an image logo or overlay watermark on top of an image               | `references/image.md`       |
| Add a text watermark or label to an image                               | `references/image.md`       |
| Compress or reduce the file size of an image                            | `references/image.md`       |
| Convert an image from one format to another (JPG, PNG, BMP, TIFF…)      | `references/image.md`       |
| Convert a PDF page to an image or generate a thumbnail                  | `references/image.md`       |
| Crop an image by removing borders or extracting a rectangular region    | `references/image.md`       |
| Flip an image horizontally or vertically / mirror it                    | `references/image.md`       |
| Read or extract technical properties / metadata from an image           | `references/image.md`       |
| Extract or OCR text from an image                                       | `references/image.md`       |
| Resize an image to specific pixel dimensions or by percentage           | `references/image.md`       |
| Auto-rotate an image using its embedded EXIF orientation data           | `references/image.md`       |
| Rotate an image by a specific angle                                     | `references/image.md`       |
| Strip or remove EXIF metadata tags from an image for privacy            | `references/image.md`       |
| Merge / combine multiple PDFs into a single file                        | `references/merge-split.md` |
| Overlay / layer one PDF on top of another PDF                           | `references/merge-split.md` |
| Split a PDF by page number, recurring interval, sequence, or range      | `references/merge-split.md` |
| Split a PDF at pages that contain a barcode value                       | `references/merge-split.md` |
| Split a PDF at pages that contain a Swiss QR bill code                  | `references/merge-split.md` |
| Split a PDF at pages that contain a specific text string                | `references/merge-split.md` |
| Compress / reduce the file size of a PDF                                | `references/optimize.md`    |
| Optimize a PDF for web delivery or online viewing                       | `references/optimize.md`    |
| Optimize a PDF for printing                                             | `references/optimize.md`    |
| Delete blank / empty pages from a PDF automatically                     | `references/organize.md`    |
| Delete specific pages by page number or range from a PDF                | `references/organize.md`    |
| Extract specific pages from a PDF into a new document                   | `references/organize.md`    |
| Rotate specific pages within a PDF                                      | `references/organize.md`    |
| Rotate all pages in an entire PDF document                              | `references/organize.md`    |
| Get raw document information / properties from a PDF                    | `references/pdf.md`         |
| Get structured metadata from a PDF (title, author, page count, etc.)    | `references/pdf.md`         |
| Repair a corrupted or damaged PDF                                       | `references/pdf.md`         |
| Password-protect or encrypt a PDF document                              | `references/security.md`    |
| Set permissions (print, copy, annotate, fill forms…) on a PDF           | `references/security.md`    |
| Remove password protection from a PDF                                   | `references/security.md`    |
| Unlock a password-protected PDF document                                | `references/security.md`    |
| Extract metadata from a Word document (author, page count, word count…) | `references/word.md`        |
| Add an image watermark to a Word document                               | `references/word.md`        |
| Delete pages from a Word document                                       | `references/word.md`        |
| Add a text watermark to a Word document                                 | `references/word.md`        |
| Compare two Word documents and track changes                            | `references/word.md`        |
| Merge / combine multiple Word documents into one                        | `references/word.md`        |
| Optimize / compress a Word document to reduce file size                 | `references/word.md`        |
| Find and replace text in a Word document                                | `references/word.md`        |
| Update or generate a Table of Contents in a Word document               | `references/word.md`        |
| Replace text with an image in a Word document                           | `references/word.md`        |
| Password-protect or restrict editing in a Word document                 | `references/word.md`        |
| Split a Word document into multiple parts                               | `references/word.md`        |
| Update headers and footers in a Word document                           | `references/word.md`        |
| Disable / turn off change tracking in a Word document                   | `references/word.md`        |
| Trigger a Power Automate / webhook flow when a PDF4me document is ready | `references/pdf4me.md`      |
| Update or replace hyperlink URLs or display text in a PDF               | `references/pdf4me.md`      |
