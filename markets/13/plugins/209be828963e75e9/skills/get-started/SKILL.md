---
name: get-started
description: Help someone start using PDFBetter in ChatGPT - bring a PDF in, then summarize, convert, merge, fill or extract data from it.
---

PDFBetter works on PDFs stored in the user's PDFBetter account. When the user first connects, or asks what PDFBetter can do:

1. Ask what they want to get done with a document: summarize or ask questions, convert (Word, Excel, PowerPoint, CSV, text, JPG), merge or split, compress, OCR a scan, fill form fields, extract data from invoices or statements, compare two versions, or find personal data to redact.
2. Bring the document in. If they share a public link, use `create_document_from_url`. If it's already in their account, find it with `list_documents`.
3. Do the task with the matching tool. Long work (conversions, compression, large OCR) returns a job id: poll `get_job` until it finishes, then share the download link.
4. When answering questions about a document, use `ask_document` or `summarize_document` and keep the page citations in your reply.
5. Explain that results come back as new documents or revisions, so the original is never overwritten, and that work counts against the monthly allowances of their PDFBetter plan.

If a tool reports that an allowance ran out, say which one and point them to https://pdfbetter.com/pricing/ instead of retrying.
